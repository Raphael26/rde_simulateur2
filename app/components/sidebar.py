"""
Composant Sidebar - Navigation latérale de l'application.
Avec affichage dynamique des informations utilisateur via AuthState.
"""

import reflex as rx
from ..state.auth_state import AuthState
from ..styles import COLORS, SHADOWS, SPACING, RADIUS


def sidebar_item(
    icon: str,
    label: str,
    href: str,
    is_active: bool = False
) -> rx.Component:
    """Élément de menu de la sidebar."""
    return rx.link(
        rx.hstack(
            rx.icon(
                tag=icon,
                size=20,
                color=COLORS["primary"] if is_active else COLORS["text_secondary"],
            ),
            rx.text(
                label,
                font_weight="600" if is_active else "normal",
                color=COLORS["primary"] if is_active else COLORS["text_primary"],
                font_size="0.95rem",
            ),
            spacing="3",
            align="center",
            padding="0.75rem 1rem",
            border_radius=RADIUS["lg"],
            background=f"{COLORS['primary']}15" if is_active else "transparent",
            _hover={
                "background": f"{COLORS['primary']}10",
            },
            transition="all 0.2s ease-in-out",
            width="100%",
        ),
        href=href,
        width="100%",
        style={"text_decoration": "none"},
    )


def sidebar_section(title: str, children: list) -> rx.Component:
    """Section de la sidebar avec titre."""
    return rx.vstack(
        rx.text(
            title,
            font_size="0.75rem",
            font_weight="600",
            color=COLORS["text_muted"],
            text_transform="uppercase",
            letter_spacing="0.05em",
            padding_left="1rem",
            margin_bottom="0.5rem",
        ),
        *children,
        spacing="1",
        width="100%",
        align_items="stretch",
    )


def user_menu() -> rx.Component:
    """Menu utilisateur en bas de la sidebar avec infos dynamiques."""
    return rx.menu.root(
        rx.menu.trigger(
            rx.hstack(
                # Avatar avec initiales - cercle parfait
                rx.box(
                    rx.text(
                        AuthState.initials,
                        font_weight="600",
                        color=COLORS["white"],
                        font_size="0.875rem",
                    ),
                    background=COLORS["primary"],
                    border_radius="50%",
                    width="40px",
                    height="40px",
                    min_width="40px",
                    min_height="40px",
                    display="flex",
                    align_items="center",
                    justify_content="center",
                ),
                # Infos utilisateur
                rx.vstack(
                    rx.text(
                        AuthState.display_name,
                        font_weight="600",
                        font_size="0.875rem",
                        color=COLORS["text_primary"],
                        no_of_lines=1,
                        max_width="140px",
                        overflow="hidden",
                        text_overflow="ellipsis",
                    ),
                    rx.text(
                        AuthState.user_email,
                        font_size="0.75rem",
                        color=COLORS["text_muted"],
                        no_of_lines=1,
                        max_width="140px",
                        overflow="hidden",
                        text_overflow="ellipsis",
                    ),
                    spacing="0",
                    align_items="start",
                ),
                spacing="3",
                align="center",
                padding="1rem",
                background=COLORS["background"],
                border_radius=RADIUS["lg"],
                width="100%",
                cursor="pointer",
                _hover={"background": f"{COLORS['primary']}10"},
                transition="all 0.2s ease",
            ),
        ),
        rx.menu.content(
            rx.menu.item(
                rx.hstack(
                    rx.icon(tag="user", size=16),
                    rx.text("Mon profil"),
                    spacing="2",
                    align="center",
                ),
                on_click=rx.redirect("/profile"),
            ),
            rx.menu.separator(),
            rx.menu.item(
                rx.hstack(
                    rx.icon(tag="log-out", size=16, color=COLORS["error"]),
                    rx.text("Déconnexion", color=COLORS["error"]),
                    spacing="2",
                    align="center",
                ),
                on_click=AuthState.handle_logout,
            ),
        ),
    )


def user_menu_logged_out() -> rx.Component:
    """Menu pour les utilisateurs non connectés."""
    return rx.link(
        rx.hstack(
            rx.box(
                rx.icon("user", size=18, color=COLORS["white"]),
                background=COLORS["text_muted"],
                border_radius="50%",
                width="40px",
                height="40px",
                min_width="40px",
                min_height="40px",
                display="flex",
                align_items="center",
                justify_content="center",
            ),
            rx.vstack(
                rx.text(
                    "Non connecté",
                    font_weight="500",
                    font_size="0.875rem",
                    color=COLORS["text_secondary"],
                ),
                rx.text(
                    "Cliquez pour vous connecter",
                    font_size="0.75rem",
                    color=COLORS["primary"],
                ),
                spacing="0",
                align_items="start",
            ),
            spacing="3",
            align="center",
            padding="1rem",
            background=COLORS["background"],
            border_radius=RADIUS["lg"],
            width="100%",
            cursor="pointer",
            _hover={"background": f"{COLORS['primary']}10"},
            transition="all 0.2s ease",
        ),
        href="/login",
        style={"text_decoration": "none"},
        width="100%",
    )


def sidebar(current_page: str = "") -> rx.Component:
    """
    Sidebar principale de l'application.
    
    Args:
        current_page: Page active pour la mise en surbrillance
    """
    return rx.box(
        rx.vstack(
            # Logo RDE Consulting - pleine largeur
            rx.box(
                rx.image(
                    src="/logo_rde.jpg",
                    width="100%",
                    height="auto",
                    object_fit="contain",
                ),
                padding="4px 8px",
                cursor="pointer",
                on_click=rx.redirect("/"),
                width="100%",
            ),
            
            rx.divider(),
            
            # Menu principal
            rx.vstack(
                sidebar_section(
                    "Navigation",
                    [
                        sidebar_item(
                            "layout-dashboard",
                            "Tableau de bord",
                            "/dashboard",
                            is_active=current_page == "dashboard",
                        ),
                        sidebar_item(
                            "plus-circle",
                            "Nouvelle simulation",
                            "/simulation/date-department",
                            is_active=current_page == "simulation",
                        ),
                    ],
                ),
                sidebar_section(
                    "Compte",
                    [
                        sidebar_item(
                            "user",
                            "Mon profil",
                            "/profile",
                            is_active=current_page == "profile",
                        ),
                    ],
                ),
                spacing="6",
                width="100%",
                padding="1rem",
                flex="1",
            ),
            
            rx.spacer(),
            
            # Menu utilisateur en bas (conditionnel)
            rx.box(
                rx.cond(
                    AuthState.is_authenticated,
                    user_menu(),
                    user_menu_logged_out(),
                ),
                width="100%",
                padding="0.5rem",
            ),
            
            spacing="0",
            height="100%",
        ),
        width="260px",
        min_width="260px",
        height="100vh",
        background=COLORS["white"],
        border_right=f"1px solid {COLORS['border']}",
        display="flex",
        flex_direction="column",
        position="sticky",
        top="0",
        left="0",
    )


# ============================================
# MOBILE SIDEBAR - Version responsive
# ============================================

def mobile_sidebar(current_page: str = "") -> rx.Component:
    """Sidebar mobile avec drawer."""
    return rx.drawer.root(
        rx.drawer.trigger(
            rx.icon_button(
                rx.icon("menu", size=24),
                variant="ghost",
                size="3",
            ),
        ),
        rx.drawer.overlay(z_index="50"),
        rx.drawer.portal(
            rx.drawer.content(
                rx.vstack(
                    # Header avec logo et bouton fermer
                    rx.hstack(
                        rx.image(
                            src="/logo_rde.jpg",
                            height="32px",
                            object_fit="contain",
                        ),
                        rx.spacer(),
                        rx.drawer.close(
                            rx.icon_button(
                                rx.icon("x", size=20),
                                variant="ghost",
                                size="2",
                            ),
                        ),
                        width="100%",
                        padding="0.5rem",
                        align="center",
                    ),
                    rx.divider(),
                    rx.vstack(
                        sidebar_item("layout-dashboard", "Tableau de bord", "/dashboard", current_page == "dashboard"),
                        sidebar_item("plus-circle", "Nouvelle simulation", "/simulation/date-department", current_page == "simulation"),
                        sidebar_item("user", "Mon profil", "/profile", current_page == "profile"),
                        rx.divider(margin_y="1rem"),
                        rx.cond(
                            AuthState.is_authenticated,
                            rx.button(
                                rx.hstack(
                                    rx.icon(tag="log-out", size=18),
                                    rx.text("Déconnexion"),
                                    spacing="2",
                                    align="center",
                                ),
                                variant="ghost",
                                color_scheme="red",
                                width="100%",
                                on_click=AuthState.handle_logout,
                            ),
                            rx.button(
                                rx.hstack(
                                    rx.icon(tag="log-in", size=18),
                                    rx.text("Se connecter"),
                                    spacing="2",
                                    align="center",
                                ),
                                variant="outline",
                                width="100%",
                                on_click=rx.redirect("/login"),
                            ),
                        ),
                        spacing="2",
                        width="100%",
                        padding="1rem",
                    ),
                    width="100%",
                ),
                background=COLORS["white"],
                height="100vh",
                width="280px",
            ),
        ),
        direction="left",
    )


# Alias pour compatibilité
def mobile_menu(current_page: str = "") -> rx.Component:
    """Alias pour mobile_sidebar (compatibilité)."""
    return mobile_sidebar(current_page)


# ============================================
# SIMULATION SIDEBAR - Navigation des étapes
# ============================================

def simulation_sidebar(current_step: int) -> rx.Component:
    """Sidebar de navigation pour les étapes de simulation."""
    
    PRIMARY = COLORS.get("primary", "#368278")
    PRIMARY_LIGHTER = f"{PRIMARY}15"
    SUCCESS = COLORS.get("success", "#22c55e")
    WHITE = COLORS.get("white", "#ffffff")
    GRAY_100 = "#f3f4f6"
    GRAY_200 = COLORS.get("border", "#e5e7eb")
    GRAY_400 = "#9ca3af"
    GRAY_500 = COLORS.get("text_muted", "#6b7280")
    GRAY_700 = COLORS.get("text_primary", "#374151")
    
    steps = [
        (1, "Date & Département", "calendar", "/simulation/date-department"),
        (2, "Secteur", "building-2", "/simulation/sector"),
        (3, "Typologie", "layers", "/simulation/typology"),
        (4, "Fiche CEE", "file-text", "/simulation/fiches"),
        (5, "Paramètres", "settings", "/simulation/form"),
        (6, "Résultats", "check-circle", "/simulation/result"),
    ]
    
    def make_step_item(step_num: int, title: str, icon: str, route: str) -> rx.Component:
        is_current = step_num == current_step
        is_completed = step_num < current_step
        is_clickable = step_num <= current_step
        
        # Couleur du cercle
        if is_completed:
            circle_bg = SUCCESS
            circle_color = WHITE
        elif is_current:
            circle_bg = PRIMARY
            circle_color = WHITE
        else:
            circle_bg = GRAY_200
            circle_color = GRAY_500
        
        # Couleur du texte
        if is_current:
            text_color = PRIMARY
            text_weight = "600"
            bg_color = PRIMARY_LIGHTER
        elif is_completed:
            text_color = GRAY_700
            text_weight = "400"
            bg_color = "transparent"
        else:
            text_color = GRAY_400
            text_weight = "400"
            bg_color = "transparent"
        
        return rx.box(
            rx.hstack(
                rx.box(
                    rx.cond(
                        is_completed,
                        rx.icon("check", size=14, color=circle_color),
                        rx.text(str(step_num), font_size="12px", font_weight="700", color=circle_color),
                    ),
                    width="28px",
                    height="28px",
                    display="flex",
                    align_items="center",
                    justify_content="center",
                    background=circle_bg,
                    border_radius="9999px",
                ),
                rx.text(
                    title,
                    font_size="14px",
                    font_weight=text_weight,
                    color=text_color,
                ),
                spacing="3",
                align="center",
                width="100%",
            ),
            padding="8px",
            border_radius="8px",
            background=bg_color,
            cursor="pointer" if is_clickable else "default",
            opacity="1" if is_clickable else "0.5",
            _hover={"background": GRAY_100} if is_clickable else {},
            on_click=rx.redirect(route) if is_clickable else None,
            width="100%",
        )
    
    def make_connector(step_num: int) -> rx.Component:
        is_done = step_num < current_step
        return rx.box(
            width="2px",
            height="16px",
            background=SUCCESS if is_done else GRAY_200,
            margin_left="13px",
        )
    
    return rx.box(
        rx.vstack(
            # Logo RDE Consulting - pleine largeur
            rx.box(
                rx.image(
                    src="/logo_rde.jpg",
                    width="100%",
                    height="auto",
                    object_fit="contain",
                ),
                padding="4px 8px",
                cursor="pointer",
                on_click=rx.redirect("/"),
                width="100%",
            ),
            
            rx.divider(margin_y="8px"),
            
            rx.text(
                "ÉTAPES DE SIMULATION",
                font_size="11px",
                font_weight="600",
                color=GRAY_400,
                letter_spacing="0.05em",
            ),
            
            # Liste des étapes
            rx.vstack(
                make_step_item(1, "Date & Département", "calendar", "/simulation/date-department"),
                make_connector(1),
                make_step_item(2, "Secteur", "building-2", "/simulation/sector"),
                make_connector(2),
                make_step_item(3, "Typologie", "layers", "/simulation/typology"),
                make_connector(3),
                make_step_item(4, "Fiche CEE", "file-text", "/simulation/fiches"),
                make_connector(4),
                make_step_item(5, "Paramètres", "settings", "/simulation/form"),
                make_connector(5),
                make_step_item(6, "Résultats", "check-circle", "/simulation/result"),
                spacing="0",
                width="100%",
            ),
            
            rx.spacer(),
            
            rx.divider(margin_y="16px"),
            
            # Navigation rapide
            rx.vstack(
                rx.box(
                    rx.hstack(
                        rx.icon("plus-circle", size=16, color=WHITE),
                        rx.text("Nouvelle simulation", color=WHITE, font_size="14px", font_weight="500"),
                        spacing="2",
                        align="center",
                    ),
                    padding="10px 12px",
                    background=PRIMARY,
                    border_radius="8px",
                    width="100%",
                    cursor="pointer",
                    _hover={"background": "#2d6b62"},
                    on_click=rx.redirect("/simulation/date-department"),
                ),
                rx.link(
                    rx.hstack(
                        rx.icon("home", size=16, color=GRAY_500),
                        rx.text("Accueil", color=GRAY_700, font_size="14px"),
                        spacing="2",
                        align="center",
                    ),
                    href="/",
                    width="100%",
                    padding="8px",
                    border_radius="8px",
                    _hover={"background": GRAY_100},
                ),
                rx.link(
                    rx.hstack(
                        rx.icon("layout-dashboard", size=16, color=GRAY_500),
                        rx.text("Tableau de bord", color=GRAY_700, font_size="14px"),
                        spacing="2",
                        align="center",
                    ),
                    href="/dashboard",
                    width="100%",
                    padding="8px",
                    border_radius="8px",
                    _hover={"background": GRAY_100},
                ),
                spacing="2",
                width="100%",
            ),
            
            # Info utilisateur connecté (si applicable)
            rx.cond(
                AuthState.is_authenticated,
                rx.box(
                    rx.hstack(
                        rx.box(
                            rx.text(
                                AuthState.initials,
                                font_size="11px",
                                font_weight="600",
                                color=WHITE,
                            ),
                            width="28px",
                            height="28px",
                            background=PRIMARY,
                            border_radius="50%",
                            display="flex",
                            align_items="center",
                            justify_content="center",
                        ),
                        rx.text(
                            AuthState.display_name,
                            font_size="13px",
                            color=GRAY_700,
                            no_of_lines=1,
                        ),
                        spacing="2",
                        align="center",
                    ),
                    padding="8px",
                    margin_top="8px",
                    background=GRAY_100,
                    border_radius="8px",
                    width="100%",
                ),
                rx.box(),
            ),
            
            spacing="4",
            align="start",
            height="100%",
            padding="20px",
        ),
        width="260px",
        min_width="260px",
        height="100vh",
        background=WHITE,
        border_right=f"1px solid {GRAY_200}",
        position="fixed",
        left="0",
        top="0",
        overflow_y="auto",
    )