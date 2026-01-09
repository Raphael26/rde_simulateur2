"""
Page Profil - Gestion du profil et des paramètres utilisateur.
"""

import reflex as rx
from ..styles import COLORS, SHADOWS, RADIUS
from ..state.user_state import UserState
from ..components.sidebar import sidebar
from ..components.header import header, page_header


def profile_info_section() -> rx.Component:
    """Section informations personnelles."""
    return rx.box(
        rx.vstack(
            rx.hstack(
                rx.text(
                    "Informations personnelles",
                    font_weight="600",
                    font_size="1rem",
                    color=COLORS["text_primary"],
                ),
                rx.spacer(),
                rx.cond(
                    UserState.edit_mode,
                    rx.hstack(
                        rx.button(
                            "Annuler",
                            variant="ghost",
                            on_click=UserState.toggle_edit_mode,
                        ),
                        rx.button(
                            "Enregistrer",
                            on_click=UserState.save_profile,
                            style={
                                "background": COLORS["primary"],
                                "color": COLORS["white"],
                            },
                        ),
                        spacing="2",
                    ),
                    rx.button(
                        rx.hstack(
                            rx.icon(tag="pencil", size=16),
                            rx.text("Modifier"),
                            spacing="2",
                        ),
                        variant="outline",
                        on_click=UserState.toggle_edit_mode,
                    ),
                ),
                width="100%",
            ),
            rx.divider(),
            
            # Avatar et nom
            rx.hstack(
                rx.box(
                    rx.text(
                        UserState.initials,
                        font_weight="700",
                        font_size="2rem",
                        color=COLORS["white"],
                    ),
                    background=COLORS["primary"],
                    border_radius=RADIUS["full"],
                    width="80px",
                    height="80px",
                    display="flex",
                    align_items="center",
                    justify_content="center",
                ),
                rx.vstack(
                    rx.cond(
                        UserState.edit_mode,
                        rx.input(
                            value=UserState.edit_full_name,
                            on_change=UserState.set_edit_full_name,
                            placeholder="Votre nom",
                            width="250px",
                        ),
                        rx.text(
                            UserState.user_full_name,
                            font_weight="600",
                            font_size="1.25rem",
                            color=COLORS["text_primary"],
                        ),
                    ),
                    rx.text(
                        UserState.user_email,
                        font_size="0.875rem",
                        color=COLORS["text_muted"],
                    ),
                    rx.badge(
                        "Compte actif",
                        color_scheme="green",
                        variant="soft",
                    ),
                    spacing="1",
                    align_items="start",
                ),
                spacing="4",
                padding_y="1rem",
            ),
            
            # Infos supplémentaires
            rx.grid(
                rx.vstack(
                    rx.text("Membre depuis", font_size="0.75rem", color=COLORS["text_muted"]),
                    rx.text(
                        UserState.user_created_at[:10] if UserState.user_created_at else "-",
                        font_weight="500",
                    ),
                    spacing="1",
                    align_items="start",
                ),
                rx.vstack(
                    rx.text("Simulations", font_size="0.75rem", color=COLORS["text_muted"]),
                    rx.text(str(UserState.total_simulations), font_weight="500"),
                    spacing="1",
                    align_items="start",
                ),
                columns="2",
                spacing="4",
                width="100%",
            ),
            
            # Messages
            rx.cond(
                UserState.profile_error != "",
                rx.callout(
                    UserState.profile_error,
                    icon="alert-circle",
                    color_scheme="red",
                    width="100%",
                ),
                rx.box(),
            ),
            rx.cond(
                UserState.profile_success != "",
                rx.callout(
                    UserState.profile_success,
                    icon="check-circle",
                    color_scheme="green",
                    width="100%",
                ),
                rx.box(),
            ),
            
            spacing="4",
            width="100%",
        ),
        background=COLORS["white"],
        border=f"1px solid {COLORS['border']}",
        border_radius=RADIUS["xl"],
        padding="1.5rem",
    )


def security_section() -> rx.Component:
    """Section sécurité - changement de mot de passe."""
    return rx.box(
        rx.vstack(
            rx.hstack(
                rx.icon(tag="shield", size=20, color=COLORS["primary"]),
                rx.text(
                    "Sécurité",
                    font_weight="600",
                    font_size="1rem",
                    color=COLORS["text_primary"],
                ),
                spacing="2",
            ),
            rx.divider(),
            
            rx.text(
                "Changer le mot de passe",
                font_weight="500",
                color=COLORS["text_primary"],
            ),
            
            rx.form(
                rx.vstack(
                    rx.vstack(
                        rx.text("Mot de passe actuel", font_size="0.875rem"),
                        rx.input(
                            type="password",
                            placeholder="••••••••",
                            value=UserState.current_password,
                            on_change=UserState.set_current_password,
                            width="100%",
                        ),
                        spacing="1",
                        width="100%",
                        align_items="stretch",
                    ),
                    rx.vstack(
                        rx.text("Nouveau mot de passe", font_size="0.875rem"),
                        rx.input(
                            type="password",
                            placeholder="••••••••",
                            value=UserState.profile_new_password,
                            on_change=UserState.set_profile_new_password,
                            width="100%",
                        ),
                        spacing="1",
                        width="100%",
                        align_items="stretch",
                    ),
                    rx.vstack(
                        rx.text("Confirmer le nouveau mot de passe", font_size="0.875rem"),
                        rx.input(
                            type="password",
                            placeholder="••••••••",
                            value=UserState.profile_confirm_password,
                            on_change=UserState.set_profile_confirm_password,
                            width="100%",
                        ),
                        spacing="1",
                        width="100%",
                        align_items="stretch",
                    ),
                    rx.button(
                        "Mettre à jour le mot de passe",
                        type="submit",
                        style={
                            "background": COLORS["primary"],
                            "color": COLORS["white"],
                        },
                    ),
                    spacing="3",
                    width="100%",
                    max_width="400px",
                ),
                on_submit=UserState.change_password,
            ),
            
            spacing="4",
            width="100%",
            align_items="stretch",
        ),
        background=COLORS["white"],
        border=f"1px solid {COLORS['border']}",
        border_radius=RADIUS["xl"],
        padding="1.5rem",
    )


def danger_zone_section() -> rx.Component:
    """Section zone de danger - suppression de compte."""
    return rx.box(
        rx.vstack(
            rx.hstack(
                rx.icon(tag="alert-triangle", size=20, color=COLORS["error"]),
                rx.text(
                    "Zone de danger",
                    font_weight="600",
                    font_size="1rem",
                    color=COLORS["error"],
                ),
                spacing="2",
            ),
            rx.divider(),
            
            rx.hstack(
                rx.vstack(
                    rx.text(
                        "Supprimer le compte",
                        font_weight="500",
                        color=COLORS["text_primary"],
                    ),
                    rx.text(
                        "Cette action est irréversible. Toutes vos données seront supprimées.",
                        font_size="0.875rem",
                        color=COLORS["text_muted"],
                    ),
                    spacing="1",
                    align_items="start",
                ),
                rx.spacer(),
                rx.alert_dialog.root(
                    rx.alert_dialog.trigger(
                        rx.button(
                            "Supprimer mon compte",
                            color_scheme="red",
                            variant="outline",
                        ),
                    ),
                    rx.alert_dialog.content(
                        rx.alert_dialog.title("Êtes-vous sûr ?"),
                        rx.alert_dialog.description(
                            "Cette action supprimera définitivement votre compte et toutes vos simulations. "
                            "Cette action ne peut pas être annulée.",
                        ),
                        rx.hstack(
                            rx.alert_dialog.cancel(
                                rx.button("Annuler", variant="soft", color_scheme="gray"),
                            ),
                            rx.alert_dialog.action(
                                rx.button("Supprimer définitivement", color_scheme="red"),
                            ),
                            spacing="3",
                            justify="end",
                        ),
                        style={"max_width": "450px"},
                    ),
                ),
                width="100%",
            ),
            
            spacing="4",
            width="100%",
        ),
        background=COLORS["white"],
        border=f"1px solid {COLORS['error']}30",
        border_radius=RADIUS["xl"],
        padding="1.5rem",
    )


def profile_content() -> rx.Component:
    """Contenu principal de la page profil."""
    return rx.vstack(
        page_header(
            title="Mon profil",
            subtitle="Gérez vos informations personnelles et vos préférences",
        ),
        
        profile_info_section(),
        security_section(),
        danger_zone_section(),
        
        spacing="4",
        width="100%",
        max_width="800px",
        padding="1.5rem",
        align_items="stretch",
    )


def profile_page() -> rx.Component:
    """Page profil complète avec sidebar."""
    return rx.hstack(
        sidebar(current_page="profile"),
        rx.box(
            header(title=""),
            rx.scroll_area(
                rx.center(
                    profile_content(),
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
