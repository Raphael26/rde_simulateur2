#!/bin/bash
# Script de démarrage pour Railway - RDE Simulateur CEE

set -e

# Port public fourni par Railway
export PORT=${PORT:-8080}

echo "🚀 Démarrage de RDE Simulateur CEE"
echo "   Port public (Caddy): $PORT"
echo "   Port backend (Reflex): 8000"

# Lancer le backend Reflex en arrière-plan
echo "📦 Démarrage du backend Reflex..."
reflex run --env prod --backend-only --backend-host 0.0.0.0 --backend-port 8000 &
BACKEND_PID=$!

# Attendre que le backend soit prêt
echo "⏳ Attente du backend..."
sleep 10

# Vérifier que le backend répond
for i in {1..30}; do
    if curl -s http://127.0.0.1:8000/ping > /dev/null 2>&1; then
        echo "✅ Backend prêt!"
        break
    fi
    echo "   Tentative $i/30..."
    sleep 2
done

# Lancer Caddy
echo "🌐 Démarrage de Caddy sur le port $PORT..."
caddy run --config /app/Caddyfile --adapter caddyfile