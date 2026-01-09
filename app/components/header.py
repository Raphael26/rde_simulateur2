"""
Composant Header - En-tête de l'application.
"""

import reflex as rx
from ..styles import COLORS, SHADOWS, RADIUS
from ..state.user_state import UserState
from .sidebar import mobile_menu


def header(
    title: str = "",
    show_back: bool = False,
    back_href: str = "",
) -> rx.Component:
    """
    En-tête de page.
    
    Args:
        title: Titre de la page
        show_back: Afficher le bouton retour
        back_href: URL de retour
    """
    return rx.box(
        rx.hstack(
            # Menu mobile
            mobile_menu(),
            
            # Bouton retour
            rx.cond(
                show_back,
                rx.link(
                    rx.icon_button(
                        rx.icon(tag="arrow-left", size=20),
                        variant="ghost",
                    ),
                    href=back_href,
                ),
                rx.box(),
            ),
            
            # Titre
            rx.cond(
                title != "",
                rx.text(
                    title,
                    font_size="1.25rem",
                    font_weight="600",
                    color=COLORS["text_primary"],
                ),
                rx.box(),
            ),
            
            rx.spacer(),
            
            # Actions à droite
            rx.hstack(
                # Bouton nouvelle simulation
                rx.button(
                    rx.hstack(
                        rx.icon(tag="plus", size=18),
                        rx.text("Nouvelle simulation", display=["none", "none", "block"]),
                        spacing="2",
                    ),
                    on_click=rx.redirect("/simulation/date-department"),
                    style={
                        "background": COLORS["primary"],
                        "color": COLORS["white"],
                        "_hover": {"background": COLORS["primary_dark"]},
                    },
                    size="2",
                ),
                
                # Menu utilisateur
                rx.cond(
                    UserState.is_authenticated,
                    rx.menu.root(
                        rx.menu.trigger(
                            rx.hstack(
                                rx.box(
                                    rx.text(
                                        UserState.initials,
                                        font_size="0.75rem",
                                        font_weight="600",
                                        color=COLORS["white"],
                                    ),
                                    background=COLORS["primary"],
                                    border_radius=RADIUS["full"],
                                    width="36px",
                                    height="36px",
                                    display="flex",
                                    align_items="center",
                                    justify_content="center",
                                    cursor="pointer",
                                ),
                                rx.icon(tag="chevron-down", size=16, color=COLORS["text_muted"]),
                                spacing="1",
                                cursor="pointer",
                            ),
                        ),
                        rx.menu.content(
                            rx.menu.item(
                                rx.hstack(
                                    rx.icon(tag="layout-dashboard", size=16),
                                    rx.text("Tableau de bord"),
                                    spacing="2",
                                ),
                                on_click=rx.redirect("/dashboard"),
                            ),
                            rx.menu.item(
                                rx.hstack(
                                    rx.icon(tag="user", size=16),
                                    rx.text("Mon profil"),
                                    spacing="2",
                                ),
                                on_click=rx.redirect("/profile"),
                            ),
                            rx.menu.separator(),
                            rx.menu.item(
                                rx.hstack(
                                    rx.icon(tag="log-out", size=16, color=COLORS["error"]),
                                    rx.text("Déconnexion", color=COLORS["error"]),
                                    spacing="2",
                                ),
                                on_click=UserState.handle_logout,
                            ),
                        ),
                    ),
                    rx.hstack(
                        rx.link(
                            rx.button(
                                "Se connecter",
                                variant="ghost",
                            ),
                            href="/login",
                        ),
                        rx.link(
                            rx.button(
                                "Créer un compte",
                                style={
                                    "background": COLORS["primary"],
                                    "color": COLORS["white"],
                                },
                            ),
                            href="/register",
                        ),
                        spacing="2",
                    ),
                ),
                spacing="3",
            ),
            width="100%",
            padding="0.75rem 1.5rem",
            align_items="center",
        ),
        background=COLORS["white"],
        border_bottom=f"1px solid {COLORS['border']}",
        position="sticky",
        top="0",
        z_index="40",
        width="100%",
    )


def page_header(
    title: str,
    subtitle: str = "",
    actions: rx.Component = None,
) -> rx.Component:
    """
    En-tête de section de page.
    
    Args:
        title: Titre principal
        subtitle: Sous-titre optionnel
        actions: Composant d'actions à droite
    """
    return rx.hstack(
        rx.vstack(
            rx.text(
                title,
                font_size="1.5rem",
                font_weight="700",
                color=COLORS["text_primary"],
            ),
            rx.cond(
                subtitle != "",
                rx.text(
                    subtitle,
                    font_size="0.875rem",
                    color=COLORS["text_muted"],
                ),
                rx.box(),
            ),
            spacing="1",
            align_items="start",
        ),
        rx.spacer(),
        rx.cond(
            actions is not None,
            actions,
            rx.box(),
        ),
        width="100%",
        margin_bottom="1.5rem",
    )
