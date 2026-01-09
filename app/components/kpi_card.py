"""
Composant KPI Card - Cartes métriques pour le dashboard.
"""

import reflex as rx
from ..styles import COLORS, SHADOWS, SPACING, RADIUS


def kpi_card(
    title: str,
    value: str,
    icon: str,
    description: str = "",
    trend: str = "",
    trend_positive: bool = True,
    color: str = "primary",
) -> rx.Component:
    """
    Carte KPI pour afficher une métrique.
    
    Args:
        title: Titre de la métrique
        value: Valeur à afficher
        icon: Nom de l'icône Lucide
        description: Description optionnelle
        trend: Tendance (ex: "+12%")
        trend_positive: Si la tendance est positive
        color: Couleur de l'accent (primary, success, warning, error, info)
    """
    color_map = {
        "primary": COLORS["primary"],
        "success": COLORS["success"],
        "warning": COLORS["warning"],
        "error": COLORS["error"],
        "info": COLORS["info"],
    }
    accent_color = color_map.get(color, COLORS["primary"])
    
    return rx.box(
        rx.hstack(
            rx.vstack(
                rx.text(
                    title,
                    font_size="0.875rem",
                    font_weight="500",
                    color=COLORS["text_secondary"],
                ),
                rx.text(
                    value,
                    font_size="1.875rem",
                    font_weight="700",
                    color=COLORS["text_primary"],
                    line_height="1.2",
                ),
                rx.cond(
                    description != "",
                    rx.text(
                        description,
                        font_size="0.75rem",
                        color=COLORS["text_muted"],
                    ),
                    rx.box(),
                ),
                rx.cond(
                    trend != "",
                    rx.badge(
                        rx.hstack(
                            rx.icon(
                                tag="trending-up" if trend_positive else "trending-down",
                                size=14,
                            ),
                            rx.text(trend, font_size="0.75rem"),
                            spacing="1",
                        ),
                        color_scheme="green" if trend_positive else "red",
                        variant="soft",
                        size="1",
                    ),
                    rx.box(),
                ),
                spacing="1",
                align_items="start",
            ),
            rx.spacer(),
            rx.box(
                rx.icon(
                    tag=icon,
                    size=28,
                    color=accent_color,
                ),
                background=f"{accent_color}15",
                padding="0.75rem",
                border_radius=RADIUS["lg"],
            ),
            width="100%",
            align_items="start",
        ),
        background=COLORS["white"],
        border=f"1px solid {COLORS['border']}",
        border_radius=RADIUS["xl"],
        padding="1.25rem",
        box_shadow=SHADOWS["sm"],
        _hover={
            "box_shadow": SHADOWS["md"],
            "border_color": accent_color,
        },
        transition="all 0.2s ease-in-out",
    )


def kpi_grid(*kpis: rx.Component) -> rx.Component:
    """
    Grille de cartes KPI responsive.
    
    Args:
        *kpis: Composants KPI à afficher
    """
    return rx.grid(
        *kpis,
        columns=rx.breakpoints({
            "initial": "1",
            "sm": "2",
            "lg": "4",
        }),
        spacing="4",
        width="100%",
    )


def mini_kpi(
    label: str,
    value: str,
    icon: str = "",
) -> rx.Component:
    """
    Mini carte KPI pour les résumés compacts.
    """
    return rx.hstack(
        rx.cond(
            icon != "",
            rx.icon(tag=icon, size=16, color=COLORS["primary"]),
            rx.box(),
        ),
        rx.vstack(
            rx.text(
                label,
                font_size="0.7rem",
                color=COLORS["text_muted"],
            ),
            rx.text(
                value,
                font_size="0.875rem",
                font_weight="600",
                color=COLORS["text_primary"],
            ),
            spacing="0",
            align_items="start",
        ),
        spacing="2",
        padding="0.5rem 0.75rem",
        background=COLORS["background"],
        border_radius=RADIUS["md"],
    )


def result_card(
    title: str,
    value: str,
    unit: str,
    icon: str,
    color: str = "primary",
    size: str = "default",
) -> rx.Component:
    """
    Carte de résultat pour afficher les résultats de simulation.
    
    Args:
        title: Titre du résultat
        value: Valeur numérique
        unit: Unité (€, kWh cumac, etc.)
        icon: Icône Lucide
        color: Couleur d'accent
        size: "default" ou "large"
    """
    color_map = {
        "primary": COLORS["primary"],
        "success": COLORS["success"],
        "warning": COLORS["warning"],
        "error": COLORS["error"],
        "info": COLORS["info"],
    }
    accent_color = color_map.get(color, COLORS["primary"])
    
    is_large = size == "large"
    
    return rx.box(
        rx.vstack(
            rx.box(
                rx.icon(
                    tag=icon,
                    size=32 if is_large else 24,
                    color=accent_color,
                ),
                background=f"{accent_color}15",
                padding="1rem" if is_large else "0.75rem",
                border_radius=RADIUS["xl"],
                margin_bottom="0.75rem",
            ),
            rx.text(
                title,
                font_size="0.875rem" if is_large else "0.75rem",
                font_weight="500",
                color=COLORS["text_secondary"],
                text_align="center",
            ),
            rx.hstack(
                rx.text(
                    value,
                    font_size="2rem" if is_large else "1.5rem",
                    font_weight="700",
                    color=COLORS["text_primary"],
                ),
                rx.text(
                    unit,
                    font_size="1rem" if is_large else "0.875rem",
                    font_weight="500",
                    color=COLORS["text_muted"],
                    align_self="flex-end",
                    margin_bottom="0.25rem",
                ),
                spacing="1",
                align_items="baseline",
            ),
            spacing="1",
            align_items="center",
        ),
        background=COLORS["white"],
        border=f"2px solid {accent_color}30",
        border_radius=RADIUS["2xl"],
        padding="1.5rem" if is_large else "1rem",
        box_shadow=SHADOWS["md"],
        text_align="center",
        min_width="200px" if is_large else "160px",
    )
