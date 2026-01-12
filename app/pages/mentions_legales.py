"""
Page Mentions Légales - RDE Consulting
"""
import reflex as rx
from ..styles.design_system import Colors, Typography, Spacing, Borders, Shadows


def section_title(title: str) -> rx.Component:
    """Titre de section."""
    return rx.text(
        title,
        font_size="1.25rem",
        font_weight="600",
        color=Colors.GRAY_900,
        margin_top="2rem",
        margin_bottom="1rem",
    )


def paragraph(text: str) -> rx.Component:
    """Paragraphe de texte."""
    return rx.text(
        text,
        font_size="0.95rem",
        color=Colors.GRAY_600,
        line_height="1.7",
        margin_bottom="1rem",
    )


def mentions_legales_content() -> rx.Component:
    """Contenu des mentions légales."""
    return rx.box(
        rx.vstack(
            # Header
            rx.box(
                rx.vstack(
                    rx.text(
                        "Mentions Légales",
                        font_size="2.5rem",
                        font_weight="700",
                        color="white",
                    ),
                    rx.text(
                        "Informations légales et conditions d'utilisation",
                        font_size="1.1rem",
                        color="rgba(255,255,255,0.9)",
                    ),
                    spacing="2",
                    align="center",
                ),
                width="100%",
                padding_y="4rem",
                padding_x="2rem",
                background=f"linear-gradient(135deg, {Colors.PRIMARY} 0%, {Colors.SECONDARY} 100%)",
                text_align="center",
            ),
            
            # Contenu
            rx.box(
                rx.vstack(
                    # 1. Éditeur du site
                    section_title("1. Éditeur du site"),
                    paragraph(
                        "Le site RDE Simulateur CEE est édité par RDE Consulting, société spécialisée dans "
                        "le conseil en efficacité énergétique et l'accompagnement des entreprises dans leurs "
                        "démarches de Certificats d'Économies d'Énergie (CEE)."
                    ),
                    rx.box(
                        rx.vstack(
                            rx.text("RDE Consulting", font_weight="600", color=Colors.GRAY_700),
                            rx.text("Forme juridique : Société par actions simplifiée (SAS)", color=Colors.GRAY_600, font_size="0.9rem"),
                            rx.text("SIREN : 941 271 454", color=Colors.GRAY_600, font_size="0.9rem"),
                            rx.text("SIRET : 941 271 454 00014", color=Colors.GRAY_600, font_size="0.9rem"),
                            rx.text("N° TVA : FR38941271454", color=Colors.GRAY_600, font_size="0.9rem"),
                            rx.text("Date de création : 19 février 2025", color=Colors.GRAY_600, font_size="0.9rem"),
                            rx.text("Activité : Conseil pour les affaires et autres conseils de gestion (NAF 7022Z)", color=Colors.GRAY_600, font_size="0.9rem"),
                            rx.text("Email : contact@rdeconsulting.fr", color=Colors.GRAY_600, font_size="0.9rem"),
                            spacing="1",
                            align="start",
                        ),
                        padding="1rem",
                        background=Colors.GRAY_50,
                        border_radius="8px",
                        margin_bottom="1rem",
                    ),
                    
                    # 2. Hébergement
                    section_title("2. Hébergement"),
                    paragraph(
                        "Le site est hébergé par Railway, Inc., société basée aux États-Unis. "
                        "Les données sont stockées sur des serveurs sécurisés conformes aux normes en vigueur."
                    ),
                    
                    # 3. Objet du site
                    section_title("3. Objet du site"),
                    paragraph(
                        "Le simulateur CEE de RDE Consulting est un outil gratuit permettant d'estimer "
                        "le montant des primes liées aux Certificats d'Économies d'Énergie. Ce service est "
                        "proposé à titre informatif et ne constitue en aucun cas un engagement contractuel."
                    ),
                    paragraph(
                        "Les estimations fournies sont basées sur les fiches d'opérations standardisées "
                        "publiées par le Ministère de la Transition Écologique. Les montants réels peuvent "
                        "varier en fonction des conditions spécifiques de chaque projet et des évolutions "
                        "réglementaires."
                    ),
                    
                    # 4. Propriété intellectuelle
                    section_title("4. Propriété intellectuelle"),
                    paragraph(
                        "L'ensemble des éléments constituant ce site (textes, graphismes, logiciels, images, "
                        "logos, etc.) est la propriété exclusive de RDE Consulting ou de ses partenaires. "
                        "Toute reproduction, représentation, modification ou exploitation non autorisée est interdite."
                    ),
                    paragraph(
                        "Les fiches CEE et les méthodes de calcul sont basées sur les documents officiels "
                        "publiés par le Ministère de la Transition Écologique et sont utilisées conformément "
                        "à leur vocation d'information publique."
                    ),
                    
                    # 5. Protection des données personnelles
                    section_title("5. Protection des données personnelles"),
                    paragraph(
                        "Conformément au Règlement Général sur la Protection des Données (RGPD) et à la loi "
                        "Informatique et Libertés, vous disposez d'un droit d'accès, de rectification, de "
                        "suppression et de portabilité de vos données personnelles."
                    ),
                    rx.box(
                        rx.vstack(
                            rx.text("Données collectées :", font_weight="600", color=Colors.GRAY_700, font_size="0.9rem"),
                            rx.text("• Adresse email (pour la création de compte)", color=Colors.GRAY_600, font_size="0.9rem"),
                            rx.text("• Données de simulation (paramètres techniques des projets)", color=Colors.GRAY_600, font_size="0.9rem"),
                            rx.text("• Données de connexion (logs techniques)", color=Colors.GRAY_600, font_size="0.9rem"),
                            spacing="1",
                            align="start",
                        ),
                        padding="1rem",
                        background=Colors.GRAY_50,
                        border_radius="8px",
                        margin_y="1rem",
                    ),
                    paragraph(
                        "Vos données sont conservées de manière sécurisée et ne sont jamais transmises à des "
                        "tiers sans votre consentement explicite. Vous pouvez exercer vos droits en nous "
                        "contactant à l'adresse : contact@rdeconsulting.fr"
                    ),
                    
                    # 6. Cookies
                    section_title("6. Cookies"),
                    paragraph(
                        "Ce site utilise des cookies techniques nécessaires au bon fonctionnement du service. "
                        "Ces cookies permettent de maintenir votre session de connexion et de mémoriser vos "
                        "préférences. Aucun cookie publicitaire ou de tracking n'est utilisé."
                    ),
                    
                    # 7. Limitation de responsabilité
                    section_title("7. Limitation de responsabilité"),
                    paragraph(
                        "Les informations et estimations fournies par le simulateur sont données à titre "
                        "indicatif. RDE Consulting ne saurait être tenu responsable des décisions prises "
                        "sur la base de ces estimations."
                    ),
                    paragraph(
                        "Les montants définitifs des primes CEE dépendent de nombreux facteurs incluant "
                        "la vérification des travaux, la conformité aux critères d'éligibilité, et les "
                        "conditions du marché au moment de la valorisation. Nous vous recommandons de "
                        "consulter un professionnel pour tout projet d'envergure."
                    ),
                    
                    # 8. Droit applicable
                    section_title("8. Droit applicable"),
                    paragraph(
                        "Les présentes mentions légales sont soumises au droit français. En cas de litige, "
                        "les tribunaux français seront seuls compétents."
                    ),
                    
                    # 9. Contact
                    section_title("9. Contact"),
                    paragraph(
                        "Pour toute question concernant ces mentions légales ou l'utilisation du site, "
                        "vous pouvez nous contacter :"
                    ),
                    rx.box(
                        rx.hstack(
                            rx.icon("mail", size=18, color=Colors.PRIMARY),
                            rx.link(
                                "contact@rdeconsulting.fr",
                                href="mailto:contact@rdeconsulting.fr",
                                color=Colors.GRAY_700,
                                _hover={"color": Colors.PRIMARY},
                            ),
                            spacing="2",
                            align="center",
                        ),
                        padding="1rem",
                        background=Colors.GRAY_50,
                        border_radius="8px",
                        margin_y="1rem",
                    ),
                    
                    # Date de mise à jour
                    rx.text(
                        "Dernière mise à jour : Janvier 2026",
                        font_size="0.85rem",
                        color=Colors.GRAY_400,
                        margin_top="3rem",
                        font_style="italic",
                    ),
                    
                    spacing="0",
                    align="start",
                    width="100%",
                ),
                max_width="800px",
                width="100%",
                padding_y="3rem",
                padding_x="2rem",
            ),
            
            # Bouton retour
            rx.link(
                rx.button(
                    rx.hstack(
                        rx.icon("arrow-left", size=18),
                        rx.text("Retour à l'accueil"),
                        spacing="2",
                        align="center",
                    ),
                    variant="outline",
                    size="3",
                    cursor="pointer",
                ),
                href="/",
                margin_bottom="3rem",
            ),
            
            spacing="0",
            align="center",
            width="100%",
        ),
        min_height="100vh",
        background="white",
    )


@rx.page(route="/mentions-legales", title="Mentions Légales - RDE Consulting")
def mentions_legales_page() -> rx.Component:
    """Page des mentions légales."""
    return mentions_legales_content()