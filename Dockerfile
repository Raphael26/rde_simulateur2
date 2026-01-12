# Dockerfile pour RDE Simulateur CEE sur Railway
FROM python:3.11-slim

# Installer les dépendances système
RUN apt-get update && apt-get install -y \
    curl \
    unzip \
    nodejs \
    npm \
    && rm -rf /var/lib/apt/lists/*

# Installer Node.js 20 (version LTS)
RUN curl -fsSL https://deb.nodesource.com/setup_20.x | bash - \
    && apt-get install -y nodejs

# Définir le répertoire de travail
WORKDIR /app

# Copier les fichiers de dépendances
COPY requirements.txt .

# Installer les dépendances Python
RUN pip install --no-cache-dir --upgrade pip \
    && pip install --no-cache-dir -r requirements.txt

# Copier le reste du projet
COPY . .

# Initialiser Reflex et exporter le frontend
RUN reflex init \
    && reflex export --frontend-only --no-zip

# Exposer le port (Railway injecte $PORT)
EXPOSE 8080

# Commande de démarrage
CMD reflex run --env prod --backend-only --backend-host 0.0.0.0 --backend-port ${PORT:-8080}