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


@rx.page(route="/simulation/typology", title="Typologie - RDE Consulting")
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