"""Page Step 3 - Typologie"""
#import reflex as rx
#from ..state import SimulationState
#from ..styles.design_system import Colors, Typography, Spacing, Borders, Shadows
#
#
#def typology_card(typo: dict) -> rx.Component:
#    """Carte de sélection d'une typologie."""
#    is_selected = SimulationState.typology == typo["name"]
#    
#    return rx.box(
#        rx.vstack(
#            rx.box(
#                rx.icon(
#                    typo["icon"],
#                    size=28,
#                    color=rx.cond(is_selected, Colors.PRIMARY, Colors.GRAY_400),
#                ),
#                padding=Spacing.MD,
#                background=rx.cond(is_selected, Colors.PRIMARY_LIGHTER, Colors.GRAY_100),
#                border_radius=Borders.RADIUS_FULL,
#            ),
#            rx.text(
#                typo["name"],
#                font_weight=Typography.WEIGHT_SEMIBOLD,
#                font_size=Typography.SIZE_BASE,
#                color=Colors.GRAY_900,
#            ),
#            rx.text(
#                typo["description"],
#                font_size=Typography.SIZE_XS,
#                color=Colors.GRAY_500,
#                text_align="center",
#            ),
#            rx.box(
#                rx.text(
#                    typo["abbr"],
#                    font_size=Typography.SIZE_XS,
#                    font_weight=Typography.WEIGHT_MEDIUM,
#                    color=rx.cond(is_selected, Colors.PRIMARY, Colors.GRAY_400),
#                ),
#                padding=f"2px {Spacing.SM}",
#                background=rx.cond(is_selected, Colors.PRIMARY_LIGHTER, Colors.GRAY_100),
#                border_radius=Borders.RADIUS_FULL,
#            ),
#            spacing="2",
#            align="center",
#        ),
#        on_click=SimulationState.select_typology(typo["name"], typo["abbr"]),
#        cursor="pointer",
#        padding=Spacing.LG,
#        background=Colors.WHITE,
#        border=rx.cond(
#            is_selected,
#            f"2px solid {Colors.PRIMARY}",
#            f"1px solid {Colors.GRAY_200}",
#        ),
#        border_radius=Borders.RADIUS_XL,
#        box_shadow=rx.cond(is_selected, Shadows.MD, Shadows.SM),
#        _hover={
#            "border_color": Colors.PRIMARY,
#            "transform": "translateY(-2px)",
#            "box_shadow": Shadows.MD,
#        },
#        transition="all 0.2s ease",
#        min_width="140px",
#        flex="1",
#    )
#
#
#def typology_content() -> rx.Component:
#    return rx.box(
#        rx.vstack(
#            # Header
#            rx.vstack(
#                rx.text("Sélection de la Typologie", font_size=Typography.SIZE_2XL, font_weight=Typography.WEIGHT_BOLD),
#                rx.text("Étape 3 sur 6 : Choisissez le type d'opération", color=Colors.GRAY_500),
#                spacing="1",
#                align="center",
#            ),
#            
#            # Progress bar
#            rx.box(
#                rx.box(
#                    width="50%",
#                    height="100%",
#                    background=Colors.PRIMARY,
#                    border_radius=Borders.RADIUS_FULL,
#                ),
#                width="100%",
#                max_width="400px",
#                height="6px",
#                background=Colors.GRAY_200,
#                border_radius=Borders.RADIUS_FULL,
#                overflow="hidden",
#            ),
#            
#            # Récap étapes précédentes
#            rx.box(
#                rx.hstack(
#                    rx.hstack(
#                        rx.icon("calendar", size=14, color=Colors.GRAY_400),
#                        rx.text(SimulationState.date_signature, font_size=Typography.SIZE_SM, color=Colors.GRAY_600),
#                        spacing="1",
#                    ),
#                    rx.box(width="1px", height="16px", background=Colors.GRAY_300),
#                    rx.hstack(
#                        rx.icon("map-pin", size=14, color=Colors.GRAY_400),
#                        rx.text(SimulationState.department, font_size=Typography.SIZE_SM, color=Colors.GRAY_600),
#                        spacing="1",
#                    ),
#                    rx.box(width="1px", height="16px", background=Colors.GRAY_300),
#                    rx.hstack(
#                        rx.icon("building-2", size=14, color=Colors.PRIMARY),
#                        rx.text(SimulationState.sector, font_size=Typography.SIZE_SM, color=Colors.PRIMARY, font_weight=Typography.WEIGHT_MEDIUM),
#                        spacing="1",
#                    ),
#                    spacing="3",
#                    align="center",
#                    wrap="wrap",
#                    justify="center",
#                ),
#                padding=Spacing.MD,
#                background=Colors.GRAY_50,
#                border_radius=Borders.RADIUS_MD,
#                border=f"1px solid {Colors.GRAY_200}",
#            ),
#            
#            # Grille des typologies
#            rx.box(
#                rx.vstack(
#                    rx.hstack(
#                        rx.icon("layers", size=16, color=Colors.PRIMARY),
#                        rx.text("Typologies disponibles pour ", font_weight=Typography.WEIGHT_MEDIUM),
#                        rx.text(SimulationState.sector, font_weight=Typography.WEIGHT_BOLD, color=Colors.PRIMARY),
#                        spacing="2",
#                    ),
#                    rx.cond(
#                        SimulationState.available_typologies.length() > 0,
#                        rx.box(
#                            rx.hstack(
#                                rx.foreach(SimulationState.available_typologies, typology_card),
#                                spacing="3",
#                                wrap="wrap",
#                                justify="center",
#                                width="100%",
#                            ),
#                            width="100%",
#                        ),
#                        rx.box(
#                            rx.vstack(
#                                rx.icon("alert-circle", size=32, color=Colors.GRAY_400),
#                                rx.text("Aucune typologie disponible", color=Colors.GRAY_500),
#                                rx.text("Veuillez d'abord sélectionner un secteur", font_size=Typography.SIZE_SM, color=Colors.GRAY_400),
#                                spacing="2",
#                                align="center",
#                            ),
#                            padding=Spacing.XL,
#                        ),
#                    ),
#                    spacing="4",
#                    width="100%",
#                ),
#                padding=Spacing.LG,
#                background=Colors.WHITE,
#                border_radius=Borders.RADIUS_LG,
#                box_shadow=Shadows.SM,
#                width="100%",
#                max_width="700px",
#            ),
#            
#            # Typologie sélectionnée
#            rx.cond(
#                SimulationState.typology != "",
#                rx.box(
#                    rx.hstack(
#                        rx.box(
#                            rx.icon("check-circle", size=18, color=Colors.SUCCESS),
#                            padding="8px",
#                            background=Colors.SUCCESS_LIGHT,
#                            border_radius=Borders.RADIUS_FULL,
#                        ),
#                        rx.vstack(
#                            rx.text("Typologie sélectionnée", font_size=Typography.SIZE_XS, color=Colors.GRAY_500),
#                            rx.hstack(
#                                rx.text(SimulationState.typology, font_weight=Typography.WEIGHT_SEMIBOLD, color=Colors.SUCCESS),
#                                rx.box(
#                                    rx.text(SimulationState.typology_abbr, font_size=Typography.SIZE_XS, color=Colors.SUCCESS),
#                                    padding=f"2px {Spacing.SM}",
#                                    background=Colors.SUCCESS_LIGHT,
#                                    border_radius=Borders.RADIUS_FULL,
#                                ),
#                                spacing="2",
#                                align="center",
#                            ),
#                            spacing="0",
#                            align="start",
#                        ),
#                        spacing="3",
#                        align="center",
#                    ),
#                    padding=Spacing.MD,
#                    background=Colors.WHITE,
#                    border=f"1px solid {Colors.SUCCESS}",
#                    border_radius=Borders.RADIUS_LG,
#                    width="100%",
#                    max_width="400px",
#                ),
#                rx.fragment(),
#            ),
#            
#            # Code fiche prévisualisation
#            rx.cond(
#                (SimulationState.sector_abbr != "") & (SimulationState.typology_abbr != ""),
#                rx.box(
#                    rx.hstack(
#                        rx.icon("file-code", size=16, color=Colors.INFO),
#                        rx.text("Préfixe des fiches : ", font_size=Typography.SIZE_SM, color=Colors.GRAY_600),
#                        rx.text(
#                            f"{SimulationState.sector_abbr}-{SimulationState.typology_abbr}-XXX",
#                            font_family="monospace",
#                            font_weight=Typography.WEIGHT_MEDIUM,
#                            color=Colors.INFO,
#                        ),
#                        spacing="2",
#                        align="center",
#                    ),
#                    padding=Spacing.MD,
#                    background=Colors.INFO_LIGHT,
#                    border_radius=Borders.RADIUS_MD,
#                    width="100%",
#                    max_width="400px",
#                ),
#                rx.fragment(),
#            ),
#            
#            # Navigation
#            rx.hstack(
#                rx.button(
#                    rx.hstack(rx.icon("chevron-left", size=18), rx.text("Retour"), spacing="2"),
#                    variant="ghost",
#                    on_click=rx.redirect("/simulation/sector"),
#                    size="3",
#                ),
#                rx.spacer(),
#                rx.button(
#                    rx.hstack(rx.text("Continuer"), rx.icon("chevron-right", size=18), spacing="2"),
#                    disabled=SimulationState.typology == "",
#                    on_click=rx.redirect("/simulation/fiches"),
#                    size="3",
#                    style={
#                        "background": Colors.PRIMARY,
#                        "color": Colors.WHITE,
#                    },
#                ),
#                width="100%",
#                max_width="400px",
#            ),
#            
#            spacing="6",
#            align="center",
#            padding=Spacing.XL,
#            width="100%",
#        ),
#        min_height="100vh",
#        background=Colors.BG_PAGE,
#        display="flex",
#        justify_content="center",
#        padding_top="40px",
#    )
#
#
#@rx.page(route="/simulation/typology", title="Typologie - SimuPrime")
#def typology_page() -> rx.Component:
#    return typology_content()

"""Page Step 3 - Typologie"""
import reflex as rx
from ..state import SimulationState
from ..styles.design_system import Colors, Typography, Spacing, Borders, Shadows
from .simulation_layout import simulation_layout, recap_bar, recap_item


def typology_card(typo: dict) -> rx.Component:
    """Carte de sélection d'une typologie."""
    is_selected = SimulationState.typology == typo["name"]
    
    return rx.box(
        rx.vstack(
            rx.box(
                rx.icon(
                    typo["icon"],
                    size=28,
                    color=rx.cond(is_selected, Colors.PRIMARY, Colors.GRAY_400),
                ),
                padding=Spacing.MD,
                background=rx.cond(is_selected, Colors.PRIMARY_LIGHTER, Colors.GRAY_100),
                border_radius=Borders.RADIUS_FULL,
            ),
            rx.text(
                typo["name"],
                font_weight=Typography.WEIGHT_SEMIBOLD,
                font_size=Typography.SIZE_BASE,
                color=Colors.GRAY_900,
                text_align="center",
            ),
            rx.text(
                typo["description"],
                font_size=Typography.SIZE_XS,
                color=Colors.GRAY_500,
                text_align="center",
            ),
            spacing="2",
            align="center",
        ),
        on_click=SimulationState.select_typology(typo["name"], typo["abbr"]),
        cursor="pointer",
        padding=Spacing.LG,
        background=Colors.WHITE,
        border=rx.cond(
            is_selected,
            f"2px solid {Colors.PRIMARY}",
            f"1px solid {Colors.GRAY_200}",
        ),
        border_radius=Borders.RADIUS_XL,
        box_shadow=rx.cond(is_selected, Shadows.MD, Shadows.SM),
        _hover={
            "border_color": Colors.PRIMARY,
            "transform": "translateY(-2px)",
            "box_shadow": Shadows.MD,
        },
        transition="all 0.2s ease",
        flex="1",
        min_width="160px",
        max_width="200px",
    )


def step3_recap() -> rx.Component:
    """Récap des étapes précédentes."""
    return recap_bar(
        recap_item("calendar", SimulationState.date_signature),
        rx.box(width="1px", height="16px", background=Colors.GRAY_300),
        recap_item("map-pin", SimulationState.department),
        rx.box(width="1px", height="16px", background=Colors.GRAY_300),
        recap_item("building-2", SimulationState.sector, is_primary=True),
    )


def step3_content() -> rx.Component:
    return rx.vstack(
        # Info secteur
        rx.box(
            rx.hstack(
                rx.icon("layers", size=16, color=Colors.PRIMARY),
                rx.text("Typologies disponibles pour ", font_size=Typography.SIZE_SM, color=Colors.GRAY_600),
                rx.text(SimulationState.sector, font_weight=Typography.WEIGHT_SEMIBOLD, color=Colors.PRIMARY),
                spacing="2",
                align="center",
            ),
            padding=Spacing.MD,
            background=Colors.PRIMARY_LIGHTER,
            border_radius=Borders.RADIUS_MD,
            width="100%",
        ),
        
        # Grille des typologies
        rx.cond(
            SimulationState.available_typologies.length() > 0,
            rx.box(
                rx.hstack(
                    rx.foreach(SimulationState.available_typologies, typology_card),
                    spacing="4",
                    wrap="wrap",
                    justify="center",
                    width="100%",
                ),
                width="100%",
            ),
            rx.box(
                rx.vstack(
                    rx.icon("alert-circle", size=32, color=Colors.GRAY_400),
                    rx.text("Aucune typologie disponible", color=Colors.GRAY_500),
                    spacing="2",
                    align="center",
                ),
                padding=Spacing.XL,
                width="100%",
            ),
        ),
        
        # Typologie sélectionnée
        rx.cond(
            SimulationState.typology != "",
            rx.box(
                rx.hstack(
                    rx.icon("check-circle", size=18, color=Colors.SUCCESS),
                    rx.text("Typologie sélectionnée : ", font_size=Typography.SIZE_SM, color=Colors.GRAY_600),
                    rx.text(SimulationState.typology, font_weight=Typography.WEIGHT_SEMIBOLD, color=Colors.SUCCESS),
                    rx.text(f"({SimulationState.typology_abbr})", font_size=Typography.SIZE_SM, color=Colors.GRAY_400),
                    spacing="2",
                    align="center",
                ),
                padding=Spacing.MD,
                background=Colors.SUCCESS_LIGHT,
                border_radius=Borders.RADIUS_LG,
                width="100%",
            ),
            rx.fragment(),
        ),
        
        spacing="5",
        width="100%",
    )


@rx.page(route="/simulation/typology", title="Typologie - SimuPrime")
def typology_page() -> rx.Component:
    return simulation_layout(
        title="Sélection de la Typologie",
        subtitle="Choisissez le type d'opération",
        step=3,
        total_steps=6,
        content=step3_content(),
        recap=step3_recap(),
        back_url="/simulation/sector",
        next_url="/simulation/fiches",
        can_continue=SimulationState.typology != "",
    )