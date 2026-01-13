"""Configuration Reflex pour RDE Simulateur CEE."""

import reflex as rx
import os

# Get the public URL from environment (Railway sets RAILWAY_PUBLIC_DOMAIN)
public_domain = os.getenv("RAILWAY_PUBLIC_DOMAIN", "")

# Build config - only include api_url if we have a public domain
if public_domain:
    config = rx.Config(
        app_name="app",
        title="RDE Simulateur CEE",
        description="Calculez votre prime CEE facilement",
        show_built_with_reflex=False,
        api_url=f"https://{public_domain}",
        theme=rx.theme(
            appearance="light",
            has_background=True,
            radius="large",
            accent_color="teal",
        ),
    )
else:
    config = rx.Config(
        app_name="app",
        title="RDE Simulateur CEE",
        description="Calculez votre prime CEE facilement",
        show_built_with_reflex=False,
        theme=rx.theme(
            appearance="light",
            has_background=True,
            radius="large",
            accent_color="teal",
        ),
    )