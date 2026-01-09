"""
Page de connexion - Login avec email et mot de passe.
"""

import reflex as rx
from ..styles import COLORS, SHADOWS, RADIUS
from ..state.auth_state import AuthState


def login_page() -> rx.Component:
    """Page de connexion."""
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
                rx.text(
                    "Connexion à votre compte",
                    font_size="0.875rem",
                    color=COLORS["text_muted"],
                ),
                spacing="2",
                align_items="center",
                margin_bottom="2rem",
            ),
            
            # Carte de connexion
            rx.box(
                rx.vstack(
                    rx.heading(
                        "Bienvenue",
                        size="6",
                        font_weight="700",
                        color=COLORS["text_primary"],
                    ),
                    rx.text(
                        "Connectez-vous pour accéder à vos simulations",
                        font_size="0.875rem",
                        color=COLORS["text_muted"],
                        margin_bottom="1rem",
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
                            # Email
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
                                    value=AuthState.login_email,
                                    on_change=AuthState.set_login_email,
                                    width="100%",
                                    size="3",
                                ),
                                spacing="2",
                                width="100%",
                                align_items="stretch",
                            ),
                            
                            # Mot de passe
                            rx.vstack(
                                rx.hstack(
                                    rx.text(
                                        "Mot de passe",
                                        font_weight="500",
                                        font_size="0.875rem",
                                        color=COLORS["text_primary"],
                                    ),
                                    rx.spacer(),
                                    rx.link(
                                        "Mot de passe oublié ?",
                                        href="/forgot-password",
                                        font_size="0.75rem",
                                        color=COLORS["primary"],
                                    ),
                                    width="100%",
                                ),
                                rx.input(
                                    placeholder="••••••••",
                                    type="password",
                                    value=AuthState.login_password,
                                    on_change=AuthState.set_login_password,
                                    width="100%",
                                    size="3",
                                ),
                                spacing="2",
                                width="100%",
                                align_items="stretch",
                            ),
                            
                            # Se souvenir de moi
                            rx.hstack(
                                rx.checkbox(
                                    "Se souvenir de moi",
                                    checked=AuthState.login_remember,
                                    on_change=AuthState.set_login_remember,
                                    size="2",
                                ),
                                width="100%",
                            ),
                            
                            # Bouton de connexion
                            rx.button(
                                rx.cond(
                                    AuthState.is_loading,
                                    rx.hstack(
                                        rx.spinner(size="2"),
                                        rx.text("Connexion..."),
                                        spacing="2",
                                    ),
                                    rx.text("Se connecter"),
                                ),
                                type="submit",
                                width="100%",
                                size="3",
                                disabled=~AuthState.is_login_valid | AuthState.is_loading,
                                style={
                                    "background": COLORS["primary"],
                                    "color": COLORS["white"],
                                    "margin_top": "0.5rem",
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
                        on_submit=AuthState.handle_login,
                        width="100%",
                    ),
                    
                    # Divider
                    rx.hstack(
                        rx.divider(width="40%"),
                        rx.text("ou", font_size="0.75rem", color=COLORS["text_muted"]),
                        rx.divider(width="40%"),
                        width="100%",
                        align_items="center",
                        margin_y="1.5rem",
                    ),
                    
                    # Lien inscription
                    rx.text(
                        rx.fragment(
                            "Pas encore de compte ? ",
                            rx.link(
                                "Créer un compte",
                                href="/register",
                                color=COLORS["primary"],
                                font_weight="600",
                            ),
                        ),
                        font_size="0.875rem",
                        color=COLORS["text_secondary"],
                        text_align="center",
                    ),
                    
                    spacing="1",
                    width="100%",
                    align_items="stretch",
                ),
                background=COLORS["white"],
                border=f"1px solid {COLORS['border']}",
                border_radius=RADIUS["xl"],
                box_shadow=SHADOWS["lg"],
                padding="2rem",
                width="100%",
                max_width="420px",
            ),
            
            # Lien retour
            rx.link(
                rx.hstack(
                    rx.icon(tag="arrow-left", size=16),
                    rx.text("Retour à l'accueil"),
                    spacing="2",
                    color=COLORS["text_muted"],
                    _hover={"color": COLORS["primary"]},
                ),
                href="/",
                margin_top="1.5rem",
            ),
            
            spacing="0",
            align_items="center",
        ),
        width="100%",
        min_height="100vh",
        background=COLORS["background"],
        padding="2rem",
    )
