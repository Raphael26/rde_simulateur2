"""
Page d'inscription - Création de compte utilisateur.
"""

import reflex as rx
from ..styles import COLORS, SHADOWS, RADIUS
from ..state.auth_state import AuthState


def password_strength_indicator(password: str) -> rx.Component:
    """Indicateur de force du mot de passe."""
    # Calcul simple de la force
    has_length = len(password) >= 8
    has_upper = any(c.isupper() for c in password)
    has_digit = any(c.isdigit() for c in password)
    has_special = any(c in "!@#$%^&*(),.?\":{}|<>" for c in password)
    
    strength = sum([has_length, has_upper, has_digit, has_special])
    
    return rx.vstack(
        rx.hstack(
            rx.box(
                height="4px",
                flex="1",
                background=COLORS["error"] if strength >= 1 else COLORS["border"],
                border_radius=RADIUS["full"],
            ),
            rx.box(
                height="4px",
                flex="1",
                background=COLORS["warning"] if strength >= 2 else COLORS["border"],
                border_radius=RADIUS["full"],
            ),
            rx.box(
                height="4px",
                flex="1",
                background=COLORS["info"] if strength >= 3 else COLORS["border"],
                border_radius=RADIUS["full"],
            ),
            rx.box(
                height="4px",
                flex="1",
                background=COLORS["success"] if strength >= 4 else COLORS["border"],
                border_radius=RADIUS["full"],
            ),
            width="100%",
            spacing="1",
        ),
        spacing="1",
        width="100%",
    )


def register_page() -> rx.Component:
    """Page d'inscription."""
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
                    "Créez votre compte gratuitement",
                    font_size="0.875rem",
                    color=COLORS["text_muted"],
                ),
                spacing="2",
                align_items="center",
                margin_bottom="2rem",
            ),
            
            # Carte d'inscription
            rx.box(
                rx.vstack(
                    rx.heading(
                        "Inscription",
                        size="6",
                        font_weight="700",
                        color=COLORS["text_primary"],
                    ),
                    rx.text(
                        "Remplissez le formulaire pour créer votre compte",
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
                    
                    # Formulaire
                    rx.form(
                        rx.vstack(
                            # Nom complet
                            rx.vstack(
                                rx.text(
                                    "Nom complet",
                                    font_weight="500",
                                    font_size="0.875rem",
                                    color=COLORS["text_primary"],
                                ),
                                rx.input(
                                    placeholder="Jean Dupont",
                                    value=AuthState.register_full_name,
                                    on_change=AuthState.set_register_full_name,
                                    width="100%",
                                    size="3",
                                ),
                                rx.cond(
                                    AuthState.name_error != "",
                                    rx.text(
                                        AuthState.name_error,
                                        font_size="0.75rem",
                                        color=COLORS["error"],
                                    ),
                                    rx.box(),
                                ),
                                spacing="2",
                                width="100%",
                                align_items="stretch",
                            ),
                            
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
                                    value=AuthState.register_email,
                                    on_change=AuthState.set_register_email,
                                    width="100%",
                                    size="3",
                                ),
                                rx.cond(
                                    AuthState.email_error != "",
                                    rx.text(
                                        AuthState.email_error,
                                        font_size="0.75rem",
                                        color=COLORS["error"],
                                    ),
                                    rx.box(),
                                ),
                                spacing="2",
                                width="100%",
                                align_items="stretch",
                            ),
                            
                            # Mot de passe
                            rx.vstack(
                                rx.text(
                                    "Mot de passe",
                                    font_weight="500",
                                    font_size="0.875rem",
                                    color=COLORS["text_primary"],
                                ),
                                rx.input(
                                    placeholder="••••••••",
                                    type="password",
                                    value=AuthState.register_password,
                                    on_change=AuthState.set_register_password,
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
                                rx.text(
                                    "Min. 8 caractères, 1 majuscule, 1 chiffre, 1 caractère spécial",
                                    font_size="0.7rem",
                                    color=COLORS["text_muted"],
                                ),
                                spacing="2",
                                width="100%",
                                align_items="stretch",
                            ),
                            
                            # Confirmation mot de passe
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
                                    value=AuthState.register_confirm_password,
                                    on_change=AuthState.set_register_confirm_password,
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
                            
                            # CGU
                            rx.hstack(
                                rx.checkbox(
                                    checked=AuthState.register_accept_terms,
                                    on_change=AuthState.set_register_accept_terms,
                                    size="2",
                                ),
                                rx.text(
                                    rx.fragment(
                                        "J'accepte les ",
                                        rx.link(
                                            "conditions d'utilisation",
                                            href="#",
                                            color=COLORS["primary"],
                                        ),
                                        " et la ",
                                        rx.link(
                                            "politique de confidentialité",
                                            href="#",
                                            color=COLORS["primary"],
                                        ),
                                    ),
                                    font_size="0.8rem",
                                    color=COLORS["text_secondary"],
                                ),
                                width="100%",
                                spacing="2",
                                align_items="start",
                            ),
                            
                            # Bouton d'inscription
                            rx.button(
                                rx.cond(
                                    AuthState.is_loading,
                                    rx.hstack(
                                        rx.spinner(size="2"),
                                        rx.text("Création du compte..."),
                                        spacing="2",
                                    ),
                                    rx.text("Créer mon compte"),
                                ),
                                type="submit",
                                width="100%",
                                size="3",
                                disabled=~AuthState.is_register_valid | AuthState.is_loading,
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
                        on_submit=AuthState.handle_register,
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
                    
                    # Lien connexion
                    rx.text(
                        rx.fragment(
                            "Déjà un compte ? ",
                            rx.link(
                                "Se connecter",
                                href="/login",
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
