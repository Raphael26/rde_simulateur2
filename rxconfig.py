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

# Détecter si on est en production (Railway définit cette variable)
IS_PRODUCTION = os.getenv("RAILWAY_ENVIRONMENT") is not None or os.getenv("RAILWAY_PUBLIC_DOMAIN") is not None

# Configuration de base
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

# En production, configurer l'API URL
if IS_PRODUCTION:
    # Domaine Railway (hardcodé pour le build)
    PROD_DOMAIN = os.getenv("RAILWAY_PUBLIC_DOMAIN", "rdesimulateur2-production.up.railway.app")
    base_config["api_url"] = f"https://{PROD_DOMAIN}"

config = rx.Config(**base_config)