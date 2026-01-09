"""
État de gestion du simulateur multi-étapes.
"""

import reflex as rx
from typing import Optional, Dict, List, Any
from datetime import date

from ..data.variables import (
    DEPARTEMENTS_FRANCE,
    SECTORS,
    SECTOR_TYPOLOGIES,
    SECTOR_ABBREVIATIONS,
    TYPOLOGY_ABBREVIATIONS,
    BENEFICIARY_TYPES,
    get_zone_climatique,
    CEE_CONSTANTS,
)


class SimulationState(rx.State):
    """État du simulateur multi-étapes."""
    
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
    
    # ==================== Étape 5: Bénéficiaire ====================
    beneficiary_type: str = ""
    simulation_name: str = "Ma simulation"
    
    # ==================== Résultats ====================
    result_cumacs: float = 0.0
    result_euros: float = 0.0
    calculation_error: str = ""
    simulation_saved: bool = False
    
    # ==================== Initialisation ====================
    
    @rx.event
    def reset_step1(self):
        """Réinitialise l'étape 1 au chargement."""
        # Ne réinitialise que si on arrive sur la page sans données
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
        self.beneficiary_type = ""
        self.simulation_name = "Ma simulation"
        self.result_cumacs = 0.0
        self.result_euros = 0.0
        self.calculation_error = ""
        self.simulation_saved = False
    
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
        """Retourne la liste des fiches disponibles (données de démo)."""
        if not self.sector_abbr or not self.typology_abbr:
            return []
        
        prefix = f"{self.sector_abbr}-{self.typology_abbr}-"
        
        # Données de démonstration
        demo_fiches = {
            "BAR-EN-": [
                {"code": "BAR-EN-101", "description": "Isolation de combles ou de toitures"},
                {"code": "BAR-EN-102", "description": "Isolation des murs"},
                {"code": "BAR-EN-103", "description": "Isolation d'un plancher"},
                {"code": "BAR-EN-104", "description": "Fenêtre ou porte-fenêtre complète"},
                {"code": "BAR-EN-105", "description": "Isolation des toitures terrasses"},
            ],
            "BAR-TH-": [
                {"code": "BAR-TH-104", "description": "Pompe à chaleur de type air/eau ou eau/eau"},
                {"code": "BAR-TH-106", "description": "Chaudière individuelle à haute performance"},
                {"code": "BAR-TH-113", "description": "Chaudière biomasse individuelle"},
                {"code": "BAR-TH-159", "description": "Pompe à chaleur hybride individuelle"},
            ],
            "BAR-EQ-": [
                {"code": "BAR-EQ-110", "description": "Luminaire à LED"},
                {"code": "BAR-EQ-111", "description": "Ventilation mécanique simple flux"},
            ],
            "BAR-SE-": [
                {"code": "BAR-SE-101", "description": "Rénovation globale"},
            ],
            "BAT-EN-": [
                {"code": "BAT-EN-101", "description": "Isolation de combles ou de toitures"},
                {"code": "BAT-EN-102", "description": "Isolation des murs"},
            ],
            "BAT-TH-": [
                {"code": "BAT-TH-102", "description": "Chaudière collective haute performance"},
                {"code": "BAT-TH-113", "description": "Pompe à chaleur de type air/eau"},
            ],
            "BAT-EQ-": [
                {"code": "BAT-EQ-111", "description": "Luminaire à LED"},
            ],
            "IND-UT-": [
                {"code": "IND-UT-102", "description": "Système de variation de vitesse"},
                {"code": "IND-UT-103", "description": "Récupérateur de chaleur"},
            ],
        }
        
        return demo_fiches.get(prefix, [])
    
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
        """Résultat formaté en kWh (sans cumac)."""
        return f"{self.result_cumacs:,.0f} kWh".replace(",", " ")

    @rx.event
    async def save_and_redirect(self):
        """Sauvegarde la simulation et redirige vers le dashboard."""
        if not self.simulation_saved:
            # Sauvegarder en base si Supabase disponible
            try:
                supabase = None
                try:
                    from ..services.supabase_service import supabase as sb_client
                    supabase = sb_client
                except ImportError:
                    pass
                
                if supabase:
                    from .auth_state import AuthState
                    auth_state = await self.get_state(AuthState)
                    user_id = getattr(auth_state, 'user_id', None)
                    
                    if user_id:
                        supabase.table("simulations").insert({
                            "user_id": user_id,
                            "name": self.simulation_name,
                            "fiche_code": self.selected_fiche,
                            "sector": self.sector,
                            "typology": self.typology,
                            "department": self.department,
                            "zone_climatique": self.zone_climatique,
                            "date_signature": self.date_signature,
                            "beneficiary_type": self.beneficiary_type,
                            "result_cumacs": self.result_cumacs,
                            "result_euros": self.result_euros,
                        }).execute()
            except Exception as e:
                print(f"Erreur sauvegarde: {e}")
            
            self.simulation_saved = True
        
        yield rx.redirect("/dashboard")
    
    @rx.var
    def can_continue_step1(self) -> bool:
        """Vérifie si on peut continuer après l'étape 1."""
        return bool(self.date_signature) and bool(self.department)
    
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
        # Si on efface tout, on efface aussi la sélection
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
        # Réinitialiser les étapes suivantes
        self.typology = ""
        self.typology_abbr = ""
        self.selected_fiche = ""
    
    @rx.event
    def select_typology(self, name: str, abbr: str):
        """Sélectionne une typologie."""
        self.typology = name
        self.typology_abbr = abbr
        # Réinitialiser la fiche
        self.selected_fiche = ""
    
    @rx.event
    def set_fiche_search(self, value: str):
        """Met à jour la recherche de fiche."""
        self.fiche_search = value
    
    @rx.event
    def select_fiche(self, code: str, description: str):
        """Sélectionne une fiche."""
        self.selected_fiche = code
        self.selected_fiche_description = description
    
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
        """Charge les fiches (placeholder)."""
        self.is_loading = True
        yield
        import asyncio
        await asyncio.sleep(0.3)
        self.is_loading = False
    
    @rx.event
    async def execute_simulation(self):
        """Exécute la simulation (calcul de démonstration)."""
        self.is_loading = True
        self.calculation_error = ""
        yield
        
        try:
            import asyncio
            await asyncio.sleep(1)  # Simuler un calcul
            
            # Calcul de démonstration basé sur la fiche
            base_cumacs = {
                "BAR-EN-101": 125000,
                "BAR-EN-102": 89000,
                "BAR-EN-103": 67000,
                "BAR-EN-104": 45000,
                "BAR-EN-105": 78000,
                "BAR-TH-104": 150000,
                "BAR-TH-106": 95000,
                "BAR-TH-113": 180000,
                "BAR-TH-159": 120000,
                "BAR-EQ-110": 25000,
                "BAR-EQ-111": 35000,
                "BAR-SE-101": 200000,
            }.get(self.selected_fiche, 50000)
            
            # Ajuster selon la zone climatique
            zone_coef = {"H1": 1.2, "H2": 1.0, "H3": 0.8}.get(self.zone_climatique, 1.0)
            
            self.result_cumacs = float(base_cumacs * zone_coef)
            self.result_euros = float(self.result_cumacs * 0.0065)  # Prix du kWh cumac
            
            self.is_loading = False
            yield rx.redirect("/simulation/result")
            
        except Exception as e:
            self.calculation_error = str(e)
            self.is_loading = False
            yield rx.toast(f"Erreur: {str(e)}", duration=5000)
    
    @rx.event
    def save_simulation(self, user_id: str):
        """Sauvegarde la simulation (placeholder)."""
        if not self.simulation_saved:
            self.simulation_saved = True
            return rx.toast("Simulation sauvegardée !", duration=3000)
    
    @rx.event
    def start_new_simulation(self):
        """Démarre une nouvelle simulation."""
        self.reset_simulation()
        return rx.redirect("/simulation/date-department")