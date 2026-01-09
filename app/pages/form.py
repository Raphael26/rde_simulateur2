"""
Page du formulaire dynamique - Étape 6 du parcours de simulation.
Génère les champs du formulaire basés sur la configuration de la fiche sélectionnée.
"""

import reflex as rx
from ..styles import COLORS, SHADOWS, RADIUS
from ..state.simulation_state import SimulationState
from ..state.user_state import UserState
from ..components.sidebar import sidebar
from ..components.header import header
from ..components.stepper import simulation_stepper, step_navigation
from ..components.dynamic_form import simulator_form, form_summary


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


def loading_state() -> rx.Component:
    """État de chargement du formulaire."""
    return rx.center(
        rx.vstack(
            rx.spinner(size="3"),
            rx.text(
                "Chargement du formulaire...",
                color=COLORS["text_muted"],
            ),
            rx.text(
                "Récupération de la configuration depuis le serveur",
                font_size="0.875rem",
                color=COLORS["text_muted"],
            ),
            spacing="3",
            padding="3rem",
        ),
    )


def form_header() -> rx.Component:
    """En-tête du formulaire avec les informations de la fiche."""
    return rx.vstack(
        rx.hstack(
            rx.icon(tag="calculator", size=24, color=COLORS["primary"]),
            rx.heading(
                "Simulateur",
                size="6",
                font_weight="700",
                color=COLORS["text_primary"],
            ),
            spacing="2",
            align_items="center",
        ),
        rx.text(
            "Remplissez les champs ci-dessous pour calculer votre prime CEE.",
            color=COLORS["text_muted"],
        ),
        spacing="2",
        align_items="start",
        width="100%",
        margin_bottom="1.5rem",
    )


def fiche_info_card() -> rx.Component:
    """Carte d'information sur la fiche sélectionnée."""
    return rx.box(
        rx.hstack(
            rx.box(
                rx.icon(tag="file-text", size=24, color=COLORS["primary"]),
                background=f"{COLORS['primary']}10",
                padding="0.75rem",
                border_radius=RADIUS["lg"],
            ),
            rx.vstack(
                rx.hstack(
                    rx.badge(
                        SimulationState.selected_fiche,
                        color_scheme="teal",
                        variant="solid",
                        size="2",
                    ),
                    rx.badge(
                        SimulationState.sector,
                        color_scheme="gray",
                        variant="soft",
                        size="1",
                    ),
                    rx.badge(
                        SimulationState.typology,
                        color_scheme="gray",
                        variant="soft",
                        size="1",
                    ),
                    spacing="2",
                ),
                rx.text(
                    SimulationState.selected_fiche_description,
                    font_size="0.875rem",
                    color=COLORS["text_secondary"],
                    max_width="500px",
                ),
                spacing="2",
                align_items="start",
                flex="1",
            ),
            spacing="3",
            align_items="start",
            width="100%",
        ),
        background=COLORS["white"],
        border=f"1px solid {COLORS['border']}",
        border_radius=RADIUS["xl"],
        padding="1.25rem",
        margin_bottom="1.5rem",
    )


def form_section() -> rx.Component:
    """Section principale du formulaire."""
    return rx.box(
        rx.vstack(
            rx.hstack(
                rx.icon(tag="settings", size=20, color=COLORS["primary"]),
                rx.text(
                    "Paramètres de l'opération",
                    font_weight="600",
                    color=COLORS["text_primary"],
                ),
                spacing="2",
            ),
            rx.divider(),
            simulator_form(),
            spacing="4",
            width="100%",
        ),
        background=COLORS["white"],
        border=f"1px solid {COLORS['border']}",
        border_radius=RADIUS["xl"],
        padding="1.5rem",
    )


def calculate_button() -> rx.Component:
    """Bouton de calcul."""
    return rx.hstack(
        rx.button(
            rx.hstack(
                rx.icon(tag="chevron-left", size=16),
                rx.text("Retour"),
                spacing="1",
            ),
            variant="ghost",
            on_click=SimulationState.previous_step,
        ),
        rx.spacer(),
        rx.button(
            rx.hstack(
                rx.cond(
                    SimulationState.is_loading,
                    rx.spinner(size="1"),
                    rx.icon(tag="calculator", size=20),
                ),
                rx.text("Calculer ma prime"),
                spacing="2",
            ),
            size="3",
            disabled=SimulationState.is_loading,
            on_click=SimulationState.execute_calculation,
            style={
                "background": COLORS["primary"],
                "color": COLORS["white"],
                "padding": "0.75rem 2rem",
                "_hover": {
                    "background": COLORS["primary_dark"],
                    "transform": "translateY(-1px)",
                },
                "_disabled": {
                    "opacity": "0.6",
                    "cursor": "not-allowed",
                },
            },
        ),
        width="100%",
        padding_top="1.5rem",
    )


def error_banner() -> rx.Component:
    """Bannière d'erreur de calcul."""
    return rx.cond(
        SimulationState.calculation_error != "",
        rx.box(
            rx.hstack(
                rx.icon(tag="alert-triangle", size=20, color=COLORS["error"]),
                rx.vstack(
                    rx.text(
                        "Erreur de calcul",
                        font_weight="600",
                        color=COLORS["error"],
                    ),
                    rx.text(
                        SimulationState.calculation_error,
                        font_size="0.875rem",
                        color=COLORS["text_secondary"],
                    ),
                    spacing="1",
                    align_items="start",
                    flex="1",
                ),
                spacing="3",
                align_items="start",
                width="100%",
            ),
            background=f"{COLORS['error']}10",
            border=f"1px solid {COLORS['error']}30",
            border_radius=RADIUS["lg"],
            padding="1rem",
            margin_top="1rem",
        ),
        rx.box(),
    )


def help_section() -> rx.Component:
    """Section d'aide."""
    return rx.box(
        rx.hstack(
            rx.icon(tag="lightbulb", size=18, color=COLORS["warning"]),
            rx.vstack(
                rx.text(
                    "Besoin d'aide ?",
                    font_weight="600",
                    font_size="0.875rem",
                    color=COLORS["text_primary"],
                ),
                rx.text(
                    "Consultez la fiche technique officielle pour plus de détails sur les conditions d'éligibilité "
                    "et les critères techniques requis.",
                    font_size="0.75rem",
                    color=COLORS["text_muted"],
                    line_height="1.4",
                ),
                spacing="1",
                align_items="start",
                flex="1",
            ),
            spacing="3",
            align_items="start",
        ),
        background=f"{COLORS['warning']}10",
        border=f"1px solid {COLORS['warning']}30",
        border_radius=RADIUS["lg"],
        padding="1rem",
        margin_top="1.5rem",
    )


def form_content() -> rx.Component:
    """Contenu de la page du formulaire."""
    return rx.vstack(
        form_header(),
        
        # Résumé des sélections
        form_summary(),
        
        # Info fiche
        fiche_info_card(),
        
        # Formulaire
        rx.cond(
            SimulationState.simulator_choices != {},
            form_section(),
            loading_state(),
        ),
        
        # Erreur
        error_banner(),
        
        # Aide
        help_section(),
        
        # Bouton de calcul
        calculate_button(),
        
        spacing="4",
        width="100%",
        align_items="stretch",
    )


def form_page() -> rx.Component:
    """Page étape 6: Formulaire dynamique."""
    return simulation_layout(form_content())
