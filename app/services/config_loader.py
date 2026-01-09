"""
Service de chargement des fichiers de configuration depuis Supabase.
Gère le chargement dynamique des fiches, secteurs, typologies et configurations de simulation.
"""

import json
from typing import Optional, Dict, List, Any
from dataclasses import dataclass
from .supabase_client import get_supabase_client, read_file_from_bucket, BUCKET_NAME


@dataclass
class FicheConfig:
    """Configuration complète d'une fiche de simulation."""
    code: str
    description: str
    function_param_values: Dict[str, Any]  # Options des inputs
    variables_mapping: Dict[str, Any]       # Mapping label → valeur
    variables_matching: Dict[str, str]      # Association label → paramètre
    string_function: str                     # Code de calcul


class ConfigLoader:
    """Service de chargement des configurations."""
    
    @staticmethod
    def load_sectors() -> List[Dict[str, Any]]:
        """
        Charge la liste des secteurs depuis Supabase ou retourne les valeurs par défaut.
        
        Returns:
            Liste des secteurs avec label, icon, value, abbr
        """
        # Valeurs par défaut (depuis variables.py existant)
        default_sectors = [
            {"label": "Industrie", "icon": "factory", "value": "Industrie", "abbr": "IND"},
            {"label": "Résidentiel", "icon": "house", "value": "Résidentiel", "abbr": "BAR"},
            {"label": "Tertiaire", "icon": "building-2", "value": "Tertiaire", "abbr": "BAT"},
            {"label": "Réseaux", "icon": "network", "value": "Réseaux", "abbr": "RES"},
            {"label": "Agriculture", "icon": "carrot", "value": "Agriculture", "abbr": "AGRI"},
            {"label": "Transport", "icon": "bus", "value": "Transport", "abbr": "TRA"},
        ]
        
        # Tentative de chargement depuis Supabase
        client = get_supabase_client()
        if client:
            try:
                response = client.table("sectors").select("*").order("display_order").execute()
                if response.data:
                    return response.data
            except Exception as e:
                print(f"⚠️ Utilisation des secteurs par défaut: {e}")
        
        return default_sectors
    
    @staticmethod
    def load_typologies(sector: str = "") -> List[Dict[str, Any]]:
        """
        Charge les typologies pour un secteur donné.
        
        Args:
            sector: Nom du secteur (optionnel, retourne tout si vide)
            
        Returns:
            Liste des typologies avec name, icon, abbr
        """
        # Mapping secteur → typologies par défaut
        sector_typology_map = {
            'Industrie': {'Utilité': 'UT', 'Bâtiment': 'BA'},
            'Résidentiel': {'Enveloppe': 'EN', 'Thermique': 'TH', 'Équipement': 'EQ', 'Service': 'SE'},
            'Tertiaire': {'Enveloppe': 'EN', 'Thermique': 'TH', 'Équipement': 'EQ', 'Service': 'SE'},
            'Réseaux': {'Eclairage': 'EC', 'Chaleur': 'CH'},
            'Agriculture': {'Utilité': 'UT', 'Thermique': 'TH', 'Équipement': 'EQ', 'Service': 'SE'},
            'Transport': {'Équipement': 'EQ', 'Service': 'SE'},
        }
        
        # Mapping icônes
        icon_map = {
            'Utilité': "plug",
            'Bâtiment': "building",
            'Enveloppe': "layers",
            'Thermique': "flame",
            'Équipement': "cpu",
            'Service': "briefcase",
            'Eclairage': "lightbulb",
            'Chaleur': "thermometer",
        }
        
        # Tentative de chargement depuis Supabase
        client = get_supabase_client()
        if client:
            try:
                query = client.table("typologies").select("*")
                if sector:
                    query = query.eq("sector", sector)
                response = query.order("display_order").execute()
                if response.data:
                    return response.data
            except Exception as e:
                print(f"⚠️ Utilisation des typologies par défaut: {e}")
        
        # Retourner les typologies par défaut
        if sector and sector in sector_typology_map:
            typologies = sector_typology_map[sector]
        else:
            # Toutes les typologies uniques
            typologies = {}
            for sector_typos in sector_typology_map.values():
                typologies.update(sector_typos)
        
        return [
            {
                "name": name,
                "abbr": abbr,
                "icon": icon_map.get(name, "circle-help")
            }
            for name, abbr in typologies.items()
        ]
    
    @staticmethod
    def get_sector_typology_map() -> Dict[str, Dict[str, str]]:
        """
        Retourne le mapping complet secteur → typologies.
        
        Returns:
            Dict avec secteur comme clé et dict de typologies comme valeur
        """
        return {
            'Industrie': {'Utilité': 'UT', 'Bâtiment': 'BA'},
            'Résidentiel': {'Enveloppe': 'EN', 'Thermique': 'TH', 'Équipement': 'EQ', 'Service': 'SE'},
            'Tertiaire': {'Enveloppe': 'EN', 'Thermique': 'TH', 'Équipement': 'EQ', 'Service': 'SE'},
            'Réseaux': {'Eclairage': 'EC', 'Chaleur': 'CH'},
            'Agriculture': {'Utilité': 'UT', 'Thermique': 'TH', 'Équipement': 'EQ', 'Service': 'SE'},
            'Transport': {'Équipement': 'EQ', 'Service': 'SE'},
        }
    
    @staticmethod
    def load_fiches(sector_abbr: str, typology_abbr: str) -> Dict[str, str]:
        """
        Charge la liste des fiches pour un secteur et une typologie.
        
        Args:
            sector_abbr: Abréviation du secteur (ex: "BAR")
            typology_abbr: Abréviation de la typologie (ex: "TH")
            
        Returns:
            Dict avec code fiche comme clé et description comme valeur
        """
        prefix = f"{sector_abbr}-{typology_abbr}-"
        
        # Tentative de chargement depuis Supabase table
        client = get_supabase_client()
        if client:
            try:
                response = client.table("documents").select(
                    "id, title, description"
                ).like("id", f"{prefix}%").execute()
                
                if response.data:
                    return {
                        doc["id"]: doc.get("description", doc.get("title", ""))
                        for doc in response.data
                    }
            except Exception as e:
                print(f"⚠️ Erreur chargement fiches: {e}")
        
        # Fallback: lecture du fichier JSON local ou retour vide
        return {}
    
    @staticmethod
    def load_fiche_config(fiche_code: str) -> Optional[FicheConfig]:
        """
        Charge la configuration complète d'une fiche depuis Supabase Storage.
        
        Args:
            fiche_code: Code de la fiche (ex: "BAR-TH-101")
            
        Returns:
            FicheConfig ou None si erreur
        """
        base_path = fiche_code
        
        try:
            # Chargement des 4 fichiers de configuration
            function_param_values = read_file_from_bucket(
                BUCKET_NAME,
                f"{base_path}/function_param_values_labeled.json",
                "json"
            )
            
            variables_mapping = read_file_from_bucket(
                BUCKET_NAME,
                f"{base_path}/variables_mapping.json",
                "json"
            )
            
            variables_matching = read_file_from_bucket(
                BUCKET_NAME,
                f"{base_path}/variables_matching.json",
                "json"
            )
            
            string_function = read_file_from_bucket(
                BUCKET_NAME,
                f"{base_path}/string_function.txt",
                "txt"
            )
            
            # Vérification que tous les fichiers ont été chargés
            if all([function_param_values, variables_mapping, variables_matching, string_function]):
                return FicheConfig(
                    code=fiche_code,
                    description="",
                    function_param_values=function_param_values,
                    variables_mapping=variables_mapping,
                    variables_matching=variables_matching,
                    string_function=string_function
                )
            else:
                print(f"❌ Fichiers manquants pour {fiche_code}")
                return None
                
        except Exception as e:
            print(f"❌ Erreur chargement config {fiche_code}: {e}")
            return None
    
    @staticmethod
    def get_departments() -> Dict[str, str]:
        """
        Retourne la liste des départements français.
        
        Returns:
            Dict avec nom du département comme clé et slug comme valeur
        """
        return {
            "Ain (01)": "ain",
            "Aisne (02)": "aisne",
            "Allier (03)": "allier",
            "Alpes-de-Haute-Provence (04)": "alpes-de-haute-provence",
            "Hautes-Alpes (05)": "hautes-alpes",
            "Alpes-Maritimes (06)": "alpes-maritimes",
            "Ardèche (07)": "ardeche",
            "Ardennes (08)": "ardennes",
            "Ariège (09)": "ariege",
            "Aube (10)": "aube",
            "Aude (11)": "aude",
            "Aveyron (12)": "aveyron",
            "Bouches-du-Rhône (13)": "bouches-du-rhone",
            "Calvados (14)": "calvados",
            "Cantal (15)": "cantal",
            "Charente (16)": "charente",
            "Charente-Maritime (17)": "charente-maritime",
            "Cher (18)": "cher",
            "Corrèze (19)": "correze",
            "Corse-du-Sud (2A)": "corse-du-sud",
            "Haute-Corse (2B)": "haute-corse",
            "Côte-d'Or (21)": "cote-d-or",
            "Côtes-d'Armor (22)": "cotes-d-armor",
            "Creuse (23)": "creuse",
            "Dordogne (24)": "dordogne",
            "Doubs (25)": "doubs",
            "Drôme (26)": "drome",
            "Eure (27)": "eure",
            "Eure-et-Loir (28)": "eure-et-loir",
            "Finistère (29)": "finistere",
            "Gard (30)": "gard",
            "Haute-Garonne (31)": "haute-garonne",
            "Gers (32)": "gers",
            "Gironde (33)": "gironde",
            "Hérault (34)": "herault",
            "Ille-et-Vilaine (35)": "ille-et-vilaine",
            "Indre (36)": "indre",
            "Indre-et-Loire (37)": "indre-et-loire",
            "Isère (38)": "isere",
            "Jura (39)": "jura",
            "Landes (40)": "landes",
            "Loir-et-Cher (41)": "loir-et-cher",
            "Loire (42)": "loire",
            "Haute-Loire (43)": "haute-loire",
            "Loire-Atlantique (44)": "loire-atlantique",
            "Loiret (45)": "loiret",
            "Lot (46)": "lot",
            "Lot-et-Garonne (47)": "lot-et-garonne",
            "Lozère (48)": "lozere",
            "Maine-et-Loire (49)": "maine-et-loire",
            "Manche (50)": "manche",
            "Marne (51)": "marne",
            "Haute-Marne (52)": "haute-marne",
            "Mayenne (53)": "mayenne",
            "Meurthe-et-Moselle (54)": "meurthe-et-moselle",
            "Meuse (55)": "meuse",
            "Morbihan (56)": "morbihan",
            "Moselle (57)": "moselle",
            "Nièvre (58)": "nievre",
            "Nord (59)": "nord",
            "Oise (60)": "oise",
            "Orne (61)": "orne",
            "Pas-de-Calais (62)": "pas-de-calais",
            "Puy-de-Dôme (63)": "puy-de-dome",
            "Pyrénées-Atlantiques (64)": "pyrenees-atlantiques",
            "Hautes-Pyrénées (65)": "hautes-pyrenees",
            "Pyrénées-Orientales (66)": "pyrenees-orientales",
            "Bas-Rhin (67)": "bas-rhin",
            "Haut-Rhin (68)": "haut-rhin",
            "Rhône (69)": "rhone",
            "Haute-Saône (70)": "haute-saone",
            "Saône-et-Loire (71)": "saone-et-loire",
            "Sarthe (72)": "sarthe",
            "Savoie (73)": "savoie",
            "Haute-Savoie (74)": "haute-savoie",
            "Paris (75)": "paris",
            "Seine-Maritime (76)": "seine-maritime",
            "Seine-et-Marne (77)": "seine-et-marne",
            "Yvelines (78)": "yvelines",
            "Deux-Sèvres (79)": "deux-sevres",
            "Somme (80)": "somme",
            "Tarn (81)": "tarn",
            "Tarn-et-Garonne (82)": "tarn-et-garonne",
            "Var (83)": "var",
            "Vaucluse (84)": "vaucluse",
            "Vendée (85)": "vendee",
            "Vienne (86)": "vienne",
            "Haute-Vienne (87)": "haute-vienne",
            "Vosges (88)": "vosges",
            "Yonne (89)": "yonne",
            "Territoire de Belfort (90)": "territoire-de-belfort",
            "Essonne (91)": "essonne",
            "Hauts-de-Seine (92)": "hauts-de-seine",
            "Seine-Saint-Denis (93)": "seine-saint-denis",
            "Val-de-Marne (94)": "val-de-marne",
            "Val-d'Oise (95)": "val-d-oise",
            "Guadeloupe (971)": "guadeloupe",
            "Martinique (972)": "martinique",
            "Guyane (973)": "guyane",
            "La Réunion (974)": "la-reunion",
            "Mayotte (976)": "mayotte"
        }


# Instance singleton
config_loader = ConfigLoader()
