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

# Détection de l'environnement
RAILWAY_ENVIRONMENT = os.getenv("RAILWAY_ENVIRONMENT")
IS_PRODUCTION = RAILWAY_ENVIRONMENT is not None

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
    # Récupérer le domaine Railway
    RAILWAY_PUBLIC_DOMAIN = os.getenv("RAILWAY_PUBLIC_DOMAIN", "")
    RAILWAY_STATIC_URL = os.getenv("RAILWAY_STATIC_URL", "")
    
    if RAILWAY_PUBLIC_DOMAIN:
        # Frontend et backend sur le même domaine (via Caddy)
        base_config["api_url"] = f"https://{RAILWAY_PUBLIC_DOMAIN}"
    elif RAILWAY_STATIC_URL:
        base_config["api_url"] = RAILWAY_STATIC_URL
    # Si aucun domaine n'est défini, Reflex utilisera des chemins relatifs

config = rx.Config(**base_config)