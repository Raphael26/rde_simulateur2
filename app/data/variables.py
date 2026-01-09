"""
Variables et données statiques pour l'application SimuPrime
"""

# =============================================================================
# DÉPARTEMENTS DE FRANCE
# =============================================================================
DEPARTEMENTS_FRANCE = {
    "Ain (01)": "ain",
    "Aisne (02)": "aisne",
    "Allier (03)": "allier",
    "Alpes-de-Haute-Provence (04)": "alpes-de-haute-provence",
    "Hautes-Alpes (05)": "hautes-alpes",
    "Alpes-Maritimes (06)": "alpes-maritimes",
    "Ardèche (07)": "ardeche",
    "Ardennes (08)": "ardennes",
    "Ariège (09)": "ariege",
    "Aube (10)": "aube",
    "Aude (11)": "aude",
    "Aveyron (12)": "aveyron",
    "Bouches-du-Rhône (13)": "bouches-du-rhone",
    "Calvados (14)": "calvados",
    "Cantal (15)": "cantal",
    "Charente (16)": "charente",
    "Charente-Maritime (17)": "charente-maritime",
    "Cher (18)": "cher",
    "Corrèze (19)": "correze",
    "Corse-du-Sud (2A)": "corse-du-sud",
    "Haute-Corse (2B)": "haute-corse",
    "Côte-d'Or (21)": "cote-d-or",
    "Côtes-d'Armor (22)": "cotes-d-armor",
    "Creuse (23)": "creuse",
    "Dordogne (24)": "dordogne",
    "Doubs (25)": "doubs",
    "Drôme (26)": "drome",
    "Eure (27)": "eure",
    "Eure-et-Loir (28)": "eure-et-loir",
    "Finistère (29)": "finistere",
    "Gard (30)": "gard",
    "Haute-Garonne (31)": "haute-garonne",
    "Gers (32)": "gers",
    "Gironde (33)": "gironde",
    "Hérault (34)": "herault",
    "Ille-et-Vilaine (35)": "ille-et-vilaine",
    "Indre (36)": "indre",
    "Indre-et-Loire (37)": "indre-et-loire",
    "Isère (38)": "isere",
    "Jura (39)": "jura",
    "Landes (40)": "landes",
    "Loir-et-Cher (41)": "loir-et-cher",
    "Loire (42)": "loire",
    "Haute-Loire (43)": "haute-loire",
    "Loire-Atlantique (44)": "loire-atlantique",
    "Loiret (45)": "loiret",
    "Lot (46)": "lot",
    "Lot-et-Garonne (47)": "lot-et-garonne",
    "Lozère (48)": "lozere",
    "Maine-et-Loire (49)": "maine-et-loire",
    "Manche (50)": "manche",
    "Marne (51)": "marne",
    "Haute-Marne (52)": "haute-marne",
    "Mayenne (53)": "mayenne",
    "Meurthe-et-Moselle (54)": "meurthe-et-moselle",
    "Meuse (55)": "meuse",
    "Morbihan (56)": "morbihan",
    "Moselle (57)": "moselle",
    "Nièvre (58)": "nievre",
    "Nord (59)": "nord",
    "Oise (60)": "oise",
    "Orne (61)": "orne",
    "Pas-de-Calais (62)": "pas-de-calais",
    "Puy-de-Dôme (63)": "puy-de-dome",
    "Pyrénées-Atlantiques (64)": "pyrenees-atlantiques",
    "Hautes-Pyrénées (65)": "hautes-pyrenees",
    "Pyrénées-Orientales (66)": "pyrenees-orientales",
    "Bas-Rhin (67)": "bas-rhin",
    "Haut-Rhin (68)": "haut-rhin",
    "Rhône (69)": "rhone",
    "Haute-Saône (70)": "haute-saone",
    "Saône-et-Loire (71)": "saone-et-loire",
    "Sarthe (72)": "sarthe",
    "Savoie (73)": "savoie",
    "Haute-Savoie (74)": "haute-savoie",
    "Paris (75)": "paris",
    "Seine-Maritime (76)": "seine-maritime",
    "Seine-et-Marne (77)": "seine-et-marne",
    "Yvelines (78)": "yvelines",
    "Deux-Sèvres (79)": "deux-sevres",
    "Somme (80)": "somme",
    "Tarn (81)": "tarn",
    "Tarn-et-Garonne (82)": "tarn-et-garonne",
    "Var (83)": "var",
    "Vaucluse (84)": "vaucluse",
    "Vendée (85)": "vendee",
    "Vienne (86)": "vienne",
    "Haute-Vienne (87)": "haute-vienne",
    "Vosges (88)": "vosges",
    "Yonne (89)": "yonne",
    "Territoire de Belfort (90)": "territoire-de-belfort",
    "Essonne (91)": "essonne",
    "Hauts-de-Seine (92)": "hauts-de-seine",
    "Seine-Saint-Denis (93)": "seine-saint-denis",
    "Val-de-Marne (94)": "val-de-marne",
    "Val-d'Oise (95)": "val-d-oise",
    "Guadeloupe (971)": "guadeloupe",
    "Martinique (972)": "martinique",
    "Guyane (973)": "guyane",
    "La Réunion (974)": "la-reunion",
    "Mayotte (976)": "mayotte"
}


# =============================================================================
# SECTEURS
# =============================================================================
SECTORS = [
    {"label": "Industrie", "value": "Industrie", "abbr": "IND", "icon": "factory", "description": "Opérations industrielles"},
    {"label": "Résidentiel", "value": "Résidentiel", "abbr": "BAR", "icon": "house", "description": "Logements"},
    {"label": "Tertiaire", "value": "Tertiaire", "abbr": "BAT", "icon": "building-2", "description": "Bureaux, commerces"},
    {"label": "Réseaux", "value": "Réseaux", "abbr": "RES", "icon": "network", "description": "Réseaux de chaleur"},
    {"label": "Agriculture", "value": "Agriculture", "abbr": "AGRI", "icon": "tractor", "description": "Exploitations agricoles"},
    {"label": "Transport", "value": "Transport", "abbr": "TRA", "icon": "truck", "description": "Transport"},
]

SECTOR_ABBREVIATIONS = {
    "Industrie": "IND",
    "Résidentiel": "BAR",
    "Tertiaire": "BAT",
    "Réseaux": "RES",
    "Agriculture": "AGRI",
    "Transport": "TRA",
}


# =============================================================================
# TYPOLOGIES PAR SECTEUR
# =============================================================================
SECTOR_TYPOLOGIES = {
    "Industrie": [
        {"name": "Utilité", "abbr": "UT", "icon": "plug", "description": "Utilités industrielles"},
        {"name": "Bâtiment", "abbr": "BA", "icon": "building", "description": "Bâtiments industriels"},
    ],
    "Résidentiel": [
        {"name": "Enveloppe", "abbr": "EN", "icon": "layers", "description": "Isolation"},
        {"name": "Thermique", "abbr": "TH", "icon": "flame", "description": "Chauffage, ECS"},
        {"name": "Équipement", "abbr": "EQ", "icon": "cpu", "description": "Équipements"},
        {"name": "Service", "abbr": "SE", "icon": "briefcase", "description": "Services"},
    ],
    "Tertiaire": [
        {"name": "Enveloppe", "abbr": "EN", "icon": "layers", "description": "Isolation"},
        {"name": "Thermique", "abbr": "TH", "icon": "flame", "description": "CVC"},
        {"name": "Équipement", "abbr": "EQ", "icon": "cpu", "description": "Équipements"},
        {"name": "Service", "abbr": "SE", "icon": "briefcase", "description": "Services"},
    ],
    "Réseaux": [
        {"name": "Eclairage", "abbr": "EC", "icon": "lightbulb", "description": "Éclairage public"},
        {"name": "Chaleur", "abbr": "CH", "icon": "thermometer", "description": "Réseaux de chaleur"},
    ],
    "Agriculture": [
        {"name": "Utilité", "abbr": "UT", "icon": "plug", "description": "Utilités"},
        {"name": "Thermique", "abbr": "TH", "icon": "flame", "description": "Chauffage"},
        {"name": "Équipement", "abbr": "EQ", "icon": "cpu", "description": "Équipements"},
        {"name": "Service", "abbr": "SE", "icon": "briefcase", "description": "Services"},
    ],
    "Transport": [
        {"name": "Équipement", "abbr": "EQ", "icon": "cpu", "description": "Équipements"},
        {"name": "Service", "abbr": "SE", "icon": "briefcase", "description": "Services"},
    ],
}

TYPOLOGY_ABBREVIATIONS = {
    "Utilité": "UT",
    "Bâtiment": "BA",
    "Enveloppe": "EN",
    "Thermique": "TH",
    "Équipement": "EQ",
    "Service": "SE",
    "Eclairage": "EC",
    "Chaleur": "CH",
}


# =============================================================================
# TYPES DE BÉNÉFICIAIRES
# =============================================================================
BENEFICIARY_TYPES = [
    {"value": "particulier", "label": "Particulier", "icon": "user", "description": "Propriétaire ou locataire"},
    {"value": "entreprise", "label": "Entreprise", "icon": "building-2", "description": "Société, PME, ETI"},
    {"value": "collectivite", "label": "Collectivité", "icon": "landmark", "description": "Mairie, département"},
    {"value": "bailleur", "label": "Bailleur social", "icon": "home", "description": "Logement social"},
    {"value": "copropriete", "label": "Copropriété", "icon": "users", "description": "Syndic"},
]


# =============================================================================
# ZONES CLIMATIQUES
# =============================================================================
DEPARTEMENT_ZONE_CLIMATIQUE = {
    "Nord (59)": "H1", "Pas-de-Calais (62)": "H1", "Somme (80)": "H1",
    "Aisne (02)": "H1", "Ardennes (08)": "H1", "Marne (51)": "H1",
    "Haute-Marne (52)": "H1", "Meuse (55)": "H1", "Meurthe-et-Moselle (54)": "H1",
    "Moselle (57)": "H1", "Bas-Rhin (67)": "H1", "Haut-Rhin (68)": "H1",
    "Vosges (88)": "H1", "Haute-Saône (70)": "H1", "Doubs (25)": "H1",
    "Jura (39)": "H1", "Côte-d'Or (21)": "H1", "Saône-et-Loire (71)": "H1",
    "Ain (01)": "H1", "Rhône (69)": "H1", "Loire (42)": "H1",
    "Haute-Loire (43)": "H1", "Savoie (73)": "H1", "Haute-Savoie (74)": "H1",
    "Isère (38)": "H1", "Hautes-Alpes (05)": "H1",
    "Pyrénées-Orientales (66)": "H3", "Aude (11)": "H3", "Hérault (34)": "H3",
    "Gard (30)": "H3", "Bouches-du-Rhône (13)": "H3", "Var (83)": "H3",
    "Alpes-Maritimes (06)": "H3", "Corse-du-Sud (2A)": "H3", "Haute-Corse (2B)": "H3",
}


# =============================================================================
# CONSTANTES CEE
# =============================================================================
CEE_CONSTANTS = {
    "PRIX_CUMAC_EUR": 0.0065,
    "DUREE_VIE_CONVENTIONNELLE": 15,
}

SUPABASE_BUCKET_NAME = "fiches-operations"


def get_abbreviation(sector: str, typology: str) -> str:
    """Génère l'abréviation complète pour un secteur et une typologie."""
    sector_abbr = SECTOR_ABBREVIATIONS.get(sector, "")
    typology_abbr = TYPOLOGY_ABBREVIATIONS.get(typology, "")
    if sector_abbr and typology_abbr:
        return f"{sector_abbr}-{typology_abbr}-"
    return ""


def get_zone_climatique(departement: str) -> str:
    """Retourne la zone climatique pour un département donné."""
    return DEPARTEMENT_ZONE_CLIMATIQUE.get(departement, "H2")