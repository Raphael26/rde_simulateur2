"""
Page de Connexion - Login
Design moderne et élégant avec Reflex
"""

import reflex as rx
from ..state.auth_state import AuthState
from ..styles.design_system import Colors, Typography, Spacing, Borders, Shadows


def login_card() -> rx.Component:
    """Carte de connexion principale."""
    return rx.box(
        rx.vstack(
            # Logo et titre
            rx.vstack(
                rx.box(
                    rx.image(
                        src="/logo_rde.jpg",
                        height="100px",
                        object_fit="contain",
                    ),
                    width="100%",
                    display="flex",
                    justify_content="center",
                ),
                rx.text(
                    "Connexion à votre compte",
                    font_size=Typography.SIZE_LG,
                    color=Colors.GRAY_600,
                    font_weight="500",
                    text_align="center",
                ),
                spacing="3",
                align="center",
                width="100%",
                margin_bottom="2rem",
            ),
            
            # Message d'erreur - Utilise has_error computed var pour une meilleure réactivité
            rx.cond(
                AuthState.has_error,
                rx.box(
                    rx.hstack(
                        rx.icon("alert-circle", size=18, color="#dc2626"),
                        rx.text(
                            AuthState.error_message,
                            font_size=Typography.SIZE_SM,
                            color="#dc2626",
                        ),
                        spacing="2",
                        align="center",
                    ),
                    padding="0.75rem 1rem",
                    background="#fef2f2",
                    border="1px solid #fecaca",
                    border_radius=Borders.RADIUS_MD,
                    width="100%",
                    margin_bottom="1rem",
                    # Animation d'apparition
                    animation="fadeIn 0.3s ease-in-out",
                ),
            ),
            
            # Message de succès - Utilise has_success computed var
            rx.cond(
                AuthState.has_success,
                rx.box(
                    rx.hstack(
                        rx.icon("check-circle", size=18, color=Colors.SUCCESS),
                        rx.text(
                            AuthState.success_message,
                            font_size=Typography.SIZE_SM,
                            color=Colors.SUCCESS,
                        ),
                        spacing="2",
                        align="center",
                    ),
                    padding="0.75rem 1rem",
                    background=Colors.SUCCESS_LIGHT,
                    border=f"1px solid {Colors.SUCCESS}30",
                    border_radius=Borders.RADIUS_MD,
                    width="100%",
                    margin_bottom="1rem",
                    # Animation d'apparition
                    animation="fadeIn 0.3s ease-in-out",
                ),
            ),
            
            # Formulaire
            rx.form(
                rx.vstack(
                    # Email
                    rx.vstack(
                        rx.text(
                            "Adresse email",
                            font_size=Typography.SIZE_SM,
                            font_weight="500",
                            color=Colors.GRAY_700,
                        ),
                        rx.box(
                            rx.hstack(
                                rx.icon("mail", size=18, color=Colors.GRAY_400),
                                rx.input(
                                    placeholder="vous@exemple.com",
                                    type="email",
                                    name="email",
                                    value=AuthState.login_email,
                                    on_change=AuthState.set_login_email,
                                    width="100%",
                                    border="none",
                                    outline="none",
                                    background="transparent",
                                    font_size=Typography.SIZE_BASE,
                                    _focus={"outline": "none"},
                                    required=True,
                                ),
                                spacing="3",
                                align="center",
                                width="100%",
                                padding="0.75rem 1rem",
                            ),
                            border=f"2px solid {Colors.GRAY_200}",
                            border_radius=Borders.RADIUS_LG,
                            background=Colors.WHITE,
                            _focus_within={
                                "border_color": Colors.PRIMARY,
                                "box_shadow": f"0 0 0 3px {Colors.PRIMARY}20",
                            },
                            transition="all 0.2s ease",
                            width="100%",
                        ),
                        spacing="1",
                        width="100%",
                    ),
                    
                    # Mot de passe
                    rx.vstack(
                        rx.hstack(
                            rx.text(
                                "Mot de passe",
                                font_size=Typography.SIZE_SM,
                                font_weight="500",
                                color=Colors.GRAY_700,
                            ),
                            rx.spacer(),
                            rx.link(
                                "Mot de passe oublié ?",
                                href="/forgot-password",
                                font_size=Typography.SIZE_SM,
                                color=Colors.PRIMARY,
                                _hover={"text_decoration": "underline"},
                            ),
                            width="100%",
                            align="center",
                        ),
                        rx.box(
                            rx.hstack(
                                rx.icon("lock", size=18, color=Colors.GRAY_400),
                                rx.input(
                                    placeholder="••••••••",
                                    type=rx.cond(AuthState.show_login_password, "text", "password"),
                                    name="password",
                                    value=AuthState.login_password,
                                    on_change=AuthState.set_login_password,
                                    width="100%",
                                    border="none",
                                    outline="none",
                                    background="transparent",
                                    font_size=Typography.SIZE_BASE,
                                    _focus={"outline": "none"},
                                    required=True,
                                ),
                                rx.icon_button(
                                    rx.cond(
                                        AuthState.show_login_password,
                                        rx.icon("eye-off", size=18),
                                        rx.icon("eye", size=18),
                                    ),
                                    variant="ghost",
                                    size="1",
                                    cursor="pointer",
                                    on_click=AuthState.toggle_login_password,
                                    color=Colors.GRAY_400,
                                    type="button",  # Important: évite de soumettre le formulaire
                                ),
                                spacing="3",
                                align="center",
                                width="100%",
                                padding="0.75rem 1rem",
                            ),
                            border=f"2px solid {Colors.GRAY_200}",
                            border_radius=Borders.RADIUS_LG,
                            background=Colors.WHITE,
                            _focus_within={
                                "border_color": Colors.PRIMARY,
                                "box_shadow": f"0 0 0 3px {Colors.PRIMARY}20",
                            },
                            transition="all 0.2s ease",
                            width="100%",
                        ),
                        spacing="1",
                        width="100%",
                    ),
                    
                    # Bouton de connexion
                    rx.button(
                        rx.cond(
                            AuthState.is_loading,
                            rx.hstack(
                                rx.spinner(size="1"),
                                rx.text("Connexion en cours..."),
                                spacing="2",
                                align="center",
                            ),
                            rx.hstack(
                                rx.text("Se connecter"),
                                rx.icon("arrow-right", size=18),
                                spacing="2",
                                align="center",
                            ),
                        ),
                        type="submit",
                        disabled=AuthState.is_loading,
                        width="100%",
                        size="3",
                        style={
                            "background": f"linear-gradient(135deg, {Colors.PRIMARY} 0%, #2d6b62 100%)",
                            "color": Colors.WHITE,
                            "font_weight": "600",
                            "padding": "0.875rem 1.5rem",
                            "border_radius": Borders.RADIUS_LG,
                            "cursor": "pointer",
                            "_hover": {
                                "transform": "translateY(-1px)",
                                "box_shadow": Shadows.LG,
                            },
                            "_disabled": {
                                "opacity": "0.7",
                                "cursor": "not-allowed",
                                "transform": "none",
                            },
                            "transition": "all 0.2s ease",
                        },
                        margin_top="0.5rem",
                    ),
                    
                    spacing="4",
                    width="100%",
                ),
                on_submit=AuthState.handle_login,
                width="100%",
                reset_on_submit=False,  # Ne pas reset le formulaire automatiquement
            ),
            
            # Séparateur
            rx.hstack(
                rx.divider(width="100%"),
                rx.text(
                    "ou",
                    font_size=Typography.SIZE_SM,
                    color=Colors.GRAY_400,
                    white_space="nowrap",
                    padding_x="1rem",
                ),
                rx.divider(width="100%"),
                width="100%",
                align="center",
                margin_y="1.5rem",
            ),
            
            # Lien vers inscription
            rx.hstack(
                rx.text(
                    "Pas encore de compte ?",
                    font_size=Typography.SIZE_SM,
                    color=Colors.GRAY_500,
                ),
                rx.link(
                    rx.hstack(
                        rx.text("Créer un compte"),
                        rx.icon("user-plus", size=16),
                        spacing="1",
                        align="center",
                    ),
                    href="/register",
                    font_size=Typography.SIZE_SM,
                    font_weight="600",
                    color=Colors.PRIMARY,
                    _hover={"text_decoration": "underline"},
                ),
                spacing="2",
                align="center",
                justify="center",
                width="100%",
            ),
            
            spacing="0",
            width="100%",
        ),
        
        # Style de la carte
        background=Colors.WHITE,
        padding="2.5rem",
        border_radius=Borders.RADIUS_2XL,
        box_shadow="0 25px 50px -12px rgba(0, 0, 0, 0.15)",
        border=f"1px solid {Colors.GRAY_100}",
        width="100%",
        max_width="420px",
    )


def login_page_content() -> rx.Component:
    """Contenu de la page de connexion."""
    return rx.box(
        # CSS pour l'animation fadeIn
        rx.html(
            """
            <style>
                @keyframes fadeIn {
                    from { opacity: 0; transform: translateY(-10px); }
                    to { opacity: 1; transform: translateY(0); }
                }
            </style>
            """
        ),
        rx.vstack(
            login_card(),
            
            # Retour à l'accueil
            rx.link(
                rx.hstack(
                    rx.icon("arrow-left", size=16),
                    rx.text("Retour à l'accueil"),
                    spacing="2",
                    align="center",
                    color=Colors.GRAY_500,
                    _hover={"color": Colors.PRIMARY},
                ),
                href="/",
                margin_top="2rem",
            ),
            
            spacing="0",
            align="center",
            justify="center",
            min_height="100vh",
            padding="2rem",
        ),
        
        # Background avec motif subtil
        background=f"linear-gradient(135deg, {Colors.GRAY_50} 0%, #e0e7e6 100%)",
        min_height="100vh",
        position="relative",
        _before={
            "content": '""',
            "position": "absolute",
            "top": "0",
            "left": "0",
            "right": "0",
            "bottom": "0",
            "background": f"radial-gradient(circle at 20% 80%, {Colors.PRIMARY}10 0%, transparent 50%), radial-gradient(circle at 80% 20%, {Colors.PRIMARY}08 0%, transparent 50%)",
            "pointer_events": "none",
        },
    )


@rx.page(
    route="/login",
    title="Connexion - RDE Consulting",
    on_load=AuthState.redirect_if_authenticated,
)
def login_page() -> rx.Component:
    """Page de connexion."""
    return login_page_content()