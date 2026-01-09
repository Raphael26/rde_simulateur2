"""
Page de sélection du type de bénéficiaire - Étape 5 du parcours de simulation.
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
                            max_width="800px",
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


def beneficiary_card(
    value: str,
    title: str,
    description: str,
    icon: str,
    details: list,
) -> rx.Component:
    """
    Carte de sélection du type de bénéficiaire.
    
    Args:
        value: Valeur interne (particulier/personne_morale)
        title: Titre affiché
        description: Description courte
        icon: Nom de l'icône
        details: Liste de points détaillés
    """
    is_selected = SimulationState.beneficiary_type == value
    
    return rx.box(
        rx.vstack(
            # Header avec icône
            rx.hstack(
                rx.box(
                    rx.icon(tag=icon, size=28, color=COLORS["primary"]),
                    background=f"{COLORS['primary']}10",
                    padding="1rem",
                    border_radius=RADIUS["xl"],
                ),
                rx.cond(
                    is_selected,
                    rx.box(
                        rx.icon(tag="check", size=16, color=COLORS["white"]),
                        background=COLORS["primary"],
                        border_radius=RADIUS["full"],
                        padding="0.25rem",
                    ),
                    rx.box(
                        border=f"2px solid {COLORS['border']}",
                        border_radius=RADIUS["full"],
                        width="24px",
                        height="24px",
                    ),
                ),
                justify="between",
                width="100%",
            ),
            
            # Titre et description
            rx.vstack(
                rx.text(
                    title,
                    font_size="1.25rem",
                    font_weight="700",
                    color=COLORS["text_primary"],
                ),
                rx.text(
                    description,
                    font_size="0.875rem",
                    color=COLORS["text_muted"],
                ),
                spacing="1",
                align_items="start",
                width="100%",
            ),
            
            rx.divider(),
            
            # Détails
            rx.vstack(
                rx.foreach(
                    details,
                    lambda detail: rx.hstack(
                        rx.icon(tag="check-circle", size=16, color=COLORS["success"]),
                        rx.text(
                            detail,
                            font_size="0.875rem",
                            color=COLORS["text_secondary"],
                        ),
                        spacing="2",
                        align_items="start",
                    ),
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
        border=rx.cond(
            is_selected,
            f"2px solid {COLORS['primary']}",
            f"1px solid {COLORS['border']}",
        ),
        border_radius=RADIUS["xl"],
        box_shadow=rx.cond(
            is_selected,
            SHADOWS["lg"],
            SHADOWS["sm"],
        ),
        cursor="pointer",
        _hover={
            "box_shadow": SHADOWS["lg"],
            "transform": "translateY(-4px)",
            "border_color": COLORS["primary"],
        },
        transition="all 0.2s ease-in-out",
        on_click=lambda: SimulationState.select_beneficiary(value),
        flex="1",
        min_width="300px",
    )


def mpr_info_banner() -> rx.Component:
    """Bannière d'information sur MaPrimeRénov'."""
    return rx.cond(
        SimulationState.is_residential_sector,
        rx.box(
            rx.hstack(
                rx.box(
                    rx.icon(tag="info", size=20, color=COLORS["info"]),
                    background=f"{COLORS['info']}20",
                    padding="0.5rem",
                    border_radius=RADIUS["lg"],
                ),
                rx.vstack(
                    rx.text(
                        "Information MaPrimeRénov'",
                        font_weight="600",
                        color=COLORS["text_primary"],
                    ),
                    rx.text(
                        "Pour les projets résidentiels, le type de bénéficiaire peut influencer l'éligibilité "
                        "aux aides MaPrimeRénov' et le montant des primes CEE.",
                        font_size="0.875rem",
                        color=COLORS["text_secondary"],
                        line_height="1.5",
                    ),
                    spacing="1",
                    align_items="start",
                    flex="1",
                ),
                spacing="3",
                align_items="start",
                width="100%",
            ),
            background=f"{COLORS['info']}10",
            border=f"1px solid {COLORS['info']}30",
            border_radius=RADIUS["xl"],
            padding="1rem",
            margin_bottom="1.5rem",
        ),
        rx.box(),
    )


def selection_summary() -> rx.Component:
    """Résumé des sélections précédentes."""
    return rx.box(
        rx.hstack(
            rx.vstack(
                rx.text("Fiche sélectionnée", font_size="0.75rem", color=COLORS["text_muted"]),
                rx.text(
                    SimulationState.selected_fiche,
                    font_weight="600",
                    color=COLORS["primary"],
                ),
                spacing="0",
                align_items="start",
            ),
            rx.divider(orientation="vertical", height="40px"),
            rx.vstack(
                rx.text("Secteur", font_size="0.75rem", color=COLORS["text_muted"]),
                rx.text(SimulationState.sector, font_weight="500"),
                spacing="0",
                align_items="start",
            ),
            rx.divider(orientation="vertical", height="40px"),
            rx.vstack(
                rx.text("Typologie", font_size="0.75rem", color=COLORS["text_muted"]),
                rx.text(SimulationState.typology, font_weight="500"),
                spacing="0",
                align_items="start",
            ),
            spacing="6",
            align_items="center",
            wrap="wrap",
        ),
        background=COLORS["white"],
        border=f"1px solid {COLORS['border']}",
        border_radius=RADIUS["lg"],
        padding="1rem",
        margin_bottom="1.5rem",
    )


def beneficiary_content() -> rx.Component:
    """Contenu de la page de sélection du bénéficiaire."""
    return rx.vstack(
        # En-tête
        rx.vstack(
            rx.hstack(
                rx.icon(tag="users", size=24, color=COLORS["primary"]),
                rx.heading(
                    "Type de bénéficiaire",
                    size="6",
                    font_weight="700",
                    color=COLORS["text_primary"],
                ),
                spacing="2",
                align_items="center",
            ),
            rx.text(
                "Sélectionnez le type de bénéficiaire pour cette opération.",
                color=COLORS["text_muted"],
            ),
            spacing="2",
            align_items="start",
            width="100%",
            margin_bottom="1rem",
        ),
        
        # Résumé
        selection_summary(),
        
        # Bannière MPR
        mpr_info_banner(),
        
        # Cartes de sélection
        rx.hstack(
            beneficiary_card(
                value="particulier",
                title="Particulier",
                description="Personne physique, propriétaire ou locataire",
                icon="user",
                details=[
                    "Propriétaire occupant ou bailleur",
                    "Locataire avec accord du propriétaire",
                    "Résidence principale ou secondaire",
                    "Éligible aux aides MaPrimeRénov'",
                ],
            ),
            beneficiary_card(
                value="personne_morale",
                title="Personne morale",
                description="Entreprise, collectivité ou association",
                icon="building-2",
                details=[
                    "Entreprises et sociétés",
                    "Collectivités territoriales",
                    "Bailleurs sociaux",
                    "Associations et copropriétés",
                ],
            ),
            spacing="4",
            width="100%",
            wrap="wrap",
            justify="center",
        ),
        
        # Message de sélection
        rx.cond(
            SimulationState.beneficiary_type == "",
            rx.center(
                rx.text(
                    "Cliquez sur une carte pour sélectionner le type de bénéficiaire",
                    font_size="0.875rem",
                    color=COLORS["text_muted"],
                    font_style="italic",
                ),
                margin_top="1rem",
            ),
            rx.box(),
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


def beneficiary_page() -> rx.Component:
    """Page étape 5: Sélection du bénéficiaire."""
    return simulation_layout(beneficiary_content())
