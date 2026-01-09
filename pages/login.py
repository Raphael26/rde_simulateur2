"""
Login Page
User authentication page with email and password
"""

import reflex as rx
from state.auth_state import AuthState
from styles.design_system import Colors, Typography, Spacing, Borders, Shadows


def login_form() -> rx.Component:
    """Login form component"""
    return rx.box(
        rx.vstack(
            # Logo and title
            rx.vstack(
                rx.hstack(
                    rx.icon("calculator", size=32, color=Colors.PRIMARY),
                    rx.text(
                        "SimuPrime",
                        font_size="1.5rem",
                        font_weight="700",
                        color=Colors.TEXT_PRIMARY,
                    ),
                    spacing="2",
                    align="center",
                ),
                rx.heading(
                    "Connexion",
                    font_size="1.75rem",
                    font_weight="700",
                    color=Colors.TEXT_PRIMARY,
                    margin_top="1rem",
                ),
                rx.text(
                    "Bienvenue ! Connectez-vous pour accéder à votre espace.",
                    font_size="0.95rem",
                    color=Colors.TEXT_SECONDARY,
                    text_align="center",
                ),
                spacing="2",
                align="center",
                width="100%",
            ),
            
            # Error message
            rx.cond(
                AuthState.error_message != "",
                rx.box(
                    rx.hstack(
                        rx.icon("alert-circle", size=18, color=Colors.ERROR),
                        rx.text(AuthState.error_message, color=Colors.ERROR, font_size="0.875rem"),
                        spacing="2",
                        align="center",
                    ),
                    background=Colors.ERROR_LIGHT,
                    padding="0.75rem 1rem",
                    border_radius=Borders.RADIUS_MD,
                    width="100%",
                    margin_top="1rem",
                ),
            ),
            
            # Success message
            rx.cond(
                AuthState.success_message != "",
                rx.box(
                    rx.hstack(
                        rx.icon("check-circle", size=18, color=Colors.SUCCESS),
                        rx.text(AuthState.success_message, color=Colors.SUCCESS, font_size="0.875rem"),
                        spacing="2",
                        align="center",
                    ),
                    background=Colors.SUCCESS_LIGHT,
                    padding="0.75rem 1rem",
                    border_radius=Borders.RADIUS_MD,
                    width="100%",
                    margin_top="1rem",
                ),
            ),
            
            # Form
            rx.form(
                rx.vstack(
                    # Email field
                    rx.box(
                        rx.text(
                            "Email",
                            font_size="0.875rem",
                            font_weight="500",
                            color=Colors.TEXT_SECONDARY,
                            margin_bottom="0.5rem",
                        ),
                        rx.input(
                            placeholder="votre@email.com",
                            type="email",
                            value=AuthState.login_email,
                            on_change=AuthState.set_login_email,
                            size="3",
                            width="100%",
                            border_radius=Borders.RADIUS_MD,
                        ),
                        width="100%",
                    ),
                    
                    # Password field
                    rx.box(
                        rx.hstack(
                            rx.text(
                                "Mot de passe",
                                font_size="0.875rem",
                                font_weight="500",
                                color=Colors.TEXT_SECONDARY,
                            ),
                            rx.spacer(),
                            rx.link(
                                "Mot de passe oublié ?",
                                href="/forgot-password",
                                font_size="0.8rem",
                                color=Colors.PRIMARY,
                                _hover={"text_decoration": "underline"},
                            ),
                            width="100%",
                            margin_bottom="0.5rem",
                        ),
                        rx.input(
                            placeholder="••••••••",
                            type="password",
                            value=AuthState.login_password,
                            on_change=AuthState.set_login_password,
                            size="3",
                            width="100%",
                            border_radius=Borders.RADIUS_MD,
                        ),
                        width="100%",
                    ),
                    
                    # Submit button
                    rx.button(
                        rx.cond(
                            AuthState.is_loading,
                            rx.hstack(
                                rx.spinner(size="1"),
                                rx.text("Connexion en cours..."),
                                spacing="2",
                                align="center",
                            ),
                            rx.text("Se connecter"),
                        ),
                        type="submit",
                        size="3",
                        width="100%",
                        background=Colors.PRIMARY,
                        color="white",
                        font_weight="600",
                        border_radius=Borders.RADIUS_MD,
                        cursor="pointer",
                        disabled=AuthState.is_loading,
                        _hover={"background": Colors.PRIMARY_DARK},
                        margin_top="0.5rem",
                    ),
                    
                    spacing="4",
                    width="100%",
                ),
                on_submit=AuthState.login,
                width="100%",
                margin_top="1.5rem",
            ),
            
            # Divider
            rx.hstack(
                rx.divider(width="100%"),
                rx.text("ou", color=Colors.TEXT_MUTED, font_size="0.8rem", white_space="nowrap"),
                rx.divider(width="100%"),
                width="100%",
                align="center",
                margin_top="1.5rem",
            ),
            
            # Register link
            rx.hstack(
                rx.text(
                    "Pas encore de compte ?",
                    font_size="0.9rem",
                    color=Colors.TEXT_SECONDARY,
                ),
                rx.link(
                    "Créer un compte",
                    href="/register",
                    font_size="0.9rem",
                    font_weight="600",
                    color=Colors.PRIMARY,
                    _hover={"text_decoration": "underline"},
                ),
                spacing="2",
                justify="center",
                margin_top="1rem",
            ),
            
            # Back to home
            rx.link(
                rx.hstack(
                    rx.icon("arrow-left", size=16),
                    rx.text("Retour à l'accueil"),
                    spacing="1",
                    align="center",
                ),
                href="/",
                font_size="0.875rem",
                color=Colors.TEXT_MUTED,
                _hover={"color": Colors.PRIMARY},
                margin_top="1.5rem",
            ),
            
            spacing="0",
            align="center",
            width="100%",
        ),
        
        background="white",
        padding=["2rem", "2.5rem", "3rem"],
        border_radius=Borders.RADIUS_XL,
        box_shadow=Shadows.LG,
        width="100%",
        max_width="420px",
    )


def login_page() -> rx.Component:
    """Login page layout"""
    return rx.box(
        rx.center(
            login_form(),
            min_height="100vh",
            padding="1.5rem",
        ),
        background=f"linear-gradient(135deg, {Colors.BACKGROUND} 0%, {Colors.PRIMARY}10 100%)",
        font_family=Typography.FONT_FAMILY,
    )


@rx.page(route="/login", title="Connexion - SimuPrime")
def login() -> rx.Component:
    return login_page()
