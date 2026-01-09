"""
Styles et thème de l'application.
Design system cohérent pour toute l'application.
"""

import reflex as rx

# ==================== Couleurs ====================

COLORS = {
    # Couleurs principales
    "primary": "#368278",        # Teal - Couleur principale
    "primary_dark": "#2a6860",   # Teal foncé
    "primary_light": "#4a9990",  # Teal clair
    
    # Couleurs secondaires
    "secondary": "#0d242c",      # Bleu très foncé
    "accent": "#10B981",         # Vert validation
    
    # Couleurs de statut
    "success": "#10B981",        # Vert
    "warning": "#F59E0B",        # Orange
    "error": "#EF4444",          # Rouge
    "info": "#3B82F6",           # Bleu
    
    # Neutres
    "white": "#FFFFFF",
    "background": "#F9FAFB",     # Gris très clair
    "surface": "#FFFFFF",
    "border": "#E5E7EB",
    "border_light": "#F3F4F6",
    
    # Textes
    "text_primary": "#111827",   # Gris très foncé
    "text_secondary": "#6B7280", # Gris moyen
    "text_muted": "#9CA3AF",     # Gris clair
    "text_inverse": "#FFFFFF",
}

# ==================== Typographie ====================

FONTS = {
    "heading": "Inter, system-ui, sans-serif",
    "body": "Inter, system-ui, sans-serif",
    "mono": "JetBrains Mono, monospace",
}

FONT_SIZES = {
    "xs": "0.75rem",    # 12px
    "sm": "0.875rem",   # 14px
    "base": "1rem",     # 16px
    "lg": "1.125rem",   # 18px
    "xl": "1.25rem",    # 20px
    "2xl": "1.5rem",    # 24px
    "3xl": "1.875rem",  # 30px
    "4xl": "2.25rem",   # 36px
    "5xl": "3rem",      # 48px
}

# ==================== Espacements ====================

SPACING = {
    "0": "0",
    "1": "0.25rem",     # 4px
    "2": "0.5rem",      # 8px
    "3": "0.75rem",     # 12px
    "4": "1rem",        # 16px
    "5": "1.25rem",     # 20px
    "6": "1.5rem",      # 24px
    "8": "2rem",        # 32px
    "10": "2.5rem",     # 40px
    "12": "3rem",       # 48px
    "16": "4rem",       # 64px
}

# ==================== Ombres ====================

SHADOWS = {
    "sm": "0 1px 2px 0 rgba(0, 0, 0, 0.05)",
    "base": "0 1px 3px 0 rgba(0, 0, 0, 0.1), 0 1px 2px -1px rgba(0, 0, 0, 0.1)",
    "md": "0 4px 6px -1px rgba(0, 0, 0, 0.1), 0 2px 4px -2px rgba(0, 0, 0, 0.1)",
    "lg": "0 10px 15px -3px rgba(0, 0, 0, 0.1), 0 4px 6px -4px rgba(0, 0, 0, 0.1)",
    "xl": "0 20px 25px -5px rgba(0, 0, 0, 0.1), 0 8px 10px -6px rgba(0, 0, 0, 0.1)",
    "card": "0 4px 6px rgba(0, 0, 0, 0.1)",
    "card_hover": "0 8px 20px rgba(0, 0, 0, 0.15)",
}

# ==================== Border Radius ====================

RADIUS = {
    "none": "0",
    "sm": "0.25rem",    # 4px
    "base": "0.375rem", # 6px
    "md": "0.5rem",     # 8px
    "lg": "0.75rem",    # 12px
    "xl": "1rem",       # 16px
    "2xl": "1.5rem",    # 24px
    "full": "9999px",
}

# ==================== Breakpoints ====================

BREAKPOINTS = {
    "sm": "640px",
    "md": "768px",
    "lg": "1024px",
    "xl": "1280px",
    "2xl": "1536px",
}

# ==================== Styles de composants ====================

# Style de base pour les cartes
CARD_STYLE = {
    "background": COLORS["white"],
    "border": f"1px solid {COLORS['border']}",
    "border_radius": RADIUS["xl"],
    "box_shadow": SHADOWS["card"],
    "padding": SPACING["6"],
}

# Style de carte au survol
CARD_HOVER_STYLE = {
    **CARD_STYLE,
    "_hover": {
        "box_shadow": SHADOWS["card_hover"],
        "transform": "translateY(-2px)",
        "transition": "all 0.2s ease-in-out",
    },
    "transition": "all 0.2s ease-in-out",
    "cursor": "pointer",
}

# Style de carte sélectionnée
CARD_SELECTED_STYLE = {
    **CARD_STYLE,
    "border": f"2px solid {COLORS['primary']}",
    "box_shadow": f"0 0 0 3px {COLORS['primary']}20",
}

# Style des boutons primaires
BUTTON_PRIMARY_STYLE = {
    "background": COLORS["primary"],
    "color": COLORS["white"],
    "border_radius": RADIUS["lg"],
    "padding": f"{SPACING['3']} {SPACING['6']}",
    "font_weight": "600",
    "box_shadow": SHADOWS["md"],
    "_hover": {
        "background": COLORS["primary_dark"],
        "transform": "translateY(-1px)",
        "box_shadow": SHADOWS["lg"],
    },
    "transition": "all 0.2s ease-in-out",
}

# Style des boutons secondaires
BUTTON_SECONDARY_STYLE = {
    "background": COLORS["white"],
    "color": COLORS["primary"],
    "border": f"1px solid {COLORS['primary']}",
    "border_radius": RADIUS["lg"],
    "padding": f"{SPACING['3']} {SPACING['6']}",
    "font_weight": "600",
    "_hover": {
        "background": f"{COLORS['primary']}10",
    },
    "transition": "all 0.2s ease-in-out",
}

# Style des inputs
INPUT_STYLE = {
    "border": f"1px solid {COLORS['border']}",
    "border_radius": RADIUS["md"],
    "padding": SPACING["3"],
    "width": "100%",
    "_focus": {
        "border_color": COLORS["primary"],
        "box_shadow": f"0 0 0 3px {COLORS['primary']}20",
        "outline": "none",
    },
    "transition": "all 0.2s ease-in-out",
}

# Style de la sidebar
SIDEBAR_STYLE = {
    "background": COLORS["white"],
    "border_right": f"1px solid {COLORS['border']}",
    "min_width": "250px",
    "height": "100vh",
    "padding": SPACING["4"],
}

# Style du header
HEADER_STYLE = {
    "background": COLORS["white"],
    "border_bottom": f"1px solid {COLORS['border']}",
    "padding": f"{SPACING['3']} {SPACING['6']}",
    "width": "100%",
}

# ==================== Styles utilitaires ====================

def title_style(size: str = "xl") -> dict:
    """Retourne le style pour un titre."""
    return {
        "font_size": FONT_SIZES.get(size, FONT_SIZES["xl"]),
        "font_weight": "700",
        "color": COLORS["text_primary"],
        "margin_bottom": SPACING["4"],
    }

def text_style(variant: str = "body") -> dict:
    """Retourne le style pour du texte."""
    variants = {
        "body": {
            "font_size": FONT_SIZES["base"],
            "color": COLORS["text_primary"],
        },
        "secondary": {
            "font_size": FONT_SIZES["sm"],
            "color": COLORS["text_secondary"],
        },
        "muted": {
            "font_size": FONT_SIZES["sm"],
            "color": COLORS["text_muted"],
        },
        "error": {
            "font_size": FONT_SIZES["sm"],
            "color": COLORS["error"],
        },
        "success": {
            "font_size": FONT_SIZES["sm"],
            "color": COLORS["success"],
        },
    }
    return variants.get(variant, variants["body"])

# ==================== Animation keyframes ====================

ANIMATIONS = {
    "fade_in": {
        "0%": {"opacity": "0"},
        "100%": {"opacity": "1"},
    },
    "slide_up": {
        "0%": {"opacity": "0", "transform": "translateY(20px)"},
        "100%": {"opacity": "1", "transform": "translateY(0)"},
    },
    "scale_in": {
        "0%": {"opacity": "0", "transform": "scale(0.95)"},
        "100%": {"opacity": "1", "transform": "scale(1)"},
    },
}
