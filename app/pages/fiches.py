"""
Page de sélection de fiche CEE - Étape 4 du parcours de simulation.
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
                            max_width="1000px",
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


def fiche_card(code: str, description: str) -> rx.Component:
    """
    Carte de sélection de fiche CEE.
    
    Args:
        code: Code de la fiche (ex: BAR-TH-101)
        description: Description de la fiche
    """
    is_selected = SimulationState.selected_fiche == code
    
    return rx.box(
        rx.hstack(
            # Indicateur de sélection
            rx.box(
                rx.cond(
                    is_selected,
                    rx.icon(tag="check-circle", size=20, color=COLORS["white"]),
                    rx.box(),
                ),
                background=rx.cond(
                    is_selected,
                    COLORS["primary"],
                    "transparent",
                ),
                border=rx.cond(
                    is_selected,
                    f"2px solid {COLORS['primary']}",
                    f"2px solid {COLORS['border']}",
                ),
                border_radius=RADIUS["full"],
                width="24px",
                height="24px",
                min_width="24px",
                display="flex",
                align_items="center",
                justify_content="center",
            ),
            # Contenu
            rx.vstack(
                rx.hstack(
                    rx.badge(
                        code,
                        color_scheme="teal",
                        variant="solid",
                        size="1",
                    ),
                    rx.cond(
                        is_selected,
                        rx.badge(
                            "Sélectionné",
                            color_scheme="green",
                            variant="soft",
                            size="1",
                        ),
                        rx.box(),
                    ),
                    spacing="2",
                ),
                rx.text(
                    description,
                    font_size="0.875rem",
                    color=COLORS["text_secondary"],
                    line_height="1.4",
                ),
                spacing="2",
                align_items="start",
                flex="1",
            ),
            # Icône de chargement ou flèche
            rx.cond(
                SimulationState.is_loading,
                rx.spinner(size="2"),
                rx.icon(tag="chevron-right", size=20, color=COLORS["text_muted"]),
            ),
            spacing="3",
            align_items="center",
            width="100%",
        ),
        background=COLORS["white"],
        border=rx.cond(
            is_selected,
            f"2px solid {COLORS['primary']}",
            f"1px solid {COLORS['border']}",
        ),
        border_radius=RADIUS["lg"],
        padding="1rem",
        cursor="pointer",
        _hover={
            "background": COLORS["background"],
            "border_color": COLORS["primary"],
        },
        transition="all 0.2s ease-in-out",
        on_click=lambda: SimulationState.select_fiche(code, description),
    )


def search_input() -> rx.Component:
    """Champ de recherche des fiches."""
    return rx.box(
        rx.hstack(
            rx.icon(tag="search", size=18, color=COLORS["text_muted"]),
            rx.input(
                placeholder="Rechercher une fiche par code ou description...",
                value=SimulationState.fiche_search,
                on_change=SimulationState.set_fiche_search,
                variant="soft",
                style={
                    "border": "none",
                    "background": "transparent",
                    "flex": "1",
                    "_focus": {"outline": "none"},
                },
            ),
            rx.cond(
                SimulationState.fiche_search != "",
                rx.icon_button(
                    rx.icon(tag="x", size=16),
                    variant="ghost",
                    size="1",
                    on_click=lambda: SimulationState.set_fiche_search(""),
                ),
                rx.box(),
            ),
            spacing="2",
            align_items="center",
            width="100%",
        ),
        background=COLORS["white"],
        border=f"1px solid {COLORS['border']}",
        border_radius=RADIUS["lg"],
        padding="0.5rem 1rem",
        width="100%",
        _focus_within={
            "border_color": COLORS["primary"],
            "box_shadow": f"0 0 0 3px {COLORS['primary']}20",
        },
    )


def fiches_content() -> rx.Component:
    """Contenu de la page de sélection de fiche."""
    return rx.vstack(
        # En-tête
        rx.vstack(
            rx.hstack(
                rx.icon(tag="file-text", size=24, color=COLORS["primary"]),
                rx.heading(
                    "Sélectionnez une fiche CEE",
                    size="6",
                    font_weight="700",
                    color=COLORS["text_primary"],
                ),
                spacing="2",
                align_items="center",
            ),
            rx.text(
                "Choisissez la fiche d'opération standardisée correspondant à votre projet.",
                color=COLORS["text_muted"],
            ),
            spacing="2",
            align_items="start",
            width="100%",
            margin_bottom="1rem",
        ),
        
        # Récapitulatif des sélections
        rx.hstack(
            rx.badge(
                rx.hstack(
                    rx.icon(tag="folder", size=14),
                    rx.text(f"Secteur: {SimulationState.sector}"),
                    spacing="1",
                ),
                color_scheme="gray",
                variant="soft",
            ),
            rx.badge(
                rx.hstack(
                    rx.icon(tag="layers-3", size=14),
                    rx.text(f"Typologie: {SimulationState.typology}"),
                    spacing="1",
                ),
                color_scheme="gray",
                variant="soft",
            ),
            rx.badge(
                rx.hstack(
                    rx.icon(tag="tag", size=14),
                    rx.text(f"Préfixe: {SimulationState.sector_abbr}-{SimulationState.typology_abbr}"),
                    spacing="1",
                ),
                color_scheme="teal",
                variant="soft",
            ),
            spacing="2",
            wrap="wrap",
            margin_bottom="1rem",
        ),
        
        # Recherche
        search_input(),
        
        # Compteur de résultats
        rx.text(
            rx.cond(
                SimulationState.filtered_fiches != {},
                f"{len(SimulationState.filtered_fiches)} fiche(s) trouvée(s)",
                "0 fiche trouvée",
            ),
            font_size="0.875rem",
            color=COLORS["text_muted"],
            margin_top="0.5rem",
        ),
        
        # Liste des fiches
        rx.box(
            rx.cond(
                SimulationState.filtered_fiches != {},
                rx.vstack(
                    rx.foreach(
                        SimulationState.filtered_fiches.items(),
                        lambda item: fiche_card(code=item[0], description=item[1]),
                    ),
                    spacing="2",
                    width="100%",
                ),
                rx.center(
                    rx.vstack(
                        rx.icon(tag="file-x", size=48, color=COLORS["text_muted"]),
                        rx.text(
                            "Aucune fiche disponible",
                            font_weight="600",
                            color=COLORS["text_secondary"],
                        ),
                        rx.text(
                            "Les fiches pour cette combinaison secteur/typologie ne sont pas encore disponibles.",
                            color=COLORS["text_muted"],
                            text_align="center",
                            max_width="400px",
                        ),
                        rx.button(
                            rx.hstack(
                                rx.icon(tag="chevron-left", size=16),
                                rx.text("Changer de typologie"),
                                spacing="1",
                            ),
                            variant="soft",
                            on_click=SimulationState.previous_step,
                        ),
                        spacing="3",
                        padding="3rem",
                        align_items="center",
                    ),
                ),
            ),
            width="100%",
            margin_top="1rem",
            max_height="400px",
            overflow_y="auto",
        ),
        
        # Navigation
        step_navigation(
            show_previous=True,
            show_next=False,  # Navigation automatique au clic sur une fiche
        ),
        
        spacing="4",
        width="100%",
        align_items="stretch",
    )


def fiches_page() -> rx.Component:
    """Page étape 4: Sélection de fiche."""
    return simulation_layout(fiches_content())
