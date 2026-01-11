"""
Page d'Inscription - Register
Design moderne et élégant avec Reflex
"""

import reflex as rx
from ..state.auth_state import AuthState
from ..styles.design_system import Colors, Typography, Spacing, Borders, Shadows


def password_strength_indicator() -> rx.Component:
    """Indicateur de force du mot de passe."""
    return rx.cond(
        AuthState.register_password != "",
        rx.vstack(
            rx.hstack(
                rx.text(
                    "Force du mot de passe:",
                    font_size=Typography.SIZE_XS,
                    color=Colors.GRAY_500,
                ),
                spacing="2",
            ),
            rx.hstack(
                # Au moins 8 caractères
                rx.hstack(
                    rx.cond(
                        AuthState.register_password.length() >= 8,
                        rx.icon("check", size=12, color=Colors.SUCCESS),
                        rx.icon("x", size=12, color=Colors.GRAY_400),
                    ),
                    rx.text("8+ caractères", font_size="11px"),
                    spacing="1",
                    color=rx.cond(
                        AuthState.register_password.length() >= 8,
                        Colors.SUCCESS,
                        Colors.GRAY_400,
                    ),
                ),
                # Une majuscule
                rx.hstack(
                    rx.cond(
                        AuthState.register_password.contains("A") | 
                        AuthState.register_password.contains("B") |
                        AuthState.register_password.contains("C") |
                        AuthState.register_password.contains("D") |
                        AuthState.register_password.contains("E") |
                        AuthState.register_password.contains("Z"),
                        rx.icon("check", size=12, color=Colors.SUCCESS),
                        rx.icon("x", size=12, color=Colors.GRAY_400),
                    ),
                    rx.text("Majuscule", font_size="11px"),
                    spacing="1",
                ),
                # Un chiffre
                rx.hstack(
                    rx.cond(
                        AuthState.register_password.contains("0") |
                        AuthState.register_password.contains("1") |
                        AuthState.register_password.contains("2") |
                        AuthState.register_password.contains("3") |
                        AuthState.register_password.contains("4") |
                        AuthState.register_password.contains("5") |
                        AuthState.register_password.contains("6") |
                        AuthState.register_password.contains("7") |
                        AuthState.register_password.contains("8") |
                        AuthState.register_password.contains("9"),
                        rx.icon("check", size=12, color=Colors.SUCCESS),
                        rx.icon("x", size=12, color=Colors.GRAY_400),
                    ),
                    rx.text("Chiffre", font_size="11px"),
                    spacing="1",
                ),
                spacing="4",
                flex_wrap="wrap",
            ),
            spacing="1",
            width="100%",
            padding="0.5rem",
            background=Colors.GRAY_50,
            border_radius=Borders.RADIUS_MD,
        ),
        rx.box(),
    )


def register_card() -> rx.Component:
    """Carte d'inscription principale."""
    return rx.box(
        rx.vstack(
            # Logo et titre
            rx.vstack(
                rx.hstack(
                    rx.icon("zap", size=32, color=Colors.PRIMARY),
                    rx.text(
                        "SimuPrime",
                        font_size="1.75rem",
                        font_weight="700",
                        color=Colors.PRIMARY,
                    ),
                    spacing="2",
                    align="center",
                ),
                rx.text(
                    "Créer votre compte",
                    font_size=Typography.SIZE_LG,
                    color=Colors.GRAY_600,
                    font_weight="500",
                ),
                rx.text(
                    "Rejoignez SimuPrime pour calculer vos primes CEE",
                    font_size=Typography.SIZE_SM,
                    color=Colors.GRAY_400,
                    text_align="center",
                ),
                spacing="2",
                align="center",
                margin_bottom="1.5rem",
            ),
            
            # Message d'erreur
            rx.cond(
                AuthState.error_message != "",
                rx.box(
                    rx.hstack(
                        rx.icon("alert-circle", size=18, color="#dc2626"),
                        rx.text(
                            AuthState.error_message,
                            font_size=Typography.SIZE_SM,
                            color="#dc2626",
                        ),
                        spacing="2",
                        align="start",
                    ),
                    padding="0.75rem 1rem",
                    background="#fef2f2",
                    border=f"1px solid #fecaca",
                    border_radius=Borders.RADIUS_MD,
                    width="100%",
                    margin_bottom="1rem",
                ),
                rx.box(),
            ),
            
            # Message de succès
            rx.cond(
                AuthState.success_message != "",
                rx.box(
                    rx.hstack(
                        rx.icon("check-circle", size=18, color=Colors.SUCCESS),
                        rx.text(
                            AuthState.success_message,
                            font_size=Typography.SIZE_SM,
                            color=Colors.SUCCESS,
                        ),
                        spacing="2",
                        align="start",
                    ),
                    padding="0.75rem 1rem",
                    background=Colors.SUCCESS_LIGHT,
                    border=f"1px solid {Colors.SUCCESS}30",
                    border_radius=Borders.RADIUS_MD,
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
                            font_size=Typography.SIZE_SM,
                            font_weight="500",
                            color=Colors.GRAY_700,
                        ),
                        rx.box(
                            rx.hstack(
                                rx.icon("user", size=18, color=Colors.GRAY_400),
                                rx.input(
                                    placeholder="Jean Dupont",
                                    value=AuthState.register_full_name,
                                    on_change=AuthState.set_register_full_name,
                                    width="100%",
                                    border="none",
                                    outline="none",
                                    background="transparent",
                                    font_size=Typography.SIZE_BASE,
                                    _focus={"outline": "none"},
                                ),
                                spacing="3",
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
                                    value=AuthState.register_email,
                                    on_change=AuthState.set_register_email,
                                    width="100%",
                                    border="none",
                                    outline="none",
                                    background="transparent",
                                    font_size=Typography.SIZE_BASE,
                                    _focus={"outline": "none"},
                                ),
                                spacing="3",
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
                        rx.text(
                            "Mot de passe",
                            font_size=Typography.SIZE_SM,
                            font_weight="500",
                            color=Colors.GRAY_700,
                        ),
                        rx.box(
                            rx.hstack(
                                rx.icon("lock", size=18, color=Colors.GRAY_400),
                                rx.input(
                                    placeholder="••••••••",
                                    type=rx.cond(AuthState.show_register_password, "text", "password"),
                                    value=AuthState.register_password,
                                    on_change=AuthState.set_register_password,
                                    width="100%",
                                    border="none",
                                    outline="none",
                                    background="transparent",
                                    font_size=Typography.SIZE_BASE,
                                    _focus={"outline": "none"},
                                ),
                                rx.icon_button(
                                    rx.cond(
                                        AuthState.show_register_password,
                                        rx.icon("eye-off", size=18),
                                        rx.icon("eye", size=18),
                                    ),
                                    variant="ghost",
                                    size="1",
                                    cursor="pointer",
                                    on_click=AuthState.toggle_register_password,
                                    color=Colors.GRAY_400,
                                ),
                                spacing="3",
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
                        rx.text(
                            "Minimum 8 caractères, 1 majuscule, 1 chiffre",
                            font_size="11px",
                            color=Colors.GRAY_400,
                            margin_top="0.25rem",
                        ),
                        spacing="1",
                        width="100%",
                    ),
                    
                    # Confirmation mot de passe
                    rx.vstack(
                        rx.text(
                            "Confirmer le mot de passe",
                            font_size=Typography.SIZE_SM,
                            font_weight="500",
                            color=Colors.GRAY_700,
                        ),
                        rx.box(
                            rx.hstack(
                                rx.icon("lock", size=18, color=Colors.GRAY_400),
                                rx.input(
                                    placeholder="••••••••",
                                    type=rx.cond(AuthState.show_register_password, "text", "password"),
                                    value=AuthState.register_password_confirm,
                                    on_change=AuthState.set_register_password_confirm,
                                    width="100%",
                                    border="none",
                                    outline="none",
                                    background="transparent",
                                    font_size=Typography.SIZE_BASE,
                                    _focus={"outline": "none"},
                                ),
                                rx.cond(
                                    (AuthState.register_password_confirm != "") & 
                                    (AuthState.register_password == AuthState.register_password_confirm),
                                    rx.icon("check-circle", size=18, color=Colors.SUCCESS),
                                    rx.box(width="18px"),
                                ),
                                spacing="3",
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
                    
                    # CGU
                    rx.hstack(
                        rx.checkbox(
                            checked=AuthState.register_accept_terms,
                            on_change=AuthState.set_register_accept_terms,
                            color_scheme="teal",
                        ),
                        rx.text(
                            rx.fragment(
                                "J'accepte les ",
                                rx.link(
                                    "conditions d'utilisation",
                                    href="/terms",
                                    color=Colors.PRIMARY,
                                    text_decoration="underline",
                                ),
                                " et la ",
                                rx.link(
                                    "politique de confidentialité",
                                    href="/privacy",
                                    color=Colors.PRIMARY,
                                    text_decoration="underline",
                                ),
                            ),
                            font_size=Typography.SIZE_SM,
                            color=Colors.GRAY_600,
                        ),
                        spacing="2",
                        align="start",
                        width="100%",
                    ),
                    
                    # Bouton d'inscription
                    rx.button(
                        rx.cond(
                            AuthState.is_loading,
                            rx.hstack(
                                rx.spinner(size="1"),
                                rx.text("Inscription en cours..."),
                                spacing="2",
                            ),
                            rx.hstack(
                                rx.text("Créer mon compte"),
                                rx.icon("user-plus", size=18),
                                spacing="2",
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
                            },
                            "transition": "all 0.2s ease",
                        },
                        margin_top="0.5rem",
                    ),
                    
                    spacing="4",
                    width="100%",
                ),
                on_submit=AuthState.handle_register,
                width="100%",
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
            
            # Lien vers connexion
            rx.hstack(
                rx.text(
                    "Déjà un compte ?",
                    font_size=Typography.SIZE_SM,
                    color=Colors.GRAY_500,
                ),
                rx.link(
                    rx.hstack(
                        rx.text("Se connecter"),
                        rx.icon("log-in", size=16),
                        spacing="1",
                    ),
                    href="/login",
                    font_size=Typography.SIZE_SM,
                    font_weight="600",
                    color=Colors.PRIMARY,
                    _hover={"text_decoration": "underline"},
                ),
                spacing="2",
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
        max_width="450px",
    )


def register_page_content() -> rx.Component:
    """Contenu de la page d'inscription."""
    return rx.box(
        rx.vstack(
            register_card(),
            
            # Retour à l'accueil
            rx.link(
                rx.hstack(
                    rx.icon("arrow-left", size=16),
                    rx.text("Retour à l'accueil"),
                    spacing="2",
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
            "background": f"radial-gradient(circle at 80% 80%, {Colors.PRIMARY}10 0%, transparent 50%), radial-gradient(circle at 20% 20%, {Colors.PRIMARY}08 0%, transparent 50%)",
            "pointer_events": "none",
        },
    )


@rx.page(
    route="/register",
    title="Inscription - SimuPrime",
    on_load=AuthState.redirect_if_authenticated,
)
def register_page() -> rx.Component:
    """Page d'inscription."""
    return register_page_content()