"""Page Step 5 - Formulaire de simulation"""
#import reflex as rx
#from ..state import SimulationState
#from ..styles.design_system import Colors, Typography, Spacing, Borders, Shadows
#from .simulation_layout import simulation_layout, recap_bar, recap_item
#
#
#def beneficiary_card(b: dict) -> rx.Component:
#    """Carte de sélection d'un type de bénéficiaire."""
#    is_selected = SimulationState.beneficiary_type == b["value"]
#    
#    return rx.box(
#        rx.vstack(
#            rx.box(
#                rx.icon(
#                    b["icon"],
#                    size=24,
#                    color=rx.cond(is_selected, Colors.PRIMARY, Colors.GRAY_400),
#                ),
#                padding=Spacing.SM,
#                background=rx.cond(is_selected, Colors.PRIMARY_LIGHTER, Colors.GRAY_100),
#                border_radius=Borders.RADIUS_FULL,
#            ),
#            rx.text(
#                b["label"],
#                font_weight=Typography.WEIGHT_MEDIUM,
#                font_size=Typography.SIZE_SM,
#                color=Colors.GRAY_900,
#                text_align="center",
#            ),
#            spacing="2",
#            align="center",
#        ),
#        on_click=SimulationState.select_beneficiary(b["value"]),
#        cursor="pointer",
#        padding=Spacing.MD,
#        background=Colors.WHITE,
#        border=rx.cond(
#            is_selected,
#            f"2px solid {Colors.PRIMARY}",
#            f"1px solid {Colors.GRAY_200}",
#        ),
#        border_radius=Borders.RADIUS_LG,
#        box_shadow=rx.cond(is_selected, Shadows.SM, "none"),
#        _hover={
#            "border_color": Colors.PRIMARY,
#            "background": Colors.GRAY_50,
#        },
#        transition="all 0.2s ease",
#        flex="1",
#        min_width="100px",
#    )
#
#
#def step5_recap() -> rx.Component:
#    """Récap des étapes précédentes."""
#    return recap_bar(
#        recap_item("map-pin", SimulationState.department),
#        rx.box(width="1px", height="16px", background=Colors.GRAY_300),
#        recap_item("building-2", SimulationState.sector),
#        rx.box(width="1px", height="16px", background=Colors.GRAY_300),
#        recap_item("layers", SimulationState.typology),
#        rx.box(width="1px", height="16px", background=Colors.GRAY_300),
#        recap_item("file-text", SimulationState.selected_fiche, is_primary=True),
#    )
#
#
#def step5_content() -> rx.Component:
#    return rx.vstack(
#        # Fiche sélectionnée (info)
#        rx.box(
#            rx.hstack(
#                rx.box(
#                    rx.icon("file-text", size=20, color=Colors.PRIMARY),
#                    padding=Spacing.SM,
#                    background=Colors.PRIMARY_LIGHTER,
#                    border_radius=Borders.RADIUS_MD,
#                ),
#                rx.vstack(
#                    rx.text(SimulationState.selected_fiche, font_weight=Typography.WEIGHT_BOLD, color=Colors.PRIMARY),
#                    rx.text(SimulationState.selected_fiche_description, font_size=Typography.SIZE_XS, color=Colors.GRAY_500, no_of_lines=1),
#                    spacing="0",
#                    align="start",
#                ),
#                spacing="3",
#                align="center",
#                width="100%",
#            ),
#            padding=Spacing.MD,
#            background=Colors.PRIMARY_LIGHTER,
#            border_radius=Borders.RADIUS_LG,
#            width="100%",
#        ),
#        
#        # Nom de la simulation
#        rx.box(
#            rx.vstack(
#                rx.hstack(
#                    rx.icon("edit-3", size=16, color=Colors.PRIMARY),
#                    rx.text("Nom de la simulation", font_weight=Typography.WEIGHT_MEDIUM, color=Colors.GRAY_700),
#                    spacing="2",
#                ),
#                rx.input(
#                    placeholder="Ex: Isolation maison M. Dupont",
#                    value=SimulationState.simulation_name,
#                    on_change=SimulationState.set_simulation_name,
#                    width="100%",
#                    size="3",
#                ),
#                rx.text("Ce nom vous permettra de retrouver facilement cette simulation", font_size=Typography.SIZE_XS, color=Colors.GRAY_400),
#                spacing="2",
#                align="start",
#                width="100%",
#            ),
#            padding=Spacing.LG,
#            background=Colors.WHITE,
#            border_radius=Borders.RADIUS_LG,
#            box_shadow=Shadows.SM,
#            width="100%",
#        ),
#        
#        # Type de bénéficiaire
#        rx.box(
#            rx.vstack(
#                rx.hstack(
#                    rx.icon("users", size=16, color=Colors.PRIMARY),
#                    rx.text("Type de bénéficiaire", font_weight=Typography.WEIGHT_MEDIUM, color=Colors.GRAY_700),
#                    spacing="2",
#                ),
#                rx.hstack(
#                    rx.foreach(SimulationState.beneficiary_types_list, beneficiary_card),
#                    spacing="3",
#                    wrap="wrap",
#                    width="100%",
#                ),
#                rx.cond(
#                    SimulationState.beneficiary_type != "",
#                    rx.hstack(
#                        rx.icon("check", size=14, color=Colors.SUCCESS),
#                        rx.text(f"Bénéficiaire : {SimulationState.beneficiary_type}", font_size=Typography.SIZE_SM, color=Colors.SUCCESS),
#                        spacing="2",
#                    ),
#                    rx.fragment(),
#                ),
#                spacing="3",
#                align="start",
#                width="100%",
#            ),
#            padding=Spacing.LG,
#            background=Colors.WHITE,
#            border_radius=Borders.RADIUS_LG,
#            box_shadow=Shadows.SM,
#            width="100%",
#        ),
#        
#        # Informations complémentaires
#        rx.box(
#            rx.vstack(
#                rx.hstack(
#                    rx.icon("info", size=16, color=Colors.PRIMARY),
#                    rx.text("Informations de calcul", font_weight=Typography.WEIGHT_MEDIUM, color=Colors.GRAY_700),
#                    spacing="2",
#                ),
#                
#                # Zone climatique
#                rx.hstack(
#                    rx.hstack(
#                        rx.icon("thermometer", size=14, color=Colors.INFO),
#                        rx.text("Zone climatique :", font_size=Typography.SIZE_SM, color=Colors.GRAY_600),
#                        spacing="2",
#                    ),
#                    rx.text(SimulationState.zone_climatique, font_weight=Typography.WEIGHT_SEMIBOLD, color=Colors.INFO),
#                    spacing="2",
#                    align="center",
#                ),
#                
#                # Date signature
#                rx.hstack(
#                    rx.hstack(
#                        rx.icon("calendar", size=14, color=Colors.GRAY_400),
#                        rx.text("Date de signature :", font_size=Typography.SIZE_SM, color=Colors.GRAY_600),
#                        spacing="2",
#                    ),
#                    rx.text(SimulationState.date_signature, font_weight=Typography.WEIGHT_MEDIUM, color=Colors.GRAY_700),
#                    spacing="2",
#                    align="center",
#                ),
#                
#                # Département
#                rx.hstack(
#                    rx.hstack(
#                        rx.icon("map-pin", size=14, color=Colors.GRAY_400),
#                        rx.text("Département :", font_size=Typography.SIZE_SM, color=Colors.GRAY_600),
#                        spacing="2",
#                    ),
#                    rx.text(SimulationState.department, font_weight=Typography.WEIGHT_MEDIUM, color=Colors.GRAY_700),
#                    spacing="2",
#                    align="center",
#                ),
#                
#                spacing="3",
#                align="start",
#                width="100%",
#            ),
#            padding=Spacing.LG,
#            background=Colors.WHITE,
#            border_radius=Borders.RADIUS_LG,
#            box_shadow=Shadows.SM,
#            width="100%",
#        ),
#        
#        # Message d'erreur
#        rx.cond(
#            SimulationState.error_message != "",
#            rx.box(
#                rx.hstack(
#                    rx.icon("alert-circle", size=16, color=Colors.ERROR),
#                    rx.text(SimulationState.error_message, color=Colors.ERROR, font_size=Typography.SIZE_SM),
#                    spacing="2",
#                    align="center",
#                ),
#                padding=Spacing.MD,
#                background=Colors.ERROR_LIGHT,
#                border_radius=Borders.RADIUS_MD,
#                width="100%",
#            ),
#            rx.fragment(),
#        ),
#        
#        spacing="4",
#        width="100%",
#    )
#
#
#@rx.page(route="/simulation/form", title="Formulaire - SimuPrime")
#def step5_form_page() -> rx.Component:
#    return rx.box(
#        rx.vstack(
#            # Header
#            rx.vstack(
#                rx.text("Configuration de la Simulation", font_size=Typography.SIZE_2XL, font_weight=Typography.WEIGHT_BOLD, text_align="center"),
#                rx.text("Étape 5 sur 6 : Paramètres et bénéficiaire", color=Colors.GRAY_500, text_align="center"),
#                spacing="1",
#                align="center",
#                width="100%",
#            ),
#            
#            # Progress bar
#            rx.box(
#                rx.box(
#                    width="83.33%",
#                    height="100%",
#                    background=Colors.PRIMARY,
#                    border_radius=Borders.RADIUS_FULL,
#                    transition="width 0.3s ease",
#                ),
#                width="100%",
#                height="6px",
#                background=Colors.GRAY_200,
#                border_radius=Borders.RADIUS_FULL,
#                overflow="hidden",
#            ),
#            
#            # Récap
#            step5_recap(),
#            
#            # Contenu
#            step5_content(),
#            
#            # Navigation
#            rx.hstack(
#                rx.button(
#                    rx.hstack(rx.icon("chevron-left", size=18), rx.text("Retour"), spacing="2"),
#                    variant="ghost",
#                    on_click=rx.redirect("/simulation/fiches"),
#                    size="3",
#                ),
#                rx.spacer(),
#                rx.button(
#                    rx.hstack(
#                        rx.cond(
#                            SimulationState.is_loading,
#                            rx.spinner(size="1"),
#                            rx.icon("calculator", size=18),
#                        ),
#                        rx.text("Calculer la prime"),
#                        spacing="2",
#                    ),
#                    disabled=(SimulationState.beneficiary_type == "") | (SimulationState.is_loading),
#                    on_click=SimulationState.execute_simulation,
#                    size="3",
#                    style={
#                        "background": Colors.SUCCESS,
#                        "color": Colors.WHITE,
#                        "cursor": rx.cond(
#                            (SimulationState.beneficiary_type == "") | (SimulationState.is_loading),
#                            "not-allowed",
#                            "pointer",
#                        ),
#                    },
#                ),
#                width="100%",
#            ),
#            
#            spacing="5",
#            align="center",
#            padding=Spacing.XL,
#            width="100%",
#            max_width="800px",
#        ),
#        min_height="100vh",
#        background=Colors.BG_PAGE,
#        display="flex",
#        justify_content="center",
#        padding_top="40px",
#        padding_x=Spacing.MD,
#    )

"""Page Step 5 - Formulaire de simulation"""
import reflex as rx
from ..state import SimulationState
from ..styles.design_system import Colors, Typography, Spacing, Borders, Shadows
from .simulation_layout import recap_bar, recap_item
from ..components.sidebar import simulation_sidebar


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


def step5_recap() -> rx.Component:
    """Récap des étapes précédentes."""
    return recap_bar(
        recap_item("map-pin", SimulationState.department),
        rx.box(width="1px", height="16px", background=Colors.GRAY_300),
        recap_item("building-2", SimulationState.sector),
        rx.box(width="1px", height="16px", background=Colors.GRAY_300),
        recap_item("layers", SimulationState.typology),
        rx.box(width="1px", height="16px", background=Colors.GRAY_300),
        recap_item("file-text", SimulationState.selected_fiche, is_primary=True),
    )


def step5_content() -> rx.Component:
    return rx.vstack(
        # Fiche sélectionnée (info)
        rx.box(
            rx.hstack(
                rx.box(
                    rx.icon("file-text", size=20, color=Colors.PRIMARY),
                    padding=Spacing.SM,
                    background=Colors.PRIMARY_LIGHTER,
                    border_radius=Borders.RADIUS_MD,
                ),
                rx.vstack(
                    rx.text(SimulationState.selected_fiche, font_weight=Typography.WEIGHT_BOLD, color=Colors.PRIMARY),
                    rx.text(SimulationState.selected_fiche_description, font_size=Typography.SIZE_XS, color=Colors.GRAY_500, no_of_lines=1),
                    spacing="0",
                    align="start",
                ),
                spacing="3",
                align="center",
                width="100%",
            ),
            padding=Spacing.MD,
            background=Colors.PRIMARY_LIGHTER,
            border_radius=Borders.RADIUS_LG,
            width="100%",
        ),
        
        # Nom de la simulation
        rx.box(
            rx.vstack(
                rx.hstack(
                    rx.icon("edit-3", size=16, color=Colors.PRIMARY),
                    rx.text("Nom de la simulation", font_weight=Typography.WEIGHT_MEDIUM, color=Colors.GRAY_700),
                    spacing="2",
                ),
                rx.input(
                    placeholder="Ex: Isolation maison M. Dupont",
                    value=SimulationState.simulation_name,
                    on_change=SimulationState.set_simulation_name,
                    width="100%",
                    size="3",
                ),
                rx.text("Ce nom vous permettra de retrouver facilement cette simulation", font_size=Typography.SIZE_XS, color=Colors.GRAY_400),
                spacing="2",
                align="start",
                width="100%",
            ),
            padding=Spacing.LG,
            background=Colors.WHITE,
            border_radius=Borders.RADIUS_LG,
            box_shadow=Shadows.SM,
            width="100%",
        ),
        
        # Type de bénéficiaire
        rx.box(
            rx.vstack(
                rx.hstack(
                    rx.icon("users", size=16, color=Colors.PRIMARY),
                    rx.text("Type de bénéficiaire", font_weight=Typography.WEIGHT_MEDIUM, color=Colors.GRAY_700),
                    spacing="2",
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
                        rx.text(f"Bénéficiaire : {SimulationState.beneficiary_type}", font_size=Typography.SIZE_SM, color=Colors.SUCCESS),
                        spacing="2",
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
        ),
        
        # Informations complémentaires
        rx.box(
            rx.vstack(
                rx.hstack(
                    rx.icon("info", size=16, color=Colors.PRIMARY),
                    rx.text("Informations de calcul", font_weight=Typography.WEIGHT_MEDIUM, color=Colors.GRAY_700),
                    spacing="2",
                ),
                rx.hstack(
                    rx.hstack(
                        rx.icon("thermometer", size=14, color=Colors.INFO),
                        rx.text("Zone climatique :", font_size=Typography.SIZE_SM, color=Colors.GRAY_600),
                        spacing="2",
                    ),
                    rx.text(SimulationState.zone_climatique, font_weight=Typography.WEIGHT_SEMIBOLD, color=Colors.INFO),
                    spacing="2",
                    align="center",
                ),
                rx.hstack(
                    rx.hstack(
                        rx.icon("calendar", size=14, color=Colors.GRAY_400),
                        rx.text("Date de signature :", font_size=Typography.SIZE_SM, color=Colors.GRAY_600),
                        spacing="2",
                    ),
                    rx.text(SimulationState.date_signature, font_weight=Typography.WEIGHT_MEDIUM, color=Colors.GRAY_700),
                    spacing="2",
                    align="center",
                ),
                rx.hstack(
                    rx.hstack(
                        rx.icon("map-pin", size=14, color=Colors.GRAY_400),
                        rx.text("Département :", font_size=Typography.SIZE_SM, color=Colors.GRAY_600),
                        spacing="2",
                    ),
                    rx.text(SimulationState.department, font_weight=Typography.WEIGHT_MEDIUM, color=Colors.GRAY_700),
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
        ),
        
        spacing="4",
        width="100%",
    )


@rx.page(route="/simulation/form", title="Formulaire - SimuPrime")
def step5_form_page() -> rx.Component:
    return rx.hstack(
        # Sidebar
        simulation_sidebar(current_step=5),
        
        # Contenu principal
        rx.box(
            rx.vstack(
                # Header
                rx.vstack(
                    rx.text("Configuration de la Simulation", font_size=Typography.SIZE_2XL, font_weight=Typography.WEIGHT_BOLD, text_align="center"),
                    rx.text("Étape 5 sur 6 : Paramètres et bénéficiaire", color=Colors.GRAY_500, text_align="center"),
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
                        rx.hstack(rx.icon("chevron-left", size=18), rx.text("Retour"), spacing="2"),
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
                        ),
                        disabled=(SimulationState.beneficiary_type == "") | SimulationState.is_loading,
                        on_click=SimulationState.execute_simulation,
                        size="3",
                        style={
                            "background": Colors.SUCCESS,
                            "color": Colors.WHITE,
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