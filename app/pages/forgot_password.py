"""
Page mot de passe oublié - Demande de réinitialisation.
"""

import reflex as rx
from ..styles import COLORS, SHADOWS, RADIUS
from ..state.auth_state import AuthState


def forgot_password_page() -> rx.Component:
    """Page de demande de réinitialisation de mot de passe."""
    return rx.center(
        rx.vstack(
            # Logo et titre
            rx.vstack(
                rx.hstack(
                    rx.text(
                        "RDE",
                        font_weight="bold",
                        font_size="1.75rem",
                        color=COLORS["primary"],
                    ),
                    rx.text(
                        "Simulateur",
                        font_weight="600",
                        font_size="1.25rem",
                        color=COLORS["text_primary"],
                    ),
                    spacing="2",
                ),
                spacing="2",
                align_items="center",
                margin_bottom="2rem",
            ),
            
            # Carte
            rx.box(
                rx.vstack(
                    rx.box(
                        rx.icon(tag="key-round", size=32, color=COLORS["primary"]),
                        background=f"{COLORS['primary']}15",
                        padding="1rem",
                        border_radius=RADIUS["xl"],
                        margin_bottom="1rem",
                    ),
                    
                    rx.heading(
                        "Mot de passe oublié ?",
                        size="6",
                        font_weight="700",
                        color=COLORS["text_primary"],
                    ),
                    rx.text(
                        "Entrez votre adresse email et nous vous enverrons un lien pour réinitialiser votre mot de passe.",
                        font_size="0.875rem",
                        color=COLORS["text_muted"],
                        text_align="center",
                        margin_bottom="1.5rem",
                    ),
                    
                    # Message d'erreur
                    rx.cond(
                        AuthState.error_message != "",
                        rx.callout(
                            AuthState.error_message,
                            icon="alert-circle",
                            color_scheme="red",
                            width="100%",
                            margin_bottom="1rem",
                        ),
                        rx.box(),
                    ),
                    
                    # Message de succès
                    rx.cond(
                        AuthState.success_message != "",
                        rx.callout(
                            AuthState.success_message,
                            icon="check-circle",
                            color_scheme="green",
                            width="100%",
                            margin_bottom="1rem",
                        ),
                        rx.box(),
                    ),
                    
                    # Formulaire
                    rx.form(
                        rx.vstack(
                            rx.vstack(
                                rx.text(
                                    "Email",
                                    font_weight="500",
                                    font_size="0.875rem",
                                    color=COLORS["text_primary"],
                                ),
                                rx.input(
                                    placeholder="votre@email.com",
                                    type="email",
                                    value=AuthState.reset_email,
                                    on_change=AuthState.set_reset_email,
                                    width="100%",
                                    size="3",
                                ),
                                spacing="2",
                                width="100%",
                                align_items="stretch",
                            ),
                            
                            rx.button(
                                rx.cond(
                                    AuthState.is_loading,
                                    rx.hstack(
                                        rx.spinner(size="2"),
                                        rx.text("Envoi en cours..."),
                                        spacing="2",
                                    ),
                                    rx.text("Envoyer le lien"),
                                ),
                                type="submit",
                                width="100%",
                                size="3",
                                disabled=AuthState.is_loading,
                                style={
                                    "background": COLORS["primary"],
                                    "color": COLORS["white"],
                                    "_hover": {
                                        "background": COLORS["primary_dark"],
                                    },
                                    "_disabled": {
                                        "opacity": "0.6",
                                        "cursor": "not-allowed",
                                    },
                                },
                            ),
                            
                            spacing="4",
                            width="100%",
                        ),
                        on_submit=AuthState.handle_reset_password_request,
                        width="100%",
                    ),
                    
                    # Lien retour
                    rx.link(
                        rx.hstack(
                            rx.icon(tag="arrow-left", size=16),
                            rx.text("Retour à la connexion"),
                            spacing="2",
                        ),
                        href="/login",
                        color=COLORS["primary"],
                        margin_top="1.5rem",
                    ),
                    
                    spacing="1",
                    width="100%",
                    align_items="center",
                ),
                background=COLORS["white"],
                border=f"1px solid {COLORS['border']}",
                border_radius=RADIUS["xl"],
                box_shadow=SHADOWS["lg"],
                padding="2rem",
                width="100%",
                max_width="420px",
            ),
            
            spacing="0",
            align_items="center",
        ),
        width="100%",
        min_height="100vh",
        background=COLORS["background"],
        padding="2rem",
    )


def reset_password_page() -> rx.Component:
    """Page de réinitialisation de mot de passe (après clic sur le lien email)."""
    return rx.center(
        rx.vstack(
            # Logo et titre
            rx.vstack(
                rx.hstack(
                    rx.text(
                        "RDE",
                        font_weight="bold",
                        font_size="1.75rem",
                        color=COLORS["primary"],
                    ),
                    rx.text(
                        "Simulateur",
                        font_weight="600",
                        font_size="1.25rem",
                        color=COLORS["text_primary"],
                    ),
                    spacing="2",
                ),
                spacing="2",
                align_items="center",
                margin_bottom="2rem",
            ),
            
            # Carte
            rx.box(
                rx.vstack(
                    rx.box(
                        rx.icon(tag="lock", size=32, color=COLORS["primary"]),
                        background=f"{COLORS['primary']}15",
                        padding="1rem",
                        border_radius=RADIUS["xl"],
                        margin_bottom="1rem",
                    ),
                    
                    rx.heading(
                        "Nouveau mot de passe",
                        size="6",
                        font_weight="700",
                        color=COLORS["text_primary"],
                    ),
                    rx.text(
                        "Choisissez un nouveau mot de passe sécurisé.",
                        font_size="0.875rem",
                        color=COLORS["text_muted"],
                        text_align="center",
                        margin_bottom="1.5rem",
                    ),
                    
                    # Message d'erreur
                    rx.cond(
                        AuthState.error_message != "",
                        rx.callout(
                            AuthState.error_message,
                            icon="alert-circle",
                            color_scheme="red",
                            width="100%",
                            margin_bottom="1rem",
                        ),
                        rx.box(),
                    ),
                    
                    # Formulaire
                    rx.form(
                        rx.vstack(
                            rx.vstack(
                                rx.text(
                                    "Nouveau mot de passe",
                                    font_weight="500",
                                    font_size="0.875rem",
                                    color=COLORS["text_primary"],
                                ),
                                rx.input(
                                    placeholder="••••••••",
                                    type="password",
                                    value=AuthState.new_password,
                                    on_change=AuthState.set_new_password,
                                    width="100%",
                                    size="3",
                                ),
                                rx.cond(
                                    AuthState.password_error != "",
                                    rx.text(
                                        AuthState.password_error,
                                        font_size="0.75rem",
                                        color=COLORS["error"],
                                    ),
                                    rx.box(),
                                ),
                                spacing="2",
                                width="100%",
                                align_items="stretch",
                            ),
                            
                            rx.vstack(
                                rx.text(
                                    "Confirmer le mot de passe",
                                    font_weight="500",
                                    font_size="0.875rem",
                                    color=COLORS["text_primary"],
                                ),
                                rx.input(
                                    placeholder="••••••••",
                                    type="password",
                                    value=AuthState.confirm_new_password,
                                    on_change=AuthState.set_confirm_new_password,
                                    width="100%",
                                    size="3",
                                ),
                                rx.cond(
                                    AuthState.confirm_password_error != "",
                                    rx.text(
                                        AuthState.confirm_password_error,
                                        font_size="0.75rem",
                                        color=COLORS["error"],
                                    ),
                                    rx.box(),
                                ),
                                spacing="2",
                                width="100%",
                                align_items="stretch",
                            ),
                            
                            rx.button(
                                rx.cond(
                                    AuthState.is_loading,
                                    rx.hstack(
                                        rx.spinner(size="2"),
                                        rx.text("Mise à jour..."),
                                        spacing="2",
                                    ),
                                    rx.text("Réinitialiser le mot de passe"),
                                ),
                                type="submit",
                                width="100%",
                                size="3",
                                disabled=AuthState.is_loading,
                                style={
                                    "background": COLORS["primary"],
                                    "color": COLORS["white"],
                                    "_hover": {
                                        "background": COLORS["primary_dark"],
                                    },
                                    "_disabled": {
                                        "opacity": "0.6",
                                        "cursor": "not-allowed",
                                    },
                                },
                            ),
                            
                            spacing="4",
                            width="100%",
                        ),
                        on_submit=AuthState.handle_update_password,
                        width="100%",
                    ),
                    
                    spacing="1",
                    width="100%",
                    align_items="center",
                ),
                background=COLORS["white"],
                border=f"1px solid {COLORS['border']}",
                border_radius=RADIUS["xl"],
                box_shadow=SHADOWS["lg"],
                padding="2rem",
                width="100%",
                max_width="420px",
            ),
            
            spacing="0",
            align_items="center",
        ),
        width="100%",
        min_height="100vh",
        background=COLORS["background"],
        padding="2rem",
    )
