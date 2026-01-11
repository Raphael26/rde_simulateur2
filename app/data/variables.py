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
# FICHES
# =============================================================================
FICHE_NAMES_MAPPING = {
    "AGRI-EQ-101": "Module d'intégration de température installé sur un ordinateur climatique",
    "AGRI-EQ-102": "Double écran thermique",
    "AGRI-EQ-104": "Écrans thermiques latéraux",
    "AGRI-EQ-105": "Stop & Start pour véhicules agricoles à moteur",
    "AGRI-EQ-106": "Régulation de la ventilation des silos et des installations de stockage en vrac de céréales",
    "AGRI-EQ-107": "Isolation des parois de serre",
    "AGRI-EQ-108": "Stockage d'eau pour une serre bioclimatique",
    "AGRI-EQ-109": "Couverture performante de serre",
    "AGRI-EQ-110": "Séchage solaire par insufflation des produits et co-produits agricoles et forestiers utilisant des panneaux solaires hybrides",
    "AGRI-EQ-111": "Simple écran thermique",
    "AGRI-EQ-112": "Double paroi gonflable",
    "AGRI-SE-101": "Contrôle et préconisations de réglage du moteur d'un tracteur",
    "AGRI-TH-101": "Dispositif de stockage d'eau chaude de type « Open Buffer »",
    "AGRI-TH-102": "Dispositif de stockage d'eau chaude",
    "AGRI-TH-103": "Pré refroidisseur de lait",
    "AGRI-TH-104": "Système de récupération de chaleur sur groupe de production de froid hors tanks à lait",
    "AGRI-TH-105": "Récupérateur de chaleur sur tank à lait",
    "AGRI-TH-108": "Pompe à chaleur de type air/eau ou eau/eau",
    "AGRI-TH-109": "Récupérateur de chaleur à condensation pour serres",
    "AGRI-TH-110": "Chaudière à haute performance énergétique pour serres",
    "AGRI-TH-113": "Échangeur récupérateur de chaleur air/air dans un bâtiment d'élevage de volailles",
    "AGRI-TH-117": "Déshumidificateur thermodynamique pour serres",
    "AGRI-TH-118": "Double tube de chauffage pour serres",
    "AGRI-TH-119": "Système de déshumidification avec air extérieur",
    "AGRI-UT-101": "Moto-variateur synchrone à aimants permanents ou à reluctance",
    "AGRI-UT-102": "Système de variation électronique de vitesse sur un moteur asynchrone",
    "AGRI-UT-103": "Système de régulation sur un groupe de production de froid permettant d'avoir une basse pression flottante",
    "AGRI-UT-104": "Système de régulation sur un groupe de production de froid permettant d'avoir une haute pression flottante",
    "BAR-EN-101": "Isolation de combles ou de toiture",
    "BAR-EN-102": "Isolation des murs",
    "BAR-EN-103": "Isolation d'un plancher",
    "BAR-EN-104": "Fenêtre ou porte-fenêtre complète avec vitrage isolant",
    "BAR-EN-105": "Isolation des toitures terrasses",
    "BAR-EN-106": "Isolation de combles ou de toitures (France d'outre-mer)",
    "BAR-EN-107": "Isolation des murs (France d'outre-mer)",
    "BAR-EN-108": "Fermeture isolante",
    "BAR-EN-109": "Réduction des apports solaires par la toiture (France d'outre-mer)",
    "BAR-EN-110": "Fenêtre ou porte-fenêtre complète avec vitrage pariétodynamique",
    "BAR-EQ-110": "Luminaire à modules LED avec dispositif de contrôle pour les parties communes",
    "BAR-EQ-115": "Dispositif d'affichage et d'interprétation des consommations d'énergie",
    "BAR-SE-104": "Réglage des organes d'équilibrage d'une installation de chauffage à eau chaude",
    "BAR-SE-105": "Contrat de Performance Energétique Services (CPE Services)",
    "BAR-SE-106": "Service de suivi des consommations d'énergie",
    "BAR-SE-107": "Abaissement de la température de retour vers un réseau de chaleur",
    "BAR-SE-108": "Désembouage d'un réseau hydraulique individuel de chauffage en France métropolitaine",
    "BAR-SE-109": "Désembouage d'un réseau hydraulique de chauffage collectif en France métropolitaine",
    "BAR-TH-101": "Chauffe-eau solaire individuel (France métropolitaine)",
    "BAR-TH-102": "Chauffe-eau solaire collectif (France métropolitaine)",
    "BAR-TH-104": "Pompe à chaleur de type air/eau ou eau/eau",
    "BAR-TH-110": "Radiateur basse température pour un chauffage central",
    "BAR-TH-111": "Régulation par sonde de température extérieure",
    "BAR-TH-112": "Appareil indépendant de chauffage au bois",
    "BAR-TH-113": "Chaudière biomasse individuelle",
    "BAR-TH-116": "Plancher chauffant hydraulique à basse température",
    "BAR-TH-117": "Robinet thermostatique",
    "BAR-TH-122": "Récupérateur de chaleur à condensation",
    "BAR-TH-123": "Optimiseur de relance en chauffage collectif comprenant une fonction auto-adaptative",
    "BAR-TH-124": "Chauffe-eau solaire individuel (France d'outre-mer)",
    "BAR-TH-125": "Système de ventilation double flux autoréglable ou modulé à haute performance (France métropolitaine)",
    "BAR-TH-127": "Ventilation mécanique simple flux hygroréglable (France métropolitaine)",
    "BAR-TH-129": "Pompe à chaleur de type air/air",
    "BAR-TH-130": "Surperformance énergétique pour un bâtiment neuf (France métropolitaine)",
    "BAR-TH-135": "Chauffe-eau solaire collectif (France d'outre-mer)",
    "BAR-TH-137": "Raccordement d'un bâtiment résidentiel à un réseau de chaleur",
    "BAR-TH-139": "Système de variation électronique de vitesse sur une pompe",
    "BAR-TH-141": "Climatiseur performant (France d'outre-mer)",
    "BAR-TH-143": "Système solaire combiné (France métropolitaine)",
    "BAR-TH-145": "Rénovation globale d'un bâtiment résidentiel collectif (France métropolitaine)",
    "BAR-TH-148": "Chauffe-eau thermodynamique à accumulation",
    "BAR-TH-150": "Pompe à chaleur collective à absorption de type air/eau ou eau/eau",
    "BAR-TH-155": "Ventilation hybride hygroréglable (France métropolitaine)",
    "BAR-TH-158": "Emetteur électrique à régulation électronique à fonctions avancées",
    "BAR-TH-159": "Pompe à chaleur hybride individuelle",
    "BAR-TH-160": "Isolation d'un réseau hydraulique de chauffage ou d'eau chaude sanitaire (France métropolitaine)",
    "BAR-TH-161": "Isolation de points singuliers d'un réseau",
    "BAR-TH-162": "Système énergétique comportant des capteurs solaires photovoltaïques et thermiques à circulation d'eau (France métropolitaine)",
    "BAR-TH-163": "Conduit d'évacuation des produits de combustion",
    "BAR-TH-165": "Chaudière biomasse collective",
    "BAR-TH-166": "Pompe à chaleur collective de type air/eau ou eau/eau",
    "BAR-TH-167": "Chauffe-bain individuel à haut rendement ou à condensation (France métropolitaine)",
    "BAR-TH-168": "Dispositif solaire thermique (France métropolitaine)",
    "BAR-TH-169": "Pompe à chaleur collective de type air/eau ou eau/eau pour l'eau chaude sanitaire",
    "BAR-TH-170": "Récupération de chaleur fatale issue de serveurs informatiques pour l'eau chaude sanitaire collective",
    "BAR-TH-171": "Pompe à chaleur de type air/eau",
    "BAR-TH-172": "Pompe à chaleur de type eau/eau ou sol/eau",
    "BAR-TH-173": "Système de régulation par programmation horaire pièce par pièce",
    "BAR-TH-174": "Rénovation d'ampleur d'une maison individuelle (France métropolitaine)",
    "BAR-TH-175": "Rénovation d'ampleur d'un appartement (France métropolitaine)",
    "BAR-TH-176": "Système de régulation de la consommation d'un chauffe-eau électrique à effet Joule",
    "BAR-TH-177": "Rénovation globale d'un bâtiment résidentiel collectif (France métropolitaine)",
    "BAT-EN-101": "Isolation de combles ou de toitures",
    "BAT-EN-102": "Isolation des murs",
    "BAT-EN-103": "Isolation d'un plancher",
    "BAT-EN-104": "Fenêtre ou porte-fenêtre complète avec vitrage isolant",
    "BAT-EN-106": "Isolation de combles ou de toitures (France métropolitaine)",
    "BAT-EN-107": "Isolation des toitures-terrasses",
    "BAT-EN-108": "Isolation des murs (France d'outre-mer)",
    "BAT-EN-109": "Réduction des apports solaires par la toiture (France d'outre-mer)",
    "BAT-EN-110": "Protections des baies contre le rayonnement solaire (France d'outre-mer)",
    "BAT-EN-111": "Fenêtre ou porte-fenêtre complète avec vitrage pariétodynamique (France métropolitaine)",
    "BAT-EN-112": "Revêtements réflectifs en toiture",
    "BAT-EN-113": "Façade rideau ou semi-rideau avec vitrage isolant",
    "BAT-EQ-117": "Installation frigorifique utilisant du CO2 subcritique ou transcritique",
    "BAT-EQ-123": "Moto-variateur synchrone à aimants permanents ou à réluctance",
    "BAT-EQ-124": "Fermeture des meubles frigorifiques de vente à température positive",
    "BAT-EQ-125": "Fermeture des meubles frigorifiques de vente à température négative",
    "BAT-EQ-127": "Luminaire à modules LED",
    "BAT-EQ-129": "Lanterneaux d'éclairage zénithal (France Métropolitaine)",
    "BAT-EQ-130": "Système de condensation frigorifique à haute efficacité",
    "BAT-EQ-131": "Conduits de lumière naturelle",
    "BAT-EQ-133": "Systèmes hydro-économes (France métropolitaine)",
    "BAT-EQ-134": "Meuble frigorifique de vente performant avec groupe de production de froid intégré",
    "BAT-EQ-135": "Dispositif performant d'alimentation sans interruption",
    "BAT-SE-103": "Réglage des organes d'équilibrage d'une installation de chauffage à eau chaude",
    "BAT-SE-104": "Contrat de Performance Energétique Services (CPE Services) Chauffage",
    "BAT-SE-105": "Abaissement de la température de retour vers un réseau de chaleur",
    "BAT-TH-103": "Plancher chauffant hydraulique à basse température",
    "BAT-TH-104": "Robinet thermostatique",
    "BAT-TH-105": "Radiateur basse température pour un chauffage central",
    "BAT-TH-108": "Système de régulation par programmation d'intermittence",
    "BAT-TH-109": "Optimiseur de relance en chauffage collectif comprenant une fonction auto-adaptative",
    "BAT-TH-110": "Récupérateur de chaleur à condensation",
    "BAT-TH-111": "Chauffe-eau solaire collectif (France métropolitaine)",
    "BAT-TH-112": "Système de variation électronique de vitesse sur un moteur asynchrone",
    "BAT-TH-113": "Pompe à chaleur de type air/eau ou eau/eau",
    "BAT-TH-115": "Climatiseur performant (France d'outre-mer)",
    "BAT-TH-116": "Système de gestion technique du bâtiment pour le chauffage, l'eau chaude sanitaire, le refroidissement/climatisation, l'éclairage et les auxiliaires",
    "BAT-TH-121": "Chauffe-eau solaire (France d'outre-mer)",
    "BAT-TH-122": "Programmateur d'intermittence pour la climatisation (France d'outre-mer)",
    "BAT-TH-125": "Ventilation mécanique simple flux à débit d'air constant ou modulé",
    "BAT-TH-126": "Ventilation mécanique double flux avec échangeur à débit d'air constant ou modulé",
    "BAT-TH-127": "Raccordement d'un bâtiment tertiaire à un réseau de chaleur",
    "BAT-TH-134": "Système de régulation sur un groupe de production de froid permettant d'avoir une haute pression flottante (France métropolitaine)",
    "BAT-TH-135": "Système de régulation sur un groupe de production de froid permettant d'avoir une haute pression flottante (France d'outre-mer)",
    "BAT-TH-139": "Système de récupération de chaleur sur un groupe de production de froid",
    "BAT-TH-140": "Pompe à chaleur à absorption de type air/eau ou eau/eau",
    "BAT-TH-141": "Pompe à chaleur à moteur gaz de type air/eau",
    "BAT-TH-142": "Système de déstratification d'air",
    "BAT-TH-143": "Ventilo-convecteurs haute performance",
    "BAT-TH-145": "Système de régulation sur un groupe de production de froid permettant d'avoir une basse pression flottante (France métropolitaine)",
    "BAT-TH-146": "Isolation d'un réseau hydraulique de chauffage ou d'eau chaude sanitaire (France métropolitaine)",
    "BAT-TH-153": "Système de confinement des allées froides et allées chaudes dans un Data Center",
    "BAT-TH-154": "Récupération instantanée de chaleur sur eaux grises",
    "BAT-TH-155": "Isolation de points singuliers d'un réseau",
    "BAT-TH-156": "Freecooling par eau de refroidissement en substitution d'un groupe froid pour la climatisation",
    "BAT-TH-157": "Chaudière biomasse collective",
    "BAT-TH-158": "Pompe à chaleur réversible de type air/air (France métropolitaine)",
    "BAT-TH-159": "Raccordement d'un bâtiment tertiaire à un réseau de froid",
    "BAT-TH-161": "Maintien en température des groupes électrogènes de secours par pompe à chaleur de type air/eau",
    "IND-BA-110": "Déstratificateur ou brasseur d'air",
    "IND-BA-112": "Système de récupération de chaleur sur une tour aéroréfrigérante",
    "IND-BA-113": "Lanterneaux d'éclairage zénithal (France Métropolitaine)",
    "IND-BA-114": "Conduits de lumière naturelle",
    "IND-BA-116": "Luminaires à modules LED",
    "IND-BA-117": "Chauffage décentralisé performant",
    "IND-EN-101": "Isolation des murs (France d'outre-mer)",
    "IND-EN-102": "Isolation de combles ou de toitures (France d'outre-mer)",
    "IND-UT-102": "Système de variation électronique de vitesse sur un moteur asynchrone",
    "IND-UT-103": "Système de récupération de chaleur sur un compresseur d'air",
    "IND-UT-104": "Économiseur sur les effluents gazeux d'une chaudière de production de vapeur",
    "IND-UT-105": "Brûleur micro-modulant sur chaudière industrielle",
    "IND-UT-113": "Système de condensation frigorifique à haute efficacité",
    "IND-UT-114": "Moto-variateur synchrone à aimants permanents ou à réluctance",
    "IND-UT-115": "Système de régulation sur un groupe de production de froid permettant d'avoir une basse pression flottante",
    "IND-UT-116": "Système de régulation sur un groupe de production de froid permettant d'avoir une haute pression flottante",
    "IND-UT-117": "Système de récupération de chaleur sur un groupe de production de froid",
    "IND-UT-118": "Brûleur avec dispositif de récupération de chaleur sur four industriel",
    "IND-UT-120": "Compresseur d'air basse pression à vis ou centrifuge",
    "IND-UT-121": "Isolation de points singuliers d'un réseau",
    "IND-UT-122": "Sécheur d'air comprimé à adsorption utilisant un apport calorifique pour sa régénération",
    "IND-UT-124": "Séquenceur électronique pour le pilotage d'une centrale de production d'air comprimé",
    "IND-UT-125": "Traitement d'eau performant sur chaudière de production de vapeur",
    "IND-UT-127": "Système de transmission performant",
    "IND-UT-129": "Presse à injecter tout électrique ou hybride",
    "IND-UT-130": "Condenseur sur les effluents gazeux d'une chaudière de production de vapeur",
    "IND-UT-131": "Isolation thermique des parois planes ou cylindriques sur des installations industrielles",
    "IND-UT-132": "Moteur asynchrone de classe IE4",
    "IND-UT-133": "Système électronique de pilotage d'un moteur électrique avec récupération d'énergie",
    "IND-UT-134": "Système de mesurage d'indicateurs de performance énergétique",
    "IND-UT-135": "Freecooling par eau de refroidissement en substitution d'un groupe froid",
    "IND-UT-136": "Systèmes moto-régulés",
    "IND-UT-137": "Mise en place d'un système de pompe(s) à chaleur en rehausse de température de chaleur fatale récupérée",
    "IND-UT-138": "Conversion de chaleur fatale en électricité ou en air comprimé",
    "IND-UT-139": "Système de stockage de chaleur fatale",
    "IND-UT-140": "Mise en veille automatique d'une machine utilisant de l'air comprimé",
    "RES-CH-103": "Réhabilitation d'un poste de livraison de chaleur d'un bâtiment tertiaire",
    "RES-CH-104": "Réhabilitation d'un poste de livraison de chaleur d'un bâtiment résidentiel",
    "RES-CH-105": "Passage d'un réseau de chaleur en basse température",
    "RES-CH-106": "Mise en place d'un calorifugeage des canalisations d'un réseau de chaleur",
    "RES-CH-107": "Isolation de points singuliers sur un réseau de chaleur",
    "RES-CH-108": "Récupération de chaleur fatale pour valorisation vers un réseau de chaleur ou vers un tiers (France métropolitaine)",
    "RES-EC-104": "Rénovation d'éclairage extérieur",
    "TRA-EQ-101": "Unité de transport intermodal pour le transport combiné rail-route",
    "TRA-EQ-103": "Télématique embarquée pour le suivi de la conduite d'un véhicule",
    "TRA-EQ-104": "Lubrifiant économiseur d'énergie pour véhicules légers",
    "TRA-EQ-106": "Pneus de véhicules légers à basse résistance au roulement",
    "TRA-EQ-107": "Unité de transport intermodal pour le transport combiné fluvial-route",
    "TRA-EQ-108": "Wagon d'autoroute ferroviaire",
    "TRA-EQ-109": "Barge fluviale",
    "TRA-EQ-110": "Automoteur fluvial",
    "TRA-EQ-111": "Groupe frigorifique autonome à haute efficacité énergétique pour camions, semi-remorques, remorques et caisse mobiles frigorifiques",
    "TRA-EQ-113": "Lubrifiant économiseur d'énergie pour des véhicules de transport de personnes ou de marchandises",
    "TRA-EQ-114": "Achat ou location d'un véhicule léger ou véhicule utilitaire léger électrique neuf ou opération de rétrofit électrique d'un véhicule léger ou véhicule utilitaire léger, par une collectivité locale ou une autre personne morale",
    "TRA-EQ-115": "Véhicule de transport de marchandises optimisé",
    "TRA-EQ-117": "Achat ou location d'un véhicule léger ou véhicule utilitaire léger électrique neuf ou opération de rétrofit électrique d'un véhicule léger ou véhicule utilitaire léger, par des particuliers",
    "TRA-EQ-118": "Lubrifiant économiseur d'énergie pour la pêche professionnelle",
    "TRA-EQ-119": "Optimisation de la combustion et de la propreté des moteurs Diesel",
    "TRA-EQ-120": "Hélice avec tuyère sur une unité de transport fluvial",
    "TRA-EQ-121": "Vélo à assistance électrique",
    "TRA-EQ-122": "« Stop & Start » pour engins automoteurs non routiers neufs",
    "TRA-EQ-123": "Simulateur de conduite",
    "TRA-EQ-124": "Branchement électrique des navires et bateaux à quai",
    "TRA-EQ-125": "« Stop & Start » pour véhicules ferroviaires",
    "TRA-EQ-126": "Remotorisation en propulsion électrique ou hybride d'un bateau naviguant en eaux intérieures",
    "TRA-EQ-127": "Acquisition d'un bateau neuf à propulsion électrique ou hybride, naviguant en eaux intérieures",
    "TRA-EQ-128": "Feuille récapitulative",
    "TRA-EQ-129": "Achat ou location d'un véhicule lourd électrique neuf de transport de marchandises ou issu d'une opération de rétrofit électrique",
    "TRA-EQ-130": "Achat ou location d'un quadricycle électrique neuf",
    "TRA-EQ-131": "Achat ou location, par une personne morale, de vélos-cargos neufs ou reconditionnés",
    "TRA-EQ-132": "Appareil de mesure, d'analyse et d'optimisation de la consommation de carburant d'un navire de pêche",
    "TRA-SE-101": "Formation d'un chauffeur de transport à la conduite économe",
    "TRA-SE-102": "Formation d'un chauffeur de véhicule léger à la conduite économe",
    "TRA-SE-104": "Station de gonflage des pneumatiques",
    "TRA-SE-105": "Recreusage des pneumatiques",
    "TRA-SE-106": "Mesure et optimisation des consommations de carburant d'une unité de transport fluvial",
    "TRA-SE-107": "Carénage sur une unité de transport fluvial",
    "TRA-SE-108": "Gestion externalisée de la globalité du poste pneumatique (Véhicules de transport de marchandises)",
    "TRA-SE-109": "Gestion externalisée de la globalité du poste pneumatique (Véhicules de transport de personnes)",
    "TRA-SE-110": "Gestion optimisée de la globalité du poste pneumatique (Véhicules de transport de marchandises)",
    "TRA-SE-111": "Gestion optimisée de la globalité du poste pneumatique (Véhicules de transport de personnes)",
    "TRA-SE-112": "Service d'autopartage en boucle",
    "TRA-SE-113": "Suivi des consommations de carburants grâce à des cartes privatives",
    "TRA-SE-116": "Fret ferroviaire",
    "TRA-SE-117": "Fret fluvial",
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


def get_zone_climatique(department: str) -> str:
    """Retourne la zone climatique pour un département donné."""
    return DEPARTEMENTS_FRANCE.get(department, "-")


def get_fiches_for_prefix(prefix: str) -> list:
    """
    Retourne la liste des fiches pour un préfixe donné.
    
    Args:
        prefix: Le préfixe (ex: "IND-UT-", "BAR-EN-")
    
    Returns:
        Liste de dicts avec 'code' et 'description'
    """
    fiches = []
    for code, description in FICHE_NAMES_MAPPING.items():
        if code.startswith(prefix.rstrip("-")):
            fiches.append({
                "code": code,
                "description": description
            })
    
    # Trier par code
    fiches.sort(key=lambda x: x["code"])
    return fiches