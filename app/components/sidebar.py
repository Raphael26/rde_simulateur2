"""
Composant Sidebar - Navigation latérale de l'application.
"""

import reflex as rx
from ..state.user_state import UserState
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


#def user_menu() -> rx.Component:
#    """Menu utilisateur en bas de la sidebar."""
#    return rx.hstack(
#        rx.box(
#            rx.text(
#                UserState.initials,
#                font_weight="600",
#                color=COLORS["white"],
#                font_size="0.875rem",
#            ),
#            background=COLORS["primary"],
#            border_radius=RADIUS["full"],
#            width="40px",
#            height="40px",
#            display="flex",
#            align_items="center",
#            justify_content="center",
#        ),
#        rx.vstack(
#            rx.text(
#                UserState.display_name,
#                font_weight="600",
#                font_size="0.875rem",
#                color=COLORS["text_primary"],
#                no_of_lines=1,
#            ),
#            rx.text(
#                UserState.user_email,
#                font_size="0.75rem",
#                color=COLORS["text_muted"],
#                no_of_lines=1,
#            ),
#            spacing="0",
#            align_items="start",
#        ),
#        rx.spacer(),
#        rx.menu.root(
#            rx.menu.trigger(
#                rx.icon_button(
#                    rx.icon(tag="more-vertical", size=18),
#                    variant="ghost",
#                    size="1",
#                    cursor="pointer",
#                ),
#            ),
#            rx.menu.content(
#                rx.menu.item(
#                    rx.hstack(
#                        rx.icon(tag="user", size=16),
#                        rx.text("Mon profil"),
#                        spacing="2",
#                    ),
#                    on_click=rx.redirect("/profile"),
#                ),
#                rx.menu.item(
#                    rx.hstack(
#                        rx.icon(tag="settings", size=16),
#                        rx.text("Paramètres"),
#                        spacing="2",
#                    ),
#                ),
#                rx.menu.separator(),
#                rx.menu.item(
#                    rx.hstack(
#                        rx.icon(tag="log-out", size=16, color=COLORS["error"]),
#                        rx.text("Déconnexion", color=COLORS["error"]),
#                        spacing="2",
#                    ),
#                    on_click=UserState.handle_logout,
#                ),
#            ),
#        ),
#        padding="1rem",
#        background=COLORS["background"],
#        border_radius=RADIUS["lg"],
#        width="100%",
#        spacing="3",
#    )


def user_menu() -> rx.Component:
    """Menu utilisateur en bas de la sidebar."""
    return rx.hstack(
        rx.box(
            rx.icon("user", size=18, color=COLORS["white"]),
            background=COLORS["primary"],
            border_radius=RADIUS["full"],
            width="40px",
            height="40px",
            display="flex",
            align_items="center",
            justify_content="center",
        ),
        rx.vstack(
            rx.text(
                "Utilisateur",
                font_weight="600",
                font_size="0.875rem",
                color=COLORS["text_primary"],
                no_of_lines=1,
            ),
            rx.text(
                "user@email.com",
                font_size="0.75rem",
                color=COLORS["text_muted"],
                no_of_lines=1,
            ),
            spacing="0",
            align_items="start",
        ),
        rx.spacer(),
        rx.menu.root(
            rx.menu.trigger(
                rx.icon_button(
                    rx.icon(tag="more-vertical", size=18),
                    variant="ghost",
                    size="1",
                    cursor="pointer",
                ),
            ),
            rx.menu.content(
                rx.menu.item(
                    rx.hstack(
                        rx.icon(tag="user", size=16),
                        rx.text("Mon profil"),
                        spacing="2",
                    ),
                    on_click=rx.redirect("/profile"),
                ),
                rx.menu.item(
                    rx.hstack(
                        rx.icon(tag="settings", size=16),
                        rx.text("Paramètres"),
                        spacing="2",
                    ),
                ),
                rx.menu.separator(),
                rx.menu.item(
                    rx.hstack(
                        rx.icon(tag="log-out", size=16, color=COLORS["error"]),
                        rx.text("Déconnexion", color=COLORS["error"]),
                        spacing="2",
                    ),
                    on_click=rx.redirect("/login"),
                ),
            ),
        ),
        padding="1rem",
        background=COLORS["background"],
        border_radius=RADIUS["lg"],
        width="100%",
        spacing="3",
    )


def sidebar(current_page: str = "") -> rx.Component:
    """
    Sidebar principale de l'application.
    
    Args:
        current_page: Page active pour la mise en surbrillance
    """
    return rx.box(
        rx.vstack(
            # Logo
            #rx.hstack(
            #    rx.image(
            #        src="/logo.png",
            #        height="40px",
            #        fallback=rx.box(
            #            rx.text(
            #                "RDE",
            #                font_weight="bold",
            #                font_size="1.5rem",
            #                color=COLORS["primary"],
            #            ),
            #            padding="0.5rem",
            #        ),
            #    ),
            #    rx.text(
            #        "Simulateur CEE",
            #        font_weight="bold",
            #        font_size="1.1rem",
            #        color=COLORS["text_primary"],
            #    ),
            #    spacing="2",
            #    padding="1rem",
            #    cursor="pointer",
            #    on_click=rx.redirect("/"),
            #),

            rx.hstack(
                rx.icon("zap", size=28, color=COLORS["primary"]),
                rx.text(
                    "SimuPrime",
                    font_weight="bold",
                    font_size="1.25rem",
                    color=COLORS["primary"],
                ),
                spacing="2",
                padding="1rem",
                cursor="pointer",
                on_click=rx.redirect("/"),
            ),
            
            rx.divider(margin_y="0.5rem"),
            
            # Navigation principale
            rx.vstack(
                sidebar_section(
                    "Menu principal",
                    [
                        sidebar_item(
                            "layout-dashboard",
                            "Tableau de bord",
                            "/dashboard",
                            is_active=current_page == "dashboard"
                        ),
                        sidebar_item(
                            "plus-circle",
                            "Nouvelle simulation",
                            "/simulation/date-department",
                            is_active=current_page == "simulation"
                        ),
                    ]
                ),
                
                sidebar_section(
                    "Mon compte",
                    [
                        sidebar_item(
                            "user",
                            "Mon profil",
                            "/profile",
                            is_active=current_page == "profile"
                        ),
                        sidebar_item(
                            "history",
                            "Historique",
                            "/dashboard",
                            is_active=False
                        ),
                    ]
                ),
                
                spacing="6",
                width="100%",
                align_items="stretch",
                flex="1",
                padding_y="1rem",
            ),
            
            rx.spacer(),
            
            # Menu utilisateur
            rx.cond(
                UserState.is_authenticated,
                user_menu(),
                rx.box(),
            ),
            
            height="100%",
            width="100%",
            spacing="0",
            align_items="stretch",
        ),
        background=COLORS["white"],
        border_right=f"1px solid {COLORS['border']}",
        width="260px",
        min_width="260px",
        height="100vh",
        position="sticky",
        top="0",
        left="0",
        padding="0.5rem",
        display=["none", "none", "none", "flex"],  # Caché sur mobile
    )


def mobile_menu() -> rx.Component:
    """Menu mobile (hamburger)."""
    return rx.drawer.root(
        rx.drawer.trigger(
            rx.icon_button(
                rx.icon(tag="menu", size=24),
                variant="ghost",
                display=["flex", "flex", "flex", "none"],  # Visible uniquement sur mobile
            ),
        ),
        rx.drawer.overlay(z_index="50"),
        rx.drawer.portal(
            rx.drawer.content(
                rx.vstack(
                    rx.hstack(
                        rx.text(
                            "Menu",
                            font_weight="bold",
                            font_size="1.25rem",
                        ),
                        rx.spacer(),
                        rx.drawer.close(
                            rx.icon_button(
                                rx.icon(tag="x", size=20),
                                variant="ghost",
                            ),
                        ),
                        width="100%",
                        padding="1rem",
                    ),
                    rx.divider(),
                    rx.vstack(
                        sidebar_item("layout-dashboard", "Tableau de bord", "/dashboard"),
                        sidebar_item("plus-circle", "Nouvelle simulation", "/simulation/date-department"),
                        sidebar_item("user", "Mon profil", "/profile"),
                        rx.divider(margin_y="1rem"),
                        rx.button(
                            rx.hstack(
                                rx.icon(tag="log-out", size=18),
                                rx.text("Déconnexion"),
                                spacing="2",
                            ),
                            variant="ghost",
                            color_scheme="red",
                            width="100%",
                            on_click=UserState.handle_logout,
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
            # Header
            rx.hstack(
                rx.icon("zap", size=24, color=PRIMARY),
                rx.text("SimuPrime", font_size="18px", font_weight="700", color=PRIMARY),
                spacing="2",
                align="center",
                cursor="pointer",
                on_click=rx.redirect("/"),
            ),
            
            rx.divider(margin_y="16px"),
            
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