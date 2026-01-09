"""
Landing Page
Modern landing page with hero section and call-to-action buttons
"""

import reflex as rx
from state.auth_state import AuthState
from styles.design_system import Colors, Typography, Spacing, Borders, Shadows


def hero_section() -> rx.Component:
    """Hero section with main CTA"""
    return rx.box(
        rx.box(
            rx.vstack(
                # Logo/Brand
                rx.hstack(
                    rx.icon("calculator", size=40, color="white"),
                    rx.text(
                        "SimuPrime",
                        font_size="2rem",
                        font_weight="700",
                        color="white",
                        letter_spacing="-0.02em",
                    ),
                    spacing="3",
                    align="center",
                ),
                
                # Main headline
                rx.heading(
                    "Calculez vos primes CEE",
                    rx.text(" en quelques clics", as_="span", color=Colors.ACCENT_LIGHT),
                    font_size=["2.5rem", "3rem", "3.5rem"],
                    font_weight="800",
                    color="white",
                    text_align="center",
                    line_height="1.1",
                    max_width="800px",
                    margin_top="3rem",
                ),
                
                # Subtitle
                rx.text(
                    "Simulez rapidement le montant de vos Certificats d'Économies d'Énergie pour tous vos projets de rénovation énergétique.",
                    font_size=["1rem", "1.125rem", "1.25rem"],
                    color="rgba(255, 255, 255, 0.9)",
                    text_align="center",
                    max_width="600px",
                    margin_top="1.5rem",
                    line_height="1.6",
                ),
                
                # CTA Buttons
                rx.hstack(
                    rx.link(
                        rx.button(
                            rx.hstack(
                                rx.text("Commencer une simulation"),
                                rx.icon("arrow-right", size=18),
                                spacing="2",
                                align="center",
                            ),
                            size="4",
                            background="white",
                            color=Colors.PRIMARY,
                            font_weight="600",
                            padding="1.5rem 2rem",
                            border_radius=Borders.RADIUS_LG,
                            cursor="pointer",
                            _hover={
                                "transform": "translateY(-2px)",
                                "box_shadow": "0 10px 30px rgba(0,0,0,0.2)",
                            },
                            transition="all 0.2s ease",
                        ),
                        href="/login",
                    ),
                    rx.link(
                        rx.button(
                            "Se connecter",
                            size="4",
                            variant="outline",
                            color="white",
                            border_color="rgba(255,255,255,0.5)",
                            font_weight="600",
                            padding="1.5rem 2rem",
                            border_radius=Borders.RADIUS_LG,
                            cursor="pointer",
                            _hover={
                                "background": "rgba(255,255,255,0.1)",
                                "border_color": "white",
                            },
                            transition="all 0.2s ease",
                        ),
                        href="/login",
                    ),
                    spacing="4",
                    margin_top="2.5rem",
                    flex_wrap="wrap",
                    justify="center",
                ),
                
                spacing="0",
                align="center",
                width="100%",
                padding=["2rem", "3rem", "4rem"],
            ),
            
            # Gradient overlay
            position="relative",
            z_index="1",
        ),
        
        # Background with gradient
        background=f"linear-gradient(135deg, {Colors.PRIMARY} 0%, {Colors.SECONDARY} 100%)",
        min_height="100vh",
        display="flex",
        align_items="center",
        justify_content="center",
        position="relative",
        overflow="hidden",
        
        # Decorative elements
        _before={
            "content": '""',
            "position": "absolute",
            "top": "-50%",
            "right": "-20%",
            "width": "80%",
            "height": "150%",
            "background": "radial-gradient(circle, rgba(255,255,255,0.1) 0%, transparent 70%)",
            "pointer_events": "none",
        },
    )


def features_section() -> rx.Component:
    """Features section showing key benefits"""
    features = [
        {
            "icon": "zap",
            "title": "Rapide",
            "description": "Obtenez une estimation en moins de 2 minutes grâce à notre simulateur optimisé."
        },
        {
            "icon": "shield-check",
            "title": "Fiable",
            "description": "Calculs basés sur les fiches officielles CEE constamment mises à jour."
        },
        {
            "icon": "history",
            "title": "Historique",
            "description": "Retrouvez toutes vos simulations sauvegardées dans votre espace personnel."
        },
        {
            "icon": "building-2",
            "title": "Multi-secteurs",
            "description": "Résidentiel, tertiaire, industrie, agriculture... tous les secteurs couverts."
        },
    ]
    
    return rx.box(
        rx.vstack(
            rx.text(
                "Pourquoi SimuPrime ?",
                font_size="0.875rem",
                font_weight="600",
                color=Colors.PRIMARY,
                text_transform="uppercase",
                letter_spacing="0.1em",
            ),
            rx.heading(
                "Tout ce dont vous avez besoin",
                font_size=["1.75rem", "2rem", "2.5rem"],
                font_weight="700",
                color=Colors.TEXT_PRIMARY,
                text_align="center",
            ),
            rx.text(
                "Un outil complet pour calculer et suivre vos primes CEE",
                font_size="1.125rem",
                color=Colors.TEXT_SECONDARY,
                text_align="center",
                max_width="500px",
            ),
            
            rx.grid(
                *[
                    rx.box(
                        rx.vstack(
                            rx.box(
                                rx.icon(feature["icon"], size=24, color=Colors.PRIMARY),
                                padding="1rem",
                                background=f"{Colors.PRIMARY}10",
                                border_radius=Borders.RADIUS_LG,
                            ),
                            rx.text(
                                feature["title"],
                                font_size="1.125rem",
                                font_weight="600",
                                color=Colors.TEXT_PRIMARY,
                            ),
                            rx.text(
                                feature["description"],
                                font_size="0.9rem",
                                color=Colors.TEXT_SECONDARY,
                                text_align="center",
                                line_height="1.6",
                            ),
                            spacing="3",
                            align="center",
                            padding="1.5rem",
                        ),
                        background="white",
                        border_radius=Borders.RADIUS_XL,
                        border=f"1px solid {Colors.BORDER}",
                        _hover={
                            "box_shadow": Shadows.HOVER,
                            "transform": "translateY(-4px)",
                            "border_color": Colors.PRIMARY,
                        },
                        transition="all 0.3s ease",
                    )
                    for feature in features
                ],
                columns=["1", "2", "4"],
                spacing="5",
                width="100%",
                margin_top="3rem",
            ),
            
            spacing="4",
            align="center",
            width="100%",
            max_width="1200px",
            margin="0 auto",
            padding=["3rem 1.5rem", "4rem 2rem", "5rem 2rem"],
        ),
        background=Colors.BACKGROUND,
    )


def sectors_section() -> rx.Component:
    """Section showing supported sectors"""
    sectors = [
        {"icon": "house", "name": "Résidentiel", "color": "#10B981"},
        {"icon": "building-2", "name": "Tertiaire", "color": "#3B82F6"},
        {"icon": "factory", "name": "Industrie", "color": "#8B5CF6"},
        {"icon": "carrot", "name": "Agriculture", "color": "#F59E0B"},
        {"icon": "network", "name": "Réseaux", "color": "#EC4899"},
        {"icon": "bus", "name": "Transport", "color": "#6366F1"},
    ]
    
    return rx.box(
        rx.vstack(
            rx.heading(
                "Tous les secteurs d'activité",
                font_size=["1.75rem", "2rem"],
                font_weight="700",
                color="white",
                text_align="center",
            ),
            rx.text(
                "Quelle que soit votre activité, trouvez les fiches CEE adaptées",
                font_size="1rem",
                color="rgba(255,255,255,0.8)",
                text_align="center",
            ),
            
            rx.hstack(
                *[
                    rx.vstack(
                        rx.box(
                            rx.icon(sector["icon"], size=28, color=sector["color"]),
                            padding="1rem",
                            background="rgba(255,255,255,0.1)",
                            border_radius=Borders.RADIUS_FULL,
                            border=f"2px solid {sector['color']}40",
                        ),
                        rx.text(
                            sector["name"],
                            font_size="0.875rem",
                            font_weight="500",
                            color="white",
                        ),
                        spacing="2",
                        align="center",
                    )
                    for sector in sectors
                ],
                spacing="6",
                flex_wrap="wrap",
                justify="center",
                margin_top="2rem",
            ),
            
            spacing="4",
            align="center",
            width="100%",
            padding=["3rem 1.5rem", "4rem 2rem"],
        ),
        background=f"linear-gradient(135deg, {Colors.SECONDARY} 0%, {Colors.PRIMARY} 100%)",
    )


def cta_section() -> rx.Component:
    """Final call-to-action section"""
    return rx.box(
        rx.vstack(
            rx.heading(
                "Prêt à calculer vos primes ?",
                font_size=["1.75rem", "2rem", "2.5rem"],
                font_weight="700",
                color=Colors.TEXT_PRIMARY,
                text_align="center",
            ),
            rx.text(
                "Créez votre compte gratuitement et commencez dès maintenant",
                font_size="1.125rem",
                color=Colors.TEXT_SECONDARY,
                text_align="center",
            ),
            rx.hstack(
                rx.link(
                    rx.button(
                        rx.hstack(
                            rx.text("Créer un compte"),
                            rx.icon("user-plus", size=18),
                            spacing="2",
                            align="center",
                        ),
                        size="4",
                        background=Colors.PRIMARY,
                        color="white",
                        font_weight="600",
                        padding="1.25rem 2rem",
                        border_radius=Borders.RADIUS_LG,
                        cursor="pointer",
                        _hover={
                            "background": Colors.PRIMARY_DARK,
                            "transform": "translateY(-2px)",
                        },
                        transition="all 0.2s ease",
                    ),
                    href="/register",
                ),
                rx.link(
                    rx.button(
                        "Se connecter",
                        size="4",
                        variant="outline",
                        color=Colors.PRIMARY,
                        border_color=Colors.PRIMARY,
                        font_weight="600",
                        padding="1.25rem 2rem",
                        border_radius=Borders.RADIUS_LG,
                        cursor="pointer",
                        _hover={
                            "background": f"{Colors.PRIMARY}10",
                        },
                        transition="all 0.2s ease",
                    ),
                    href="/login",
                ),
                spacing="4",
                margin_top="2rem",
                flex_wrap="wrap",
                justify="center",
            ),
            spacing="4",
            align="center",
            width="100%",
            max_width="600px",
            margin="0 auto",
            padding=["4rem 1.5rem", "5rem 2rem"],
        ),
        background="white",
    )


def footer() -> rx.Component:
    """Footer section"""
    return rx.box(
        rx.hstack(
            rx.hstack(
                rx.icon("calculator", size=20, color=Colors.TEXT_MUTED),
                rx.text(
                    "SimuPrime",
                    font_weight="600",
                    color=Colors.TEXT_SECONDARY,
                ),
                spacing="2",
                align="center",
            ),
            rx.text(
                "© 2025 SimuPrime. Tous droits réservés.",
                font_size="0.875rem",
                color=Colors.TEXT_MUTED,
            ),
            justify="between",
            align="center",
            width="100%",
            max_width="1200px",
            margin="0 auto",
            padding="1.5rem 2rem",
            flex_wrap="wrap",
            gap="4",
        ),
        background=Colors.BACKGROUND,
        border_top=f"1px solid {Colors.BORDER}",
    )


def landing_page() -> rx.Component:
    """Main landing page component"""
    return rx.box(
        hero_section(),
        features_section(),
        sectors_section(),
        cta_section(),
        footer(),
        font_family=Typography.FONT_FAMILY,
    )


# Page route
@rx.page(route="/", title="SimuPrime - Simulateur de Primes CEE")
def index() -> rx.Component:
    return landing_page()
