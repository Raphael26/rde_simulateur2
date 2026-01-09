"""
Design System - SimuPrime
"""

# =============================================================================
# COULEURS
# =============================================================================
class Colors:
    # Couleurs principales
    PRIMARY = "#368278"
    PRIMARY_DARK = "#2a6860"
    PRIMARY_LIGHT = "#4a9a8f"
    PRIMARY_LIGHTER = "#e8f4f2"
    
    SECONDARY = "#466c82"
    SECONDARY_DARK = "#375566"
    SECONDARY_LIGHT = "#5a8aa3"
    
    # États
    SUCCESS = "#10B981"
    SUCCESS_LIGHT = "#D1FAE5"
    WARNING = "#F59E0B"
    WARNING_LIGHT = "#FEF3C7"
    ERROR = "#EF4444"
    ERROR_LIGHT = "#FEE2E2"
    INFO = "#3B82F6"
    INFO_LIGHT = "#DBEAFE"
    
    # Neutres
    WHITE = "#FFFFFF"
    GRAY_50 = "#F9FAFB"
    GRAY_100 = "#F3F4F6"
    GRAY_200 = "#E5E7EB"
    GRAY_300 = "#D1D5DB"
    GRAY_400 = "#9CA3AF"
    GRAY_500 = "#6B7280"
    GRAY_600 = "#4B5563"
    GRAY_700 = "#374151"
    GRAY_800 = "#1F2937"
    GRAY_900 = "#111827"
    BLACK = "#000000"
    
    # Backgrounds
    BG_PAGE = "#F8FAFC"
    BG_CARD = "#FFFFFF"
    BG_SIDEBAR = "#FFFFFF"
    BG_HEADER = "#FFFFFF"


# =============================================================================
# TYPOGRAPHIE
# =============================================================================
class Typography:
    FONT_FAMILY = "Inter, -apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, sans-serif"
    
    # Tailles
    SIZE_XS = "0.75rem"
    SIZE_SM = "0.875rem"
    SIZE_BASE = "1rem"
    SIZE_LG = "1.125rem"
    SIZE_XL = "1.25rem"
    SIZE_2XL = "1.5rem"
    SIZE_3XL = "1.875rem"
    SIZE_4XL = "2.25rem"
    
    # Poids
    WEIGHT_NORMAL = "400"
    WEIGHT_MEDIUM = "500"
    WEIGHT_SEMIBOLD = "600"
    WEIGHT_BOLD = "700"


# =============================================================================
# ESPACEMENTS
# =============================================================================
class Spacing:
    XS = "0.25rem"
    SM = "0.5rem"
    MD = "1rem"
    LG = "1.5rem"
    XL = "2rem"
    XXL = "3rem"


# =============================================================================
# BORDURES
# =============================================================================
class Borders:
    RADIUS_SM = "0.25rem"
    RADIUS_MD = "0.5rem"
    RADIUS_LG = "0.75rem"
    RADIUS_XL = "1rem"
    RADIUS_2XL = "1.5rem"
    RADIUS_FULL = "9999px"


# =============================================================================
# OMBRES
# =============================================================================
class Shadows:
    SM = "0 1px 2px 0 rgba(0, 0, 0, 0.05)"
    MD = "0 4px 6px -1px rgba(0, 0, 0, 0.1)"
    LG = "0 10px 15px -3px rgba(0, 0, 0, 0.1)"
    XL = "0 20px 25px -5px rgba(0, 0, 0, 0.1)"
    CARD = "0 1px 3px rgba(0,0,0,0.08)"