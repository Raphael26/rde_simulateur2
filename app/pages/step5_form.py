"""
Page Step 5 - Formulaire de simulation avec champs dynamiques
Charge les paramètres depuis la configuration de la fiche sélectionnée.
"""

import reflex as rx
from typing import Dict
from ..state.simulation_state import SimulationState
from ..styles.design_system import Colors, Typography, Spacing, Borders, Shadows
from ..components.sidebar import simulation_sidebar


def step5_recap() -> rx.Component:
    """Barre de récap des étapes précédentes."""
    return rx.hstack(
        rx.hstack(
            rx.icon("map-pin", size=14, color=Colors.GRAY_400),
            rx.text(SimulationState.department, font_size=Typography.SIZE_SM, color=Colors.GRAY_600, no_of_lines=1),
            spacing="1",
            align="center",
        ),
        rx.box(width="1px", height="16px", background=Colors.GRAY_300),
        rx.hstack(
            rx.icon("building-2", size=14, color=Colors.GRAY_400),
            rx.text(SimulationState.sector, font_size=Typography.SIZE_SM, color=Colors.GRAY_600, no_of_lines=1),
            spacing="1",
            align="center",
        ),
        rx.box(width="1px", height="16px", background=Colors.GRAY_300),
        rx.hstack(
            rx.icon("layers", size=14, color=Colors.GRAY_400),
            rx.text(SimulationState.typology, font_size=Typography.SIZE_SM, color=Colors.GRAY_600, no_of_lines=1),
            spacing="1",
            align="center",
        ),
        rx.box(width="1px", height="16px", background=Colors.GRAY_300),
        rx.hstack(
            rx.icon("file-text", size=14, color=Colors.PRIMARY),
            rx.text(SimulationState.selected_fiche, font_size=Typography.SIZE_SM, color=Colors.PRIMARY, font_weight="600"),
            spacing="1",
            align="center",
        ),
        spacing="3",
        padding="0.75rem 1rem",
        background=Colors.GRAY_50,
        border_radius=Borders.RADIUS_LG,
        width="100%",
        flex_wrap="wrap",
        justify="center",
        align="center",
    )


def beneficiary_card(b: dict) -> rx.Component:
    """Carte de sélection d'un type de bénéficiaire."""
    is_selected = SimulationState.beneficiary_type == b["value"]
    
    return rx.box(
        rx.vstack(
            rx.box(
                rx.icon(
                    b["icon"],
                    size=24,
                    color=rx.cond(is_selected, Colors.PRIMARY, Colors.GRAY_400),
                ),
                padding=Spacing.SM,
                background=rx.cond(is_selected, Colors.PRIMARY_LIGHTER, Colors.GRAY_100),
                border_radius=Borders.RADIUS_FULL,
            ),
            rx.text(
                b["label"],
                font_weight=Typography.WEIGHT_MEDIUM,
                font_size=Typography.SIZE_SM,
                color=Colors.GRAY_900,
                text_align="center",
            ),
            spacing="2",
            align="center",
        ),
        on_click=SimulationState.select_beneficiary(b["value"]),
        cursor="pointer",
        padding=Spacing.MD,
        background=Colors.WHITE,
        border=rx.cond(
            is_selected,
            f"2px solid {Colors.PRIMARY}",
            f"1px solid {Colors.GRAY_200}",
        ),
        border_radius=Borders.RADIUS_LG,
        box_shadow=rx.cond(is_selected, Shadows.SM, "none"),
        _hover={
            "border_color": Colors.PRIMARY,
            "background": Colors.GRAY_50,
        },
        transition="all 0.2s ease",
        flex="1",
        min_width="100px",
    )


def render_select_field(field: rx.Var[Dict[str, str]]) -> rx.Component:
    """Render un champ dropdown."""
    param_name = field["param_name"]
    label = field["label"]
    options_str = field["options_str"]
    
    return rx.box(
        rx.vstack(
            rx.hstack(
                rx.icon("list", size=14, color=Colors.PRIMARY),
                rx.text(
                    label,
                    font_weight=Typography.WEIGHT_MEDIUM,
                    font_size=Typography.SIZE_SM,
                    color=Colors.GRAY_700,
                ),
                spacing="2",
                align="center",
            ),
            rx.select.root(
                rx.select.trigger(
                    placeholder="Sélectionnez une option",
                    width="100%",
                ),
                rx.select.content(
                    rx.foreach(
                        options_str.split("|"),
                        lambda opt: rx.select.item(opt, value=opt),
                    ),
                ),
                on_change=lambda val, p=param_name, l=label: SimulationState.set_param(p, l, val),
                width="100%",
            ),
            spacing="2",
            width="100%",
            align_items="start",
        ),
        padding=Spacing.MD,
        background=Colors.WHITE,
        border_radius=Borders.RADIUS_LG,
        border=f"1px solid {Colors.GRAY_200}",
        width="100%",
    )


def render_number_field(field: rx.Var[Dict[str, str]]) -> rx.Component:
    """Render un champ input numérique."""
    param_name = field["param_name"]
    label = field["label"]
    
    return rx.box(
        rx.vstack(
            rx.hstack(
                rx.icon("hash", size=14, color=Colors.PRIMARY),
                rx.text(
                    label,
                    font_weight=Typography.WEIGHT_MEDIUM,
                    font_size=Typography.SIZE_SM,
                    color=Colors.GRAY_700,
                ),
                spacing="2",
                align="center",
            ),
            rx.input(
                placeholder="Entrez une valeur numérique",
                type="number",
                on_change=lambda val, p=param_name: SimulationState.set_numeric_param(p, val),
                width="100%",
                size="3",
            ),
            spacing="2",
            width="100%",
            align_items="start",
        ),
        padding=Spacing.MD,
        background=Colors.WHITE,
        border_radius=Borders.RADIUS_LG,
        border=f"1px solid {Colors.GRAY_200}",
        width="100%",
    )


def dynamic_fields_section() -> rx.Component:
    """Section des champs dynamiques chargés depuis la configuration."""
    return rx.cond(
        SimulationState.has_dynamic_fields,
        rx.box(
            rx.vstack(
                rx.hstack(
                    rx.icon("sliders", size=16, color=Colors.PRIMARY),
                    rx.text(
                        "Paramètres de calcul",
                        font_weight=Typography.WEIGHT_MEDIUM,
                        color=Colors.GRAY_700,
                    ),
                    spacing="2",
                    width="100%",
                    align="center",
                ),
                rx.divider(),
                # Afficher les champs select
                rx.foreach(
                    SimulationState.select_fields,
                    render_select_field,
                ),
                # Afficher les champs numériques
                rx.foreach(
                    SimulationState.number_fields,
                    render_number_field,
                ),
                spacing="3",
                align="start",
                width="100%",
            ),
            padding=Spacing.LG,
            background=Colors.WHITE,
            border_radius=Borders.RADIUS_LG,
            box_shadow=Shadows.SM,
            width="100%",
        ),
        # Message si pas de champs dynamiques
        rx.box(
            rx.hstack(
                rx.icon("info", size=18, color=Colors.INFO),
                rx.vstack(
                    rx.text(
                        "Mode démonstration",
                        font_weight=Typography.WEIGHT_MEDIUM,
                        color=Colors.INFO,
                    ),
                    rx.text(
                        "Cette fiche utilise un calcul simplifié. Les paramètres détaillés seront disponibles prochainement.",
                        font_size=Typography.SIZE_SM,
                        color=Colors.GRAY_500,
                    ),
                    spacing="1",
                    align="start",
                ),
                spacing="3",
                align="start",
            ),
            padding=Spacing.LG,
            background=f"{Colors.INFO}10",
            border=f"1px solid {Colors.INFO}30",
            border_radius=Borders.RADIUS_LG,
            width="100%",
        ),
    )


def fiche_info_card() -> rx.Component:
    """Carte d'information sur la fiche sélectionnée."""
    return rx.box(
        rx.hstack(
            rx.box(
                rx.icon("file-text", size=20, color=Colors.PRIMARY),
                padding=Spacing.SM,
                background=Colors.PRIMARY_LIGHTER,
                border_radius=Borders.RADIUS_MD,
            ),
            rx.vstack(
                rx.text(
                    SimulationState.selected_fiche,
                    font_weight=Typography.WEIGHT_BOLD,
                    color=Colors.PRIMARY,
                ),
                rx.text(
                    SimulationState.selected_fiche_description,
                    font_size=Typography.SIZE_XS,
                    color=Colors.GRAY_500,
                    no_of_lines=2,
                ),
                spacing="0",
                align="start",
            ),
            rx.spacer(),
            rx.cond(
                SimulationState.fiche_loaded,
                rx.hstack(
                    rx.icon("check-circle", size=16, color=Colors.SUCCESS),
                    rx.text("Configurée", font_size=Typography.SIZE_XS, color=Colors.SUCCESS),
                    spacing="1",
                    align="center",
                ),
                rx.cond(
                    SimulationState.is_loading,
                    rx.spinner(size="1"),
                    rx.hstack(
                        rx.icon("alert-circle", size=16, color=Colors.WARNING),
                        rx.text("Mode démo", font_size=Typography.SIZE_XS, color=Colors.WARNING),
                        spacing="1",
                        align="center",
                    ),
                ),
            ),
            spacing="3",
            align="center",
            width="100%",
        ),
        padding=Spacing.MD,
        background=Colors.PRIMARY_LIGHTER,
        border_radius=Borders.RADIUS_LG,
        width="100%",
    )


def simulation_name_card() -> rx.Component:
    """Carte pour le nom de la simulation."""
    return rx.box(
        rx.vstack(
            rx.hstack(
                rx.icon("edit-3", size=16, color=Colors.PRIMARY),
                rx.text(
                    "Nom de la simulation",
                    font_weight=Typography.WEIGHT_MEDIUM,
                    color=Colors.GRAY_700,
                ),
                spacing="2",
                align="center",
            ),
            rx.input(
                placeholder="Ex: Isolation maison M. Dupont",
                value=SimulationState.simulation_name,
                on_change=SimulationState.set_simulation_name,
                width="100%",
                size="3",
            ),
            rx.text(
                "Ce nom vous permettra de retrouver facilement cette simulation",
                font_size=Typography.SIZE_XS,
                color=Colors.GRAY_400,
            ),
            spacing="2",
            align="start",
            width="100%",
        ),
        padding=Spacing.LG,
        background=Colors.WHITE,
        border_radius=Borders.RADIUS_LG,
        box_shadow=Shadows.SM,
        width="100%",
    )


def beneficiary_card_section() -> rx.Component:
    """Section de sélection du bénéficiaire."""
    return rx.box(
        rx.vstack(
            rx.hstack(
                rx.icon("users", size=16, color=Colors.PRIMARY),
                rx.text(
                    "Type de bénéficiaire",
                    font_weight=Typography.WEIGHT_MEDIUM,
                    color=Colors.GRAY_700,
                ),
                spacing="2",
                align="center",
            ),
            rx.hstack(
                rx.foreach(SimulationState.beneficiary_types_list, beneficiary_card),
                spacing="3",
                wrap="wrap",
                width="100%",
            ),
            rx.cond(
                SimulationState.beneficiary_type != "",
                rx.hstack(
                    rx.icon("check", size=14, color=Colors.SUCCESS),
                    rx.text(
                        SimulationState.beneficiary_type,
                        font_size=Typography.SIZE_SM,
                        color=Colors.SUCCESS,
                    ),
                    spacing="2",
                    align="center",
                ),
                rx.fragment(),
            ),
            spacing="3",
            align="start",
            width="100%",
        ),
        padding=Spacing.LG,
        background=Colors.WHITE,
        border_radius=Borders.RADIUS_LG,
        box_shadow=Shadows.SM,
        width="100%",
    )


def info_card_section() -> rx.Component:
    """Section des informations de calcul."""
    return rx.box(
        rx.vstack(
            rx.hstack(
                rx.icon("info", size=16, color=Colors.PRIMARY),
                rx.text(
                    "Informations de calcul",
                    font_weight=Typography.WEIGHT_MEDIUM,
                    color=Colors.GRAY_700,
                ),
                spacing="2",
                align="center",
            ),
            rx.hstack(
                rx.hstack(
                    rx.icon("thermometer", size=14, color=Colors.INFO),
                    rx.text("Zone climatique :", font_size=Typography.SIZE_SM, color=Colors.GRAY_600),
                    spacing="2",
                    align="center",
                ),
                rx.text(
                    SimulationState.zone_climatique,
                    font_weight=Typography.WEIGHT_SEMIBOLD,
                    color=Colors.INFO,
                ),
                spacing="2",
                align="center",
            ),
            rx.hstack(
                rx.hstack(
                    rx.icon("calendar", size=14, color=Colors.GRAY_400),
                    rx.text("Date de signature :", font_size=Typography.SIZE_SM, color=Colors.GRAY_600),
                    spacing="2",
                    align="center",
                ),
                rx.text(
                    SimulationState.date_signature,
                    font_weight=Typography.WEIGHT_MEDIUM,
                    color=Colors.GRAY_700,
                ),
                spacing="2",
                align="center",
            ),
            rx.hstack(
                rx.hstack(
                    rx.icon("map-pin", size=14, color=Colors.GRAY_400),
                    rx.text("Département :", font_size=Typography.SIZE_SM, color=Colors.GRAY_600),
                    spacing="2",
                    align="center",
                ),
                rx.text(
                    SimulationState.department,
                    font_weight=Typography.WEIGHT_MEDIUM,
                    color=Colors.GRAY_700,
                ),
                spacing="2",
                align="center",
            ),
            spacing="3",
            align="start",
            width="100%",
        ),
        padding=Spacing.LG,
        background=Colors.WHITE,
        border_radius=Borders.RADIUS_LG,
        box_shadow=Shadows.SM,
        width="100%",
    )


def step5_content() -> rx.Component:
    """Contenu principal de l'étape 5."""
    return rx.vstack(
        # Fiche sélectionnée
        fiche_info_card(),
        
        # Nom de la simulation
        simulation_name_card(),
        
        # Type de bénéficiaire
        beneficiary_card_section(),
        
        # Champs dynamiques
        dynamic_fields_section(),
        
        # Informations de calcul
        info_card_section(),
        
        spacing="4",
        width="100%",
    )


@rx.page(route="/simulation/form", title="Formulaire - RDE Consulting")
def step5_form_page() -> rx.Component:
    return rx.hstack(
        # Sidebar
        simulation_sidebar(current_step=5),
        
        # Contenu principal
        rx.box(
            rx.vstack(
                # Header
                rx.vstack(
                    rx.text(
                        "Configuration de la Simulation",
                        font_size=Typography.SIZE_2XL,
                        font_weight=Typography.WEIGHT_BOLD,
                        text_align="center",
                    ),
                    rx.text(
                        "Étape 5 sur 6 : Paramètres et bénéficiaire",
                        color=Colors.GRAY_500,
                        text_align="center",
                    ),
                    spacing="1",
                    align="center",
                    width="100%",
                ),
                
                # Progress bar
                rx.box(
                    rx.box(
                        width="83.33%",
                        height="100%",
                        background=Colors.PRIMARY,
                        border_radius=Borders.RADIUS_FULL,
                        transition="width 0.3s ease",
                    ),
                    width="100%",
                    height="6px",
                    background=Colors.GRAY_200,
                    border_radius=Borders.RADIUS_FULL,
                    overflow="hidden",
                ),
                
                # Récap
                step5_recap(),
                
                # Contenu
                step5_content(),
                
                # Navigation
                rx.hstack(
                    rx.button(
                        rx.hstack(
                            rx.icon("chevron-left", size=18),
                            rx.text("Retour"),
                            spacing="2",
                            align="center",
                        ),
                        variant="ghost",
                        on_click=rx.redirect("/simulation/fiches"),
                        size="3",
                    ),
                    rx.spacer(),
                    rx.button(
                        rx.hstack(
                            rx.cond(
                                SimulationState.is_loading,
                                rx.spinner(size="1"),
                                rx.icon("calculator", size=18),
                            ),
                            rx.text("Calculer la prime"),
                            spacing="2",
                            align="center",
                        ),
                        disabled=(SimulationState.beneficiary_type == "") | SimulationState.is_loading,
                        on_click=SimulationState.execute_simulation,
                        size="3",
                        style={
                            "background": Colors.SUCCESS,
                            "color": Colors.WHITE,
                            "_disabled": {
                                "opacity": "0.5",
                                "cursor": "not-allowed",
                            },
                        },
                    ),
                    width="100%",
                ),
                
                spacing="5",
                align="center",
                padding=Spacing.XL,
                width="100%",
                max_width="800px",
            ),
            min_height="100vh",
            background=Colors.BG_PAGE,
            display="flex",
            justify_content="center",
            padding_top="40px",
            padding_x=Spacing.MD,
            margin_left="260px",
            width="100%",
        ),
        
        spacing="0",
        width="100%",
    )