#"""Page Dashboard - Tableau de bord"""
#import reflex as rx
#from ..state import DashboardState
#from ..state.auth_state import AuthState
#from ..styles.design_system import Colors, Typography, Spacing, Borders, Shadows
#from ..components.sidebar import sidebar
#
#
#def stat_card(title: str, value: rx.Var, subtitle: str, icon: str, color: str) -> rx.Component:
#    """Carte de statistique."""
#    return rx.box(
#        rx.vstack(
#            rx.hstack(
#                rx.box(
#                    rx.icon(icon, size=20, color=color),
#                    padding="10px",
#                    background=f"{color}15",
#                    border_radius=Borders.RADIUS_MD,
#                ),
#                rx.text(
#                    title,
#                    font_size=Typography.SIZE_XS,
#                    color=Colors.GRAY_500,
#                    text_transform="uppercase",
#                    letter_spacing="0.05em",
#                    font_weight=Typography.WEIGHT_MEDIUM,
#                ),
#                spacing="3",
#                align="center",
#                width="100%",
#            ),
#            rx.text(
#                value,
#                font_size=Typography.SIZE_2XL,
#                font_weight=Typography.WEIGHT_BOLD,
#                color=Colors.GRAY_900,
#            ),
#            rx.text(
#                subtitle,
#                font_size=Typography.SIZE_XS,
#                color=Colors.GRAY_400,
#            ),
#            spacing="2",
#            align="start",
#            width="100%",
#        ),
#        padding=Spacing.LG,
#        background=Colors.WHITE,
#        border_radius=Borders.RADIUS_XL,
#        box_shadow=Shadows.SM,
#        border=f"1px solid {Colors.GRAY_100}",
#        flex="1",
#        min_height="140px",
#    )
#
#
#def section_header(title: str, icon: str) -> rx.Component:
#    """En-tête de section."""
#    return rx.hstack(
#        rx.box(
#            rx.icon(icon, size=18, color=Colors.PRIMARY),
#            padding="8px",
#            background=Colors.PRIMARY_LIGHTER,
#            border_radius=Borders.RADIUS_MD,
#        ),
#        rx.text(title, font_size=Typography.SIZE_LG, font_weight=Typography.WEIGHT_SEMIBOLD, color=Colors.GRAY_900),
#        spacing="3",
#        align="center",
#    )
#
#
#def quick_action_card(title: str, description: str, icon: str, href: str, color: str) -> rx.Component:
#    """Carte d'action rapide."""
#    return rx.link(
#        rx.box(
#            rx.hstack(
#                rx.box(
#                    rx.icon(icon, size=22, color=Colors.WHITE),
#                    padding="10px",
#                    background=color,
#                    border_radius=Borders.RADIUS_LG,
#                ),
#                rx.vstack(
#                    rx.text(title, font_weight=Typography.WEIGHT_SEMIBOLD, font_size=Typography.SIZE_SM, color=Colors.GRAY_900),
#                    rx.text(description, font_size=Typography.SIZE_XS, color=Colors.GRAY_500),
#                    spacing="0",
#                    align="start",
#                    flex="1",
#                ),
#                rx.icon("chevron-right", size=18, color=Colors.GRAY_400),
#                spacing="3",
#                align="center",
#                width="100%",
#            ),
#            padding=Spacing.MD,
#            background=Colors.WHITE,
#            border_radius=Borders.RADIUS_XL,
#            box_shadow=Shadows.SM,
#            border=f"1px solid {Colors.GRAY_100}",
#            _hover={"border_color": color, "box_shadow": Shadows.MD},
#            transition="all 0.2s ease",
#            cursor="pointer",
#        ),
#        href=href,
#        style={"text_decoration": "none"},
#        flex="1",
#    )
#
#
#def simulation_row(sim: dict) -> rx.Component:
#    """Ligne du tableau de simulation."""
#    return rx.table.row(
#        rx.table.cell(
#            rx.hstack(
#                rx.box(
#                    rx.icon("file-text", size=14, color=Colors.PRIMARY),
#                    padding="6px",
#                    background=Colors.PRIMARY_LIGHTER,
#                    border_radius=Borders.RADIUS_SM,
#                ),
#                rx.vstack(
#                    rx.text(sim["name"], font_weight=Typography.WEIGHT_SEMIBOLD, font_size=Typography.SIZE_SM, color=Colors.GRAY_900),
#                    rx.text(sim["fiche"], font_size=Typography.SIZE_XS, color=Colors.GRAY_500),
#                    spacing="0",
#                    align="start",
#                ),
#                spacing="2",
#                align="center",
#            ),
#        ),
#        rx.table.cell(
#            rx.text(sim["sector"], font_size=Typography.SIZE_SM, color=Colors.GRAY_700),
#        ),
#        rx.table.cell(
#            rx.hstack(
#                rx.icon("map-pin", size=12, color=Colors.GRAY_400),
#                rx.text(sim["department"], font_size=Typography.SIZE_SM, color=Colors.GRAY_600),
#                spacing="1",
#                align="center",
#            ),
#        ),
#        rx.table.cell(
#            rx.text(sim["euros"], font_weight=Typography.WEIGHT_BOLD, font_size=Typography.SIZE_SM, color=Colors.SUCCESS),
#        ),
#        rx.table.cell(
#            rx.text(sim["date"], font_size=Typography.SIZE_XS, color=Colors.GRAY_400),
#        ),
#        rx.table.cell(
#            rx.hstack(
#                rx.icon_button(rx.icon("eye", size=14), variant="ghost", size="1", cursor="pointer"),
#                rx.icon_button(rx.icon("download", size=14), variant="ghost", size="1", cursor="pointer"),
#                rx.icon_button(rx.icon("trash-2", size=14, color=Colors.ERROR), variant="ghost", size="1", cursor="pointer"),
#                spacing="1",
#            ),
#        ),
#        _hover={"background": Colors.GRAY_50},
#    )
#
#
#def simulations_table() -> rx.Component:
#    """Tableau des simulations avec rx.table."""
#    return rx.box(
#        rx.table.root(
#            rx.table.header(
#                rx.table.row(
#                    rx.table.column_header_cell(
#                        rx.text("Simulation", font_size=Typography.SIZE_XS, font_weight=Typography.WEIGHT_SEMIBOLD, color=Colors.GRAY_500),
#                        width="25%",
#                    ),
#                    rx.table.column_header_cell(
#                        rx.text("Secteur", font_size=Typography.SIZE_XS, font_weight=Typography.WEIGHT_SEMIBOLD, color=Colors.GRAY_500),
#                        width="15%",
#                    ),
#                    rx.table.column_header_cell(
#                        rx.text("Lieu", font_size=Typography.SIZE_XS, font_weight=Typography.WEIGHT_SEMIBOLD, color=Colors.GRAY_500),
#                        width="20%",
#                    ),
#                    rx.table.column_header_cell(
#                        rx.text("Prime", font_size=Typography.SIZE_XS, font_weight=Typography.WEIGHT_SEMIBOLD, color=Colors.GRAY_500),
#                        width="15%",
#                    ),
#                    rx.table.column_header_cell(
#                        rx.text("Date", font_size=Typography.SIZE_XS, font_weight=Typography.WEIGHT_SEMIBOLD, color=Colors.GRAY_500),
#                        width="10%",
#                    ),
#                    rx.table.column_header_cell(
#                        rx.text("Actions", font_size=Typography.SIZE_XS, font_weight=Typography.WEIGHT_SEMIBOLD, color=Colors.GRAY_500),
#                        width="15%",
#                    ),
#                ),
#            ),
#            rx.table.body(
#                rx.cond(
#                    DashboardState.has_simulations,
#                    rx.foreach(DashboardState.simulations_list, simulation_row),
#                    rx.table.row(
#                        rx.table.cell(
#                            rx.vstack(
#                                rx.icon("inbox", size=32, color=Colors.GRAY_300),
#                                rx.text("Aucune simulation", color=Colors.GRAY_500, font_size=Typography.SIZE_SM),
#                                spacing="2",
#                                align="center",
#                                padding=Spacing.XL,
#                            ),
#                            col_span=6,
#                        ),
#                    ),
#                ),
#            ),
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
#                style={"background": Colors.PRIMARY, "color": Colors.WHITE},
#            ),
#            width="100%",
#            align="center",
#        ),
#        
#        # Statistiques
#        rx.hstack(
#            stat_card("Simulations", DashboardState.total_simulations_str, "Ce mois-ci", "file-text", Colors.PRIMARY),
#            stat_card("Prime totale", DashboardState.total_euros_str, "Montant estimé", "euro", Colors.SUCCESS),
#            stat_card("Volume CEE", DashboardState.total_cumacs_str, "Total généré", "zap", Colors.INFO),
#            stat_card("Taux de conversion", "67%", "Simulations finalisées", "trending-up", Colors.WARNING),
#            spacing="4",
#            width="100%",
#        ),
#        
#        # Actions rapides
#        rx.vstack(
#            section_header("Actions rapides", "rocket"),
#            rx.hstack(
#                quick_action_card("Nouvelle simulation", "Calculer une prime CEE", "plus-circle", "/simulation/date-department", Colors.PRIMARY),
#                quick_action_card("Consulter les fiches", "Parcourir les opérations", "file-search", "/simulation/fiches", Colors.INFO),
#                quick_action_card("Exporter les données", "Télécharger vos simulations", "download", "#", Colors.SUCCESS),
#                spacing="4",
#                width="100%",
#            ),
#            spacing="4",
#            width="100%",
#        ),
#        
#        # Simulations récentes
#        rx.vstack(
#            section_header("Simulations récentes", "history"),
#            simulations_table(),
#            spacing="4",
#            width="100%",
#        ),
#        
#        spacing="6",
#        align="start",
#        width="100%",
#    )
#
#
#@rx.page(
#    route="/dashboard",
#    title="Tableau de bord - RDE Consulting",
#    on_load=[AuthState.require_auth, DashboardState.load_simulations],
#)
#def dashboard_page() -> rx.Component:
#    """Page du tableau de bord - requiert authentification."""
#    return rx.cond(
#        AuthState.is_authenticated,
#        # Contenu du dashboard si connecté
#        rx.hstack(
#            # Sidebar
#            sidebar(current_page="dashboard"),
#            
#            # Contenu principal
#            rx.box(
#                rx.box(
#                    dashboard_content(),
#                    width="100%",
#                    max_width="1100px",
#                    margin="0 auto",
#                ),
#                min_height="100vh",
#                background=Colors.BG_PAGE,
#                padding="40px",
#                flex="1",
#            ),
#            spacing="0",
#            width="100%",
#            align="stretch",
#        ),
#        # Écran de chargement pendant la vérification
#        rx.center(
#            rx.vstack(
#                rx.spinner(size="3"),
#                rx.text("Vérification de l'authentification...", color=Colors.GRAY_500),
#                spacing="4",
#            ),
#            min_height="100vh",
#            background=Colors.BG_PAGE,
#        ),
#    )
"""Page Dashboard - Tableau de bord"""
import reflex as rx
from ..state.dashboard_state import DashboardState
from ..styles.design_system import Colors, Typography, Spacing, Borders, Shadows
from ..components.sidebar import sidebar


# ============================================
# COMPOSANTS DU DASHBOARD
# ============================================

def stat_card(title: str, value: rx.Var, subtitle: str, icon: str, color: str) -> rx.Component:
    """Carte de statistique."""
    return rx.box(
        rx.hstack(
            rx.box(
                rx.icon(icon, size=24, color=color),
                padding="12px",
                background=f"{color}15",
                border_radius=Borders.RADIUS_LG,
            ),
            rx.vstack(
                rx.text(title, font_size=Typography.SIZE_XS, color=Colors.GRAY_500, text_transform="uppercase", letter_spacing="0.05em"),
                rx.text(value, font_size=Typography.SIZE_2XL, font_weight=Typography.WEIGHT_BOLD, color=Colors.GRAY_900),
                rx.text(subtitle, font_size=Typography.SIZE_XS, color=Colors.GRAY_400),
                spacing="0",
                align="start",
            ),
            spacing="4",
            align="center",
            width="100%",
        ),
        padding=Spacing.LG,
        background=Colors.WHITE,
        border_radius=Borders.RADIUS_XL,
        box_shadow=Shadows.SM,
        border=f"1px solid {Colors.GRAY_100}",
        flex="1",
        min_width="200px",
    )


def section_header(title: str, icon: str, action: rx.Component = None) -> rx.Component:
    """En-tête de section."""
    return rx.hstack(
        rx.hstack(
            rx.box(
                rx.icon(icon, size=18, color=Colors.PRIMARY),
                padding="8px",
                background=Colors.PRIMARY_LIGHTER,
                border_radius=Borders.RADIUS_MD,
            ),
            rx.text(title, font_size=Typography.SIZE_LG, font_weight=Typography.WEIGHT_SEMIBOLD, color=Colors.GRAY_900),
            spacing="3",
            align="center",
        ),
        rx.spacer(),
        action if action else rx.fragment(),
        width="100%",
        align="center",
    )


def quick_action_card(title: str, description: str, icon: str, href: str, color: str) -> rx.Component:
    """Carte d'action rapide."""
    return rx.link(
        rx.box(
            rx.hstack(
                rx.box(
                    rx.icon(icon, size=20, color=color),
                    padding="10px",
                    background=f"{color}15",
                    border_radius=Borders.RADIUS_MD,
                ),
                rx.vstack(
                    rx.text(title, font_weight=Typography.WEIGHT_SEMIBOLD, font_size=Typography.SIZE_SM, color=Colors.GRAY_900),
                    rx.text(description, font_size=Typography.SIZE_XS, color=Colors.GRAY_500),
                    spacing="0",
                    align="start",
                ),
                spacing="3",
                align="center",
            ),
            padding=Spacing.MD,
            background=Colors.WHITE,
            border_radius=Borders.RADIUS_LG,
            box_shadow=Shadows.SM,
            border=f"1px solid {Colors.GRAY_100}",
            _hover={"box_shadow": Shadows.MD, "transform": "translateY(-2px)"},
            transition="all 0.2s ease",
            cursor="pointer",
            width="100%",
        ),
        href=href,
        text_decoration="none",
        flex="1",
    )


def simulation_row(sim: dict) -> rx.Component:
    """Ligne du tableau de simulation."""
    return rx.table.row(
        # N°
        rx.table.cell(
            rx.box(
                rx.text(sim["number"], font_weight=Typography.WEIGHT_BOLD, font_size=Typography.SIZE_SM, color=Colors.PRIMARY),
                padding="4px 8px",
                background=Colors.PRIMARY_LIGHTER,
                border_radius=Borders.RADIUS_SM,
                display="inline-block",
            ),
        ),
        # Simulation (nom + fiche)
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
        # Secteur
        rx.table.cell(
            rx.text(sim["sector"], font_size=Typography.SIZE_SM, color=Colors.GRAY_700),
        ),
        # Lieu
        rx.table.cell(
            rx.hstack(
                rx.icon("map-pin", size=12, color=Colors.GRAY_400),
                rx.text(sim["department"], font_size=Typography.SIZE_SM, color=Colors.GRAY_600),
                spacing="1",
                align="center",
            ),
        ),
        # kWh cumac
        rx.table.cell(
            rx.hstack(
                rx.icon("zap", size=12, color=Colors.INFO),
                rx.text(sim["cumacs"], font_weight=Typography.WEIGHT_MEDIUM, font_size=Typography.SIZE_SM, color=Colors.INFO),
                spacing="1",
                align="center",
            ),
        ),
        # Prime €
        rx.table.cell(
            rx.text(sim["euros"], font_weight=Typography.WEIGHT_BOLD, font_size=Typography.SIZE_SM, color=Colors.SUCCESS),
        ),
        # Date
        rx.table.cell(
            rx.text(sim["date"], font_size=Typography.SIZE_XS, color=Colors.GRAY_400),
        ),
        # Actions (télécharger PDF uniquement)
        rx.table.cell(
            rx.icon_button(
                rx.icon("download", size=14),
                variant="ghost",
                size="1",
                cursor="pointer",
                title="Télécharger PDF",
                on_click=DashboardState.download_simulation_pdf(sim["id"]),
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
                        rx.text("N°", font_size=Typography.SIZE_XS, font_weight=Typography.WEIGHT_SEMIBOLD, color=Colors.GRAY_500),
                        width="5%",
                    ),
                    rx.table.column_header_cell(
                        rx.text("Simulation", font_size=Typography.SIZE_XS, font_weight=Typography.WEIGHT_SEMIBOLD, color=Colors.GRAY_500),
                        width="20%",
                    ),
                    rx.table.column_header_cell(
                        rx.text("Secteur", font_size=Typography.SIZE_XS, font_weight=Typography.WEIGHT_SEMIBOLD, color=Colors.GRAY_500),
                        width="12%",
                    ),
                    rx.table.column_header_cell(
                        rx.text("Lieu", font_size=Typography.SIZE_XS, font_weight=Typography.WEIGHT_SEMIBOLD, color=Colors.GRAY_500),
                        width="15%",
                    ),
                    rx.table.column_header_cell(
                        rx.text("kWh cumac", font_size=Typography.SIZE_XS, font_weight=Typography.WEIGHT_SEMIBOLD, color=Colors.GRAY_500),
                        width="12%",
                    ),
                    rx.table.column_header_cell(
                        rx.text("Prime", font_size=Typography.SIZE_XS, font_weight=Typography.WEIGHT_SEMIBOLD, color=Colors.GRAY_500),
                        width="12%",
                    ),
                    rx.table.column_header_cell(
                        rx.text("Date", font_size=Typography.SIZE_XS, font_weight=Typography.WEIGHT_SEMIBOLD, color=Colors.GRAY_500),
                        width="10%",
                    ),
                    rx.table.column_header_cell(
                        rx.text("Actions", font_size=Typography.SIZE_XS, font_weight=Typography.WEIGHT_SEMIBOLD, color=Colors.GRAY_500),
                        width="10%",
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
                                rx.text("Créez votre première simulation pour la voir apparaître ici", color=Colors.GRAY_400, font_size=Typography.SIZE_XS),
                                spacing="2",
                                align="center",
                                padding=Spacing.XL,
                            ),
                            col_span=8,
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
            stat_card("Simulations", DashboardState.total_simulations_str, "Total enregistrées", "file-text", Colors.PRIMARY),
            stat_card("Prime totale", DashboardState.total_euros_str, "Montant estimé", "euro", Colors.SUCCESS),
            stat_card("Volume CEE", DashboardState.total_cumacs_str, "Total généré", "zap", Colors.INFO),
            spacing="4",
            width="100%",
        ),
        
        # Actions rapides
        rx.vstack(
            section_header("Actions rapides", "rocket"),
            rx.hstack(
                quick_action_card("Nouvelle simulation", "Calculer une prime CEE", "plus-circle", "/simulation/date-department", Colors.PRIMARY),
                quick_action_card("Consulter les fiches", "Parcourir les opérations", "file-search", "/simulation/sector-typology", Colors.INFO),
                spacing="4",
                width="100%",
            ),
            spacing="4",
            width="100%",
        ),
        
        # Simulations récentes
        rx.vstack(
            section_header("Mes simulations", "history"),
            simulations_table(),
            spacing="4",
            width="100%",
        ),
        
        spacing="6",
        align="start",
        width="100%",
    )


@rx.page(route="/dashboard", title="Tableau de bord - RDE Consulting", on_load=DashboardState.load_simulations)
def dashboard_page() -> rx.Component:
    return rx.flex(
        # Sidebar
        sidebar(current_page="dashboard"),
        
        # Contenu principal
        rx.box(
            rx.box(
                dashboard_content(),
                width="100%",
                max_width="1200px",
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