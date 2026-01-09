"""
Composant Dynamic Form - Formulaire généré dynamiquement pour le simulateur.
"""

import reflex as rx
from typing import Dict, Any, List
from ..styles import COLORS, SHADOWS, RADIUS
from ..state.simulation_state import SimulationState


def form_field(
    label: str,
    field_type: str,
    options: List[Any] = None,
    value: str = "",
    param_key: str = "",
    required: bool = False,
) -> rx.Component:
    """
    Champ de formulaire générique.
    
    Args:
        label: Label du champ
        field_type: Type de champ (text, number, select, radio, checkbox)
        options: Options pour select/radio
        value: Valeur actuelle
        param_key: Clé du paramètre
        required: Si le champ est requis
    """
    field_label = rx.hstack(
        rx.text(
            label,
            font_weight="500",
            font_size="0.875rem",
            color=COLORS["text_primary"],
        ),
        rx.cond(
            required,
            rx.text("*", color=COLORS["error"]),
            rx.box(),
        ),
        spacing="1",
    )
    
    if field_type == "select" and options:
        field_input = rx.select(
            options,
            placeholder=f"Sélectionner {label}",
            value=value,
            on_change=lambda v: SimulationState.set_param(label, param_key, v),
            width="100%",
        )
    elif field_type == "radio" and options:
        field_input = rx.radio_group(
            rx.hstack(
                rx.foreach(
                    options,
                    lambda opt: rx.radio(opt, value=opt),
                ),
                spacing="4",
            ),
            value=value,
            on_change=lambda v: SimulationState.set_param(label, param_key, v),
        )
    elif field_type == "checkbox":
        field_input = rx.checkbox(
            label,
            checked=value == "Oui" or value == True,
            on_change=lambda v: SimulationState.set_param(label, param_key, "Oui" if v else "Non"),
        )
    elif field_type == "number":
        field_input = rx.input(
            type="number",
            placeholder="0",
            value=str(value) if value else "",
            on_change=lambda v: SimulationState.set_param(label, param_key, v),
            width="100%",
        )
    else:
        field_input = rx.input(
            placeholder=f"Entrez {label}",
            value=str(value) if value else "",
            on_change=lambda v: SimulationState.set_param(label, param_key, v),
            width="100%",
        )
    
    return rx.vstack(
        field_label,
        field_input,
        spacing="2",
        width="100%",
        align_items="stretch",
    )


def dynamic_form_field(
    param_name: str,
    param_config: Dict[str, Any],
) -> rx.Component:
    """
    Génère un champ de formulaire basé sur la configuration.
    
    Args:
        param_name: Nom du paramètre (label)
        param_config: Configuration du paramètre (options, type, etc.)
    """
    # Déterminer le type de champ
    is_select = isinstance(param_config, list) and len(param_config) > 1
    is_boolean = isinstance(param_config, list) and set(param_config) == {"Oui", "Non"}
    
    return rx.box(
        rx.vstack(
            rx.text(
                param_name,
                font_weight="500",
                font_size="0.875rem",
                color=COLORS["text_primary"],
            ),
            rx.cond(
                is_boolean,
                # Radio Oui/Non
                rx.radio_group(
                    rx.hstack(
                        rx.radio("Oui", value="Oui"),
                        rx.radio("Non", value="Non"),
                        spacing="4",
                    ),
                    on_change=lambda v: SimulationState.set_param(param_name, param_name, v),
                ),
                rx.cond(
                    is_select,
                    # Select dropdown
                    rx.select(
                        param_config,
                        placeholder=f"Sélectionner...",
                        on_change=lambda v: SimulationState.set_param(param_name, param_name, v),
                        width="100%",
                    ),
                    # Input text/number
                    rx.input(
                        placeholder="Entrez une valeur",
                        on_change=lambda v: SimulationState.set_param(param_name, param_name, v),
                        width="100%",
                    ),
                ),
            ),
            spacing="2",
            width="100%",
            align_items="stretch",
        ),
        padding="1rem",
        background=COLORS["white"],
        border=f"1px solid {COLORS['border']}",
        border_radius=RADIUS["lg"],
        width="100%",
    )


def simulator_form() -> rx.Component:
    """
    Formulaire dynamique complet du simulateur.
    Génère les champs basés sur simulator_choices.
    """
    return rx.vstack(
        # Nom de la simulation
        rx.box(
            rx.vstack(
                rx.text(
                    "Nom de la simulation",
                    font_weight="600",
                    font_size="0.875rem",
                    color=COLORS["text_primary"],
                ),
                rx.input(
                    placeholder="Ma simulation",
                    value=SimulationState.simulation_name,
                    on_change=SimulationState.set_simulation_name,
                    width="100%",
                ),
                spacing="2",
            ),
            padding="1rem",
            background=COLORS["background"],
            border_radius=RADIUS["lg"],
            width="100%",
            margin_bottom="1rem",
        ),
        
        # Champs dynamiques
        rx.cond(
            SimulationState.simulator_choices != {},
            rx.vstack(
                rx.foreach(
                    SimulationState.simulator_choices.items(),
                    lambda item: dynamic_form_field(item[0], item[1]),
                ),
                spacing="3",
                width="100%",
            ),
            rx.center(
                rx.vstack(
                    rx.spinner(size="3"),
                    rx.text(
                        "Chargement du formulaire...",
                        color=COLORS["text_muted"],
                    ),
                    spacing="3",
                    padding="2rem",
                ),
            ),
        ),
        
        # Message d'erreur
        rx.cond(
            SimulationState.calculation_error != "",
            rx.callout(
                SimulationState.calculation_error,
                icon="alert-triangle",
                color_scheme="red",
                width="100%",
            ),
            rx.box(),
        ),
        
        spacing="3",
        width="100%",
        align_items="stretch",
    )


def form_summary() -> rx.Component:
    """
    Résumé des sélections avant le formulaire.
    """
    return rx.box(
        rx.vstack(
            rx.text(
                "Récapitulatif de votre sélection",
                font_weight="600",
                font_size="1rem",
                color=COLORS["text_primary"],
            ),
            rx.divider(),
            rx.grid(
                rx.vstack(
                    rx.text("Date de signature", font_size="0.75rem", color=COLORS["text_muted"]),
                    rx.text(SimulationState.date_signature, font_weight="500"),
                    spacing="0",
                    align_items="start",
                ),
                rx.vstack(
                    rx.text("Département", font_size="0.75rem", color=COLORS["text_muted"]),
                    rx.text(SimulationState.department, font_weight="500"),
                    spacing="0",
                    align_items="start",
                ),
                rx.vstack(
                    rx.text("Secteur", font_size="0.75rem", color=COLORS["text_muted"]),
                    rx.text(SimulationState.sector, font_weight="500"),
                    spacing="0",
                    align_items="start",
                ),
                rx.vstack(
                    rx.text("Typologie", font_size="0.75rem", color=COLORS["text_muted"]),
                    rx.text(SimulationState.typology, font_weight="500"),
                    spacing="0",
                    align_items="start",
                ),
                rx.vstack(
                    rx.text("Fiche", font_size="0.75rem", color=COLORS["text_muted"]),
                    rx.text(SimulationState.selected_fiche, font_weight="500"),
                    spacing="0",
                    align_items="start",
                ),
                rx.vstack(
                    rx.text("Bénéficiaire", font_size="0.75rem", color=COLORS["text_muted"]),
                    rx.text(
                        rx.cond(
                            SimulationState.beneficiary_type == "particulier",
                            "Particulier",
                            "Personne morale"
                        ),
                        font_weight="500",
                    ),
                    spacing="0",
                    align_items="start",
                ),
                columns="3",
                spacing="4",
                width="100%",
            ),
            spacing="3",
            width="100%",
        ),
        padding="1.25rem",
        background=COLORS["background"],
        border_radius=RADIUS["xl"],
        width="100%",
    )
