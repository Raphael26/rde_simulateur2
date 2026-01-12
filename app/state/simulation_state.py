"""
État de gestion du simulateur multi-étapes avec chargement dynamique des paramètres.
"""

import reflex as rx
from typing import Optional, Dict, List, Any, Union
from datetime import date, datetime
import json

from ..data.variables import (
    DEPARTEMENTS_FRANCE,
    SECTORS,
    SECTOR_TYPOLOGIES,
    SECTOR_ABBREVIATIONS,
    TYPOLOGY_ABBREVIATIONS,
    BENEFICIARY_TYPES,
    get_zone_climatique,
    get_fiches_for_prefix,
    CEE_CONSTANTS,
)


# Nom du bucket Supabase Storage
BUCKET_NAME = "fiches-operations"


class SimulationState(rx.State):
    """État du simulateur multi-étapes avec chargement dynamique."""
    
    # ==================== Navigation ====================
    current_step: int = 0
    is_loading: bool = False
    error_message: str = ""
    
    # ==================== Étape 1: Date et Département ====================
    date_signature: str = ""
    department: str = ""
    department_search: str = ""
    show_department_dropdown: bool = False
    
    # ==================== Étape 2: Secteur ====================
    sector: str = ""
    sector_abbr: str = ""
    
    # ==================== Étape 3: Typologie ====================
    typology: str = ""
    typology_abbr: str = ""
    
    # ==================== Étape 4: Fiche ====================
    selected_fiche: str = ""
    selected_fiche_description: str = ""
    fiche_search: str = ""
    fiche_loaded: bool = False
    fiche_loading_error: str = ""
    
    # ==================== Étape 5: Paramètres dynamiques ====================
    beneficiary_type: str = ""
    simulation_name: str = "Ma simulation"
    
    # Configuration chargée depuis Supabase Storage
    simulator_choices: Dict[str, List[str]] = {}  # Deprecated - utiliser variables_mapping
    simulator_input_choices: Dict[str, Any] = {}  # Deprecated
    simulator_var_matching: Dict[str, str] = {}  # label_affiché -> param_fonction
    simulator_variables_mapping: Dict[str, Dict[str, Any]] = {}  # label -> {option_affichée: valeur_réelle}
    simulator_function_params: Dict[str, Any] = {}  # param_fonction -> valeur
    simulator_string_function: str = ""  # Code de la fonction
    simulator_function_requirements: Dict[str, Dict[str, Any]] = {}  # Infos sur les paramètres requis
    
    # Listes des champs à afficher (séparées par type pour le typage Reflex)
    # select_fields: [{param_name, label, options_str}] où options_str = "opt1|opt2|opt3"
    select_fields: List[Dict[str, str]] = []
    number_fields: List[Dict[str, str]] = []  # [{param_name, label}]
    
    # ==================== Résultats ====================
    result_cumacs: float = 0.0
    result_euros: float = 0.0
    calculation_error: str = ""
    simulation_saved: bool = False
    missing_arguments: str = ""
    
    # ==================== Helpers Supabase ====================
    
    def _get_supabase_client(self):
        """Récupère le client Supabase pour l'authentification."""
        try:
            from ..services.supabase_service import get_supabase_client
            return get_supabase_client()
        except ImportError:
            pass
        try:
            from ..services.supabase_client import get_supabase_client
            return get_supabase_client()
        except ImportError:
            pass
        return None
    
    def _get_service_client(self):
        """Récupère le client Supabase service (bypass RLS) pour les opérations DB."""
        try:
            from ..services.supabase_service import get_service_client
            return get_service_client()
        except ImportError:
            # Fallback sur le client normal
            return self._get_supabase_client()
    
    def _is_valid_uuid(self, value: str) -> bool:
        """
        Vérifie si la valeur est un UUID valide.
        Sécurité: empêche l'injection de valeurs malformées.
        """
        if not value or not isinstance(value, str):
            return False
        
        import re
        uuid_pattern = re.compile(
            r'^[0-9a-f]{8}-[0-9a-f]{4}-[0-9a-f]{4}-[0-9a-f]{4}-[0-9a-f]{12}$',
            re.IGNORECASE
        )
        return bool(uuid_pattern.match(value))
    
    async def _get_authenticated_user_id(self) -> Optional[str]:
        """
        Récupère et valide l'user_id de l'utilisateur authentifié.
        Retourne None si non authentifié ou UUID invalide.
        """
        try:
            from .auth_state import AuthState
            auth_state = await self.get_state(AuthState)
            
            user_id = getattr(auth_state, 'user_id', None)
            is_authenticated = getattr(auth_state, 'is_authenticated', False)
            
            # Vérifications de sécurité
            if not is_authenticated:
                print("🔒 Sécurité: Utilisateur non authentifié")
                return None
            
            if not user_id:
                print("🔒 Sécurité: user_id manquant")
                return None
            
            if not self._is_valid_uuid(user_id):
                print(f"🔒 Sécurité: UUID invalide détecté: {user_id[:20]}...")
                return None
            
            return user_id
            
        except Exception as e:
            print(f"🔒 Sécurité: Erreur récupération auth: {e}")
            return None
    
    def _read_file_from_bucket(self, file_path: str, file_type: str = "txt") -> Any:
        """Lit un fichier depuis le bucket Supabase Storage."""
        client = self._get_supabase_client()
        if not client:
            print(f"❌ Client Supabase non disponible")
            return None
        
        try:
            print(f"📁 Lecture: {BUCKET_NAME}/{file_path}")
            raw = client.storage.from_(BUCKET_NAME).download(file_path)
            print(f"✅ Fichier téléchargé: {len(raw)} bytes")
            
            if file_type == "txt":
                return raw.decode("utf-8")
            elif file_type == "json":
                return json.loads(raw)
            return raw
            
        except Exception as e:
            print(f"❌ Erreur téléchargement {file_path}: {e}")
            return None
    
    # ==================== Initialisation ====================
    
    @rx.event
    def reset_step1(self):
        """Réinitialise l'étape 1 au chargement."""
        if not self.department:
            self.date_signature = ""
            self.department_search = ""
            self.show_department_dropdown = False
    
    @rx.event
    def reset_simulation(self):
        """Réinitialise toute la simulation."""
        self.date_signature = ""
        self.department = ""
        self.department_search = ""
        self.show_department_dropdown = False
        self.sector = ""
        self.sector_abbr = ""
        self.typology = ""
        self.typology_abbr = ""
        self.selected_fiche = ""
        self.selected_fiche_description = ""
        self.fiche_search = ""
        self.fiche_loaded = False
        self.fiche_loading_error = ""
        self.beneficiary_type = ""
        self.simulation_name = "Ma simulation"
        self.simulator_choices = {}
        self.simulator_input_choices = {}
        self.simulator_var_matching = {}
        self.simulator_variables_mapping = {}
        self.simulator_function_params = {}
        self.simulator_string_function = ""
        self.simulator_function_requirements = {}
        self.select_fields = []
        self.number_fields = []
        self.result_cumacs = 0.0
        self.result_euros = 0.0
        self.calculation_error = ""
        self.simulation_saved = False
        self.missing_arguments = ""
    
    # ==================== Computed Vars ====================
    
    @rx.var
    def all_departments(self) -> List[str]:
        """Retourne tous les départements."""
        return list(DEPARTEMENTS_FRANCE.keys())
    
    @rx.var
    def filtered_departments(self) -> List[str]:
        """Retourne les départements filtrés par la recherche."""
        if not self.department_search or self.department:
            return []
        search = self.department_search.lower()
        return [d for d in DEPARTEMENTS_FRANCE.keys() if search in d.lower()][:8]
    
    @rx.var
    def available_typologies(self) -> List[Dict[str, str]]:
        """Retourne les typologies disponibles pour le secteur sélectionné."""
        if not self.sector:
            return []
        return SECTOR_TYPOLOGIES.get(self.sector, [])
    
    @rx.var
    def fiches_list(self) -> List[Dict[str, str]]:
        """Retourne la liste des fiches disponibles pour le secteur/typologie sélectionné."""
        if not self.sector_abbr or not self.typology_abbr:
            return []
        
        prefix = f"{self.sector_abbr}-{self.typology_abbr}-"
        
        # Charger les fiches depuis le mapping
        return get_fiches_for_prefix(prefix)
    
    @rx.var
    def filtered_fiches(self) -> List[Dict[str, str]]:
        """Retourne les fiches filtrées par la recherche."""
        fiches = self.fiches_list
        if not self.fiche_search:
            return fiches
        search = self.fiche_search.lower()
        return [f for f in fiches if search in f["code"].lower() or search in f["description"].lower()]
    
    @rx.var
    def beneficiary_types_list(self) -> List[Dict[str, str]]:
        """Retourne la liste des types de bénéficiaires."""
        return BENEFICIARY_TYPES
    
    @rx.var
    def zone_climatique(self) -> str:
        """Retourne la zone climatique du département."""
        if not self.department or not isinstance(self.department, str):
            return "H2"
        return get_zone_climatique(self.department)
    
    @rx.var
    def result_euros_formatted(self) -> str:
        """Résultat formaté en euros."""
        return f"{self.result_euros:,.2f} €".replace(",", " ")
    
    @rx.var
    def result_cumacs_formatted(self) -> str:
        """Résultat formaté en kWh cumac."""
        return f"{self.result_cumacs:,.0f} kWh".replace(",", " ")
    
    @rx.var
    def has_dynamic_fields(self) -> bool:
        """Vérifie si des champs dynamiques sont chargés."""
        return len(self.select_fields) > 0 or len(self.number_fields) > 0
    
    @rx.var
    def can_calculate(self) -> bool:
        """Vérifie si le calcul peut être lancé."""
        if not self.beneficiary_type:
            return False
        return True
    
    @rx.var
    def can_continue_step1(self) -> bool:
        """Vérifie si on peut continuer après l'étape 1."""
        return bool(self.date_signature) and bool(self.department)
    
    # ==================== Chargement des fichiers de configuration ====================
    
    @rx.event
    async def load_fiche_configuration(self):
        """Charge les fichiers de configuration pour la fiche sélectionnée."""
        if not self.selected_fiche:
            return
        
        self.is_loading = True
        self.fiche_loading_error = ""
        self.fiche_loaded = False
        self.select_fields = []
        self.number_fields = []
        yield
        
        fiche_code = self.selected_fiche.strip()
        print(f"=== Chargement configuration pour: {fiche_code} ===")
        
        try:
            # Charger variables_mapping.json (label -> {option_affichée: valeur_réelle})
            variables_mapping = self._read_file_from_bucket(
                f"{fiche_code}/variables_mapping.json",
                "json"
            )
            
            # Charger variables_matching.json (label_affiché -> param_fonction)
            variables_matching = self._read_file_from_bucket(
                f"{fiche_code}/variables_matching.json",
                "json"
            )
            
            # Charger string_function.txt (code de la fonction)
            string_function = self._read_file_from_bucket(
                f"{fiche_code}/string_function.txt",
                "txt"
            )
            
            # Vérifier que les fichiers essentiels sont chargés
            if not string_function:
                self.fiche_loading_error = "Fichier string_function.txt manquant"
                self.is_loading = False
                yield rx.toast.error("Cette fiche n'est pas encore configurée", duration=5000)
                return
            
            # Stocker les configurations
            self.simulator_variables_mapping = variables_mapping or {}
            self.simulator_var_matching = variables_matching or {}
            self.simulator_string_function = string_function
            
            # Extraire les paramètres de la fonction (SOURCE DE VÉRITÉ)
            function_params = self._extract_parameters(string_function)
            self.simulator_function_params = function_params
            
            print(f"📋 Paramètres de la fonction: {list(function_params.keys())}")
            print(f"📋 Variables matching: {variables_matching}")
            print(f"📋 Variables mapping: {variables_mapping}")
            
            # Inverser le matching pour avoir param_fonction -> label_affiché
            param_to_label = {}
            if variables_matching:
                param_to_label = {v: k for k, v in variables_matching.items()}
            
            # Construire les listes de champs séparées
            select_fields_list = []
            number_fields_list = []
            
            for param_name in function_params.keys():
                # Trouver le label affiché (ou formater le nom du paramètre)
                if param_name in param_to_label:
                    label = param_to_label[param_name]
                else:
                    # Formater le nom: surface_isolant_en_m2 -> Surface isolant en m²
                    label = self._format_param_name(param_name)
                
                # Vérifier si ce champ a des options prédéfinies
                has_options = False
                options = []
                
                if variables_mapping and label in variables_mapping:
                    mapping = variables_mapping[label]
                    if isinstance(mapping, dict) and len(mapping) > 0:
                        options = list(mapping.keys())
                        has_options = True
                    elif isinstance(mapping, list) and len(mapping) > 0:
                        options = mapping
                        has_options = True
                
                if has_options:
                    # Encoder les options comme string séparée par "|"
                    options_str = "|".join(str(o) for o in options)
                    select_fields_list.append({
                        "param_name": param_name,
                        "label": label,
                        "options_str": options_str,
                    })
                    print(f"   ✅ Select: {label} ({param_name}) - options: {options}")
                else:
                    number_fields_list.append({
                        "param_name": param_name,
                        "label": label,
                    })
                    print(f"   ✅ Number: {label} ({param_name})")
            
            self.select_fields = select_fields_list
            self.number_fields = number_fields_list
            self.fiche_loaded = True
            self.is_loading = False
            
            print(f"✅ Configuration chargée: {len(select_fields_list)} selects, {len(number_fields_list)} numbers")
            
            yield rx.toast.success("Configuration de la fiche chargée", duration=3000)
            
        except Exception as e:
            print(f"❌ Erreur chargement configuration: {e}")
            import traceback
            traceback.print_exc()
            self.fiche_loading_error = str(e)
            self.is_loading = False
            yield rx.toast.error(f"Erreur: {str(e)[:50]}", duration=5000)
    
    def _format_param_name(self, param_name: str) -> str:
        """
        Formate un nom de paramètre pour l'affichage.
        surface_isolant_en_m2 -> Surface isolant en m²
        zone_climatique -> Zone climatique
        """
        # Remplacer les underscores par des espaces
        formatted = param_name.replace("_", " ")
        
        # Remplacer les unités courantes
        formatted = formatted.replace(" m2", " m²")
        formatted = formatted.replace(" m3", " m³")
        formatted = formatted.replace(" kwh", " kWh")
        
        # Mettre en majuscule la première lettre
        formatted = formatted.capitalize()
        
        return formatted
    
    def _extract_parameters(self, function_str: str) -> Dict[str, Any]:
        """Extrait les paramètres d'une fonction depuis son code."""
        import ast
        try:
            tree = ast.parse(function_str)
            for node in ast.walk(tree):
                if isinstance(node, ast.FunctionDef):
                    return {arg.arg: "" for arg in node.args.args}
        except Exception as e:
            print(f"Erreur extraction paramètres: {e}")
        return {}
    
    # ==================== Gestion des paramètres ====================
    
    @rx.event
    def set_param(self, param_name: str, label: str, value: str):
        """
        Met à jour un paramètre du simulateur (pour les selects).
        
        Args:
            param_name: Le nom du paramètre dans la fonction
            label: Le label affiché à l'utilisateur
            value: La valeur sélectionnée par l'utilisateur (option affichée)
        """
        print(f"📝 set_param: param={param_name}, label={label}, value={value}")
        
        # Déterminer la valeur finale
        final_value = value
        
        # Vérifier si un mapping de valeurs existe
        if label in self.simulator_variables_mapping:
            mapping = self.simulator_variables_mapping[label]
            if isinstance(mapping, dict) and value in mapping:
                final_value = mapping[value]
                print(f"   Mapping: '{value}' -> {final_value}")
        
        # Gérer les booléens
        if final_value == "Oui":
            final_value = True
        elif final_value == "Non":
            final_value = False
        
        # Mettre à jour le paramètre
        if param_name in self.simulator_function_params:
            self.simulator_function_params[param_name] = final_value
            print(f"   ✅ {param_name} = {final_value}")
        else:
            print(f"   ⚠️ Param not found: {param_name}")
        
        print(f"   Params: {self.simulator_function_params}")
    
    @rx.event
    def set_numeric_param(self, param_name: str, value: str):
        """
        Met à jour un paramètre numérique du simulateur.
        
        Args:
            param_name: Le nom du paramètre dans la fonction
            value: La valeur entrée par l'utilisateur
        """
        print(f"📝 set_numeric_param: param={param_name}, value={value}")
        
        try:
            # Convertir en float
            numeric_value = float(value) if value else 0.0
            
            # Mettre à jour le paramètre
            if param_name in self.simulator_function_params:
                self.simulator_function_params[param_name] = numeric_value
                print(f"   ✅ {param_name} = {numeric_value}")
            else:
                print(f"   ⚠️ Param not found: {param_name}")
            
            print(f"   Params: {self.simulator_function_params}")
        except ValueError:
            print(f"⚠️ Valeur non numérique: {value}")
    
    def _detect_empty_params(self) -> List[str]:
        """Détecte les paramètres vides ou non remplis."""
        empty_keys = [
            key for key, value in self.simulator_function_params.items()
            if value == "" or value is None or isinstance(value, dict)
        ]
        return empty_keys
    
    # ==================== Event Handlers ====================
    
    @rx.event
    def set_date_signature(self, value: str):
        """Définit la date de signature."""
        self.date_signature = value
    
    @rx.event
    def set_department_search(self, value: str):
        """Met à jour la recherche de département."""
        self.department_search = value
        self.show_department_dropdown = True
        if not value:
            self.department = ""
            self.show_department_dropdown = False
    
    @rx.event
    def select_department(self, value: str):
        """Sélectionne un département."""
        self.department = value
        self.department_search = value
        self.show_department_dropdown = False
    
    @rx.event
    def clear_department(self):
        """Efface le département sélectionné."""
        self.department = ""
        self.department_search = ""
        self.show_department_dropdown = False
    
    @rx.event
    def close_department_dropdown(self):
        """Ferme le dropdown des départements."""
        self.show_department_dropdown = False
    
    @rx.event
    def open_department_dropdown(self):
        """Ouvre le dropdown si il y a une recherche."""
        if self.department_search and not self.department:
            self.show_department_dropdown = True
    
    @rx.event
    def select_sector(self, value: str):
        """Sélectionne un secteur."""
        self.sector = value
        self.sector_abbr = SECTOR_ABBREVIATIONS.get(value, "")
        self.typology = ""
        self.typology_abbr = ""
        self.selected_fiche = ""
        self.fiche_loaded = False
    
    @rx.event
    def select_typology(self, name: str, abbr: str):
        """Sélectionne une typologie."""
        self.typology = name
        self.typology_abbr = abbr
        self.selected_fiche = ""
        self.fiche_loaded = False
    
    @rx.event
    def set_fiche_search(self, value: str):
        """Met à jour la recherche de fiche."""
        self.fiche_search = value
    
    @rx.event
    async def select_fiche(self, code: str, description: str):
        """Sélectionne une fiche et charge sa configuration."""
        self.selected_fiche = code
        self.selected_fiche_description = description
        self.fiche_loaded = False
        
        # Réinitialiser les paramètres
        self.simulator_choices = {}
        self.simulator_input_choices = {}
        self.simulator_var_matching = {}
        self.simulator_variables_mapping = {}
        self.simulator_function_params = {}
        self.simulator_string_function = ""
        self.select_fields = []
        self.number_fields = []
        
        # Charger la configuration
        yield SimulationState.load_fiche_configuration
    
    @rx.event
    def select_beneficiary(self, value: str):
        """Sélectionne le type de bénéficiaire."""
        self.beneficiary_type = value
    
    @rx.event
    def set_simulation_name(self, value: str):
        """Définit le nom de la simulation."""
        self.simulation_name = value
    
    @rx.event
    async def load_fiches(self):
        """Charge les fiches (placeholder pour on_load)."""
        self.is_loading = True
        yield
        import asyncio
        await asyncio.sleep(0.3)
        self.is_loading = False
    
    # ==================== Exécution du calcul ====================
    
    @rx.event
    async def execute_simulation(self):
        """Exécute le calcul de la simulation."""
        self.is_loading = True
        self.calculation_error = ""
        yield
        
        # Vérifier les paramètres manquants
        empty_params = self._detect_empty_params()
        if empty_params and self.fiche_loaded:
            self.missing_arguments = f"Paramètres manquants: {', '.join(empty_params)}"
            self.calculation_error = self.missing_arguments
            self.is_loading = False
            yield rx.toast.error(self.missing_arguments, duration=5000)
            return
        
        try:
            if self.fiche_loaded and self.simulator_string_function:
                # Calcul avec la fonction dynamique
                from ..services.function_loader import FunctionLoader
                
                func = FunctionLoader(self.simulator_string_function)
                result = func.call_with_dict(dict(self.simulator_function_params))
                
                self.result_cumacs = float(result)
                self.result_euros = float(result * CEE_CONSTANTS.get("prix_kwh_cumac", 0.0065))
                
                print(f"✅ Calcul réussi: {self.result_cumacs} kWh cumac = {self.result_euros} €")
                
            else:
                # Calcul de démonstration (fallback)
                print("⚠️ Mode démo - pas de fonction chargée")
                
                base_cumacs = {
                    "BAR-EN-101": 125000,
                    "BAR-EN-102": 89000,
                    "BAR-EN-103": 67000,
                    "BAR-TH-104": 150000,
                    "BAR-TH-106": 95000,
                    "BAR-TH-113": 180000,
                }.get(self.selected_fiche, 50000)
                
                zone_coef = {"H1": 1.2, "H2": 1.0, "H3": 0.8}.get(self.zone_climatique, 1.0)
                
                self.result_cumacs = float(base_cumacs * zone_coef)
                self.result_euros = float(self.result_cumacs * 0.0065)
            
            self.is_loading = False
            yield rx.redirect("/simulation/result")
            
        except Exception as e:
            print(f"❌ Erreur calcul: {e}")
            self.calculation_error = str(e)
            self.is_loading = False
            yield rx.toast.error(f"Erreur de calcul: {str(e)[:50]}", duration=5000)
    
    # ==================== Sauvegarde ====================
    
    @rx.event
    async def save_and_redirect(self):
        """Sauvegarde la simulation et redirige vers le dashboard."""
        if self.simulation_saved:
            yield rx.redirect("/dashboard")
            return
        
        try:
            # Utiliser le service client (bypass RLS)
            client = self._get_service_client()
            
            if client:
                # Récupérer et valider l'user_id (sécurisé)
                user_id = await self._get_authenticated_user_id()
                
                if not user_id:
                    print("🔒 Tentative de sauvegarde sans authentification valide")
                    yield rx.toast.warning("Session expirée. Veuillez vous reconnecter.", duration=3000)
                    yield rx.redirect("/login")
                    return
                
                # Préparer les données
                simulation_data = {
                    "user_id": user_id,
                    "name": self.simulation_name,
                    "fiche_code": self.selected_fiche,
                    "fiche_description": self.selected_fiche_description,
                    "sector": self.sector,
                    "typology": self.typology,
                    "department": self.department,
                    "zone_climatique": self.zone_climatique,
                    "date_signature": self.date_signature,
                    "beneficiary_type": self.beneficiary_type,
                    "result_cumacs": self.result_cumacs,
                    "result_euros": self.result_euros,
                    "input_data": json.dumps(self.simulator_function_params),
                }
                
                print(f"💾 Sauvegarde simulation pour user: {user_id[:8]}...")
                
                response = client.table("simulations").insert(simulation_data).execute()
                
                if response.data:
                    self.simulation_saved = True
                    print(f"✅ Simulation sauvegardée: ID={response.data[0].get('id', 'N/A')}")
                    yield rx.toast.success("Simulation sauvegardée !", duration=3000)
                else:
                    print(f"❌ Erreur: pas de data dans response")
                    yield rx.toast.error("Erreur lors de la sauvegarde", duration=3000)
            else:
                yield rx.toast.warning("Base de données non disponible", duration=3000)
                
        except Exception as e:
            print(f"❌ Erreur sauvegarde: {e}")
            yield rx.toast.error(f"Erreur: {str(e)[:50]}", duration=3000)
        
        yield rx.redirect("/dashboard")
    
    @rx.event
    def start_new_simulation(self):
        """Démarre une nouvelle simulation."""
        self.reset_simulation()
        return rx.redirect("/simulation/date-department")
    
    @rx.event
    async def export_pdf(self):
        """Exporte les résultats de la simulation en PDF (compatible production)."""
        try:
            from reportlab.lib.pagesizes import A4
            from reportlab.lib import colors
            from reportlab.lib.styles import getSampleStyleSheet, ParagraphStyle
            from reportlab.lib.units import cm
            from reportlab.platypus import SimpleDocTemplate, Paragraph, Spacer, Table, TableStyle
            from reportlab.lib.enums import TA_CENTER
            from datetime import datetime
            import io
            import base64
            
            # Générer le PDF en mémoire (pas sur le disque)
            buffer = io.BytesIO()
            
            # Nom du fichier pour le téléchargement
            timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
            safe_name = "".join(c if c.isalnum() or c in (' ', '-', '_') else '_' for c in (self.simulation_name or "simulation"))[:30]
            safe_name = safe_name.replace(" ", "_")
            filename = f"simulation_{safe_name}_{timestamp}.pdf"
            
            # Créer le document
            doc = SimpleDocTemplate(
                buffer,
                pagesize=A4,
                rightMargin=2*cm,
                leftMargin=2*cm,
                topMargin=2*cm,
                bottomMargin=2*cm
            )
            
            # Styles
            styles = getSampleStyleSheet()
            
            title_style = ParagraphStyle(
                'CustomTitle',
                parent=styles['Heading1'],
                fontSize=24,
                spaceAfter=30,
                alignment=TA_CENTER,
                textColor=colors.HexColor("#1a365d")
            )
            
            subtitle_style = ParagraphStyle(
                'CustomSubtitle',
                parent=styles['Normal'],
                fontSize=12,
                spaceAfter=20,
                alignment=TA_CENTER,
                textColor=colors.HexColor("#718096")
            )
            
            heading_style = ParagraphStyle(
                'CustomHeading',
                parent=styles['Heading2'],
                fontSize=14,
                spaceBefore=20,
                spaceAfter=10,
                textColor=colors.HexColor("#2d3748")
            )
            
            # Contenu du PDF
            story = []
            
            # En-tête
            story.append(Paragraph("Rapport de Simulation CEE", title_style))
            story.append(Paragraph(self.simulation_name or "Simulation", subtitle_style))
            story.append(Paragraph(f"Généré le {datetime.now().strftime('%d/%m/%Y à %H:%M')}", subtitle_style))
            story.append(Spacer(1, 20))
            
            # Résultats principaux
            story.append(Paragraph("Résultats de la simulation", heading_style))
            
            results_data = [
                ["Indicateur", "Valeur"],
                ["Prime CEE estimée", f"{self.result_euros:,.2f} €".replace(",", " ")],
                ["Volume CEE", f"{self.result_cumacs:,.0f} kWh cumac".replace(",", " ")],
            ]
            
            results_table = Table(results_data, colWidths=[8*cm, 8*cm])
            results_table.setStyle(TableStyle([
                ('BACKGROUND', (0, 0), (-1, 0), colors.HexColor("#22c55e")),
                ('TEXTCOLOR', (0, 0), (-1, 0), colors.white),
                ('ALIGN', (0, 0), (-1, -1), 'CENTER'),
                ('FONTNAME', (0, 0), (-1, 0), 'Helvetica-Bold'),
                ('FONTSIZE', (0, 0), (-1, 0), 12),
                ('BOTTOMPADDING', (0, 0), (-1, 0), 12),
                ('TOPPADDING', (0, 0), (-1, 0), 12),
                ('BACKGROUND', (0, 1), (-1, -1), colors.HexColor("#f0fdf4")),
                ('FONTSIZE', (0, 1), (-1, -1), 14),
                ('FONTNAME', (0, 1), (-1, -1), 'Helvetica-Bold'),
                ('BOTTOMPADDING', (0, 1), (-1, -1), 15),
                ('TOPPADDING', (0, 1), (-1, -1), 15),
                ('GRID', (0, 0), (-1, -1), 1, colors.HexColor("#86efac")),
            ]))
            story.append(results_table)
            story.append(Spacer(1, 20))
            
            # Détails de l'opération
            story.append(Paragraph("Détails de l'opération", heading_style))
            
            desc = self.selected_fiche_description or "-"
            if len(desc) > 50:
                desc = desc[:50] + "..."
            
            details_data = [
                ["Paramètre", "Valeur"],
                ["Fiche d'opération", self.selected_fiche or "-"],
                ["Description", desc],
                ["Secteur", self.sector or "-"],
                ["Typologie", self.typology or "-"],
                ["Type de bénéficiaire", self.beneficiary_type or "-"],
            ]
            
            details_table = Table(details_data, colWidths=[6*cm, 10*cm])
            details_table.setStyle(TableStyle([
                ('BACKGROUND', (0, 0), (-1, 0), colors.HexColor("#5a7a91")),
                ('TEXTCOLOR', (0, 0), (-1, 0), colors.white),
                ('ALIGN', (0, 0), (0, -1), 'LEFT'),
                ('ALIGN', (1, 0), (1, -1), 'LEFT'),
                ('FONTNAME', (0, 0), (-1, 0), 'Helvetica-Bold'),
                ('FONTSIZE', (0, 0), (-1, -1), 10),
                ('BOTTOMPADDING', (0, 0), (-1, -1), 8),
                ('TOPPADDING', (0, 0), (-1, -1), 8),
                ('BACKGROUND', (0, 1), (0, -1), colors.HexColor("#f1f5f9")),
                ('GRID', (0, 0), (-1, -1), 0.5, colors.HexColor("#cbd5e1")),
            ]))
            story.append(details_table)
            story.append(Spacer(1, 20))
            
            # Localisation
            story.append(Paragraph("Localisation et date", heading_style))
            
            location_data = [
                ["Paramètre", "Valeur"],
                ["Département", self.department or "-"],
                ["Zone climatique", self.zone_climatique or "-"],
                ["Date de signature", self.date_signature or "-"],
            ]
            
            location_table = Table(location_data, colWidths=[6*cm, 10*cm])
            location_table.setStyle(TableStyle([
                ('BACKGROUND', (0, 0), (-1, 0), colors.HexColor("#5a7a91")),
                ('TEXTCOLOR', (0, 0), (-1, 0), colors.white),
                ('ALIGN', (0, 0), (0, -1), 'LEFT'),
                ('ALIGN', (1, 0), (1, -1), 'LEFT'),
                ('FONTNAME', (0, 0), (-1, 0), 'Helvetica-Bold'),
                ('FONTSIZE', (0, 0), (-1, -1), 10),
                ('BOTTOMPADDING', (0, 0), (-1, -1), 8),
                ('TOPPADDING', (0, 0), (-1, -1), 8),
                ('BACKGROUND', (0, 1), (0, -1), colors.HexColor("#f1f5f9")),
                ('GRID', (0, 0), (-1, -1), 0.5, colors.HexColor("#cbd5e1")),
            ]))
            story.append(location_table)
            story.append(Spacer(1, 20))
            
            # Paramètres de calcul (si disponibles)
            if self.simulator_function_params:
                story.append(Paragraph("Paramètres de calcul", heading_style))
                
                params_data = [["Paramètre", "Valeur"]]
                for key, value in self.simulator_function_params.items():
                    param_name = key.replace("_", " ").title()
                    params_data.append([param_name, str(value)])
                
                params_table = Table(params_data, colWidths=[6*cm, 10*cm])
                params_table.setStyle(TableStyle([
                    ('BACKGROUND', (0, 0), (-1, 0), colors.HexColor("#5a7a91")),
                    ('TEXTCOLOR', (0, 0), (-1, 0), colors.white),
                    ('ALIGN', (0, 0), (0, -1), 'LEFT'),
                    ('ALIGN', (1, 0), (1, -1), 'LEFT'),
                    ('FONTNAME', (0, 0), (-1, 0), 'Helvetica-Bold'),
                    ('FONTSIZE', (0, 0), (-1, -1), 10),
                    ('BOTTOMPADDING', (0, 0), (-1, -1), 8),
                    ('TOPPADDING', (0, 0), (-1, -1), 8),
                    ('BACKGROUND', (0, 1), (0, -1), colors.HexColor("#f1f5f9")),
                    ('GRID', (0, 0), (-1, -1), 0.5, colors.HexColor("#cbd5e1")),
                ]))
                story.append(params_table)
                story.append(Spacer(1, 20))
            
            # Note de bas de page
            story.append(Spacer(1, 30))
            footer_style = ParagraphStyle(
                'Footer',
                parent=styles['Normal'],
                fontSize=8,
                textColor=colors.HexColor("#718096"),
                alignment=TA_CENTER
            )
            story.append(Paragraph(
                "Ce document est une estimation indicative. Le montant réel de la prime CEE peut varier "
                "en fonction des conditions du marché et des critères d'éligibilité. "
                "Prix unitaire utilisé : 0,0065 €/kWh cumac.",
                footer_style
            ))
            story.append(Paragraph(
                f"Document généré par RDE Consulting - {datetime.now().strftime('%d/%m/%Y %H:%M')}",
                footer_style
            ))
            
            # Construire le PDF en mémoire
            doc.build(story)
            
            # Récupérer les bytes du PDF
            pdf_bytes = buffer.getvalue()
            buffer.close()
            
            # Encoder en base64 pour le téléchargement
            pdf_base64 = base64.b64encode(pdf_bytes).decode('utf-8')
            
            print(f"✅ PDF généré en mémoire: {len(pdf_bytes)} bytes")
            yield rx.toast.success("PDF généré avec succès !", duration=3000)
            
            # Télécharger directement depuis la mémoire
            yield rx.download(
                data=f"data:application/pdf;base64,{pdf_base64}",
                filename=filename
            )
            
        except ImportError as e:
            print(f"❌ Module manquant: {e}")
            yield rx.toast.error("Module PDF non disponible. Installez: pip install reportlab", duration=5000)
        except Exception as e:
            print(f"❌ Erreur export PDF: {e}")
            import traceback
            traceback.print_exc()
            yield rx.toast.error(f"Erreur lors de l'export: {str(e)[:50]}", duration=3000)