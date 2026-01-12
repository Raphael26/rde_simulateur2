# Dockerfile pour RDE Simulateur CEE sur Railway
FROM python:3.11-slim

# Installer les dépendances système + Caddy
RUN apt-get update && apt-get install -y \
    curl \
    unzip \
    debian-keyring \
    debian-archive-keyring \
    apt-transport-https \
    gnupg \
    && curl -1sLf 'https://dl.cloudsmith.io/public/caddy/stable/gpg.key' | gpg --dearmor -o /usr/share/keyrings/caddy-stable-archive-keyring.gpg \
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

# Rendre le script exécutable
RUN chmod +x start.sh

# Initialiser et exporter le frontend Reflex
RUN reflex init && reflex export --frontend-only --no-zip

# Exposer le port
EXPOSE 8080

# Utiliser le script de démarrage
CMD ["./start.sh"]