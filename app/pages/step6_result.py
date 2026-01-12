#"""Page Step 6 - Résultats de la simulation"""
#import reflex as rx
#from ..state import SimulationState
#from ..styles.design_system import Colors, Typography, Spacing, Borders, Shadows
#from ..components.sidebar import simulation_sidebar
#
#
#def success_badge() -> rx.Component:
#    """Badge de succès."""
#    return rx.box(
#        rx.icon("check", size=32, color=Colors.WHITE),
#        width="64px",
#        height="64px",
#        display="flex",
#        align_items="center",
#        justify_content="center",
#        background=Colors.SUCCESS,
#        border_radius="50%",
#        box_shadow=f"0 0 0 8px {Colors.SUCCESS}20",
#    )
#
#
#def main_result_card(
#    title: str,
#    value: rx.Var,
#    subtitle: str,
#    icon: str,
#    gradient_from: str,
#    gradient_to: str,
#) -> rx.Component:
#    """Carte principale de résultat avec gradient."""
#    return rx.box(
#        rx.vstack(
#            rx.hstack(
#                rx.box(
#                    rx.icon(icon, size=28, color=Colors.WHITE),
#                    padding="14px",
#                    background="rgba(255,255,255,0.2)",
#                    border_radius=Borders.RADIUS_LG,
#                ),
#                rx.spacer(),
#                rx.icon("trending-up", size=24, color="rgba(255,255,255,0.7)"),
#                width="100%",
#            ),
#            rx.vstack(
#                rx.text(title, font_size=Typography.SIZE_BASE, color="rgba(255,255,255,0.9)", font_weight=Typography.WEIGHT_MEDIUM),
#                rx.text(value, font_size="2.75rem", font_weight=Typography.WEIGHT_BOLD, color=Colors.WHITE, line_height="1.2"),
#                rx.text(subtitle, font_size=Typography.SIZE_SM, color="rgba(255,255,255,0.7)"),
#                spacing="2",
#                align="start",
#                width="100%",
#            ),
#            spacing="5",
#            align="start",
#            width="100%",
#            height="100%",
#        ),
#        padding=Spacing.XL,
#        background=f"linear-gradient(135deg, {gradient_from} 0%, {gradient_to} 100%)",
#        border_radius=Borders.RADIUS_XL,
#        box_shadow=Shadows.LG,
#        width="50%",
#        min_width="320px",
#        min_height="220px",
#    )
#
#
#def detail_section_card(title: str, icon: str, children: rx.Component) -> rx.Component:
#    """Carte de section avec titre."""
#    return rx.box(
#        rx.vstack(
#            rx.hstack(
#                rx.box(
#                    rx.icon(icon, size=18, color=Colors.PRIMARY),
#                    padding="8px",
#                    background=Colors.PRIMARY_LIGHTER,
#                    border_radius=Borders.RADIUS_MD,
#                ),
#                rx.text(title, font_size=Typography.SIZE_BASE, font_weight=Typography.WEIGHT_SEMIBOLD, color=Colors.GRAY_900),
#                spacing="3",
#                align="center",
#            ),
#            rx.divider(margin_y=Spacing.SM),
#            children,
#            spacing="0",
#            width="100%",
#            height="100%",
#        ),
#        padding=Spacing.LG,
#        background=Colors.WHITE,
#        border_radius=Borders.RADIUS_XL,
#        box_shadow=Shadows.SM,
#        border=f"1px solid {Colors.GRAY_100}",
#        width="100%",
#        height="100%",
#    )
#
#
#def summary_row(icon: str, label: str, value: rx.Var, highlight: bool = False) -> rx.Component:
#    """Ligne de résumé."""
#    return rx.hstack(
#        rx.hstack(
#            rx.icon(icon, size=14, color=Colors.PRIMARY if highlight else Colors.GRAY_400),
#            rx.text(label, font_size=Typography.SIZE_SM, color=Colors.GRAY_600),
#            spacing="2",
#            min_width="140px",
#        ),
#        rx.spacer(),
#        rx.text(
#            value,
#            font_size=Typography.SIZE_SM,
#            font_weight=Typography.WEIGHT_SEMIBOLD if highlight else Typography.WEIGHT_MEDIUM,
#            color=Colors.PRIMARY if highlight else Colors.GRAY_900,
#            text_align="right",
#        ),
#        width="100%",
#        padding_y="10px",
#    )
#
#
#def info_stat_item(label: str, value: rx.Var, icon: str) -> rx.Component:
#    """Item de statistique."""
#    return rx.hstack(
#        rx.box(
#            rx.icon(icon, size=16, color=Colors.PRIMARY),
#            padding="8px",
#            background=Colors.PRIMARY_LIGHTER,
#            border_radius=Borders.RADIUS_MD,
#        ),
#        rx.vstack(
#            rx.text(label, font_size=Typography.SIZE_XS, color=Colors.GRAY_500),
#            rx.text(value, font_size=Typography.SIZE_SM, font_weight=Typography.WEIGHT_SEMIBOLD, color=Colors.GRAY_900),
#            spacing="0",
#            align="start",
#        ),
#        spacing="3",
#        align="center",
#        flex="1",
#    )
#
#
#def cee_info_box() -> rx.Component:
#    """Box d'information sur les CEE."""
#    return rx.box(
#        rx.hstack(
#            rx.icon("info", size=16, color=Colors.INFO),
#            rx.text(
#                "Le montant indiqué est une estimation basée sur le prix moyen du marché (0,0065 €/kWh cumac).",
#                font_size=Typography.SIZE_XS,
#                color=Colors.INFO,
#            ),
#            spacing="2",
#            align="start",
#        ),
#        padding=Spacing.MD,
#        background=f"{Colors.INFO}10",
#        border_radius=Borders.RADIUS_MD,
#        width="100%",
#    )
#
#
#def save_button() -> rx.Component:
#    """Bouton de sauvegarde avec état dynamique."""
#    return rx.cond(
#        SimulationState.simulation_saved,
#        rx.button(
#            rx.hstack(rx.icon("check", size=18), rx.text("Sauvegardée"), spacing="2"),
#            disabled=True,
#            size="3",
#            style={
#                "background": Colors.GRAY_200,
#                "color": Colors.GRAY_500,
#                "cursor": "not-allowed",
#                "min_width": "180px",
#            },
#        ),
#        rx.button(
#            rx.hstack(rx.icon("save", size=18), rx.text("Sauvegarder"), spacing="2"),
#            on_click=SimulationState.save_and_redirect,
#            size="3",
#            style={
#                "background": Colors.SUCCESS,
#                "color": Colors.WHITE,
#                "_hover": {"background": "#1ea34d"},
#                "transition": "all 0.2s ease",
#                "min_width": "180px",
#            },
#        ),
#    )
#
#
#def export_button() -> rx.Component:
#    """Bouton d'export PDF."""
#    return rx.button(
#        rx.hstack(rx.icon("download", size=18), rx.text("Exporter PDF"), spacing="2"),
#        variant="outline",
#        size="3",
#        style={
#            "border": f"2px solid {Colors.PRIMARY}",
#            "color": Colors.PRIMARY,
#            "_hover": {"background": Colors.PRIMARY_LIGHTER},
#            "transition": "all 0.2s ease",
#            "min_width": "180px",
#        },
#    )
#
#
#def result_content() -> rx.Component:
#    """Contenu de la page résultats."""
#    return rx.vstack(
#        # Header avec badge de succès
#        rx.vstack(
#            success_badge(),
#            rx.vstack(
#                rx.text("Simulation terminée !", font_size=Typography.SIZE_2XL, font_weight=Typography.WEIGHT_BOLD, color=Colors.GRAY_900),
#                rx.text(SimulationState.simulation_name, font_size=Typography.SIZE_BASE, color=Colors.GRAY_500),
#                spacing="1",
#                align="center",
#            ),
#            spacing="4",
#            align="center",
#        ),
#        
#        # Cartes de résultats principaux
#        rx.hstack(
#            main_result_card(
#                title="Prime CEE estimée",
#                value=SimulationState.result_euros_formatted,
#                subtitle="Montant indicatif HT",
#                icon="euro",
#                gradient_from=Colors.SUCCESS,
#                gradient_to="#059669",
#            ),
#            main_result_card(
#                title="Volume CEE",
#                value=SimulationState.result_cumacs_formatted,
#                subtitle="Certificats générés",
#                icon="zap",
#                gradient_from=Colors.PRIMARY,
#                gradient_to="#466c82",
#            ),
#            spacing="4",
#            width="100%",
#        ),
#        
#        # Récapitulatif et Localisation - côte à côte
#        rx.hstack(
#            rx.box(
#                detail_section_card(
#                    "Récapitulatif de l'opération",
#                    "clipboard-list",
#                    rx.vstack(
#                        summary_row("file-text", "Fiche d'opération", SimulationState.selected_fiche, highlight=True),
#                        rx.divider(),
#                        summary_row("building-2", "Secteur", SimulationState.sector),
#                        rx.divider(),
#                        summary_row("layers", "Typologie", SimulationState.typology),
#                        rx.divider(),
#                        summary_row("user", "Bénéficiaire", SimulationState.beneficiary_type),
#                        spacing="0",
#                        width="100%",
#                    ),
#                ),
#                width="50%",
#            ),
#            rx.box(
#                detail_section_card(
#                    "Localisation & Date",
#                    "map",
#                    rx.vstack(
#                        summary_row("map-pin", "Département", SimulationState.department),
#                        rx.divider(),
#                        summary_row("thermometer", "Zone climatique", SimulationState.zone_climatique, highlight=True),
#                        rx.divider(),
#                        summary_row("calendar", "Date de signature", SimulationState.date_signature),
#                        rx.divider(),
#                        rx.box(height="42px"),
#                        spacing="0",
#                        width="100%",
#                    ),
#                ),
#                width="50%",
#            ),
#            spacing="4",
#            width="100%",
#            align="stretch",
#        ),
#        
#        # Détail du calcul
#        detail_section_card(
#            "Détail du calcul",
#            "calculator",
#            rx.vstack(
#                rx.hstack(
#                    info_stat_item("Volume généré", SimulationState.result_cumacs_formatted, "zap"),
#                    rx.box(
#                        rx.text("×", font_size=Typography.SIZE_XL, color=Colors.GRAY_400),
#                        padding_x=Spacing.MD,
#                    ),
#                    info_stat_item("Prix unitaire", "0,0065 €/kWh", "tag"),
#                    rx.box(
#                        rx.text("=", font_size=Typography.SIZE_XL, color=Colors.GRAY_400),
#                        padding_x=Spacing.MD,
#                    ),
#                    rx.box(
#                        rx.vstack(
#                            rx.text("Prime estimée", font_size=Typography.SIZE_XS, color=Colors.GRAY_500),
#                            rx.text(SimulationState.result_euros_formatted, font_size=Typography.SIZE_XL, font_weight=Typography.WEIGHT_BOLD, color=Colors.SUCCESS),
#                            spacing="0",
#                            align="center",
#                        ),
#                        padding=Spacing.MD,
#                        background=Colors.SUCCESS_LIGHT,
#                        border_radius=Borders.RADIUS_LG,
#                        min_width="150px",
#                    ),
#                    spacing="2",
#                    width="100%",
#                    align="center",
#                    justify="center",
#                    flex_wrap="wrap",
#                ),
#                cee_info_box(),
#                spacing="4",
#                width="100%",
#            ),
#        ),
#        
#        # Actions - centrées
#        rx.hstack(
#            save_button(),
#            export_button(),
#            spacing="4",
#            justify="center",
#            width="100%",
#        ),
#        
#        spacing="5",
#        align="center",
#        padding=Spacing.XL,
#        width="100%",
#        max_width="1000px",
#    )
#
#
#@rx.page(route="/simulation/result", title="Résultats - RDE Consulting")
#def step6_result_page() -> rx.Component:
#    return rx.hstack(
#        simulation_sidebar(current_step=6),
#        rx.box(
#            result_content(),
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


#"""Page Step 6 - Résultats de la simulation"""
#import reflex as rx
#from ..state import SimulationState
#from ..styles.design_system import Colors, Typography, Spacing, Borders, Shadows
#from ..components.sidebar import simulation_sidebar
#
#
#def result_card(title: str, value: rx.Var, subtitle: str, icon: str, color: str) -> rx.Component:
#    """Carte de résultat."""
#    return rx.box(
#        rx.vstack(
#            rx.box(
#                rx.icon(icon, size=32, color=color),
#                padding=Spacing.LG,
#                background=f"{color}15",
#                border_radius=Borders.RADIUS_FULL,
#            ),
#            rx.text(title, font_size=Typography.SIZE_SM, color=Colors.GRAY_500),
#            rx.text(value, font_size=Typography.SIZE_2XL, font_weight=Typography.WEIGHT_BOLD, color=Colors.GRAY_900),
#            rx.text(subtitle, font_size=Typography.SIZE_XS, color=Colors.GRAY_400),
#            spacing="2",
#            align="center",
#        ),
#        padding=Spacing.XL,
#        background=Colors.WHITE,
#        border_radius=Borders.RADIUS_XL,
#        box_shadow=Shadows.MD,
#        border=f"1px solid {Colors.GRAY_100}",
#        flex="1",
#        min_width="200px",
#    )
#
#
#def summary_item(icon: str, label: str, value: rx.Var) -> rx.Component:
#    """Item du récapitulatif."""
#    return rx.hstack(
#        rx.hstack(
#            rx.icon(icon, size=14, color=Colors.GRAY_400),
#            rx.text(label, font_size=Typography.SIZE_SM, color=Colors.GRAY_500),
#            spacing="2",
#        ),
#        rx.spacer(),
#        rx.text(value, font_size=Typography.SIZE_SM, font_weight=Typography.WEIGHT_MEDIUM, color=Colors.GRAY_700),
#        width="100%",
#        padding_y=Spacing.SM,
#        border_bottom=f"1px solid {Colors.GRAY_100}",
#    )
#
#
#def result_content() -> rx.Component:
#    """Contenu de la page résultats."""
#    return rx.vstack(
#        # Header succès
#        rx.vstack(
#            rx.box(
#                rx.icon("check-circle", size=48, color=Colors.SUCCESS),
#                padding=Spacing.LG,
#                background=Colors.SUCCESS_LIGHT,
#                border_radius=Borders.RADIUS_FULL,
#            ),
#            rx.text("Simulation terminée !", font_size=Typography.SIZE_2XL, font_weight=Typography.WEIGHT_BOLD),
#            rx.text(SimulationState.simulation_name, color=Colors.GRAY_500),
#            spacing="3",
#            align="center",
#        ),
#        
#        # Progress bar (complète)
#        rx.box(
#            rx.box(
#                width="100%",
#                height="100%",
#                background=Colors.SUCCESS,
#                border_radius=Borders.RADIUS_FULL,
#            ),
#            width="100%",
#            max_width="400px",
#            height="6px",
#            background=Colors.GRAY_200,
#            border_radius=Borders.RADIUS_FULL,
#            overflow="hidden",
#        ),
#        
#        # Résultats principaux
#        rx.hstack(
#            result_card(
#                "Prime CEE estimée",
#                SimulationState.result_euros_formatted,
#                "Montant indicatif",
#                "euro",
#                Colors.SUCCESS,
#            ),
#            result_card(
#                "Volume CEE",
#                SimulationState.result_cumacs_formatted,
#                "kWh cumac",
#                "zap",
#                Colors.PRIMARY,
#            ),
#            spacing="4",
#            width="100%",
#            max_width="500px",
#        ),
#        
#        # Récapitulatif
#        rx.box(
#            rx.vstack(
#                rx.hstack(
#                    rx.icon("clipboard-list", size=16, color=Colors.PRIMARY),
#                    rx.text("Récapitulatif", font_weight=Typography.WEIGHT_SEMIBOLD, color=Colors.GRAY_700),
#                    spacing="2",
#                ),
#                summary_item("calendar", "Date de signature", SimulationState.date_signature),
#                summary_item("map-pin", "Département", SimulationState.department),
#                summary_item("thermometer", "Zone climatique", SimulationState.zone_climatique),
#                summary_item("building-2", "Secteur", SimulationState.sector),
#                summary_item("layers", "Typologie", SimulationState.typology),
#                summary_item("file-text", "Fiche CEE", SimulationState.selected_fiche),
#                summary_item("user", "Bénéficiaire", SimulationState.beneficiary_type),
#                spacing="1",
#                width="100%",
#            ),
#            padding=Spacing.LG,
#            background=Colors.WHITE,
#            border_radius=Borders.RADIUS_LG,
#            box_shadow=Shadows.SM,
#            width="100%",
#            max_width="500px",
#        ),
#        
#        # Actions
#        rx.vstack(
#            rx.hstack(
#                rx.button(
#                    rx.hstack(
#                        rx.cond(
#                            SimulationState.simulation_saved,
#                            rx.icon("check", size=16),
#                            rx.icon("save", size=16),
#                        ),
#                        rx.text(
#                            rx.cond(
#                                SimulationState.simulation_saved,
#                                "Sauvegardée",
#                                "Sauvegarder",
#                            )
#                        ),
#                        spacing="2",
#                    ),
#                    on_click=SimulationState.save_simulation(""),
#                    disabled=SimulationState.simulation_saved,
#                    size="3",
#                    style={
#                        "background": rx.cond(SimulationState.simulation_saved, Colors.GRAY_300, Colors.PRIMARY),
#                        "color": Colors.WHITE,
#                    },
#                ),
#                rx.button(
#                    rx.hstack(rx.icon("download", size=16), rx.text("Exporter PDF"), spacing="2"),
#                    variant="outline",
#                    size="3",
#                ),
#                spacing="3",
#            ),
#            rx.hstack(
#                rx.button(
#                    rx.hstack(rx.icon("plus", size=16), rx.text("Nouvelle simulation"), spacing="2"),
#                    on_click=SimulationState.start_new_simulation,
#                    variant="ghost",
#                    size="3",
#                ),
#                rx.button(
#                    rx.hstack(rx.icon("layout-dashboard", size=16), rx.text("Tableau de bord"), spacing="2"),
#                    on_click=rx.redirect("/dashboard"),
#                    variant="ghost",
#                    size="3",
#                ),
#                spacing="3",
#            ),
#            spacing="3",
#            align="center",
#        ),
#        
#        # Message de sauvegarde
#        rx.cond(
#            SimulationState.simulation_saved,
#            rx.box(
#                rx.hstack(
#                    rx.icon("check-circle", size=16, color=Colors.SUCCESS),
#                    rx.text("Simulation sauvegardée avec succès !", color=Colors.SUCCESS, font_size=Typography.SIZE_SM),
#                    spacing="2",
#                    align="center",
#                ),
#                padding=Spacing.MD,
#                background=Colors.SUCCESS_LIGHT,
#                border_radius=Borders.RADIUS_MD,
#            ),
#            rx.fragment(),
#        ),
#        
#        spacing="6",
#        align="center",
#        padding=Spacing.XL,
#        width="100%",
#        max_width="800px",
#    )
#
#
#@rx.page(route="/simulation/result", title="Résultats - RDE Consulting")
#def step6_result_page() -> rx.Component:
#    return rx.hstack(
#        # Sidebar
#        simulation_sidebar(current_step=6),
#        
#        # Contenu principal
#        rx.box(
#            result_content(),
#            min_height="100vh",
#            background=Colors.BG_PAGE,
#            display="flex",
#            justify_content="center",
#            padding_top="40px",
#            padding_x=Spacing.MD,
#            margin_left="260px",
#            width="100%",
#        ),
#        
#        spacing="0",
#        width="100%",
#    )



"""Page Step 6 - Résultats de la simulation"""
import reflex as rx
from ..state import SimulationState
from ..styles.design_system import Colors, Typography, Spacing, Borders, Shadows
from ..components.sidebar import simulation_sidebar


def success_badge() -> rx.Component:
    """Badge de succès."""
    return rx.box(
        rx.icon("check", size=32, color=Colors.WHITE),
        width="64px",
        height="64px",
        display="flex",
        align_items="center",
        justify_content="center",
        background=Colors.SUCCESS,
        border_radius="50%",
        box_shadow=f"0 0 0 8px {Colors.SUCCESS}20",
    )


def main_result_card(
    title: str,
    value: rx.Var,
    subtitle: str,
    icon: str,
    gradient_from: str,
    gradient_to: str,
) -> rx.Component:
    """Carte principale de résultat avec gradient."""
    return rx.box(
        rx.vstack(
            rx.hstack(
                rx.box(
                    rx.icon(icon, size=28, color=Colors.WHITE),
                    padding="14px",
                    background="rgba(255,255,255,0.2)",
                    border_radius=Borders.RADIUS_LG,
                ),
                rx.spacer(),
                rx.icon("trending-up", size=24, color="rgba(255,255,255,0.7)"),
                width="100%",
            ),
            rx.vstack(
                rx.text(title, font_size=Typography.SIZE_BASE, color="rgba(255,255,255,0.9)", font_weight=Typography.WEIGHT_MEDIUM),
                rx.text(value, font_size="2.75rem", font_weight=Typography.WEIGHT_BOLD, color=Colors.WHITE, line_height="1.2"),
                rx.text(subtitle, font_size=Typography.SIZE_SM, color="rgba(255,255,255,0.7)"),
                spacing="2",
                align="start",
                width="100%",
            ),
            spacing="5",
            align="start",
            width="100%",
            height="100%",
        ),
        padding=Spacing.XL,
        background=f"linear-gradient(135deg, {gradient_from} 0%, {gradient_to} 100%)",
        border_radius=Borders.RADIUS_XL,
        box_shadow=Shadows.LG,
        width="50%",
        min_width="320px",
        min_height="220px",
    )


def detail_section_card(title: str, icon: str, children: rx.Component) -> rx.Component:
    """Carte de section avec titre."""
    return rx.box(
        rx.vstack(
            rx.hstack(
                rx.box(
                    rx.icon(icon, size=18, color=Colors.PRIMARY),
                    padding="8px",
                    background=Colors.PRIMARY_LIGHTER,
                    border_radius=Borders.RADIUS_MD,
                ),
                rx.text(title, font_size=Typography.SIZE_BASE, font_weight=Typography.WEIGHT_SEMIBOLD, color=Colors.GRAY_900),
                spacing="3",
                align="center",
            ),
            rx.divider(margin_y=Spacing.SM),
            children,
            spacing="0",
            width="100%",
            height="100%",
        ),
        padding=Spacing.LG,
        background=Colors.WHITE,
        border_radius=Borders.RADIUS_XL,
        box_shadow=Shadows.SM,
        border=f"1px solid {Colors.GRAY_100}",
        width="100%",
        height="100%",
    )


def summary_row(icon: str, label: str, value: rx.Var, highlight: bool = False) -> rx.Component:
    """Ligne de résumé."""
    return rx.hstack(
        rx.hstack(
            rx.icon(icon, size=14, color=Colors.PRIMARY if highlight else Colors.GRAY_400),
            rx.text(label, font_size=Typography.SIZE_SM, color=Colors.GRAY_600),
            spacing="2",
            min_width="140px",
        ),
        rx.spacer(),
        rx.text(
            value,
            font_size=Typography.SIZE_SM,
            font_weight=Typography.WEIGHT_SEMIBOLD if highlight else Typography.WEIGHT_MEDIUM,
            color=Colors.PRIMARY if highlight else Colors.GRAY_900,
            text_align="right",
        ),
        width="100%",
        padding_y="10px",
    )


def info_stat_item(label: str, value: rx.Var, icon: str) -> rx.Component:
    """Item de statistique."""
    return rx.hstack(
        rx.box(
            rx.icon(icon, size=16, color=Colors.PRIMARY),
            padding="8px",
            background=Colors.PRIMARY_LIGHTER,
            border_radius=Borders.RADIUS_MD,
        ),
        rx.vstack(
            rx.text(label, font_size=Typography.SIZE_XS, color=Colors.GRAY_500),
            rx.text(value, font_size=Typography.SIZE_SM, font_weight=Typography.WEIGHT_SEMIBOLD, color=Colors.GRAY_900),
            spacing="0",
            align="start",
        ),
        spacing="3",
        align="center",
        flex="1",
    )


def cee_info_box() -> rx.Component:
    """Box d'information sur les CEE."""
    return rx.box(
        rx.hstack(
            rx.icon("info", size=16, color=Colors.INFO),
            rx.text(
                "Le montant indiqué est une estimation basée sur le prix moyen du marché (0,0065 €/kWh cumac).",
                font_size=Typography.SIZE_XS,
                color=Colors.INFO,
            ),
            spacing="2",
            align="start",
        ),
        padding=Spacing.MD,
        background=f"{Colors.INFO}10",
        border_radius=Borders.RADIUS_MD,
        width="100%",
    )


def save_button() -> rx.Component:
    """Bouton de sauvegarde avec état dynamique."""
    return rx.cond(
        SimulationState.simulation_saved,
        rx.button(
            rx.hstack(rx.icon("check", size=18), rx.text("Sauvegardée"), spacing="2"),
            disabled=True,
            size="3",
            style={
                "background": Colors.GRAY_200,
                "color": Colors.GRAY_500,
                "cursor": "not-allowed",
                "min_width": "180px",
            },
        ),
        rx.button(
            rx.hstack(rx.icon("save", size=18), rx.text("Sauvegarder"), spacing="2"),
            on_click=SimulationState.save_and_redirect,
            size="3",
            style={
                "background": Colors.SUCCESS,
                "color": Colors.WHITE,
                "_hover": {"background": "#1ea34d"},
                "transition": "all 0.2s ease",
                "min_width": "180px",
            },
        ),
    )


def export_button() -> rx.Component:
    """Bouton d'export PDF."""
    return rx.button(
        rx.hstack(rx.icon("download", size=18), rx.text("Exporter PDF"), spacing="2"),
        on_click=SimulationState.export_pdf,
        variant="outline",
        size="3",
        style={
            "border": f"2px solid {Colors.PRIMARY}",
            "color": Colors.PRIMARY,
            "_hover": {"background": Colors.PRIMARY_LIGHTER},
            "transition": "all 0.2s ease",
            "min_width": "180px",
        },
    )


def result_content() -> rx.Component:
    """Contenu de la page résultats."""
    return rx.vstack(
        # Header avec badge de succès
        rx.vstack(
            success_badge(),
            rx.vstack(
                rx.text("Simulation terminée !", font_size=Typography.SIZE_2XL, font_weight=Typography.WEIGHT_BOLD, color=Colors.GRAY_900),
                rx.text(SimulationState.simulation_name, font_size=Typography.SIZE_BASE, color=Colors.GRAY_500),
                spacing="1",
                align="center",
            ),
            spacing="4",
            align="center",
        ),
        
        # Cartes de résultats principaux
        rx.hstack(
            main_result_card(
                title="Prime CEE estimée",
                value=SimulationState.result_euros_formatted,
                subtitle="Montant indicatif HT",
                icon="euro",
                gradient_from=Colors.SUCCESS,
                gradient_to="#059669",
            ),
            main_result_card(
                title="Volume CEE",
                value=SimulationState.result_cumacs_formatted,
                subtitle="Certificats générés",
                icon="zap",
                gradient_from=Colors.PRIMARY,
                gradient_to="#466c82",
            ),
            spacing="4",
            width="100%",
        ),
        
        # Récapitulatif et Localisation - côte à côte
        rx.hstack(
            rx.box(
                detail_section_card(
                    "Récapitulatif de l'opération",
                    "clipboard-list",
                    rx.vstack(
                        summary_row("file-text", "Fiche d'opération", SimulationState.selected_fiche, highlight=True),
                        rx.divider(),
                        summary_row("building-2", "Secteur", SimulationState.sector),
                        rx.divider(),
                        summary_row("layers", "Typologie", SimulationState.typology),
                        rx.divider(),
                        summary_row("user", "Bénéficiaire", SimulationState.beneficiary_type),
                        spacing="0",
                        width="100%",
                    ),
                ),
                width="50%",
            ),
            rx.box(
                detail_section_card(
                    "Localisation & Date",
                    "map",
                    rx.vstack(
                        summary_row("map-pin", "Département", SimulationState.department),
                        rx.divider(),
                        summary_row("thermometer", "Zone climatique", SimulationState.zone_climatique, highlight=True),
                        rx.divider(),
                        summary_row("calendar", "Date de signature", SimulationState.date_signature),
                        rx.divider(),
                        rx.box(height="42px"),
                        spacing="0",
                        width="100%",
                    ),
                ),
                width="50%",
            ),
            spacing="4",
            width="100%",
            align="stretch",
        ),
        
        # Détail du calcul
        detail_section_card(
            "Détail du calcul",
            "calculator",
            rx.vstack(
                rx.hstack(
                    info_stat_item("Volume généré", SimulationState.result_cumacs_formatted, "zap"),
                    rx.box(
                        rx.text("×", font_size=Typography.SIZE_XL, color=Colors.GRAY_400),
                        padding_x=Spacing.MD,
                    ),
                    info_stat_item("Prix unitaire", "0,0065 €/kWh", "tag"),
                    rx.box(
                        rx.text("=", font_size=Typography.SIZE_XL, color=Colors.GRAY_400),
                        padding_x=Spacing.MD,
                    ),
                    rx.box(
                        rx.vstack(
                            rx.text("Prime estimée", font_size=Typography.SIZE_XS, color=Colors.GRAY_500),
                            rx.text(SimulationState.result_euros_formatted, font_size=Typography.SIZE_XL, font_weight=Typography.WEIGHT_BOLD, color=Colors.SUCCESS),
                            spacing="0",
                            align="center",
                        ),
                        padding=Spacing.MD,
                        background=Colors.SUCCESS_LIGHT,
                        border_radius=Borders.RADIUS_LG,
                        min_width="150px",
                    ),
                    spacing="2",
                    width="100%",
                    align="center",
                    justify="center",
                    flex_wrap="wrap",
                ),
                cee_info_box(),
                spacing="4",
                width="100%",
            ),
        ),
        
        # Actions - centrées
        rx.hstack(
            save_button(),
            export_button(),
            spacing="4",
            justify="center",
            width="100%",
        ),
        
        spacing="5",
        align="center",
        padding=Spacing.XL,
        width="100%",
        max_width="1000px",
    )


@rx.page(route="/simulation/result", title="Résultats - RDE Consulting")
def step6_result_page() -> rx.Component:
    return rx.hstack(
        simulation_sidebar(current_step=6),
        rx.box(
            result_content(),
            min_height="100vh",
            background=Colors.BG_PAGE,
            display="flex",
            justify_content="center",
            padding_top="40px",
            padding_bottom="40px",
            padding_x=Spacing.MD,
            margin_left="260px",
            width="100%",
        ),
        spacing="0",
        width="100%",
    )