"""
Landing Page - Design moderne et épuré
RDE Consulting - Simulateur CEE
Adapte le contenu selon l'état de connexion de l'utilisateur
"""
import reflex as rx
from ..state.auth_state import AuthState
from ..state.simulation_state import SimulationState
from ..styles.design_system import Colors, Typography, Spacing, Borders, Shadows


# ============================================
# HERO SECTION - Pleine page avec image de fond
# ============================================

def hero_buttons_logged_out() -> rx.Component:
    """Boutons CTA pour utilisateur non connecté."""
    return rx.hstack(
        rx.link(
            rx.button(
                "Commencer une simulation",
                size="4",
                style={
                    "background": "white",
                    "color": Colors.PRIMARY,
                    "font_weight": "600",
                    "padding": "1.5rem 2rem",
                    "border": "2px solid white",
                    "border_radius": "12px",
                    "cursor": "pointer",
                    "transition": "all 0.3s ease",
                    "_hover": {
                        "transform": "translateY(-2px)",
                        "box_shadow": "0 10px 40px rgba(0,0,0,0.2)",
                    },
                },
            ),
            href="/simulation/date-department",
        ),
        rx.link(
            rx.button(
                "Se connecter",
                size="4",
                style={
                    "border": "2px solid rgba(255,255,255,0.9)",
                    "color": "white",
                    "font_weight": "600",
                    "padding": "1.5rem 2rem",
                    "border_radius": "12px",
                    "background": "rgba(255,255,255,0.1)",
                    "cursor": "pointer",
                    "transition": "all 0.3s ease",
                    "_hover": {
                        "background": "rgba(255,255,255,0.2)",
                        "border_color": "white",
                    },
                },
            ),
            href="/login",
        ),
        spacing="4",
        margin_top="2.5rem",
        flex_wrap="wrap",
        justify="center",
    )


def hero_buttons_logged_in() -> rx.Component:
    """Boutons CTA pour utilisateur connecté."""
    return rx.hstack(
        rx.link(
            rx.button(
                rx.hstack(
                    rx.icon("layout-dashboard", size=20),
                    rx.text("Accéder au tableau de bord"),
                    spacing="2",
                    align="center",
                ),
                size="4",
                style={
                    "background": "white",
                    "color": Colors.PRIMARY,
                    "font_weight": "600",
                    "padding": "1.5rem 2rem",
                    "border": "2px solid white",
                    "border_radius": "12px",
                    "cursor": "pointer",
                    "transition": "all 0.3s ease",
                    "_hover": {
                        "transform": "translateY(-2px)",
                        "box_shadow": "0 10px 40px rgba(0,0,0,0.2)",
                    },
                },
            ),
            href="/dashboard",
        ),
        rx.button(
            rx.hstack(
                rx.icon("plus", size=20),
                rx.text("Nouvelle simulation"),
                spacing="2",
                align="center",
            ),
            size="4",
            on_click=SimulationState.start_new_simulation,
            style={
                "border": "2px solid rgba(255,255,255,0.9)",
                "color": "white",
                "font_weight": "600",
                "padding": "1.5rem 2rem",
                "border_radius": "12px",
                "background": "rgba(255,255,255,0.1)",
                "cursor": "pointer",
                "transition": "all 0.3s ease",
                "_hover": {
                    "background": "rgba(255,255,255,0.2)",
                    "border_color": "white",
                },
            },
        ),
        spacing="4",
        margin_top="2.5rem",
        flex_wrap="wrap",
        justify="center",
    )


def user_welcome_badge() -> rx.Component:
    """Badge de bienvenue pour l'utilisateur connecté."""
    return rx.hstack(
        rx.box(
            rx.text(
                AuthState.initials,
                font_size="0.9rem",
                font_weight="600",
                color=Colors.PRIMARY,
            ),
            width="36px",
            height="36px",
            display="flex",
            align_items="center",
            justify_content="center",
            background="white",
            border_radius="50%",
            border=f"2px solid {Colors.PRIMARY}",
        ),
        rx.vstack(
            rx.text(
                "Bienvenue,",
                font_size="0.75rem",
                color="rgba(255,255,255,0.9)",
                line_height="1",
            ),
            rx.text(
                AuthState.display_name,
                font_size="0.95rem",
                font_weight="600",
                color="white",
                line_height="1.2",
            ),
            spacing="0",
            align="start",
        ),
        spacing="2",
        align="center",
        padding="0.5rem 1rem",
        background="rgba(0,0,0,0.4)",
        border_radius="100px",
        border="1px solid rgba(255,255,255,0.5)",
        backdrop_filter="blur(10px)",
    )


def hero_header_logged_out() -> rx.Component:
    """Header du hero pour utilisateur non connecté."""
    return rx.box(
        rx.image(
            src="/logo_rde_transparent.jpg",
            height="120px",
            object_fit="contain",
        ),
        position="absolute",
        top="2rem",
        left="2rem",
        z_index="10",
    )


def hero_header_logged_in() -> rx.Component:
    """Header du hero pour utilisateur connecté."""
    return rx.hstack(
        rx.image(
            src="/logo_rde_transparent.jpg",
            height="100px",
            object_fit="contain",
        ),
        rx.spacer(),
        user_welcome_badge(),
        position="absolute",
        top="2rem",
        left="2rem",
        right="2rem",
        z_index="10",
        align="center",
    )


def hero_section() -> rx.Component:
    """Section hero avec image de fond."""
    return rx.box(
        # Overlay semi-transparent
        rx.box(
            position="absolute",
            top="0",
            left="0",
            right="0",
            bottom="0",
            background="linear-gradient(135deg, rgba(45, 155, 109, 0.2) 0%, rgba(30, 123, 154, 0.2) 100%)",
            z_index="1",
        ),
        
        # Header conditionnel
        rx.cond(
            AuthState.is_authenticated,
            hero_header_logged_in(),
            hero_header_logged_out(),
        ),
        
        # Contenu centré
        rx.box(
            rx.vstack(
                # Titre principal
                rx.text(
                    "Simulateur de Primes CEE",
                    font_size=["2.5rem", "3rem", "3.5rem", "4rem"],
                    font_weight="700",
                    color="white",
                    text_align="center",
                    line_height="1.1",
                    letter_spacing="-0.02em",
                ),
                
                # Sous-titre conditionnel
                rx.cond(
                    AuthState.is_authenticated,
                    rx.text(
                        "Ravi de vous revoir ! Accédez à vos simulations ou créez-en une nouvelle.",
                        font_size=["1rem", "1.1rem", "1.25rem"],
                        color="rgba(255, 255, 255, 0.95)",
                        text_align="center",
                        max_width="600px",
                        line_height="1.6",
                        margin_top="1rem",
                    ),
                    rx.text(
                        "Estimez vos Certificats d'Économies d'Énergie en quelques clics",
                        font_size=["1rem", "1.1rem", "1.25rem"],
                        color="rgba(255, 255, 255, 0.95)",
                        text_align="center",
                        max_width="600px",
                        line_height="1.6",
                        margin_top="1rem",
                    ),
                ),
                
                # Boutons CTA conditionnels
                rx.cond(
                    AuthState.is_authenticated,
                    hero_buttons_logged_in(),
                    hero_buttons_logged_out(),
                ),
                
                spacing="2",
                align="center",
                max_width="800px",
                padding_x="2rem",
            ),
            position="relative",
            z_index="2",
            display="flex",
            align_items="center",
            justify_content="center",
            min_height="100vh",
            width="100%",
        ),
        
        # Image de fond
        background_image="url('/hero_bg.jpg')",
        background_size="cover",
        background_position="center",
        background_repeat="no-repeat",
        position="relative",
        min_height="100vh",
        width="100%",
        overflow="hidden",
    )


# ============================================
# STATS SECTION - Chiffres clés
# ============================================

def stat_item(number: str, label: str) -> rx.Component:
    """Item de statistique."""
    return rx.vstack(
        rx.text(
            number,
            font_size=["2rem", "2.5rem", "3rem"],
            font_weight="700",
            color=Colors.PRIMARY,
            line_height="1",
        ),
        rx.text(
            label,
            font_size="0.95rem",
            color=Colors.GRAY_600,
            text_align="center",
        ),
        spacing="2",
        align="center",
    )


def stats_section() -> rx.Component:
    """Section des statistiques."""
    return rx.box(
        rx.hstack(
            stat_item("200+", "Fiches CEE disponibles"),
            rx.divider(orientation="vertical", height="60px", opacity="0.3"),
            stat_item("6", "Secteurs d'activité"),
            rx.divider(orientation="vertical", height="60px", opacity="0.3"),
            stat_item("100%", "Gratuit"),
            rx.divider(orientation="vertical", height="60px", opacity="0.3"),
            stat_item("5 min", "Pour une estimation"),
            spacing="8",
            justify="center",
            align="center",
            flex_wrap="wrap",
            width="100%",
            max_width="900px",
        ),
        padding_y="4rem",
        padding_x="2rem",
        display="flex",
        justify_content="center",
        background="white",
    )


# ============================================
# FEATURES SECTION - Avantages
# ============================================

def feature_card(icon: str, title: str, description: str) -> rx.Component:
    """Carte de fonctionnalité moderne."""
    return rx.box(
        rx.vstack(
            rx.box(
                rx.icon(icon, size=28, color=Colors.PRIMARY),
                width="60px",
                height="60px",
                display="flex",
                align_items="center",
                justify_content="center",
                background=f"{Colors.PRIMARY}10",
                border_radius="16px",
            ),
            rx.text(
                title,
                font_size="1.25rem",
                font_weight="600",
                color=Colors.GRAY_900,
                margin_top="1rem",
            ),
            rx.text(
                description,
                font_size="0.95rem",
                color=Colors.GRAY_600,
                text_align="center",
                line_height="1.6",
            ),
            spacing="2",
            align="center",
            padding="2rem",
        ),
        background="white",
        border_radius="20px",
        box_shadow="0 4px 20px rgba(0,0,0,0.05)",
        border=f"1px solid {Colors.GRAY_100}",
        transition="all 0.3s ease",
        _hover={
            "transform": "translateY(-5px)",
            "box_shadow": "0 12px 40px rgba(0,0,0,0.1)",
        },
        flex="1",
        min_width="250px",
        max_width="300px",
    )


def features_section() -> rx.Component:
    """Section des fonctionnalités."""
    return rx.box(
        rx.vstack(
            rx.text(
                "Pourquoi utiliser notre simulateur ?",
                font_size=["1.75rem", "2rem", "2.25rem"],
                font_weight="700",
                color=Colors.GRAY_900,
                text_align="center",
            ),
            rx.text(
                "Un outil simple et efficace pour estimer vos primes CEE",
                font_size="1.1rem",
                color=Colors.GRAY_600,
                text_align="center",
                max_width="500px",
            ),
            rx.hstack(
                feature_card(
                    "zap",
                    "Rapide",
                    "Obtenez une estimation précise en moins de 5 minutes"
                ),
                feature_card(
                    "shield-check",
                    "Fiable",
                    "Calculs basés sur les fiches CEE officielles du ministère"
                ),
                feature_card(
                    "history",
                    "Historique",
                    "Retrouvez et exportez toutes vos simulations en PDF"
                ),
                spacing="6",
                justify="center",
                flex_wrap="wrap",
                margin_top="3rem",
                width="100%",
            ),
            spacing="4",
            align="center",
            width="100%",
            max_width="1100px",
        ),
        padding_y="5rem",
        padding_x="2rem",
        display="flex",
        justify_content="center",
        background=Colors.GRAY_50,
    )


# ============================================
# SECTORS SECTION - Secteurs couverts
# ============================================

def sector_badge(name: str, icon: str) -> rx.Component:
    """Badge de secteur."""
    return rx.hstack(
        rx.icon(icon, size=18, color=Colors.PRIMARY),
        rx.text(
            name,
            font_weight="500",
            color=Colors.GRAY_700,
        ),
        spacing="2",
        align="center",
        padding="0.75rem 1.25rem",
        background="white",
        border_radius="100px",
        box_shadow="0 2px 10px rgba(0,0,0,0.05)",
        border=f"1px solid {Colors.GRAY_100}",
        transition="all 0.2s ease",
        _hover={
            "transform": "scale(1.05)",
            "box_shadow": "0 4px 15px rgba(0,0,0,0.1)",
        },
    )


def sectors_section() -> rx.Component:
    """Section des secteurs."""
    return rx.box(
        rx.vstack(
            rx.text(
                "Tous les secteurs couverts",
                font_size=["1.75rem", "2rem"],
                font_weight="700",
                color=Colors.GRAY_900,
                text_align="center",
            ),
            rx.hstack(
                sector_badge("Résidentiel", "home"),
                sector_badge("Tertiaire", "building-2"),
                sector_badge("Industrie", "factory"),
                sector_badge("Agriculture", "wheat"),
                sector_badge("Transport", "truck"),
                sector_badge("Réseaux", "network"),
                spacing="3",
                justify="center",
                flex_wrap="wrap",
                margin_top="2rem",
            ),
            spacing="4",
            align="center",
        ),
        padding_y="4rem",
        padding_x="2rem",
        display="flex",
        justify_content="center",
        background="white",
    )


# ============================================
# HOW IT WORKS - Comment ça marche
# ============================================

def step_item(number: str, title: str, description: str) -> rx.Component:
    """Étape du processus."""
    return rx.vstack(
        rx.box(
            rx.text(
                number,
                font_size="1.5rem",
                font_weight="700",
                color="white",
            ),
            width="60px",
            height="60px",
            display="flex",
            align_items="center",
            justify_content="center",
            background=Colors.PRIMARY,
            border_radius="50%",
        ),
        rx.text(
            title,
            font_size="1.1rem",
            font_weight="600",
            color=Colors.GRAY_900,
            text_align="center",
            margin_top="1rem",
        ),
        rx.text(
            description,
            font_size="0.9rem",
            color=Colors.GRAY_600,
            line_height="1.5",
            text_align="center",
            max_width="280px",
        ),
        spacing="2",
        align="center",
        flex="1",
        min_width="200px",
    )


def step_connector() -> rx.Component:
    """Connecteur entre les étapes."""
    return rx.box(
        rx.icon("chevron-right", size=24, color=Colors.GRAY_300),
        display=["none", "none", "flex", "flex"],
        align_items="center",
        padding_x="1rem",
    )


def how_it_works_section() -> rx.Component:
    """Section comment ça marche."""
    return rx.box(
        rx.vstack(
            rx.text(
                "Comment ça marche ?",
                font_size=["1.75rem", "2rem"],
                font_weight="700",
                color=Colors.GRAY_900,
                text_align="center",
            ),
            rx.text(
                "3 étapes simples pour estimer votre prime",
                font_size="1.1rem",
                color=Colors.GRAY_600,
                text_align="center",
            ),
            rx.hstack(
                step_item(
                    "1",
                    "Sélectionnez votre opération",
                    "Choisissez le secteur, la typologie et la fiche CEE correspondante"
                ),
                step_connector(),
                step_item(
                    "2",
                    "Renseignez les paramètres",
                    "Complétez les informations techniques de votre projet"
                ),
                step_connector(),
                step_item(
                    "3",
                    "Obtenez votre estimation",
                    "Visualisez et exportez le montant estimé de votre prime"
                ),
                spacing="4",
                justify="center",
                align="center",
                margin_top="3rem",
                width="100%",
                flex_wrap="wrap",
            ),
            spacing="4",
            align="center",
            width="100%",
            max_width="1100px",
        ),
        padding_y="5rem",
        padding_x="2rem",
        display="flex",
        justify_content="center",
        background=Colors.GRAY_50,
    )


# ============================================
# CTA SECTION - Appel à l'action
# ============================================

def cta_section() -> rx.Component:
    """Section appel à l'action - adapté selon connexion."""
    return rx.box(
        rx.vstack(
            rx.cond(
                AuthState.is_authenticated,
                rx.text(
                    "Lancez une nouvelle simulation",
                    font_size=["1.75rem", "2rem", "2.5rem"],
                    font_weight="700",
                    color="white",
                    text_align="center",
                ),
                rx.text(
                    "Prêt à calculer vos primes ?",
                    font_size=["1.75rem", "2rem", "2.5rem"],
                    font_weight="700",
                    color="white",
                    text_align="center",
                ),
            ),
            rx.cond(
                AuthState.is_authenticated,
                rx.text(
                    "Vos simulations sont sauvegardées automatiquement",
                    font_size="1.1rem",
                    color="rgba(255,255,255,0.85)",
                    text_align="center",
                ),
                rx.text(
                    "Commencez gratuitement dès maintenant",
                    font_size="1.1rem",
                    color="rgba(255,255,255,0.85)",
                    text_align="center",
                ),
            ),
            rx.cond(
                AuthState.is_authenticated,
                # Utilisateur connecté
                rx.hstack(
                    rx.button(
                        rx.hstack(
                            rx.icon("plus", size=20),
                            rx.text("Nouvelle simulation"),
                            spacing="2",
                            align="center",
                        ),
                        size="4",
                        on_click=SimulationState.start_new_simulation,
                        style={
                            "background": "white",
                            "color": Colors.PRIMARY,
                            "font_weight": "600",
                            "padding": "1.5rem 2.5rem",
                            "border_radius": "12px",
                            "cursor": "pointer",
                            "transition": "all 0.3s ease",
                            "_hover": {
                                "transform": "translateY(-2px)",
                                "box_shadow": "0 10px 40px rgba(0,0,0,0.2)",
                            },
                        },
                    ),
                    rx.link(
                        rx.button(
                            rx.hstack(
                                rx.icon("file-search", size=20),
                                rx.text("Consulter les fiches"),
                                spacing="2",
                                align="center",
                            ),
                            size="4",
                            style={
                                "border": "2px solid rgba(255,255,255,0.9)",
                                "color": "white",
                                "font_weight": "600",
                                "padding": "1.5rem 2rem",
                                "border_radius": "12px",
                                "background": "rgba(255,255,255,0.1)",
                                "cursor": "pointer",
                                "transition": "all 0.3s ease",
                                "_hover": {
                                    "background": "rgba(255,255,255,0.2)",
                                },
                            },
                        ),
                        href="/fiches",
                    ),
                    spacing="4",
                    flex_wrap="wrap",
                    justify="center",
                ),
                # Utilisateur non connecté
                rx.link(
                    rx.button(
                        rx.hstack(
                            rx.text("Démarrer une simulation"),
                            rx.icon("arrow-right", size=20),
                            spacing="2",
                            align="center",
                        ),
                        size="4",
                        style={
                            "background": "white",
                            "color": Colors.PRIMARY,
                            "font_weight": "600",
                            "padding": "1.5rem 2.5rem",
                            "border_radius": "12px",
                            "cursor": "pointer",
                            "transition": "all 0.3s ease",
                            "_hover": {
                                "transform": "translateY(-2px)",
                                "box_shadow": "0 10px 40px rgba(0,0,0,0.2)",
                            },
                        },
                    ),
                    href="/simulation/date-department",
                ),
            ),
            spacing="4",
            align="center",
        ),
        padding_y="5rem",
        padding_x="2rem",
        display="flex",
        justify_content="center",
        background=f"linear-gradient(135deg, {Colors.PRIMARY} 0%, {Colors.SECONDARY} 100%)",
    )


# ============================================
# CONTACT MODAL
# ============================================

def contact_modal() -> rx.Component:
    """Modal de contact."""
    return rx.dialog.root(
        rx.dialog.trigger(
            rx.link(
                "Contact",
                color=Colors.GRAY_500,
                font_size="0.85rem",
                cursor="pointer",
                _hover={"color": Colors.PRIMARY},
            ),
        ),
        rx.dialog.content(
            rx.dialog.title(
                rx.hstack(
                    rx.image(
                        src="/logo_rde.jpg",
                        height="50px",
                        border_radius="8px",
                    ),
                    rx.spacer(),
                    rx.dialog.close(
                        rx.icon_button(
                            rx.icon("x", size=18),
                            variant="ghost",
                            cursor="pointer",
                        ),
                    ),
                    width="100%",
                    align="center",
                ),
            ),
            rx.dialog.description(
                rx.vstack(
                    rx.text(
                        "Contactez-nous",
                        font_size="1.5rem",
                        font_weight="700",
                        color=Colors.GRAY_900,
                    ),
                    rx.text(
                        "Une question sur le simulateur CEE ou nos services de conseil en efficacité énergétique ? N'hésitez pas à nous écrire.",
                        font_size="0.95rem",
                        color=Colors.GRAY_600,
                        line_height="1.6",
                        text_align="center",
                    ),
                    
                    # Email
                    rx.box(
                        rx.vstack(
                            rx.hstack(
                                rx.box(
                                    rx.icon("mail", size=20, color=Colors.PRIMARY),
                                    padding="10px",
                                    background=f"{Colors.PRIMARY}10",
                                    border_radius="10px",
                                ),
                                rx.vstack(
                                    rx.text("Email", font_size="0.8rem", color=Colors.GRAY_500),
                                    rx.text("contact@rdeconsulting.fr", font_weight="500", color=Colors.GRAY_700),
                                    spacing="0",
                                    align="start",
                                ),
                                spacing="3",
                                align="center",
                            ),
                            spacing="2",
                            width="100%",
                        ),
                        padding="1rem",
                        background=Colors.GRAY_50,
                        border_radius="12px",
                        width="100%",
                    ),
                    
                    # Bouton mailto
                    rx.link(
                        rx.button(
                            rx.hstack(
                                rx.icon("send", size=18),
                                rx.text("Envoyer un email"),
                                spacing="2",
                                align="center",
                            ),
                            size="3",
                            width="100%",
                            cursor="pointer",
                            style={
                                "background": Colors.PRIMARY,
                                "color": "white",
                                "_hover": {
                                    "background": Colors.SECONDARY,
                                },
                            },
                        ),
                        href="mailto:contact@rdeconsulting.fr?subject=Contact%20via%20Simulateur%20CEE",
                        width="100%",
                    ),
                    
                    # Séparateur
                    rx.hstack(
                        rx.divider(width="100%"),
                        rx.text("ou", font_size="0.8rem", color=Colors.GRAY_400, white_space="nowrap", padding_x="1rem"),
                        rx.divider(width="100%"),
                        width="100%",
                        align="center",
                    ),
                    
                    # LinkedIn
                    rx.link(
                        rx.button(
                            rx.hstack(
                                rx.icon("linkedin", size=18),
                                rx.text("Suivez-nous sur LinkedIn"),
                                spacing="2",
                                align="center",
                            ),
                            variant="outline",
                            size="3",
                            width="100%",
                            cursor="pointer",
                        ),
                        href="https://www.linkedin.com/company/rde-consulting-france/",
                        is_external=True,
                        width="100%",
                    ),
                    
                    spacing="4",
                    align="center",
                    width="100%",
                    padding_top="1rem",
                ),
            ),
            style={
                "max_width": "400px",
                "padding": "1.5rem",
            },
        ),
    )


# ============================================
# FOOTER
# ============================================

def footer_section() -> rx.Component:
    """Footer moderne - adapté selon connexion."""
    return rx.box(
        rx.hstack(
            rx.image(
                src="/logo_rde.jpg",
                height="40px",
                border_radius="4px",
            ),
            rx.spacer(),
            rx.hstack(
                # Lien conditionnel Dashboard/Connexion
                rx.cond(
                    AuthState.is_authenticated,
                    rx.link(
                        "Mon tableau de bord",
                        href="/dashboard",
                        color=Colors.GRAY_500,
                        font_size="0.85rem",
                        _hover={"color": Colors.PRIMARY},
                    ),
                    rx.link(
                        "Connexion",
                        href="/login",
                        color=Colors.GRAY_500,
                        font_size="0.85rem",
                        _hover={"color": Colors.PRIMARY},
                    ),
                ),
                rx.link(
                    "Mentions légales",
                    href="/mentions-legales",
                    color=Colors.GRAY_500,
                    font_size="0.85rem",
                    _hover={"color": Colors.PRIMARY},
                ),
                contact_modal(),
                spacing="5",
                align="center",
            ),
            rx.spacer(),
            rx.text(
                "© 2026 RDE Consulting",
                font_size="0.8rem",
                color=Colors.GRAY_400,
            ),
            width="100%",
            max_width="1100px",
            align="center",
        ),
        padding_y="1rem",
        padding_x="2rem",
        display="flex",
        justify_content="center",
        background="white",
        border_top=f"1px solid {Colors.GRAY_100}",
    )


# ============================================
# PAGE PRINCIPALE
# ============================================

def landing_page() -> rx.Component:
    """Page d'accueil complète."""
    return rx.box(
        hero_section(),
        stats_section(),
        features_section(),
        sectors_section(),
        how_it_works_section(),
        cta_section(),
        footer_section(),
        min_height="100vh",
        background="white",
    )