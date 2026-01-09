"""
Page de sélection de typologie - Étape 3 du parcours de simulation.
"""

import reflex as rx
from ..styles import COLORS, SHADOWS, RADIUS
from ..state.simulation_state import SimulationState
from ..state.user_state import UserState
from ..components.sidebar import sidebar
from ..components.header import header
from ..components.stepper import simulation_stepper, step_navigation


def simulation_layout(content: rx.Component) -> rx.Component:
    """Layout commun pour les pages de simulation."""
    return rx.hstack(
        sidebar(current_page="simulation"),
        rx.box(
            header(title="Nouvelle simulation"),
            rx.scroll_area(
                rx.vstack(
                    # Stepper
                    rx.box(
                        simulation_stepper(),
                        background=COLORS["white"],
                        border_bottom=f"1px solid {COLORS['border']}",
                        padding="0.5rem 1.5rem",
                        width="100%",
                    ),
                    # Contenu
                    rx.center(
                        rx.box(
                            content,
                            width="100%",
                            max_width="900px",
                            padding="2rem",
                        ),
                    ),
                    width="100%",
                    spacing="0",
                ),
                type="hover",
                scrollbars="vertical",
                style={"height": "calc(100vh - 60px)"},
            ),
            flex="1",
            background=COLORS["background"],
            min_height="100vh",
        ),
        spacing="0",
        width="100%",
    )


def typology_card(
    name: str,
    abbr: str,
    icon: str,
) -> rx.Component:
    """
    Carte de sélection de typologie.
    
    Args:
        name: Nom de la typologie
        abbr: Abréviation
        icon: Nom de l'icône lucide
    """
    # Mapping des icônes
    icon_map = {
        "plug": "plug",
        "building": "building",
        "layers": "layers-3",
        "flame": "flame",
        "cpu": "cpu",
        "briefcase": "briefcase",
        "lightbulb": "lightbulb",
        "thermometer": "thermometer",
        "circle-help": "circle-help",
    }
    
    icon_name = icon_map.get(icon, "circle-help")
    
    return rx.box(
        rx.vstack(
            # Icône
            rx.box(
                rx.icon(tag=icon_name, size=32, color=COLORS["primary"]),
                background=f"{COLORS['primary']}10",
                padding="1rem",
                border_radius=RADIUS["xl"],
            ),
            # Nom
            rx.text(
                name,
                font_weight="600",
                font_size="1rem",
                color=COLORS["text_primary"],
                text_align="center",
            ),
            # Badge abréviation
            rx.badge(
                abbr,
                color_scheme="teal",
                variant="soft",
                size="1",
            ),
            spacing="2",
            align_items="center",
            padding="1.5rem",
        ),
        background=COLORS["white"],
        border=rx.cond(
            SimulationState.typology == name,
            f"2px solid {COLORS['primary']}",
            f"1px solid {COLORS['border']}",
        ),
        border_radius=RADIUS["xl"],
        box_shadow=SHADOWS["sm"],
        cursor="pointer",
        _hover={
            "box_shadow": SHADOWS["md"],
            "transform": "translateY(-4px)",
            "border_color": COLORS["primary"],
        },
        transition="all 0.2s ease-in-out",
        on_click=lambda: SimulationState.select_typology(name, abbr),
        min_height="160px",
    )


def typology_content() -> rx.Component:
    """Contenu de la page de sélection de typologie."""
    return rx.vstack(
        # En-tête
        rx.vstack(
            rx.hstack(
                rx.icon(tag="layers-3", size=24, color=COLORS["primary"]),
                rx.heading(
                    "Choisissez une typologie",
                    size="6",
                    font_weight="700",
                    color=COLORS["text_primary"],
                ),
                spacing="2",
                align_items="center",
            ),
            rx.text(
                "Sélectionnez le type d'opération correspondant à votre projet.",
                color=COLORS["text_muted"],
            ),
            spacing="2",
            align_items="start",
            width="100%",
            margin_bottom="1.5rem",
        ),
        
        # Info secteur sélectionné
        rx.box(
            rx.hstack(
                rx.icon(tag="info", size=18, color=COLORS["info"]),
                rx.text(
                    rx.text.span("Secteur sélectionné : ", font_weight="600"),
                    rx.text.span(SimulationState.sector, color=COLORS["primary"]),
                    font_size="0.875rem",
                    color=COLORS["text_secondary"],
                ),
                spacing="2",
                align_items="center",
            ),
            background=f"{COLORS['info']}10",
            padding="0.75rem 1rem",
            border_radius=RADIUS["lg"],
            margin_bottom="1.5rem",
        ),
        
        # Grille des typologies
        rx.cond(
            SimulationState.available_typologies.length() > 0,
            rx.grid(
                rx.foreach(
                    SimulationState.available_typologies,
                    lambda typo: typology_card(
                        name=typo["name"],
                        abbr=typo["abbr"],
                        icon=typo.get("icon", "circle-help"),
                    ),
                ),
                columns=rx.breakpoints({"initial": "2", "md": "3", "lg": "4"}),
                spacing="4",
                width="100%",
            ),
            rx.center(
                rx.vstack(
                    rx.icon(tag="alert-circle", size=48, color=COLORS["text_muted"]),
                    rx.text(
                        "Aucune typologie disponible pour ce secteur.",
                        color=COLORS["text_muted"],
                        text_align="center",
                    ),
                    spacing="3",
                    padding="2rem",
                ),
            ),
        ),
        
        # Navigation
        step_navigation(
            show_previous=True,
            show_next=False,  # Navigation automatique au clic sur une carte
        ),
        
        spacing="4",
        width="100%",
        align_items="stretch",
    )


def typology_page() -> rx.Component:
    """Page étape 3: Typologie."""
    return simulation_layout(typology_content())
