#import reflex as rx
#
#config = rx.Config(
#    app_name="app",
#    title="RDE Simulateur CEE",
#    description="Calculez votre prime CEE facilement",
#    theme=rx.theme(
#        appearance="light",
#        has_background=True,
#        radius="large",
#        accent_color="teal",
#    ),
#)
#


"""Configuration Reflex pour RDE Simulateur CEE."""

import reflex as rx
import os

# Détection de l'environnement Railway
RAILWAY_ENVIRONMENT = os.getenv("RAILWAY_ENVIRONMENT")
IS_PRODUCTION = RAILWAY_ENVIRONMENT is not None

# Configuration de base (identique dev et prod)
base_config = {
    "app_name": "app",
    "title": "RDE Simulateur CEE",
    "description": "Calculez votre prime CEE facilement",
    "theme": rx.theme(
        appearance="light",
        has_background=True,
        radius="large",
        accent_color="teal",
    ),
}

# Ajouter api_url uniquement en production
if IS_PRODUCTION:
    RAILWAY_PUBLIC_DOMAIN = os.getenv("RAILWAY_PUBLIC_DOMAIN", "")
    if RAILWAY_PUBLIC_DOMAIN:
        base_config["api_url"] = f"https://{RAILWAY_PUBLIC_DOMAIN}"
    else:
        PORT = os.getenv("PORT", "8080")
        base_config["api_url"] = f"http://0.0.0.0:{PORT}"

config = rx.Config(**base_config)