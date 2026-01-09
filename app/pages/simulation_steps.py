"""
Pages de simulation - Parcours multi-étapes.
Étapes 1-2: Date/Département et Secteur.
"""

import reflex as rx
from ..styles import COLORS, SHADOWS, RADIUS
from ..state.simulation_state import SimulationState
from ..state.user_state import UserState
from ..components.sidebar import sidebar
from ..components.header import header
from ..components.stepper import simulation_stepper, step_navigation


def simulation_layout(content: rx.Component, step: int = 0) -> rx.Component:
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


# ==================== Étape 1: Date et Département ====================

def date_department_content() -> rx.Component:
    """Contenu de l'étape 1."""
    return rx.vstack(
        rx.vstack(
            rx.heading(
                "Informations générales",
                size="6",
                font_weight="700",
                color=COLORS["text_primary"],
            ),
            rx.text(
                "Renseignez la date de signature et le département du projet.",
                color=COLORS["text_muted"],
            ),
            spacing="2",
            align_items="start",
            width="100%",
            margin_bottom="1.5rem",
        ),
        
        rx.box(
            rx.vstack(
                # Date de signature
                rx.vstack(
                    rx.hstack(
                        rx.icon(tag="calendar", size=18, color=COLORS["primary"]),
                        rx.text(
                            "Date de signature du devis",
                            font_weight="600",
                            color=COLORS["text_primary"],
                        ),
                        spacing="2",
                    ),
                    rx.text(
                        "Date à laquelle le devis sera signé par le bénéficiaire.",
                        font_size="0.875rem",
                        color=COLORS["text_muted"],
                    ),
                    rx.input(
                        type="date",
                        value=SimulationState.date_signature,
                        on_change=SimulationState.set_date_signature,
                        width="100%",
                        max_width="300px",
                        size="3",
                    ),
                    spacing="2",
                    align_items="start",
                    width="100%",
                ),
                
                rx.divider(margin_y="1.5rem"),
                
                # Département
                rx.vstack(
                    rx.hstack(
                        rx.icon(tag="map-pin", size=18, color=COLORS["primary"]),
                        rx.text(
                            "Département",
                            font_weight="600",
                            color=COLORS["text_primary"],
                        ),
                        spacing="2",
                    ),
                    rx.text(
                        "Département où seront réalisés les travaux.",
                        font_size="0.875rem",
                        color=COLORS["text_muted"],
                    ),
                    rx.select(
                        SimulationState.all_departments,
                        placeholder="Sélectionner un département",
                        value=SimulationState.department,
                        on_change=SimulationState.select_department,
                        width="100%",
                        size="3",
                    ),
                    spacing="2",
                    align_items="start",
                    width="100%",
                ),
                
                spacing="4",
                width="100%",
                padding="1.5rem",
            ),
            background=COLORS["white"],
            border=f"1px solid {COLORS['border']}",
            border_radius=RADIUS["xl"],
            width="100%",
        ),
        
        # Navigation
        step_navigation(
            show_previous=False,
            next_disabled=~SimulationState.can_proceed_step1,
        ),
        
        spacing="4",
        width="100%",
        align_items="stretch",
    )


def date_department_page() -> rx.Component:
    """Page étape 1: Date et Département."""
    return simulation_layout(date_department_content(), step=0)


# ==================== Étape 2: Secteur ====================

def sector_card(
    label: str,
    icon: str,
    abbr: str,
    is_selected: bool = False,
) -> rx.Component:
    """Carte de sélection de secteur."""
    return rx.box(
        rx.vstack(
            rx.box(
                rx.cond(
                    icon == "factory",
                    rx.icon(tag="factory", size=32, color=COLORS["primary"]),
                    rx.cond(
                        icon == "house",
                        rx.icon(tag="house", size=32, color=COLORS["primary"]),
                        rx.cond(
                            icon == "building-2",
                            rx.icon(tag="building-2", size=32, color=COLORS["primary"]),
                            rx.cond(
                                icon == "network",
                                rx.icon(tag="network", size=32, color=COLORS["primary"]),
                                rx.cond(
                                    icon == "carrot",
                                    rx.icon(tag="carrot", size=32, color=COLORS["primary"]),
                                    rx.icon(tag="bus", size=32, color=COLORS["primary"]),
                                ),
                            ),
                        ),
                    ),
                ),
                background=f"{COLORS['primary']}10",
                padding="1rem",
                border_radius=RADIUS["xl"],
            ),
            rx.text(
                label,
                font_weight="600",
                font_size="1rem",
                color=COLORS["text_primary"],
            ),
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
        border=f"{'2px' if is_selected else '1px'} solid {COLORS['primary'] if is_selected else COLORS['border']}",
        border_radius=RADIUS["xl"],
        box_shadow=SHADOWS["sm"],
        cursor="pointer",
        _hover={
            "box_shadow": SHADOWS["md"],
            "transform": "translateY(-4px)",
            "border_color": COLORS["primary"],
        },
        transition="all 0.2s ease-in-out",
        on_click=lambda: SimulationState.select_sector(label, abbr),
        min_height="180px",
    )


def sector_content() -> rx.Component:
    """Contenu de l'étape 2."""
    return rx.vstack(
        rx.vstack(
            rx.heading(
                "Choisissez un secteur",
                size="6",
                font_weight="700",
                color=COLORS["text_primary"],
            ),
            rx.text(
                "Sélectionnez le secteur d'activité correspondant à votre projet.",
                color=COLORS["text_muted"],
            ),
            spacing="2",
            align_items="start",
            width="100%",
            margin_bottom="1.5rem",
        ),
        
        rx.grid(
            sector_card("Industrie", "factory", "IND", SimulationState.sector == "Industrie"),
            sector_card("Résidentiel", "house", "BAR", SimulationState.sector == "Résidentiel"),
            sector_card("Tertiaire", "building-2", "BAT", SimulationState.sector == "Tertiaire"),
            sector_card("Réseaux", "network", "RES", SimulationState.sector == "Réseaux"),
            sector_card("Agriculture", "carrot", "AGRI", SimulationState.sector == "Agriculture"),
            sector_card("Transport", "bus", "TRA", SimulationState.sector == "Transport"),
            columns=rx.breakpoints({"initial": "2", "md": "3"}),
            spacing="4",
            width="100%",
        ),
        
        # Navigation
        step_navigation(
            show_previous=True,
            show_next=False,  # Navigation automatique au clic
        ),
        
        spacing="4",
        width="100%",
        align_items="stretch",
    )


def sector_page() -> rx.Component:
    """Page étape 2: Secteur."""
    return simulation_layout(sector_content(), step=1)
