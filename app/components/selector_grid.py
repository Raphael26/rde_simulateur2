"""
Composant Selector Grid - Grille de sélection pour secteurs et typologies.
"""

import reflex as rx
from ..styles import COLORS, SHADOWS, RADIUS


def selector_card(
    label: str,
    icon: str,
    is_selected: bool = False,
    on_click: callable = None,
    description: str = "",
) -> rx.Component:
    """
    Carte de sélection individuelle.
    
    Args:
        label: Texte à afficher
        icon: Nom de l'icône Lucide
        is_selected: Si la carte est sélectionnée
        on_click: Handler de clic
        description: Description optionnelle
    """
    return rx.box(
        rx.vstack(
            rx.box(
                rx.icon(
                    tag=icon,
                    size=32,
                    color=COLORS["primary"],
                ),
                background=f"{COLORS['primary']}10",
                padding="1rem",
                border_radius=RADIUS["xl"],
                margin_bottom="0.5rem",
            ),
            rx.text(
                label,
                font_size="1rem",
                font_weight="600" if is_selected else "500",
                color=COLORS["text_primary"],
                text_align="center",
            ),
            rx.cond(
                description != "",
                rx.text(
                    description,
                    font_size="0.75rem",
                    color=COLORS["text_muted"],
                    text_align="center",
                ),
                rx.box(),
            ),
            rx.cond(
                is_selected,
                rx.icon(
                    tag="check-circle-2",
                    size=20,
                    color=COLORS["primary"],
                    position="absolute",
                    top="0.5rem",
                    right="0.5rem",
                ),
                rx.box(),
            ),
            spacing="1",
            align_items="center",
            padding="1.5rem",
        ),
        background=COLORS["white"],
        border=f"{'2px' if is_selected else '1px'} solid {COLORS['primary'] if is_selected else COLORS['border']}",
        border_radius=RADIUS["xl"],
        box_shadow=SHADOWS["card"] if is_selected else SHADOWS["sm"],
        cursor="pointer",
        position="relative",
        _hover={
            "box_shadow": SHADOWS["card_hover"],
            "transform": "translateY(-4px)",
            "border_color": COLORS["primary"],
        },
        transition="all 0.2s ease-in-out",
        on_click=on_click,
        min_width="150px",
        min_height="160px",
    )


def selector_grid(
    items: list,
    selected_value: str,
    on_select: callable,
    columns: int = 3,
) -> rx.Component:
    """
    Grille de cartes de sélection.
    
    Args:
        items: Liste de dicts avec {label, value, icon, description?}
        selected_value: Valeur actuellement sélectionnée
        on_select: Handler appelé avec (value, abbr) lors de la sélection
        columns: Nombre de colonnes
    """
    return rx.grid(
        rx.foreach(
            items,
            lambda item: selector_card(
                label=item["label"],
                icon=item.get("icon", "folder"),
                is_selected=item["value"] == selected_value,
                on_click=lambda i=item: on_select(i["value"], i.get("abbr", "")),
                description=item.get("description", ""),
            )
        ),
        columns=rx.breakpoints({
            "initial": "2",
            "md": str(columns),
        }),
        spacing="4",
        width="100%",
    )


def typology_card(
    name: str,
    abbr: str,
    icon: str,
    is_selected: bool = False,
    on_click: callable = None,
) -> rx.Component:
    """
    Carte de sélection de typologie (version simplifiée).
    """
    return rx.box(
        rx.vstack(
            rx.cond(
                icon == "plug",
                rx.icon(tag="plug", size=30, color=COLORS["primary"]),
                rx.cond(
                    icon == "building",
                    rx.icon(tag="building", size=30, color=COLORS["primary"]),
                    rx.cond(
                        icon == "layers",
                        rx.icon(tag="layers", size=30, color=COLORS["primary"]),
                        rx.cond(
                            icon == "flame",
                            rx.icon(tag="flame", size=30, color=COLORS["primary"]),
                            rx.cond(
                                icon == "cpu",
                                rx.icon(tag="cpu", size=30, color=COLORS["primary"]),
                                rx.cond(
                                    icon == "briefcase",
                                    rx.icon(tag="briefcase", size=30, color=COLORS["primary"]),
                                    rx.cond(
                                        icon == "lightbulb",
                                        rx.icon(tag="lightbulb", size=30, color=COLORS["primary"]),
                                        rx.cond(
                                            icon == "thermometer",
                                            rx.icon(tag="thermometer", size=30, color=COLORS["primary"]),
                                            rx.icon(tag="circle-help", size=30, color=COLORS["primary"]),
                                        ),
                                    ),
                                ),
                            ),
                        ),
                    ),
                ),
            ),
            rx.text(
                name,
                font_size="1.1rem",
                font_weight="bold" if is_selected else "medium",
                color=COLORS["text_primary"],
            ),
            align_items="center",
            spacing="2",
            padding="1.5rem",
        ),
        background=COLORS["white"],
        border=f"{'2px' if is_selected else '1px'} solid {COLORS['primary'] if is_selected else COLORS['border']}",
        border_radius=RADIUS["xl"],
        box_shadow=SHADOWS["card"] if is_selected else SHADOWS["sm"],
        cursor="pointer",
        _hover={
            "box_shadow": SHADOWS["card_hover"],
            "transform": "scale(1.02)",
        },
        transition="all 0.2s ease-in-out",
        on_click=on_click,
        width="100%",
        text_align="center",
    )


def beneficiary_card(
    label: str,
    value: str,
    icon: str,
    description: str,
    is_selected: bool = False,
    on_click: callable = None,
) -> rx.Component:
    """
    Carte de sélection du type de bénéficiaire.
    """
    return rx.box(
        rx.hstack(
            rx.box(
                rx.icon(
                    tag=icon,
                    size=28,
                    color=COLORS["primary"] if is_selected else COLORS["text_secondary"],
                ),
                background=f"{COLORS['primary']}15" if is_selected else COLORS["background"],
                padding="1rem",
                border_radius=RADIUS["lg"],
            ),
            rx.vstack(
                rx.text(
                    label,
                    font_size="1rem",
                    font_weight="600",
                    color=COLORS["text_primary"],
                ),
                rx.text(
                    description,
                    font_size="0.875rem",
                    color=COLORS["text_muted"],
                ),
                spacing="0",
                align_items="start",
            ),
            rx.spacer(),
            rx.cond(
                is_selected,
                rx.icon(
                    tag="check-circle-2",
                    size=24,
                    color=COLORS["primary"],
                ),
                rx.box(
                    border=f"2px solid {COLORS['border']}",
                    border_radius=RADIUS["full"],
                    width="24px",
                    height="24px",
                ),
            ),
            width="100%",
            spacing="4",
            padding="1.25rem",
        ),
        background=COLORS["white"],
        border=f"{'2px' if is_selected else '1px'} solid {COLORS['primary'] if is_selected else COLORS['border']}",
        border_radius=RADIUS["xl"],
        box_shadow=SHADOWS["sm"],
        cursor="pointer",
        _hover={
            "border_color": COLORS["primary"],
            "box_shadow": SHADOWS["md"],
        },
        transition="all 0.2s ease-in-out",
        on_click=on_click,
        width="100%",
    )
