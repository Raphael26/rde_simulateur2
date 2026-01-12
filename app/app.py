"""
RDE Consulting - Simulateur de Primes CEE
Application Reflex avec Supabase backend
"""

# TODO: donner des noms de variables plus digestibles que 1x8h, 2x8h etc
# TODO: clean this Mode de fonctionnement du site industriel ""3"""
# TODO: damaged PDF file
# TODO: 0 simulations dans la page profile
# TODO: action rapide: consulter les fiches



import reflex as rx

# Import des états
from .state import AuthState, SimulationState, DashboardState

# Import des pages
from .pages import (
    landing_page,
    login_page,
    register_page,
    dashboard_page,
    profile_page,
    step1_date_department_page,
    step2_sector_page,
    step3_typology_page,
    step4_fiches_page,
    step5_form_page,
    step6_result_page,
)

from .pages.mentions_legales import mentions_legales_page

# Import des styles
from .styles.design_system import Colors


# Configuration du thème
def get_theme() -> dict:
    return {
        "accent_color": "teal",
        "gray_color": "slate",
        "radius": "medium",
        "scaling": "100%",
    }


# Page d'accueil (redirection)
@rx.page(route="/", title="RDE Consulting - Accueil")
def index() -> rx.Component:
    return landing_page()


# Application
app = rx.App(
    theme=rx.theme(
        accent_color="teal",
        gray_color="slate",
        radius="medium",
    ),
    stylesheets=[
        "https://fonts.googleapis.com/css2?family=Inter:wght@400;500;600;700&display=swap",
    ],
)