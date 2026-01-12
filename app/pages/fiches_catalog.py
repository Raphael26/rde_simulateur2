"""Page Catalogue des Fiches CEE"""
import reflex as rx
from typing import List, Dict
from ..state import SimulationState
from ..styles.design_system import Colors, Typography, Spacing, Borders, Shadows
from ..components.sidebar import sidebar


# ============================================
# DONNÉES DES FICHES CEE
# ============================================

# Mapping secteur -> abbr
SECTOR_MAPPING = {
    "BAR": {"name": "Résidentiel", "icon": "house"},
    "BAT": {"name": "Tertiaire", "icon": "building-2"},
    "IND": {"name": "Industrie", "icon": "factory"},
    "AGRI": {"name": "Agriculture", "icon": "carrot"},
    "TRA": {"name": "Transport", "icon": "bus"},
    "RES": {"name": "Réseaux", "icon": "network"},
}

# Mapping typologie -> abbr
TYPOLOGY_MAPPING = {
    "EN": {"name": "Enveloppe", "icon": "home"},
    "TH": {"name": "Thermique", "icon": "flame"},
    "EQ": {"name": "Équipement", "icon": "cpu"},
    "SE": {"name": "Service", "icon": "briefcase"},
    "UT": {"name": "Utilité", "icon": "plug"},
    "BA": {"name": "Bâtiment", "icon": "building"},
    "CH": {"name": "Chaleur", "icon": "thermometer"},
    "EC": {"name": "Éclairage", "icon": "lightbulb"},
}

# Liste complète des fiches CEE
ALL_FICHES = [
    # RÉSIDENTIEL - Enveloppe
    {"code": "BAR-EN-101", "description": "Isolation de combles ou de toiture", "sector": "Résidentiel", "sector_abbr": "BAR", "typology": "Enveloppe", "typology_abbr": "EN"},
    {"code": "BAR-EN-102", "description": "Isolation des murs", "sector": "Résidentiel", "sector_abbr": "BAR", "typology": "Enveloppe", "typology_abbr": "EN"},
    {"code": "BAR-EN-103", "description": "Isolation d'un plancher", "sector": "Résidentiel", "sector_abbr": "BAR", "typology": "Enveloppe", "typology_abbr": "EN"},
    {"code": "BAR-EN-104", "description": "Fenêtre ou porte-fenêtre complète avec vitrage isolant", "sector": "Résidentiel", "sector_abbr": "BAR", "typology": "Enveloppe", "typology_abbr": "EN"},
    {"code": "BAR-EN-105", "description": "Isolation des toitures terrasses", "sector": "Résidentiel", "sector_abbr": "BAR", "typology": "Enveloppe", "typology_abbr": "EN"},
    {"code": "BAR-EN-108", "description": "Fermeture isolante", "sector": "Résidentiel", "sector_abbr": "BAR", "typology": "Enveloppe", "typology_abbr": "EN"},
    
    # RÉSIDENTIEL - Thermique
    {"code": "BAR-TH-101", "description": "Chauffe-eau solaire individuel (France métropolitaine)", "sector": "Résidentiel", "sector_abbr": "BAR", "typology": "Thermique", "typology_abbr": "TH"},
    {"code": "BAR-TH-104", "description": "Pompe à chaleur de type air/eau ou eau/eau", "sector": "Résidentiel", "sector_abbr": "BAR", "typology": "Thermique", "typology_abbr": "TH"},
    {"code": "BAR-TH-106", "description": "Chaudière individuelle à haute performance énergétique", "sector": "Résidentiel", "sector_abbr": "BAR", "typology": "Thermique", "typology_abbr": "TH"},
    {"code": "BAR-TH-112", "description": "Appareil indépendant de chauffage au bois", "sector": "Résidentiel", "sector_abbr": "BAR", "typology": "Thermique", "typology_abbr": "TH"},
    {"code": "BAR-TH-113", "description": "Chaudière biomasse individuelle", "sector": "Résidentiel", "sector_abbr": "BAR", "typology": "Thermique", "typology_abbr": "TH"},
    {"code": "BAR-TH-117", "description": "Robinet thermostatique", "sector": "Résidentiel", "sector_abbr": "BAR", "typology": "Thermique", "typology_abbr": "TH"},
    {"code": "BAR-TH-125", "description": "Système de ventilation double flux autoréglable", "sector": "Résidentiel", "sector_abbr": "BAR", "typology": "Thermique", "typology_abbr": "TH"},
    {"code": "BAR-TH-127", "description": "Ventilation mécanique simple flux hygroréglable", "sector": "Résidentiel", "sector_abbr": "BAR", "typology": "Thermique", "typology_abbr": "TH"},
    {"code": "BAR-TH-129", "description": "Pompe à chaleur de type air/air", "sector": "Résidentiel", "sector_abbr": "BAR", "typology": "Thermique", "typology_abbr": "TH"},
    {"code": "BAR-TH-148", "description": "Chauffe-eau thermodynamique à accumulation", "sector": "Résidentiel", "sector_abbr": "BAR", "typology": "Thermique", "typology_abbr": "TH"},
    {"code": "BAR-TH-159", "description": "Pompe à chaleur hybride individuelle", "sector": "Résidentiel", "sector_abbr": "BAR", "typology": "Thermique", "typology_abbr": "TH"},
    {"code": "BAR-TH-171", "description": "Pompe à chaleur de type air/eau", "sector": "Résidentiel", "sector_abbr": "BAR", "typology": "Thermique", "typology_abbr": "TH"},
    {"code": "BAR-TH-172", "description": "Pompe à chaleur de type eau/eau ou sol/eau", "sector": "Résidentiel", "sector_abbr": "BAR", "typology": "Thermique", "typology_abbr": "TH"},
    
    # RÉSIDENTIEL - Équipement
    {"code": "BAR-EQ-110", "description": "Luminaire à modules LED avec dispositif de contrôle", "sector": "Résidentiel", "sector_abbr": "BAR", "typology": "Équipement", "typology_abbr": "EQ"},
    {"code": "BAR-EQ-115", "description": "Dispositif d'affichage et d'interprétation des consommations", "sector": "Résidentiel", "sector_abbr": "BAR", "typology": "Équipement", "typology_abbr": "EQ"},
    
    # RÉSIDENTIEL - Service
    {"code": "BAR-SE-104", "description": "Réglage des organes d'équilibrage d'une installation de chauffage", "sector": "Résidentiel", "sector_abbr": "BAR", "typology": "Service", "typology_abbr": "SE"},
    {"code": "BAR-SE-106", "description": "Service de suivi des consommations d'énergie", "sector": "Résidentiel", "sector_abbr": "BAR", "typology": "Service", "typology_abbr": "SE"},
    {"code": "BAR-SE-108", "description": "Désembouage d'un réseau hydraulique individuel", "sector": "Résidentiel", "sector_abbr": "BAR", "typology": "Service", "typology_abbr": "SE"},
    
    # TERTIAIRE - Enveloppe
    {"code": "BAT-EN-101", "description": "Isolation de combles ou de toitures", "sector": "Tertiaire", "sector_abbr": "BAT", "typology": "Enveloppe", "typology_abbr": "EN"},
    {"code": "BAT-EN-102", "description": "Isolation des murs", "sector": "Tertiaire", "sector_abbr": "BAT", "typology": "Enveloppe", "typology_abbr": "EN"},
    {"code": "BAT-EN-103", "description": "Isolation d'un plancher", "sector": "Tertiaire", "sector_abbr": "BAT", "typology": "Enveloppe", "typology_abbr": "EN"},
    {"code": "BAT-EN-104", "description": "Fenêtre ou porte-fenêtre complète avec vitrage isolant", "sector": "Tertiaire", "sector_abbr": "BAT", "typology": "Enveloppe", "typology_abbr": "EN"},
    {"code": "BAT-EN-107", "description": "Isolation des toitures-terrasses", "sector": "Tertiaire", "sector_abbr": "BAT", "typology": "Enveloppe", "typology_abbr": "EN"},
    
    # TERTIAIRE - Thermique
    {"code": "BAT-TH-103", "description": "Plancher chauffant hydraulique à basse température", "sector": "Tertiaire", "sector_abbr": "BAT", "typology": "Thermique", "typology_abbr": "TH"},
    {"code": "BAT-TH-113", "description": "Pompe à chaleur de type air/eau ou eau/eau", "sector": "Tertiaire", "sector_abbr": "BAT", "typology": "Thermique", "typology_abbr": "TH"},
    {"code": "BAT-TH-116", "description": "Système de gestion technique du bâtiment", "sector": "Tertiaire", "sector_abbr": "BAT", "typology": "Thermique", "typology_abbr": "TH"},
    {"code": "BAT-TH-125", "description": "Ventilation mécanique simple flux", "sector": "Tertiaire", "sector_abbr": "BAT", "typology": "Thermique", "typology_abbr": "TH"},
    {"code": "BAT-TH-126", "description": "Ventilation mécanique double flux avec échangeur", "sector": "Tertiaire", "sector_abbr": "BAT", "typology": "Thermique", "typology_abbr": "TH"},
    {"code": "BAT-TH-157", "description": "Chaudière biomasse collective", "sector": "Tertiaire", "sector_abbr": "BAT", "typology": "Thermique", "typology_abbr": "TH"},
    
    # TERTIAIRE - Équipement
    {"code": "BAT-EQ-117", "description": "Installation frigorifique utilisant du CO2", "sector": "Tertiaire", "sector_abbr": "BAT", "typology": "Équipement", "typology_abbr": "EQ"},
    {"code": "BAT-EQ-127", "description": "Luminaire à modules LED", "sector": "Tertiaire", "sector_abbr": "BAT", "typology": "Équipement", "typology_abbr": "EQ"},
    {"code": "BAT-EQ-133", "description": "Systèmes hydro-économes", "sector": "Tertiaire", "sector_abbr": "BAT", "typology": "Équipement", "typology_abbr": "EQ"},
    
    # INDUSTRIE - Utilité
    {"code": "IND-UT-102", "description": "Système de variation électronique de vitesse", "sector": "Industrie", "sector_abbr": "IND", "typology": "Utilité", "typology_abbr": "UT"},
    {"code": "IND-UT-103", "description": "Système de récupération de chaleur sur un compresseur d'air", "sector": "Industrie", "sector_abbr": "IND", "typology": "Utilité", "typology_abbr": "UT"},
    {"code": "IND-UT-104", "description": "Économiseur sur les effluents gazeux d'une chaudière", "sector": "Industrie", "sector_abbr": "IND", "typology": "Utilité", "typology_abbr": "UT"},
    {"code": "IND-UT-113", "description": "Système de condensation frigorifique à haute efficacité", "sector": "Industrie", "sector_abbr": "IND", "typology": "Utilité", "typology_abbr": "UT"},
    {"code": "IND-UT-114", "description": "Moto-variateur synchrone à aimants permanents", "sector": "Industrie", "sector_abbr": "IND", "typology": "Utilité", "typology_abbr": "UT"},
    {"code": "IND-UT-116", "description": "Système de régulation sur un groupe de production de froid", "sector": "Industrie", "sector_abbr": "IND", "typology": "Utilité", "typology_abbr": "UT"},
    {"code": "IND-UT-121", "description": "Isolation de points singuliers d'un réseau", "sector": "Industrie", "sector_abbr": "IND", "typology": "Utilité", "typology_abbr": "UT"},
    {"code": "IND-UT-131", "description": "Isolation thermique des parois planes ou cylindriques", "sector": "Industrie", "sector_abbr": "IND", "typology": "Utilité", "typology_abbr": "UT"},
    
    # INDUSTRIE - Bâtiment
    {"code": "IND-BA-110", "description": "Déstratificateur ou brasseur d'air", "sector": "Industrie", "sector_abbr": "IND", "typology": "Bâtiment", "typology_abbr": "BA"},
    {"code": "IND-BA-116", "description": "Luminaires à modules LED", "sector": "Industrie", "sector_abbr": "IND", "typology": "Bâtiment", "typology_abbr": "BA"},
    
    # AGRICULTURE - Thermique
    {"code": "AGRI-TH-104", "description": "Système de récupération de chaleur sur groupe de production de froid", "sector": "Agriculture", "sector_abbr": "AGRI", "typology": "Thermique", "typology_abbr": "TH"},
    {"code": "AGRI-TH-108", "description": "Pompe à chaleur de type air/eau ou eau/eau", "sector": "Agriculture", "sector_abbr": "AGRI", "typology": "Thermique", "typology_abbr": "TH"},
    
    # AGRICULTURE - Équipement
    {"code": "AGRI-EQ-102", "description": "Double écran thermique", "sector": "Agriculture", "sector_abbr": "AGRI", "typology": "Équipement", "typology_abbr": "EQ"},
    {"code": "AGRI-EQ-111", "description": "Simple écran thermique", "sector": "Agriculture", "sector_abbr": "AGRI", "typology": "Équipement", "typology_abbr": "EQ"},
    
    # TRANSPORT - Équipement
    {"code": "TRA-EQ-103", "description": "Télématique embarquée pour le suivi de la conduite", "sector": "Transport", "sector_abbr": "TRA", "typology": "Équipement", "typology_abbr": "EQ"},
    {"code": "TRA-EQ-114", "description": "Achat ou location d'un véhicule léger électrique", "sector": "Transport", "sector_abbr": "TRA", "typology": "Équipement", "typology_abbr": "EQ"},
    {"code": "TRA-EQ-121", "description": "Vélo à assistance électrique", "sector": "Transport", "sector_abbr": "TRA", "typology": "Équipement", "typology_abbr": "EQ"},
    
    # TRANSPORT - Service
    {"code": "TRA-SE-101", "description": "Formation d'un chauffeur de transport à la conduite économe", "sector": "Transport", "sector_abbr": "TRA", "typology": "Service", "typology_abbr": "SE"},
    {"code": "TRA-SE-102", "description": "Formation d'un chauffeur de véhicule léger à la conduite économe", "sector": "Transport", "sector_abbr": "TRA", "typology": "Service", "typology_abbr": "SE"},
    
    # RÉSEAUX - Chaleur
    {"code": "RES-CH-104", "description": "Réhabilitation d'un poste de livraison de chaleur résidentiel", "sector": "Réseaux", "sector_abbr": "RES", "typology": "Chaleur", "typology_abbr": "CH"},
    {"code": "RES-CH-106", "description": "Mise en place d'un calorifugeage des canalisations", "sector": "Réseaux", "sector_abbr": "RES", "typology": "Chaleur", "typology_abbr": "CH"},
    
    # RÉSEAUX - Éclairage
    {"code": "RES-EC-104", "description": "Rénovation d'éclairage extérieur", "sector": "Réseaux", "sector_abbr": "RES", "typology": "Éclairage", "typology_abbr": "EC"},
]


# ============================================
# STATE DU CATALOGUE
# ============================================

class CatalogState(rx.State):
    """État du catalogue des fiches."""
    
    search_query: str = ""
    selected_sector: str = ""
    selected_typology: str = ""
    
    @rx.var
    def all_sectors(self) -> List[str]:
        """Liste unique des secteurs."""
        return list(set(f["sector"] for f in ALL_FICHES))
    
    @rx.var
    def all_typologies(self) -> List[str]:
        """Liste unique des typologies."""
        return list(set(f["typology"] for f in ALL_FICHES))
    
    @rx.var
    def filtered_fiches(self) -> List[Dict]:
        """Fiches filtrées par recherche, secteur et typologie."""
        result = ALL_FICHES
        
        # Filtre par secteur
        if self.selected_sector:
            result = [f for f in result if f["sector"] == self.selected_sector]
        
        # Filtre par typologie
        if self.selected_typology:
            result = [f for f in result if f["typology"] == self.selected_typology]
        
        # Filtre par recherche
        if self.search_query:
            search = self.search_query.lower()
            result = [f for f in result if search in f["code"].lower() or search in f["description"].lower()]
        
        return result
    
    @rx.var
    def fiches_count(self) -> int:
        """Nombre de fiches filtrées."""
        return len(self.filtered_fiches)
    
    @rx.event
    def set_search(self, value: str):
        """Met à jour la recherche."""
        self.search_query = value
    
    @rx.event
    def set_sector_filter(self, value: str):
        """Met à jour le filtre secteur."""
        self.selected_sector = value if value != "Tous" else ""
    
    @rx.event
    def set_typology_filter(self, value: str):
        """Met à jour le filtre typologie."""
        self.selected_typology = value if value != "Toutes" else ""
    
    @rx.event
    def clear_filters(self):
        """Réinitialise tous les filtres."""
        self.search_query = ""
        self.selected_sector = ""
        self.selected_typology = ""


# ============================================
# COMPOSANTS UI
# ============================================

def sector_badge(sector: str) -> rx.Component:
    """Badge de secteur avec couleur."""
    colors = {
        "Résidentiel": Colors.PRIMARY,
        "Tertiaire": Colors.INFO,
        "Industrie": "#f59e0b",
        "Agriculture": "#22c55e",
        "Transport": "#8b5cf6",
        "Réseaux": "#ec4899",
    }
    color = colors.get(sector, Colors.GRAY_500)
    
    return rx.box(
        rx.text(sector, font_size=Typography.SIZE_XS, color=color, font_weight=Typography.WEIGHT_MEDIUM),
        padding="4px 8px",
        background=f"{color}15",
        border_radius=Borders.RADIUS_FULL,
    )


def typology_badge(typology: str) -> rx.Component:
    """Badge de typologie."""
    return rx.box(
        rx.text(typology, font_size=Typography.SIZE_XS, color=Colors.GRAY_600),
        padding="4px 8px",
        background=Colors.GRAY_100,
        border_radius=Borders.RADIUS_FULL,
    )


def fiche_card(fiche: Dict) -> rx.Component:
    """Carte d'une fiche CEE."""
    return rx.box(
        rx.vstack(
            # Header avec code et badges
            rx.hstack(
                rx.box(
                    rx.text(fiche["code"], font_weight=Typography.WEIGHT_BOLD, font_size=Typography.SIZE_BASE, color=Colors.PRIMARY),
                    padding="6px 12px",
                    background=Colors.PRIMARY_LIGHTER,
                    border_radius=Borders.RADIUS_MD,
                ),
                rx.spacer(),
                sector_badge(fiche["sector"]),
                typology_badge(fiche["typology"]),
                width="100%",
                align="center",
                flex_wrap="wrap",
                gap="2",
            ),
            
            # Description
            rx.text(
                fiche["description"],
                font_size=Typography.SIZE_SM,
                color=Colors.GRAY_700,
                line_height="1.5",
            ),
            
            # Bouton simuler
            rx.button(
                rx.hstack(
                    rx.icon("play", size=16),
                    rx.text("Simuler cette fiche"),
                    spacing="2",
                    align="center",
                ),
                on_click=SimulationState.select_fiche_from_catalog(
                    fiche["code"],
                    fiche["description"],
                    fiche["sector"],
                    fiche["sector_abbr"],
                    fiche["typology"],
                    fiche["typology_abbr"],
                ),
                width="100%",
                size="2",
                style={
                    "background": Colors.PRIMARY,
                    "color": Colors.WHITE,
                    "_hover": {"background": "#2d6b62"},
                },
            ),
            
            spacing="4",
            align="start",
            width="100%",
        ),
        padding=Spacing.LG,
        background=Colors.WHITE,
        border_radius=Borders.RADIUS_XL,
        box_shadow=Shadows.SM,
        border=f"1px solid {Colors.GRAY_100}",
        _hover={"box_shadow": Shadows.MD, "border_color": Colors.PRIMARY},
        transition="all 0.2s ease",
        width="100%",
    )


def filter_section() -> rx.Component:
    """Section des filtres."""
    return rx.box(
        rx.vstack(
            # Barre de recherche
            rx.box(
                rx.hstack(
                    rx.icon("search", size=18, color=Colors.GRAY_400),
                    rx.input(
                        placeholder="Rechercher par code ou description...",
                        value=CatalogState.search_query,
                        on_change=CatalogState.set_search,
                        width="100%",
                        variant="soft",
                        size="3",
                    ),
                    spacing="3",
                    align="center",
                    width="100%",
                ),
                width="100%",
            ),
            
            # Filtres secteur et typologie
            rx.hstack(
                # Filtre Secteur
                rx.box(
                    rx.select.root(
                        rx.select.trigger(placeholder="Secteur"),
                        rx.select.content(
                            rx.select.item("Tous", value="Tous"),
                            rx.select.item("Résidentiel", value="Résidentiel"),
                            rx.select.item("Tertiaire", value="Tertiaire"),
                            rx.select.item("Industrie", value="Industrie"),
                            rx.select.item("Agriculture", value="Agriculture"),
                            rx.select.item("Transport", value="Transport"),
                            rx.select.item("Réseaux", value="Réseaux"),
                        ),
                        on_change=CatalogState.set_sector_filter,
                    ),
                    flex="1",
                ),
                
                # Filtre Typologie
                rx.box(
                    rx.select.root(
                        rx.select.trigger(placeholder="Typologie"),
                        rx.select.content(
                            rx.select.item("Toutes", value="Toutes"),
                            rx.select.item("Enveloppe", value="Enveloppe"),
                            rx.select.item("Thermique", value="Thermique"),
                            rx.select.item("Équipement", value="Équipement"),
                            rx.select.item("Service", value="Service"),
                            rx.select.item("Utilité", value="Utilité"),
                            rx.select.item("Bâtiment", value="Bâtiment"),
                            rx.select.item("Chaleur", value="Chaleur"),
                            rx.select.item("Éclairage", value="Éclairage"),
                        ),
                        on_change=CatalogState.set_typology_filter,
                    ),
                    flex="1",
                ),
                
                # Bouton reset
                rx.button(
                    rx.hstack(rx.icon("x", size=16), rx.text("Réinitialiser"), spacing="2", align="center"),
                    on_click=CatalogState.clear_filters,
                    variant="outline",
                    size="2",
                ),
                
                spacing="3",
                width="100%",
                flex_wrap="wrap",
            ),
            
            spacing="4",
            width="100%",
        ),
        padding=Spacing.LG,
        background=Colors.WHITE,
        border_radius=Borders.RADIUS_XL,
        box_shadow=Shadows.SM,
        border=f"1px solid {Colors.GRAY_100}",
        width="100%",
    )


def catalog_content() -> rx.Component:
    """Contenu principal du catalogue."""
    return rx.vstack(
        # Header
        rx.hstack(
            rx.vstack(
                rx.text("Catalogue des fiches CEE", font_size=Typography.SIZE_2XL, font_weight=Typography.WEIGHT_BOLD, color=Colors.GRAY_900),
                rx.text("Parcourez les opérations standardisées et lancez une simulation", font_size=Typography.SIZE_BASE, color=Colors.GRAY_500),
                spacing="1",
                align="start",
            ),
            rx.spacer(),
            rx.link(
                rx.button(
                    rx.hstack(rx.icon("arrow-left", size=18), rx.text("Retour"), spacing="2", align="center"),
                    variant="outline",
                    size="3",
                ),
                href="/dashboard",
            ),
            width="100%",
            align="center",
        ),
        
        # Filtres
        filter_section(),
        
        # Compteur de résultats
        rx.hstack(
            rx.icon("file-text", size=16, color=Colors.GRAY_500),
            rx.text(
                CatalogState.fiches_count,
                font_weight=Typography.WEIGHT_SEMIBOLD,
                color=Colors.PRIMARY,
            ),
            rx.text("fiche(s) trouvée(s)", color=Colors.GRAY_500),
            spacing="2",
            align="center",
        ),
        
        # Grille des fiches
        rx.box(
            rx.foreach(
                CatalogState.filtered_fiches,
                fiche_card,
            ),
            display="grid",
            grid_template_columns="repeat(auto-fill, minmax(350px, 1fr))",
            gap=Spacing.LG,
            width="100%",
        ),
        
        spacing="6",
        align="start",
        width="100%",
    )


# ============================================
# PAGE
# ============================================

@rx.page(route="/fiches", title="Catalogue des fiches CEE - RDE Consulting")
def fiches_catalog_page() -> rx.Component:
    return rx.flex(
        # Sidebar
        sidebar(current_page="fiches"),
        
        # Contenu principal
        rx.box(
            rx.box(
                catalog_content(),
                width="100%",
                max_width="1400px",
                margin="0 auto",
            ),
            min_height="100vh",
            background=Colors.BG_PAGE,
            padding="40px",
            flex="1",
            width="100%",
        ),
        direction="row",
        width="100%",
        min_height="100vh",
        background=Colors.BG_PAGE,
    )