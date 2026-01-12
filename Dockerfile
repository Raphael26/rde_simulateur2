# Dockerfile pour RDE Simulateur CEE sur Railway
# SOLUTION SIMPLE - Sans Caddy

FROM python:3.11-slim

# Installer les dépendances système
RUN apt-get update && apt-get install -y \
    curl \
    unzip \
    && rm -rf /var/lib/apt/lists/*

# Installer Node.js 20
RUN curl -fsSL https://deb.nodesource.com/setup_20.x | bash - \
    && apt-get install -y nodejs \
    && rm -rf /var/lib/apt/lists/*

# Définir le répertoire de travail
WORKDIR /app

# Copier les fichiers de dépendances
COPY requirements.txt .

# Installer les dépendances Python
RUN pip install --no-cache-dir --upgrade pip \
    && pip install --no-cache-dir -r requirements.txt

# Copier le reste du projet
COPY . .

# Rendre le script exécutable
RUN chmod +x start.sh

# Initialiser Reflex (prépare la structure)
RUN reflex init

# Variables d'environnement pour Reflex
ENV REFLEX_SKIP_COMPILE=true

# Exposer le port
EXPOSE 8080

# Utiliser le script de démarrage
CMD ["./start.sh"]