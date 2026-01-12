#!/bin/bash
# Script de démarrage avec Caddy - RDE Simulateur CEE
# NOTE: Utilisez ce fichier SEULEMENT si la solution simple ne fonctionne pas

set -e

# Ports
export PORT=${PORT:-8080}
export BACKEND_PORT=8000

echo "🚀 Démarrage de RDE Simulateur CEE avec Caddy"
echo "📍 Caddy Port: $PORT"
echo "📍 Backend Port: $BACKEND_PORT"

# Exporter le frontend uniquement
echo "🔨 Export du frontend..."
reflex export --frontend-only

# Lancer le backend Reflex en arrière-plan
echo "🔧 Démarrage du backend Reflex..."
reflex run --env prod --backend-only --backend-host 127.0.0.1 --backend-port $BACKEND_PORT &

# Attendre que le backend soit prêt
echo "⏳ Attente du backend..."
sleep 10

# Vérifier que le backend répond
MAX_RETRIES=30
RETRY_COUNT=0
while ! curl -s http://127.0.0.1:$BACKEND_PORT/ping > /dev/null; do
    RETRY_COUNT=$((RETRY_COUNT + 1))
    if [ $RETRY_COUNT -ge $MAX_RETRIES ]; then
        echo "❌ Le backend ne répond pas après $MAX_RETRIES tentatives"
        exit 1
    fi
    echo "⏳ Backend pas encore prêt (tentative $RETRY_COUNT/$MAX_RETRIES)..."
    sleep 2
done

echo "✅ Backend prêt!"

# Lancer Caddy en premier plan
echo "🌐 Démarrage de Caddy..."
exec caddy run --config /app/Caddyfile --adapter caddyfile