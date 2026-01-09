"""Page Dashboard - Tableau de bord"""
#import reflex as rx
#from ..state import SimulationState, DashboardState
#from ..styles.design_system import Colors, Typography, Spacing, Borders, Shadows
#from ..components.sidebar import sidebar
#
#
## ============================================
## COMPOSANTS DU DASHBOARD
## ============================================
#
#def stat_card(title: str, value: str, subtitle: str, icon: str, color: str) -> rx.Component:
#    """Carte de statistique."""
#    return rx.box(
#        rx.hstack(
#            rx.box(
#                rx.icon(icon, size=24, color=color),
#                padding="12px",
#                background=f"{color}15",
#                border_radius=Borders.RADIUS_LG,
#            ),
#            rx.vstack(
#                rx.text(title, font_size=Typography.SIZE_XS, color=Colors.GRAY_500, text_transform="uppercase", letter_spacing="0.05em"),
#                rx.text(value, font_size=Typography.SIZE_2XL, font_weight=Typography.WEIGHT_BOLD, color=Colors.GRAY_900),
#                rx.text(subtitle, font_size=Typography.SIZE_XS, color=Colors.GRAY_400),
#                spacing="0",
#                align="start",
#            ),
#            spacing="4",
#            align="center",
#            width="100%",
#        ),
#        padding=Spacing.LG,
#        background=Colors.WHITE,
#        border_radius=Borders.RADIUS_XL,
#        box_shadow=Shadows.SM,
#        border=f"1px solid {Colors.GRAY_100}",
#        flex="1",
#        min_width="200px",
#    )
#
#
#def section_header(title: str, icon: str, action: rx.Component = None) -> rx.Component:
#    """En-tête de section."""
#    return rx.hstack(
#        rx.hstack(
#            rx.box(
#                rx.icon(icon, size=18, color=Colors.PRIMARY),
#                padding="8px",
#                background=Colors.PRIMARY_LIGHTER,
#                border_radius=Borders.RADIUS_MD,
#            ),
#            rx.text(title, font_size=Typography.SIZE_LG, font_weight=Typography.WEIGHT_SEMIBOLD, color=Colors.GRAY_900),
#            spacing="3",
#            align="center",
#        ),
#        rx.spacer(),
#        action if action else rx.fragment(),
#        width="100%",
#        align="center",
#    )
#
#
#def empty_state() -> rx.Component:
#    """État vide quand il n'y a pas de simulations."""
#    return rx.box(
#        rx.vstack(
#            rx.box(
#                rx.icon("file-plus", size=48, color=Colors.GRAY_300),
#                padding="20px",
#                background=Colors.GRAY_100,
#                border_radius=Borders.RADIUS_FULL,
#            ),
#            rx.text("Aucune simulation", font_size=Typography.SIZE_LG, font_weight=Typography.WEIGHT_SEMIBOLD, color=Colors.GRAY_700),
#            rx.text("Commencez par créer votre première simulation CEE", font_size=Typography.SIZE_SM, color=Colors.GRAY_500, text_align="center"),
#            rx.button(
#                rx.hstack(rx.icon("plus", size=18), rx.text("Nouvelle simulation"), spacing="2"),
#                on_click=rx.redirect("/simulation/date-department"),
#                size="3",
#                style={
#                    "background": Colors.PRIMARY,
#                    "color": Colors.WHITE,
#                    "margin_top": Spacing.MD,
#                },
#            ),
#            spacing="3",
#            align="center",
#            padding=Spacing.XXL,
#        ),
#        width="100%",
#        background=Colors.WHITE,
#        border_radius=Borders.RADIUS_XL,
#        box_shadow=Shadows.SM,
#        border=f"1px dashed {Colors.GRAY_300}",
#    )
#
#
#def simulation_row(simulation: dict) -> rx.Component:
#    """Ligne d'une simulation dans le tableau."""
#    return rx.box(
#        rx.hstack(
#            # Nom et fiche
#            rx.hstack(
#                rx.box(
#                    rx.icon("file-text", size=16, color=Colors.PRIMARY),
#                    padding="8px",
#                    background=Colors.PRIMARY_LIGHTER,
#                    border_radius=Borders.RADIUS_MD,
#                ),
#                rx.vstack(
#                    rx.text(simulation["name"], font_weight=Typography.WEIGHT_SEMIBOLD, font_size=Typography.SIZE_SM, color=Colors.GRAY_900),
#                    rx.text(simulation["fiche"], font_size=Typography.SIZE_XS, color=Colors.GRAY_500),
#                    spacing="0",
#                    align="start",
#                ),
#                spacing="3",
#                align="center",
#                flex="2",
#            ),
#            # Secteur
#            rx.box(
#                rx.text(simulation["sector"], font_size=Typography.SIZE_SM, color=Colors.GRAY_700),
#                flex="1",
#            ),
#            # Département
#            rx.box(
#                rx.hstack(
#                    rx.icon("map-pin", size=12, color=Colors.GRAY_400),
#                    rx.text(simulation["department"], font_size=Typography.SIZE_SM, color=Colors.GRAY_600),
#                    spacing="1",
#                ),
#                flex="1",
#            ),
#            # Prime
#            rx.box(
#                rx.text(simulation["euros"], font_weight=Typography.WEIGHT_BOLD, font_size=Typography.SIZE_SM, color=Colors.SUCCESS),
#                flex="1",
#                text_align="right",
#            ),
#            # Date
#            rx.box(
#                rx.text(simulation["date"], font_size=Typography.SIZE_XS, color=Colors.GRAY_400),
#                flex="1",
#                text_align="right",
#            ),
#            # Actions
#            rx.hstack(
#                rx.icon_button(
#                    rx.icon("eye", size=16),
#                    variant="ghost",
#                    size="1",
#                    cursor="pointer",
#                ),
#                rx.icon_button(
#                    rx.icon("download", size=16),
#                    variant="ghost",
#                    size="1",
#                    cursor="pointer",
#                ),
#                rx.icon_button(
#                    rx.icon("trash-2", size=16, color=Colors.ERROR),
#                    variant="ghost",
#                    size="1",
#                    cursor="pointer",
#                ),
#                spacing="1",
#            ),
#            width="100%",
#            align="center",
#        ),
#        padding=Spacing.MD,
#        border_bottom=f"1px solid {Colors.GRAY_100}",
#        _hover={"background": Colors.GRAY_50},
#        transition="background 0.2s ease",
#    )
#
#
#def simulations_table() -> rx.Component:
#    """Tableau des simulations."""
#    # Données de démonstration
#    demo_simulations = [
#        {"name": "Isolation Dupont", "fiche": "BAR-EN-101", "sector": "Résidentiel", "department": "Paris (75)", "euros": "812,50 €", "date": "09/01/2026"},
#        {"name": "PAC Martin", "fiche": "BAR-TH-104", "sector": "Résidentiel", "department": "Lyon (69)", "euros": "1 170,00 €", "date": "08/01/2026"},
#        {"name": "Chaudière Bernard", "fiche": "BAR-TH-106", "sector": "Résidentiel", "department": "Marseille (13)", "euros": "494,00 €", "date": "07/01/2026"},
#    ]
#    
#    return rx.box(
#        rx.vstack(
#            # En-tête du tableau
#            rx.box(
#                rx.hstack(
#                    rx.text("Simulation", font_size=Typography.SIZE_XS, font_weight=Typography.WEIGHT_SEMIBOLD, color=Colors.GRAY_500, flex="2"),
#                    rx.text("Secteur", font_size=Typography.SIZE_XS, font_weight=Typography.WEIGHT_SEMIBOLD, color=Colors.GRAY_500, flex="1"),
#                    rx.text("Lieu", font_size=Typography.SIZE_XS, font_weight=Typography.WEIGHT_SEMIBOLD, color=Colors.GRAY_500, flex="1"),
#                    rx.text("Prime", font_size=Typography.SIZE_XS, font_weight=Typography.WEIGHT_SEMIBOLD, color=Colors.GRAY_500, flex="1", text_align="right"),
#                    rx.text("Date", font_size=Typography.SIZE_XS, font_weight=Typography.WEIGHT_SEMIBOLD, color=Colors.GRAY_500, flex="1", text_align="right"),
#                    rx.box(width="80px"),
#                    width="100%",
#                ),
#                padding=f"{Spacing.SM} {Spacing.MD}",
#                background=Colors.GRAY_50,
#                border_bottom=f"1px solid {Colors.GRAY_200}",
#            ),
#            # Lignes
#            *[simulation_row(sim) for sim in demo_simulations],
#            spacing="0",
#            width="100%",
#        ),
#        background=Colors.WHITE,
#        border_radius=Borders.RADIUS_XL,
#        box_shadow=Shadows.SM,
#        border=f"1px solid {Colors.GRAY_100}",
#        overflow="hidden",
#        width="100%",
#    )
#
#
#def quick_action_card(title: str, description: str, icon: str, href: str, color: str) -> rx.Component:
#    """Carte d'action rapide."""
#    return rx.link(
#        rx.box(
#            rx.hstack(
#                rx.box(
#                    rx.icon(icon, size=24, color=Colors.WHITE),
#                    padding="12px",
#                    background=color,
#                    border_radius=Borders.RADIUS_LG,
#                ),
#                rx.vstack(
#                    rx.text(title, font_weight=Typography.WEIGHT_SEMIBOLD, font_size=Typography.SIZE_BASE, color=Colors.GRAY_900),
#                    rx.text(description, font_size=Typography.SIZE_XS, color=Colors.GRAY_500),
#                    spacing="0",
#                    align="start",
#                ),
#                rx.spacer(),
#                rx.icon("chevron-right", size=20, color=Colors.GRAY_400),
#                spacing="4",
#                align="center",
#                width="100%",
#            ),
#            padding=Spacing.LG,
#            background=Colors.WHITE,
#            border_radius=Borders.RADIUS_XL,
#            box_shadow=Shadows.SM,
#            border=f"1px solid {Colors.GRAY_100}",
#            _hover={
#                "border_color": color,
#                "box_shadow": Shadows.MD,
#                "transform": "translateY(-2px)",
#            },
#            transition="all 0.2s ease",
#            cursor="pointer",
#        ),
#        href=href,
#        style={"text_decoration": "none"},
#        width="100%",
#    )
#
#
## ============================================
## PAGE PRINCIPALE
## ============================================
#
#def dashboard_content() -> rx.Component:
#    """Contenu du tableau de bord."""
#    return rx.vstack(
#        # Header
#        rx.hstack(
#            rx.vstack(
#                rx.text("Tableau de bord", font_size=Typography.SIZE_2XL, font_weight=Typography.WEIGHT_BOLD, color=Colors.GRAY_900),
#                rx.text("Bienvenue ! Gérez vos simulations CEE", font_size=Typography.SIZE_BASE, color=Colors.GRAY_500),
#                spacing="1",
#                align="start",
#            ),
#            rx.spacer(),
#            rx.button(
#                rx.hstack(rx.icon("plus", size=18), rx.text("Nouvelle simulation"), spacing="2"),
#                on_click=rx.redirect("/simulation/date-department"),
#                size="3",
#                style={
#                    "background": Colors.PRIMARY,
#                    "color": Colors.WHITE,
#                },
#            ),
#            width="100%",
#            align="center",
#        ),
#        
#        # Statistiques
#        rx.hstack(
#            stat_card("Simulations", "3", "Ce mois-ci", "file-text", Colors.PRIMARY),
#            stat_card("Prime totale", "2 476,50 €", "Montant estimé", "euro", Colors.SUCCESS),
#            stat_card("Volume CEE", "380 769 kWh", "Total généré", "zap", Colors.INFO),
#            stat_card("Taux de conversion", "67%", "Simulations finalisées", "trending-up", Colors.WARNING),
#            spacing="4",
#            width="100%",
#            flex_wrap="wrap",
#        ),
#        
#        # Actions rapides
#        rx.vstack(
#            section_header("Actions rapides", "rocket"),
#            rx.hstack(
#                quick_action_card(
#                    "Nouvelle simulation",
#                    "Calculer une prime CEE",
#                    "plus-circle",
#                    "/simulation/date-department",
#                    Colors.PRIMARY,
#                ),
#                quick_action_card(
#                    "Consulter les fiches",
#                    "Parcourir les opérations disponibles",
#                    "file-search",
#                    "/simulation/fiches",
#                    Colors.INFO,
#                ),
#                quick_action_card(
#                    "Exporter les données",
#                    "Télécharger vos simulations",
#                    "download",
#                    "#",
#                    Colors.SUCCESS,
#                ),
#                spacing="4",
#                width="100%",
#            ),
#            spacing="4",
#            width="100%",
#        ),
#        
#        # Simulations récentes
#        rx.vstack(
#            section_header(
#                "Simulations récentes",
#                "history",
#                rx.button(
#                    rx.hstack(rx.text("Voir tout"), rx.icon("arrow-right", size=14), spacing="1"),
#                    variant="ghost",
#                    size="2",
#                    color=Colors.PRIMARY,
#                ),
#            ),
#            simulations_table(),
#            spacing="4",
#            width="100%",
#        ),
#        
#        spacing="6",
#        align="start",
#        padding=Spacing.XL,
#        width="100%",
#        max_width="1100px",
#    )
#
#
#@rx.page(route="/dashboard", title="Tableau de bord - SimuPrime")
#def dashboard_page() -> rx.Component:
#    return rx.hstack(
#        sidebar(current_page="dashboard"),
#        rx.box(
#            dashboard_content(),
#            min_height="100vh",
#            background=Colors.BG_PAGE,
#            display="flex",
#            justify_content="center",
#            padding_top="40px",
#            padding_bottom="40px",
#            padding_x=Spacing.MD,
#            margin_left="260px",
#            width="100%",
#        ),
#        spacing="0",
#        width="100%",
#    )


"""Page Dashboard - Tableau de bord"""
import reflex as rx
from ..state import DashboardState
from ..styles.design_system import Colors, Typography, Spacing, Borders, Shadows
from ..components.sidebar import sidebar


def stat_card(title: str, value: rx.Var, subtitle: str, icon: str, color: str) -> rx.Component:
    """Carte de statistique."""
    return rx.box(
        rx.vstack(
            rx.hstack(
                rx.box(
                    rx.icon(icon, size=20, color=color),
                    padding="10px",
                    background=f"{color}15",
                    border_radius=Borders.RADIUS_MD,
                ),
                rx.text(
                    title,
                    font_size=Typography.SIZE_XS,
                    color=Colors.GRAY_500,
                    text_transform="uppercase",
                    letter_spacing="0.05em",
                    font_weight=Typography.WEIGHT_MEDIUM,
                ),
                spacing="3",
                align="center",
                width="100%",
            ),
            rx.text(
                value,
                font_size=Typography.SIZE_2XL,
                font_weight=Typography.WEIGHT_BOLD,
                color=Colors.GRAY_900,
            ),
            rx.text(
                subtitle,
                font_size=Typography.SIZE_XS,
                color=Colors.GRAY_400,
            ),
            spacing="2",
            align="start",
            width="100%",
        ),
        padding=Spacing.LG,
        background=Colors.WHITE,
        border_radius=Borders.RADIUS_XL,
        box_shadow=Shadows.SM,
        border=f"1px solid {Colors.GRAY_100}",
        flex="1",
        min_height="140px",
    )


def section_header(title: str, icon: str) -> rx.Component:
    """En-tête de section."""
    return rx.hstack(
        rx.box(
            rx.icon(icon, size=18, color=Colors.PRIMARY),
            padding="8px",
            background=Colors.PRIMARY_LIGHTER,
            border_radius=Borders.RADIUS_MD,
        ),
        rx.text(title, font_size=Typography.SIZE_LG, font_weight=Typography.WEIGHT_SEMIBOLD, color=Colors.GRAY_900),
        spacing="3",
        align="center",
    )


def quick_action_card(title: str, description: str, icon: str, href: str, color: str) -> rx.Component:
    """Carte d'action rapide."""
    return rx.link(
        rx.box(
            rx.hstack(
                rx.box(
                    rx.icon(icon, size=22, color=Colors.WHITE),
                    padding="10px",
                    background=color,
                    border_radius=Borders.RADIUS_LG,
                ),
                rx.vstack(
                    rx.text(title, font_weight=Typography.WEIGHT_SEMIBOLD, font_size=Typography.SIZE_SM, color=Colors.GRAY_900),
                    rx.text(description, font_size=Typography.SIZE_XS, color=Colors.GRAY_500),
                    spacing="0",
                    align="start",
                    flex="1",
                ),
                rx.icon("chevron-right", size=18, color=Colors.GRAY_400),
                spacing="3",
                align="center",
                width="100%",
            ),
            padding=Spacing.MD,
            background=Colors.WHITE,
            border_radius=Borders.RADIUS_XL,
            box_shadow=Shadows.SM,
            border=f"1px solid {Colors.GRAY_100}",
            _hover={"border_color": color, "box_shadow": Shadows.MD},
            transition="all 0.2s ease",
            cursor="pointer",
        ),
        href=href,
        style={"text_decoration": "none"},
        flex="1",
    )


def simulation_row(sim: dict) -> rx.Component:
    """Ligne du tableau de simulation."""
    return rx.table.row(
        rx.table.cell(
            rx.hstack(
                rx.box(
                    rx.icon("file-text", size=14, color=Colors.PRIMARY),
                    padding="6px",
                    background=Colors.PRIMARY_LIGHTER,
                    border_radius=Borders.RADIUS_SM,
                ),
                rx.vstack(
                    rx.text(sim["name"], font_weight=Typography.WEIGHT_SEMIBOLD, font_size=Typography.SIZE_SM, color=Colors.GRAY_900),
                    rx.text(sim["fiche"], font_size=Typography.SIZE_XS, color=Colors.GRAY_500),
                    spacing="0",
                    align="start",
                ),
                spacing="2",
                align="center",
            ),
        ),
        rx.table.cell(
            rx.text(sim["sector"], font_size=Typography.SIZE_SM, color=Colors.GRAY_700),
        ),
        rx.table.cell(
            rx.hstack(
                rx.icon("map-pin", size=12, color=Colors.GRAY_400),
                rx.text(sim["department"], font_size=Typography.SIZE_SM, color=Colors.GRAY_600),
                spacing="1",
                align="center",
            ),
        ),
        rx.table.cell(
            rx.text(sim["euros"], font_weight=Typography.WEIGHT_BOLD, font_size=Typography.SIZE_SM, color=Colors.SUCCESS),
        ),
        rx.table.cell(
            rx.text(sim["date"], font_size=Typography.SIZE_XS, color=Colors.GRAY_400),
        ),
        rx.table.cell(
            rx.hstack(
                rx.icon_button(rx.icon("eye", size=14), variant="ghost", size="1", cursor="pointer"),
                rx.icon_button(rx.icon("download", size=14), variant="ghost", size="1", cursor="pointer"),
                rx.icon_button(rx.icon("trash-2", size=14, color=Colors.ERROR), variant="ghost", size="1", cursor="pointer"),
                spacing="1",
            ),
        ),
        _hover={"background": Colors.GRAY_50},
    )


def simulations_table() -> rx.Component:
    """Tableau des simulations avec rx.table."""
    return rx.box(
        rx.table.root(
            rx.table.header(
                rx.table.row(
                    rx.table.column_header_cell(
                        rx.text("Simulation", font_size=Typography.SIZE_XS, font_weight=Typography.WEIGHT_SEMIBOLD, color=Colors.GRAY_500),
                        width="25%",
                    ),
                    rx.table.column_header_cell(
                        rx.text("Secteur", font_size=Typography.SIZE_XS, font_weight=Typography.WEIGHT_SEMIBOLD, color=Colors.GRAY_500),
                        width="15%",
                    ),
                    rx.table.column_header_cell(
                        rx.text("Lieu", font_size=Typography.SIZE_XS, font_weight=Typography.WEIGHT_SEMIBOLD, color=Colors.GRAY_500),
                        width="20%",
                    ),
                    rx.table.column_header_cell(
                        rx.text("Prime", font_size=Typography.SIZE_XS, font_weight=Typography.WEIGHT_SEMIBOLD, color=Colors.GRAY_500),
                        width="15%",
                    ),
                    rx.table.column_header_cell(
                        rx.text("Date", font_size=Typography.SIZE_XS, font_weight=Typography.WEIGHT_SEMIBOLD, color=Colors.GRAY_500),
                        width="10%",
                    ),
                    rx.table.column_header_cell(
                        rx.text("Actions", font_size=Typography.SIZE_XS, font_weight=Typography.WEIGHT_SEMIBOLD, color=Colors.GRAY_500),
                        width="15%",
                    ),
                ),
            ),
            rx.table.body(
                rx.cond(
                    DashboardState.has_simulations,
                    rx.foreach(DashboardState.simulations_list, simulation_row),
                    rx.table.row(
                        rx.table.cell(
                            rx.vstack(
                                rx.icon("inbox", size=32, color=Colors.GRAY_300),
                                rx.text("Aucune simulation", color=Colors.GRAY_500, font_size=Typography.SIZE_SM),
                                spacing="2",
                                align="center",
                                padding=Spacing.XL,
                            ),
                            col_span=6,
                        ),
                    ),
                ),
            ),
            width="100%",
        ),
        background=Colors.WHITE,
        border_radius=Borders.RADIUS_XL,
        box_shadow=Shadows.SM,
        border=f"1px solid {Colors.GRAY_100}",
        overflow="hidden",
        width="100%",
    )


def dashboard_content() -> rx.Component:
    """Contenu du tableau de bord."""
    return rx.vstack(
        # Header
        rx.hstack(
            rx.vstack(
                rx.text("Tableau de bord", font_size=Typography.SIZE_2XL, font_weight=Typography.WEIGHT_BOLD, color=Colors.GRAY_900),
                rx.text("Bienvenue ! Gérez vos simulations CEE", font_size=Typography.SIZE_BASE, color=Colors.GRAY_500),
                spacing="1",
                align="start",
            ),
            rx.spacer(),
            rx.button(
                rx.hstack(rx.icon("plus", size=18), rx.text("Nouvelle simulation"), spacing="2"),
                on_click=rx.redirect("/simulation/date-department"),
                size="3",
                style={"background": Colors.PRIMARY, "color": Colors.WHITE},
            ),
            width="100%",
            align="center",
        ),
        
        # Statistiques
        rx.hstack(
            stat_card("Simulations", DashboardState.total_simulations_str, "Ce mois-ci", "file-text", Colors.PRIMARY),
            stat_card("Prime totale", DashboardState.total_euros_str, "Montant estimé", "euro", Colors.SUCCESS),
            stat_card("Volume CEE", DashboardState.total_cumacs_str, "Total généré", "zap", Colors.INFO),
            stat_card("Taux de conversion", "67%", "Simulations finalisées", "trending-up", Colors.WARNING),
            spacing="4",
            width="100%",
        ),
        
        # Actions rapides
        rx.vstack(
            section_header("Actions rapides", "rocket"),
            rx.hstack(
                quick_action_card("Nouvelle simulation", "Calculer une prime CEE", "plus-circle", "/simulation/date-department", Colors.PRIMARY),
                quick_action_card("Consulter les fiches", "Parcourir les opérations", "file-search", "/simulation/fiches", Colors.INFO),
                quick_action_card("Exporter les données", "Télécharger vos simulations", "download", "#", Colors.SUCCESS),
                spacing="4",
                width="100%",
            ),
            spacing="4",
            width="100%",
        ),
        
        # Simulations récentes
        rx.vstack(
            section_header("Simulations récentes", "history"),
            simulations_table(),
            spacing="4",
            width="100%",
        ),
        
        spacing="6",
        align="start",
        width="100%",
    )


@rx.page(route="/dashboard", title="Tableau de bord - SimuPrime", on_load=DashboardState.load_simulations)
def dashboard_page() -> rx.Component:
    return rx.box(
        # Sidebar
        sidebar(current_page="dashboard"),
        
        # Contenu principal - directement après la sidebar
        rx.box(
            rx.box(
                dashboard_content(),
                width="100%",
                max_width="1100px",
                margin="0 auto",
            ),
            min_height="100vh",
            background=Colors.BG_PAGE,
            padding="40px",
            margin_left="260px",
            width="calc(100% - 260px)",
        ),
    )