"""Page Landing - Page d'accueil"""
import reflex as rx
from ..styles.design_system import Colors, Typography, Spacing, Borders, Shadows
from ..state import AuthState


def hero_section() -> rx.Component:
    return rx.box(
        rx.vstack(
            rx.text(
                "SimuPrime",
                font_size=Typography.SIZE_4XL,
                font_weight=Typography.WEIGHT_BOLD,
                color=Colors.WHITE,
            ),
            rx.text(
                "Simulateur de Primes CEE",
                font_size=Typography.SIZE_XL,
                color=Colors.WHITE,
                opacity="0.9",
            ),
            rx.text(
                "Calculez vos Certificats d'Économies d'Énergie en quelques clics",
                font_size=Typography.SIZE_LG,
                color=Colors.WHITE,
                opacity="0.8",
                text_align="center",
                max_width="600px",
            ),
            rx.hstack(
                rx.link(
                    rx.button(
                        "Commencer une simulation",
                        size="3",
                        style={
                            "background": Colors.WHITE,
                            "color": Colors.PRIMARY,
                            "padding": f"{Spacing.MD} {Spacing.XL}",
                            "font_weight": Typography.WEIGHT_SEMIBOLD,
                        },
                    ),
                    href="/simulation/date-department",
                ),
                rx.link(
                    rx.button(
                        "Se connecter",
                        size="3",
                        variant="outline",
                        style={
                            "border_color": Colors.WHITE,
                            "color": Colors.WHITE,
                            "padding": f"{Spacing.MD} {Spacing.XL}",
                        },
                    ),
                    href="/login",
                ),
                spacing="4",
            ),
            spacing="5",
            align="center",
            padding_y=Spacing.XXL,
        ),
        background=f"linear-gradient(135deg, {Colors.PRIMARY} 0%, {Colors.SECONDARY} 100%)",
        padding=Spacing.XXL,
        min_height="70vh",
        display="flex",
        align_items="center",
        justify_content="center",
    )


def feature_card(icon: str, title: str, description: str) -> rx.Component:
    return rx.box(
        rx.vstack(
            rx.box(
                rx.icon(icon, size=28, color=Colors.PRIMARY),
                padding=Spacing.MD,
                background=Colors.PRIMARY_LIGHTER,
                border_radius=Borders.RADIUS_FULL,
            ),
            rx.text(title, font_weight=Typography.WEIGHT_SEMIBOLD, font_size=Typography.SIZE_LG),
            rx.text(description, color=Colors.GRAY_500, text_align="center"),
            spacing="2",
            align="center",
        ),
        padding=Spacing.XL,
        background=Colors.WHITE,
        border_radius=Borders.RADIUS_XL,
        box_shadow=Shadows.CARD,
        flex="1",
        min_width="250px",
    )


def features_section() -> rx.Component:
    return rx.box(
        rx.vstack(
            rx.text("Pourquoi SimuPrime ?", font_size=Typography.SIZE_2XL, font_weight=Typography.WEIGHT_BOLD),
            rx.hstack(
                feature_card("zap", "Rapide", "Obtenez une estimation en moins de 5 minutes"),
                feature_card("shield-check", "Fiable", "Calculs basés sur les fiches CEE officielles"),
                feature_card("euro", "Gratuit", "Service entièrement gratuit et sans engagement"),
                feature_card("history", "Historique", "Retrouvez toutes vos simulations"),
                spacing="5",
                wrap="wrap",
                justify="center",
            ),
            spacing="6",
            align="center",
            width="100%",
            max_width="1200px",
        ),
        padding=Spacing.XXL,
        background=Colors.GRAY_50,
        display="flex",
        justify_content="center",
    )


def sectors_section() -> rx.Component:
    sectors = ["Résidentiel", "Tertiaire", "Industrie", "Agriculture", "Transport", "Réseaux"]
    return rx.box(
        rx.vstack(
            rx.text("Tous les secteurs couverts", font_size=Typography.SIZE_2XL, font_weight=Typography.WEIGHT_BOLD),
            rx.hstack(
                *[
                    rx.box(
                        rx.text(s, font_weight=Typography.WEIGHT_MEDIUM),
                        padding=f"{Spacing.SM} {Spacing.LG}",
                        background=Colors.PRIMARY_LIGHTER,
                        border_radius=Borders.RADIUS_FULL,
                        color=Colors.PRIMARY,
                    )
                    for s in sectors
                ],
                spacing="3",
                wrap="wrap",
                justify="center",
            ),
            spacing="5",
            align="center",
        ),
        padding=Spacing.XXL,
    )


def cta_section() -> rx.Component:
    return rx.box(
        rx.vstack(
            rx.text("Prêt à calculer vos primes ?", font_size=Typography.SIZE_2XL, font_weight=Typography.WEIGHT_BOLD, color=Colors.WHITE),
            rx.link(
                rx.button(
                    "Démarrer maintenant",
                    size="3",
                    style={"background": Colors.WHITE, "color": Colors.PRIMARY, "padding": f"{Spacing.MD} {Spacing.XL}"},
                ),
                href="/simulation/date-department",
            ),
            spacing="5",
            align="center",
        ),
        background=Colors.PRIMARY,
        padding=Spacing.XXL,
        text_align="center",
    )


def footer_section() -> rx.Component:
    return rx.box(
        rx.hstack(
            rx.text("© 2024 SimuPrime", color=Colors.GRAY_500),
            rx.spacer(),
            rx.hstack(
                rx.link("Mentions légales", href="#", color=Colors.GRAY_500),
                rx.link("Contact", href="#", color=Colors.GRAY_500),
                spacing="5",
            ),
            width="100%",
            max_width="1200px",
        ),
        padding=Spacing.XL,
        border_top=f"1px solid {Colors.GRAY_200}",
        display="flex",
        justify_content="center",
    )


def landing_page() -> rx.Component:
    return rx.box(
        hero_section(),
        features_section(),
        sectors_section(),
        cta_section(),
        footer_section(),
        min_height="100vh",
    )