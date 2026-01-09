"""
Dashboard Page
Main dashboard with KPIs, filters, and simulation history table
"""

import reflex as rx
from state.auth_state import AuthState
from state.dashboard_state import DashboardState
from styles.design_system import Colors, Typography, Spacing, Borders, Shadows
from components.sidebar import sidebar
from components.header import header


def kpi_card(title: str, value: rx.Var, icon: str, color: str, subtitle: str = "") -> rx.Component:
    """KPI card component"""
    return rx.box(
        rx.vstack(
            rx.hstack(
                rx.box(
                    rx.icon(icon, size=22, color=color),
                    padding="0.75rem",
                    background=f"{color}15",
                    border_radius=Borders.RADIUS_MD,
                ),
                rx.spacer(),
                rx.box(
                    rx.icon("trending-up", size=16, color=Colors.SUCCESS),
                    padding="0.25rem",
                ),
                width="100%",
            ),
            rx.text(
                value,
                font_size="1.75rem",
                font_weight="700",
                color=Colors.TEXT_PRIMARY,
            ),
            rx.text(
                title,
                font_size="0.875rem",
                color=Colors.TEXT_SECONDARY,
            ),
            rx.cond(
                subtitle != "",
                rx.text(
                    subtitle,
                    font_size="0.75rem",
                    color=Colors.TEXT_MUTED,
                ),
            ),
            spacing="2",
            align="start",
            width="100%",
        ),
        background="white",
        padding="1.25rem",
        border_radius=Borders.RADIUS_LG,
        border=f"1px solid {Colors.BORDER}",
        _hover={"box_shadow": Shadows.MD},
        transition="all 0.2s ease",
    )


def kpi_section() -> rx.Component:
    """Section with all KPI cards"""
    return rx.grid(
        kpi_card(
            "Total Simulations",
            DashboardState.total_simulations,
            "calculator",
            Colors.PRIMARY,
        ),
        kpi_card(
            "Montant Total (€)",
            DashboardState.total_eur.to(int).to_string() + " €",
            "euro",
            Colors.SUCCESS,
        ),
        kpi_card(
            "Ce mois",
            DashboardState.monthly_count,
            "calendar",
            Colors.INFO,
            "derniers 30 jours",
        ),
        kpi_card(
            "Dernière simulation",
            DashboardState.last_simulation_date,
            "clock",
            Colors.SECONDARY,
        ),
        columns=["1", "2", "4"],
        spacing="4",
        width="100%",
    )


def filters_section() -> rx.Component:
    """Filters section"""
    sectors = ["", "Résidentiel", "Tertiaire", "Industrie", "Agriculture", "Réseaux", "Transport"]
    typologies = ["", "Thermique", "Enveloppe", "Équipement", "Service", "Utilité", "Bâtiment", "Eclairage", "Chaleur"]
    
    return rx.box(
        rx.hstack(
            # Search input
            rx.box(
                rx.hstack(
                    rx.icon("search", size=18, color=Colors.TEXT_MUTED),
                    rx.input(
                        placeholder="Rechercher...",
                        value=DashboardState.filter_search,
                        on_change=DashboardState.set_filter_search,
                        border="none",
                        width="200px",
                        _focus={"outline": "none"},
                    ),
                    spacing="2",
                    align="center",
                    padding="0.5rem 1rem",
                    background=Colors.BACKGROUND,
                    border_radius=Borders.RADIUS_MD,
                    border=f"1px solid {Colors.BORDER}",
                ),
            ),
            
            # Sector filter
            rx.select(
                sectors,
                placeholder="Secteur",
                value=DashboardState.filter_sector,
                on_change=DashboardState.set_filter_sector,
                size="2",
            ),
            
            # Typology filter
            rx.select(
                typologies,
                placeholder="Typologie",
                value=DashboardState.filter_typology,
                on_change=DashboardState.set_filter_typology,
                size="2",
            ),
            
            # Date range
            rx.input(
                type="date",
                value=DashboardState.filter_date_start,
                on_change=DashboardState.set_filter_date_start,
                size="2",
            ),
            rx.text("à", color=Colors.TEXT_MUTED),
            rx.input(
                type="date",
                value=DashboardState.filter_date_end,
                on_change=DashboardState.set_filter_date_end,
                size="2",
            ),
            
            # Clear filters button
            rx.button(
                rx.hstack(
                    rx.icon("x", size=16),
                    rx.text("Effacer"),
                    spacing="1",
                ),
                variant="ghost",
                color=Colors.TEXT_SECONDARY,
                on_click=DashboardState.clear_filters,
                size="2",
            ),
            
            rx.spacer(),
            
            # New simulation button
            rx.link(
                rx.button(
                    rx.hstack(
                        rx.icon("plus", size=18),
                        rx.text("Nouvelle simulation"),
                        spacing="2",
                    ),
                    background=Colors.PRIMARY,
                    color="white",
                    size="2",
                    cursor="pointer",
                ),
                href="/date-department",
            ),
            
            spacing="3",
            align="center",
            width="100%",
            flex_wrap="wrap",
            gap="3",
        ),
        padding="1rem",
        background="white",
        border_radius=Borders.RADIUS_LG,
        border=f"1px solid {Colors.BORDER}",
    )


def simulation_table() -> rx.Component:
    """Simulation history table"""
    
    def table_header_cell(label: str, column: str) -> rx.Component:
        return rx.table.column_header_cell(
            rx.hstack(
                rx.text(label),
                rx.cond(
                    DashboardState.sort_column == column,
                    rx.icon(
                        rx.cond(DashboardState.sort_ascending, "chevron-up", "chevron-down"),
                        size=14,
                    ),
                ),
                spacing="1",
                align="center",
                cursor="pointer",
                on_click=lambda: DashboardState.set_sort(column),
            ),
        )
    
    def table_row(simulation: dict) -> rx.Component:
        return rx.table.row(
            rx.table.cell(
                rx.text(
                    simulation.get("created_at", "")[:10] if simulation.get("created_at") else "—",
                    font_size="0.875rem",
                ),
            ),
            rx.table.cell(
                rx.text(
                    simulation.get("name", "Sans nom"),
                    font_weight="500",
                    font_size="0.875rem",
                ),
            ),
            rx.table.cell(
                rx.badge(
                    simulation.get("sector", "—"),
                    color_scheme="teal",
                    variant="soft",
                ),
            ),
            rx.table.cell(
                rx.text(
                    simulation.get("typology", "—"),
                    font_size="0.875rem",
                ),
            ),
            rx.table.cell(
                rx.text(
                    simulation.get("document_id", "—"),
                    font_size="0.875rem",
                    font_family="monospace",
                ),
            ),
            rx.table.cell(
                rx.text(
                    f"{simulation.get('result_eur', 0):.2f} €",
                    font_weight="600",
                    color=Colors.SUCCESS,
                ),
            ),
            rx.table.cell(
                rx.hstack(
                    rx.button(
                        rx.icon("eye", size=16),
                        variant="ghost",
                        size="1",
                        on_click=lambda: DashboardState.view_simulation(simulation.get("id", "")),
                    ),
                    rx.button(
                        rx.icon("trash-2", size=16),
                        variant="ghost",
                        size="1",
                        color=Colors.ERROR,
                        on_click=lambda: DashboardState.open_delete_modal(simulation.get("id", "")),
                    ),
                    spacing="1",
                ),
            ),
            _hover={"background": Colors.BACKGROUND},
        )
    
    return rx.box(
        rx.table.root(
            rx.table.header(
                rx.table.row(
                    table_header_cell("Date", "created_at"),
                    table_header_cell("Nom", "name"),
                    table_header_cell("Secteur", "sector"),
                    table_header_cell("Typologie", "typology"),
                    table_header_cell("Fiche", "document_id"),
                    table_header_cell("Résultat", "result_eur"),
                    rx.table.column_header_cell("Actions"),
                ),
            ),
            rx.table.body(
                rx.foreach(
                    DashboardState.paginated_simulations,
                    table_row,
                ),
            ),
            width="100%",
        ),
        overflow_x="auto",
    )


def pagination_section() -> rx.Component:
    """Pagination controls"""
    return rx.hstack(
        rx.text(
            DashboardState.showing_range,
            font_size="0.875rem",
            color=Colors.TEXT_SECONDARY,
        ),
        rx.spacer(),
        rx.hstack(
            rx.select(
                ["10", "25", "50"],
                value=DashboardState.items_per_page.to_string(),
                on_change=DashboardState.set_items_per_page,
                size="1",
            ),
            rx.text("par page", font_size="0.875rem", color=Colors.TEXT_SECONDARY),
            spacing="2",
            align="center",
        ),
        rx.hstack(
            rx.button(
                rx.icon("chevron-left", size=18),
                variant="outline",
                size="1",
                on_click=DashboardState.prev_page,
                disabled=DashboardState.current_page <= 1,
            ),
            rx.text(
                f"Page {DashboardState.current_page} / {DashboardState.total_pages}",
                font_size="0.875rem",
            ),
            rx.button(
                rx.icon("chevron-right", size=18),
                variant="outline",
                size="1",
                on_click=DashboardState.next_page,
                disabled=DashboardState.current_page >= DashboardState.total_pages,
            ),
            spacing="2",
            align="center",
        ),
        width="100%",
        padding="1rem",
        border_top=f"1px solid {Colors.BORDER}",
    )


def delete_confirmation_modal() -> rx.Component:
    """Delete confirmation modal"""
    return rx.dialog.root(
        rx.dialog.content(
            rx.dialog.title(
                rx.hstack(
                    rx.icon("alert-triangle", size=24, color=Colors.ERROR),
                    rx.text("Confirmer la suppression"),
                    spacing="2",
                ),
            ),
            rx.dialog.description(
                rx.text(
                    "Êtes-vous sûr de vouloir supprimer cette simulation ? Cette action est irréversible.",
                    color=Colors.TEXT_SECONDARY,
                ),
            ),
            rx.hstack(
                rx.dialog.close(
                    rx.button(
                        "Annuler",
                        variant="outline",
                        on_click=DashboardState.close_delete_modal,
                    ),
                ),
                rx.button(
                    rx.cond(
                        DashboardState.is_deleting,
                        rx.hstack(rx.spinner(size="1"), rx.text("Suppression..."), spacing="2"),
                        rx.text("Supprimer"),
                    ),
                    color_scheme="red",
                    on_click=DashboardState.confirm_delete,
                    disabled=DashboardState.is_deleting,
                ),
                spacing="3",
                justify="end",
                margin_top="1rem",
            ),
        ),
        open=DashboardState.show_delete_modal,
    )


def empty_state() -> rx.Component:
    """Empty state when no simulations"""
    return rx.center(
        rx.vstack(
            rx.box(
                rx.icon("inbox", size=48, color=Colors.TEXT_MUTED),
                padding="1.5rem",
                background=Colors.BACKGROUND,
                border_radius=Borders.RADIUS_FULL,
            ),
            rx.text(
                "Aucune simulation",
                font_size="1.25rem",
                font_weight="600",
                color=Colors.TEXT_PRIMARY,
            ),
            rx.text(
                "Commencez par créer votre première simulation.",
                color=Colors.TEXT_SECONDARY,
                text_align="center",
            ),
            rx.link(
                rx.button(
                    rx.hstack(
                        rx.icon("plus", size=18),
                        rx.text("Nouvelle simulation"),
                        spacing="2",
                    ),
                    background=Colors.PRIMARY,
                    color="white",
                    size="3",
                    margin_top="1rem",
                ),
                href="/date-department",
            ),
            spacing="3",
            align="center",
            padding="3rem",
        ),
        width="100%",
        padding="2rem",
    )


def dashboard_content() -> rx.Component:
    """Main dashboard content"""
    return rx.box(
        rx.vstack(
            # Page header
            rx.hstack(
                rx.vstack(
                    rx.heading(
                        "Tableau de bord",
                        font_size="1.75rem",
                        font_weight="700",
                        color=Colors.TEXT_PRIMARY,
                    ),
                    rx.text(
                        "Gérez vos simulations et suivez vos résultats",
                        color=Colors.TEXT_SECONDARY,
                    ),
                    spacing="1",
                    align="start",
                ),
                rx.spacer(),
                rx.button(
                    rx.hstack(
                        rx.icon("download", size=18),
                        rx.text("Exporter"),
                        spacing="2",
                    ),
                    variant="outline",
                    on_click=DashboardState.export_simulations,
                ),
                width="100%",
                align="center",
            ),
            
            # KPIs
            kpi_section(),
            
            # Filters and table
            rx.box(
                filters_section(),
                rx.cond(
                    DashboardState.is_loading,
                    rx.center(
                        rx.vstack(
                            rx.spinner(size="3"),
                            rx.text("Chargement...", color=Colors.TEXT_MUTED),
                            spacing="2",
                        ),
                        padding="3rem",
                    ),
                    rx.cond(
                        DashboardState.has_simulations,
                        rx.box(
                            simulation_table(),
                            pagination_section(),
                            background="white",
                            border_radius=Borders.RADIUS_LG,
                            border=f"1px solid {Colors.BORDER}",
                            overflow="hidden",
                            margin_top="1rem",
                        ),
                        empty_state(),
                    ),
                ),
                width="100%",
            ),
            
            # Messages
            rx.cond(
                DashboardState.error_message != "",
                rx.callout(
                    DashboardState.error_message,
                    icon="alert-circle",
                    color="red",
                    margin_top="1rem",
                ),
            ),
            rx.cond(
                DashboardState.success_message != "",
                rx.callout(
                    DashboardState.success_message,
                    icon="check-circle",
                    color="green",
                    margin_top="1rem",
                ),
            ),
            
            spacing="5",
            width="100%",
            padding=["1.5rem", "2rem"],
        ),
        flex="1",
        min_height="100vh",
    )


def dashboard_page() -> rx.Component:
    """Dashboard page with sidebar layout"""
    return rx.hstack(
        sidebar(),
        rx.box(
            header(),
            dashboard_content(),
            delete_confirmation_modal(),
            flex="1",
            margin_left="280px",
            background=Colors.BACKGROUND,
            min_height="100vh",
        ),
        spacing="0",
        width="100%",
        font_family=Typography.FONT_FAMILY,
        on_mount=DashboardState.load_simulations,
    )


@rx.page(route="/dashboard", title="Tableau de bord - SimuPrime", on_load=AuthState.check_auth)
def dashboard() -> rx.Component:
    return rx.cond(
        AuthState.is_authenticated,
        dashboard_page(),
        rx.center(
            rx.vstack(
                rx.spinner(size="3"),
                rx.text("Vérification de l'authentification..."),
                spacing="3",
            ),
            min_height="100vh",
        ),
    )
