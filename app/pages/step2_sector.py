"""Page Step 2 - Secteur"""
import reflex as rx
from ..state import SimulationState
from ..styles.design_system import Colors, Typography, Spacing, Borders, Shadows
from ..data.variables import SECTORS
from .simulation_layout import simulation_layout, recap_bar, recap_item


def sector_card(sector: dict) -> rx.Component:
    """Carte de sélection d'un secteur."""
    is_selected = SimulationState.sector == sector["value"]
    
    return rx.box(
        rx.vstack(
            rx.box(
                rx.icon(
                    sector["icon"],
                    size=28,
                    color=rx.cond(is_selected, Colors.PRIMARY, Colors.GRAY_400),
                ),
                padding=Spacing.MD,
                background=rx.cond(is_selected, Colors.PRIMARY_LIGHTER, Colors.GRAY_100),
                border_radius=Borders.RADIUS_FULL,
            ),
            rx.text(
                sector["label"],
                font_weight=Typography.WEIGHT_SEMIBOLD,
                font_size=Typography.SIZE_BASE,
                color=Colors.GRAY_900,
                text_align="center",
            ),
            rx.text(
                sector["description"],
                font_size=Typography.SIZE_XS,
                color=Colors.GRAY_500,
                text_align="center",
            ),
            spacing="2",
            align="center",
        ),
        on_click=SimulationState.select_sector(sector["value"]),
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
        width="calc(33.33% - 12px)",
        min_width="200px",
    )


def step2_recap() -> rx.Component:
    """Récap de l'étape 1."""
    return recap_bar(
        recap_item("calendar", SimulationState.date_signature),
        rx.box(width="1px", height="16px", background=Colors.GRAY_300),
        recap_item("map-pin", SimulationState.department),
    )


def step2_content() -> rx.Component:
    return rx.vstack(
        # Grille des secteurs (2 lignes de 3)
        rx.box(
            rx.vstack(
                # Première ligne
                rx.hstack(
                    sector_card(SECTORS[0]),
                    sector_card(SECTORS[1]),
                    sector_card(SECTORS[2]),
                    spacing="4",
                    width="100%",
                    justify="center",
                ),
                # Deuxième ligne
                rx.hstack(
                    sector_card(SECTORS[3]),
                    sector_card(SECTORS[4]),
                    sector_card(SECTORS[5]),
                    spacing="4",
                    width="100%",
                    justify="center",
                ),
                spacing="4",
                width="100%",
            ),
            width="100%",
        ),
        
        # Secteur sélectionné
        rx.cond(
            SimulationState.sector != "",
            rx.box(
                rx.hstack(
                    rx.icon("check-circle", size=18, color=Colors.SUCCESS),
                    rx.text("Secteur sélectionné : ", font_size=Typography.SIZE_SM, color=Colors.GRAY_600),
                    rx.text(SimulationState.sector, font_weight=Typography.WEIGHT_SEMIBOLD, color=Colors.SUCCESS),
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


@rx.page(route="/simulation/sector", title="Secteur - RDE Consulting")
def sector_page() -> rx.Component:
    return simulation_layout(
        title="Sélection du Secteur",
        subtitle="Choisissez votre secteur d'activité",
        step=2,
        total_steps=6,
        content=step2_content(),
        recap=step2_recap(),
        back_url="/simulation/date-department",
        next_url="/simulation/typology",
        can_continue=SimulationState.sector != "",
    )