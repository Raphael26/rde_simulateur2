"""
Forgot Password Page
Password reset request page
"""

import reflex as rx
from state.auth_state import AuthState
from styles.design_system import Colors, Typography, Spacing, Borders, Shadows


def forgot_password_form() -> rx.Component:
    """Forgot password form component"""
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
                rx.box(
                    rx.icon("key-round", size=40, color=Colors.PRIMARY),
                    padding="1rem",
                    background=f"{Colors.PRIMARY}10",
                    border_radius=Borders.RADIUS_FULL,
                    margin_top="1.5rem",
                ),
                rx.heading(
                    "Mot de passe oublié ?",
                    font_size="1.5rem",
                    font_weight="700",
                    color=Colors.TEXT_PRIMARY,
                    margin_top="1rem",
                ),
                rx.text(
                    "Pas de souci ! Entrez votre adresse email et nous vous enverrons un lien pour réinitialiser votre mot de passe.",
                    font_size="0.9rem",
                    color=Colors.TEXT_SECONDARY,
                    text_align="center",
                    line_height="1.6",
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
                    rx.vstack(
                        rx.hstack(
                            rx.icon("check-circle", size=20, color=Colors.SUCCESS),
                            rx.text(
                                "Email envoyé !",
                                color=Colors.SUCCESS,
                                font_weight="600",
                            ),
                            spacing="2",
                            align="center",
                        ),
                        rx.text(
                            AuthState.success_message,
                            color=Colors.SUCCESS,
                            font_size="0.875rem",
                            text_align="center",
                        ),
                        spacing="2",
                        align="center",
                    ),
                    background=Colors.SUCCESS_LIGHT,
                    padding="1rem",
                    border_radius=Borders.RADIUS_MD,
                    width="100%",
                    margin_top="1rem",
                ),
            ),
            
            # Form
            rx.cond(
                AuthState.success_message == "",
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
                                value=AuthState.forgot_email,
                                on_change=AuthState.set_forgot_email,
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
                                    rx.text("Envoi en cours..."),
                                    spacing="2",
                                    align="center",
                                ),
                                rx.hstack(
                                    rx.icon("mail", size=18),
                                    rx.text("Envoyer le lien de réinitialisation"),
                                    spacing="2",
                                    align="center",
                                ),
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
                    on_submit=AuthState.request_password_reset,
                    width="100%",
                    margin_top="1.5rem",
                ),
            ),
            
            # Back to login link
            rx.link(
                rx.hstack(
                    rx.icon("arrow-left", size=16),
                    rx.text("Retour à la connexion"),
                    spacing="2",
                    align="center",
                ),
                href="/login",
                font_size="0.9rem",
                color=Colors.PRIMARY,
                font_weight="500",
                _hover={"text_decoration": "underline"},
                margin_top="2rem",
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


def forgot_password_page() -> rx.Component:
    """Forgot password page layout"""
    return rx.box(
        rx.center(
            forgot_password_form(),
            min_height="100vh",
            padding="1.5rem",
        ),
        background=f"linear-gradient(135deg, {Colors.BACKGROUND} 0%, {Colors.PRIMARY}10 100%)",
        font_family=Typography.FONT_FAMILY,
    )


@rx.page(route="/forgot-password", title="Mot de passe oublié - SimuPrime")
def forgot_password() -> rx.Component:
    return forgot_password_page()
