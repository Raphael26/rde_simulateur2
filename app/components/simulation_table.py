"""
Composant Simulation Table - Tableau des simulations pour le dashboard.
"""

import reflex as rx
from ..styles import COLORS, SHADOWS, RADIUS
from ..state.user_state import UserState


def table_header_cell(
    label: str,
    sort_key: str = "",
    sortable: bool = False,
) -> rx.Component:
    """Cellule d'en-tête de tableau avec tri optionnel."""
    return rx.table.column_header_cell(
        rx.cond(
            sortable,
            rx.hstack(
                rx.text(label, font_weight="600", font_size="0.75rem"),
                rx.cond(
                    UserState.sort_column == sort_key,
                    rx.icon(
                        tag="chevron-up" if UserState.sort_direction == "asc" else "chevron-down",
                        size=14,
                        color=COLORS["primary"],
                    ),
                    rx.icon(tag="chevrons-up-down", size=14, color=COLORS["text_muted"]),
                ),
                spacing="1",
                cursor="pointer",
                on_click=lambda: UserState.sort_by(sort_key),
                _hover={"color": COLORS["primary"]},
            ),
            rx.text(label, font_weight="600", font_size="0.75rem"),
        ),
        style={
            "background": COLORS["background"],
            "color": COLORS["text_secondary"],
            "text_transform": "uppercase",
            "letter_spacing": "0.05em",
        },
    )


def simulation_row(simulation: dict) -> rx.Component:
    """Ligne de simulation dans le tableau."""
    return rx.table.row(
        # Nom
        rx.table.cell(
            rx.vstack(
                rx.text(
                    simulation["name"],
                    font_weight="500",
                    color=COLORS["text_primary"],
                    font_size="0.875rem",
                ),
                rx.text(
                    simulation["fiche_code"],
                    font_size="0.75rem",
                    color=COLORS["text_muted"],
                ),
                spacing="0",
                align_items="start",
            ),
        ),
        # Date
        rx.table.cell(
            rx.text(
                simulation["created_at"][:10] if simulation["created_at"] else "-",
                font_size="0.875rem",
                color=COLORS["text_secondary"],
            ),
        ),
        # Secteur
        rx.table.cell(
            rx.badge(
                simulation["sector"],
                color_scheme="teal",
                variant="soft",
                size="1",
            ),
        ),
        # Typologie
        rx.table.cell(
            rx.badge(
                simulation["typology"],
                color_scheme="blue",
                variant="soft",
                size="1",
            ),
        ),
        # Résultat
        rx.table.cell(
            rx.vstack(
                rx.text(
                    f"{simulation['result_euros']:,.2f} €".replace(",", " "),
                    font_weight="600",
                    color=COLORS["primary"],
                    font_size="0.875rem",
                ),
                rx.text(
                    f"{simulation['result_cumacs']:,.0f} kWh".replace(",", " "),
                    font_size="0.7rem",
                    color=COLORS["text_muted"],
                ),
                spacing="0",
                align_items="end",
            ),
        ),
        # Actions
        rx.table.cell(
            rx.hstack(
                rx.tooltip(
                    rx.icon_button(
                        rx.icon(tag="eye", size=16),
                        variant="ghost",
                        size="1",
                        cursor="pointer",
                    ),
                    content="Voir les détails",
                ),
                rx.tooltip(
                    rx.icon_button(
                        rx.icon(tag="copy", size=16),
                        variant="ghost",
                        size="1",
                        cursor="pointer",
                    ),
                    content="Dupliquer",
                ),
                rx.alert_dialog.root(
                    rx.alert_dialog.trigger(
                        rx.tooltip(
                            rx.icon_button(
                                rx.icon(tag="trash-2", size=16, color=COLORS["error"]),
                                variant="ghost",
                                size="1",
                                cursor="pointer",
                            ),
                            content="Supprimer",
                        ),
                    ),
                    rx.alert_dialog.content(
                        rx.alert_dialog.title("Supprimer la simulation"),
                        rx.alert_dialog.description(
                            f"Êtes-vous sûr de vouloir supprimer cette simulation ? Cette action est irréversible.",
                        ),
                        rx.hstack(
                            rx.alert_dialog.cancel(
                                rx.button("Annuler", variant="soft", color_scheme="gray"),
                            ),
                            rx.alert_dialog.action(
                                rx.button(
                                    "Supprimer",
                                    color_scheme="red",
                                    on_click=lambda: UserState.delete_simulation(simulation["id"]),
                                ),
                            ),
                            spacing="3",
                            justify="end",
                        ),
                        style={"max_width": "400px"},
                    ),
                ),
                spacing="1",
            ),
        ),
        _hover={"background": COLORS["background"]},
    )


def simulation_table() -> rx.Component:
    """Tableau complet des simulations."""
    return rx.box(
        # Filtres
        rx.hstack(
            rx.input(
                placeholder="Rechercher...",
                value=UserState.filter_search,
                on_change=UserState.set_filter_search,
                width="250px",
            ),
            rx.select(
                [""] + UserState.available_sectors,
                placeholder="Secteur",
                value=UserState.filter_sector,
                on_change=UserState.set_filter_sector,
                width="150px",
            ),
            rx.select(
                [""] + UserState.available_typologies,
                placeholder="Typologie",
                value=UserState.filter_typology,
                on_change=UserState.set_filter_typology,
                width="150px",
            ),
            rx.spacer(),
            rx.button(
                rx.hstack(
                    rx.icon(tag="x", size=16),
                    rx.text("Effacer filtres"),
                    spacing="1",
                ),
                variant="ghost",
                size="2",
                on_click=UserState.clear_filters,
            ),
            width="100%",
            padding="1rem",
            flex_wrap="wrap",
            gap="2",
        ),
        
        # Tableau
        rx.table.root(
            rx.table.header(
                rx.table.row(
                    table_header_cell("Simulation", "name", True),
                    table_header_cell("Date", "created_at", True),
                    table_header_cell("Secteur", "sector", True),
                    table_header_cell("Typologie", "typology", True),
                    table_header_cell("Résultat", "result_euros", True),
                    table_header_cell("Actions"),
                ),
            ),
            rx.table.body(
                rx.foreach(
                    UserState.paginated_simulations,
                    simulation_row,
                ),
            ),
            width="100%",
        ),
        
        # État vide
        rx.cond(
            UserState.total_simulations == 0,
            rx.center(
                rx.vstack(
                    rx.icon(tag="inbox", size=48, color=COLORS["text_muted"]),
                    rx.text(
                        "Aucune simulation trouvée",
                        color=COLORS["text_muted"],
                        font_size="1rem",
                    ),
                    rx.button(
                        "Créer une simulation",
                        on_click=rx.redirect("/simulation/date-department"),
                        style={
                            "background": COLORS["primary"],
                            "color": COLORS["white"],
                        },
                    ),
                    spacing="3",
                    padding="3rem",
                ),
            ),
            rx.box(),
        ),
        
        # Pagination
        rx.cond(
            UserState.total_simulations > 0,
            rx.hstack(
                rx.hstack(
                    rx.text(
                        f"{UserState.total_simulations} simulation(s)",
                        font_size="0.875rem",
                        color=COLORS["text_muted"],
                    ),
                    rx.select(
                        ["10", "25", "50"],
                        value=str(UserState.page_size),
                        on_change=UserState.set_page_size,
                        width="80px",
                    ),
                    rx.text("par page", font_size="0.875rem", color=COLORS["text_muted"]),
                    spacing="2",
                ),
                rx.spacer(),
                rx.hstack(
                    rx.icon_button(
                        rx.icon(tag="chevron-left", size=18),
                        variant="ghost",
                        disabled=UserState.current_page <= 1,
                        on_click=UserState.previous_page,
                    ),
                    rx.text(
                        f"Page {UserState.current_page} / {UserState.total_pages}",
                        font_size="0.875rem",
                    ),
                    rx.icon_button(
                        rx.icon(tag="chevron-right", size=18),
                        variant="ghost",
                        disabled=UserState.current_page >= UserState.total_pages,
                        on_click=UserState.next_page,
                    ),
                    spacing="2",
                ),
                width="100%",
                padding="1rem",
            ),
            rx.box(),
        ),
        
        background=COLORS["white"],
        border=f"1px solid {COLORS['border']}",
        border_radius=RADIUS["xl"],
        overflow="hidden",
    )
