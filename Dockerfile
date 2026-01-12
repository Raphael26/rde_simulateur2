# Dockerfile pour RDE Simulateur CEE sur Railway
FROM python:3.11-slim

# Installer les dépendances système
RUN apt-get update && \
    apt-get install -y --no-install-recommends unzip curl caddy && \
    apt-get clean && \
    rm -rf /var/lib/apt/lists/*

WORKDIR /app

# Copier et installer les dépendances Python
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# Copier le projet
COPY . .

# Initialiser et compiler le frontend Reflex
RUN reflex init && reflex export --frontend-only --no-zip

# Configuration
EXPOSE 8080
COPY Caddyfile /etc/caddy/Caddyfile

# Script de démarrage
RUN echo '#!/bin/bash\n\
set -e\n\
\n\
# Démarrer le backend Reflex\n\
reflex run --env prod --backend-only &\n\
\n\
# Attendre que le backend soit prêt\n\
for i in {1..30}; do\n\
  curl -s http://localhost:8000/ping > /dev/null 2>&1 && break\n\
  sleep 1\n\
done\n\
\n\
# Démarrer Caddy\n\
exec caddy run --config /etc/caddy/Caddyfile --adapter caddyfile\n\
' > /app/start.sh && chmod +x /app/start.sh

CMD ["/bin/bash", "/app/start.sh"]