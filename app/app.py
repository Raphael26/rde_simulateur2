"""
RDE Consulting - Simulateur de Primes CEE
Application Reflex avec Supabase backend
"""

# TODO: donner des noms de variables plus digestibles que 1x8h, 2x8h etc
# TODO: clean this Mode de fonctionnement du site industriel ""3"""
# TODO: damaged PDF file
# TODO: 0 simulations dans la page profile
# TODO: action rapide: consulter les fiches
# TODO: RAG sur questions réponses


import reflex as rx

from .pages import landing_page


@rx.page(route="/", title="RDE Consulting - Accueil")
def index() -> rx.Component:
    return landing_page()


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