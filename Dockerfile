# Dockerfile avec Caddy pour RDE Simulateur CEE sur Railway
# NOTE: Utilisez ce fichier SEULEMENT si la solution simple ne fonctionne pas

FROM python:3.11-slim

# Installer les dépendances système
RUN apt-get update && apt-get install -y \
    curl \
    unzip \
    debian-keyring \
    debian-archive-keyring \
    apt-transport-https \
    && rm -rf /var/lib/apt/lists/*

# Installer Caddy
RUN curl -1sLf 'https://dl.cloudsmith.io/public/caddy/stable/gpg.key' | gpg --dearmor -o /usr/share/keyrings/caddy-stable-archive-keyring.gpg \
    && curl -1sLf 'https://dl.cloudsmith.io/public/caddy/stable/debian.deb.txt' | tee /etc/apt/sources.list.d/caddy-stable.list \
    && apt-get update \
    && apt-get install -y caddy \
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

# Rendre les scripts exécutables
RUN chmod +x start.sh start_with_caddy.sh

# Initialiser Reflex (prépare la structure)
RUN reflex init

# Variables d'environnement pour Reflex
ENV REFLEX_SKIP_COMPILE=true

# Exposer le port
EXPOSE 8080

# Utiliser le script de démarrage avec Caddy
CMD ["./start_with_caddy.sh"]