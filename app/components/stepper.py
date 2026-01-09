"""
Composant Stepper - Indicateur de progression pour le parcours de simulation.
"""

import reflex as rx
from ..styles import COLORS, RADIUS
from ..state.simulation_state import SimulationState


def step_indicator(
    step_number: int,
    title: str,
    description: str = "",
    is_active: bool = False,
    is_completed: bool = False,
    is_last: bool = False,
) -> rx.Component:
    """
    Indicateur d'étape individuel.
    
    Args:
        step_number: Numéro de l'étape
        title: Titre de l'étape
        description: Description/valeur sélectionnée
        is_active: Si l'étape est active
        is_completed: Si l'étape est terminée
        is_last: Si c'est la dernière étape
    """
    # Couleur du cercle
    circle_bg = COLORS["primary"] if is_completed or is_active else COLORS["white"]
    circle_border = COLORS["primary"] if is_completed or is_active else COLORS["border"]
    circle_text = COLORS["white"] if is_completed or is_active else COLORS["text_muted"]
    
    # Couleur de la ligne
    line_color = COLORS["primary"] if is_completed else COLORS["border"]
    
    return rx.hstack(
        rx.vstack(
            # Cercle avec numéro ou check
            rx.box(
                rx.cond(
                    is_completed,
                    rx.icon(tag="check", size=16, color=circle_text),
                    rx.text(
                        str(step_number),
                        font_size="0.875rem",
                        font_weight="600",
                        color=circle_text,
                    ),
                ),
                background=circle_bg,
                border=f"2px solid {circle_border}",
                border_radius=RADIUS["full"],
                width="32px",
                height="32px",
                display="flex",
                align_items="center",
                justify_content="center",
                z_index="1",
            ),
            # Titre et description
            rx.vstack(
                rx.text(
                    title,
                    font_size="0.875rem",
                    font_weight="600" if is_active else "500",
                    color=COLORS["text_primary"] if is_active else COLORS["text_secondary"],
                    white_space="nowrap",
                ),
                rx.cond(
                    description != "",
                    rx.text(
                        description,
                        font_size="0.75rem",
                        color=COLORS["text_muted"],
                        max_width="80px",
                        overflow="hidden",
                        text_overflow="ellipsis",
                        white_space="nowrap",
                    ),
                    rx.box(),
                ),
                spacing="0",
                align_items="center",
            ),
            spacing="2",
            align_items="center",
        ),
        # Ligne de connexion
        rx.cond(
            ~is_last,
            rx.box(
                background=line_color,
                height="2px",
                flex="1",
                min_width="40px",
                margin_top="-16px",
            ),
            rx.box(),
        ),
        spacing="0",
        align_items="flex-start",
    )


def simulation_stepper() -> rx.Component:
    """
    Stepper complet pour le parcours de simulation.
    Affiche les 5 étapes avec leur état.
    """
    return rx.hstack(
        # Étape 1: Date et Département
        step_indicator(
            step_number=1,
            title="Données",
            description=SimulationState.truncated_department,
            is_active=SimulationState.current_step == 0,
            is_completed=SimulationState.current_step > 0,
        ),
        
        # Étape 2: Secteur
        step_indicator(
            step_number=2,
            title="Secteur",
            description=SimulationState.sector,
            is_active=SimulationState.current_step == 1,
            is_completed=SimulationState.current_step > 1,
        ),
        
        # Étape 3: Typologie
        step_indicator(
            step_number=3,
            title="Typologie",
            description=SimulationState.typology,
            is_active=SimulationState.current_step == 2,
            is_completed=SimulationState.current_step > 2,
        ),
        
        # Étape 4: Fiche
        step_indicator(
            step_number=4,
            title="Opérations",
            description=SimulationState.truncated_fiche,
            is_active=SimulationState.current_step == 3,
            is_completed=SimulationState.current_step > 3,
        ),
        
        # Étape 5: Simulateur
        step_indicator(
            step_number=5,
            title="Simulateur",
            description="",
            is_active=SimulationState.current_step >= 4,
            is_completed=SimulationState.result_cumacs > 0,
            is_last=True,
        ),
        
        width="100%",
        justify="center",
        spacing="0",
        padding_y="1rem",
        overflow_x="auto",
    )


def progress_bar() -> rx.Component:
    """
    Barre de progression simple.
    """
    return rx.box(
        rx.box(
            background=COLORS["primary"],
            height="100%",
            width=f"{SimulationState.progress_percent}%",
            border_radius=RADIUS["full"],
            transition="width 0.3s ease-in-out",
        ),
        background=COLORS["border"],
        height="6px",
        width="100%",
        border_radius=RADIUS["full"],
        overflow="hidden",
    )


def step_navigation(
    show_previous: bool = True,
    show_next: bool = True,
    next_label: str = "Continuer",
    next_disabled: bool = False,
    on_next: callable = None,
    on_previous: callable = None,
) -> rx.Component:
    """
    Boutons de navigation entre les étapes.
    
    Args:
        show_previous: Afficher le bouton précédent
        show_next: Afficher le bouton suivant
        next_label: Label du bouton suivant
        next_disabled: Si le bouton suivant est désactivé
        on_next: Handler pour le bouton suivant
        on_previous: Handler pour le bouton précédent
    """
    return rx.hstack(
        rx.cond(
            show_previous,
            rx.button(
                rx.hstack(
                    rx.icon(tag="chevron-left", size=20),
                    rx.text("Retour"),
                    spacing="1",
                ),
                variant="ghost",
                on_click=on_previous or SimulationState.previous_step,
            ),
            rx.box(),
        ),
        rx.spacer(),
        rx.cond(
            show_next,
            rx.button(
                rx.hstack(
                    rx.text(next_label),
                    rx.icon(tag="chevron-right", size=20),
                    spacing="1",
                ),
                disabled=next_disabled,
                on_click=on_next or SimulationState.next_step,
                style={
                    "background": COLORS["primary"],
                    "color": COLORS["white"],
                    "padding": "0.75rem 1.5rem",
                    "_hover": {
                        "background": COLORS["primary_dark"],
                        "transform": "translateY(-1px)",
                    },
                    "_disabled": {
                        "opacity": "0.5",
                        "cursor": "not-allowed",
                    },
                },
            ),
            rx.box(),
        ),
        width="100%",
        padding_y="1rem",
    )
