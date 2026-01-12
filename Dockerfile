# Utilise une image Python officielle
FROM python:3.11-slim

# Installe les paquets système requis
RUN apt-get update && \
    apt-get install -y unzip curl caddy && \
    apt-get clean && \
    rm -rf /var/lib/apt/lists/*

# Crée un dossier de travail
WORKDIR /app

# Copie les fichiers du projet
COPY . .

# Installe les dépendances Python
RUN pip install --no-cache-dir -r requirements.txt

# Initialiser et pré-compiler le frontend
RUN reflex init
RUN reflex export --frontend-only --no-zip

# Debug: afficher la structure des fichiers statiques
RUN echo "=== Contenu de .web ===" && ls -la .web/ && \
    echo "=== Recherche index.html ===" && find .web -name "index.html" -type f

# Exposer le port
EXPOSE 8080

# Copier le Caddyfile
COPY Caddyfile /etc/caddy/Caddyfile

# Script de démarrage avec support $PORT
RUN echo '#!/bin/bash\n\
set -e\n\
\n\
# Utiliser PORT de Railway ou 8080 par défaut\n\
export PORT=${PORT:-8080}\n\
export BACKEND_PORT=8000\n\
echo "Port public: $PORT"\n\
echo "Backend port: $BACKEND_PORT"\n\
\n\
# Mettre à jour le Caddyfile avec le bon port\n\
sed -i "s/:8080/:$PORT/g" /etc/caddy/Caddyfile\n\
\n\
echo "Starting Reflex backend on port 8000..."\n\
reflex run --env prod --backend-only --loglevel debug &\n\
BACKEND_PID=$!\n\
\n\
# Wait for backend to be ready\n\
echo "Waiting for backend to start..."\n\
for i in {1..30}; do\n\
  if curl -s http://localhost:8000/ping > /dev/null 2>&1; then\n\
    echo "Backend is ready!"\n\
    break\n\
  fi\n\
  echo "Waiting... ($i/30)"\n\
  sleep 1\n\
done\n\
\n\
echo "=== Debug: Contenu de /app/.web ==="\n\
ls -la /app/.web/ || echo "Pas de .web"\n\
ls -la /app/.web/build/client/ 2>/dev/null || ls -la /app/.web/_static/ 2>/dev/null || echo "Pas de fichiers statiques"\n\
\n\
echo "Starting Caddy on port $PORT..."\n\
exec caddy run --config /etc/caddy/Caddyfile --adapter caddyfile\n\
' > /app/start.sh && chmod +x /app/start.sh

CMD ["/bin/bash", "/app/start.sh"]