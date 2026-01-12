#!/bin/bash
# Script de démarrage pour Railway - RDE Simulateur CEE

set -e

# Utiliser le port fourni par Railway, ou 8080 par défaut
export PORT=${PORT:-8080}

echo "🚀 Démarrage de RDE Simulateur CEE"
echo "   Port public: $PORT"
echo "   Backend Reflex: localhost:8000"

# Fonction de nettoyage
cleanup() {
    echo "🛑 Arrêt des services..."
    kill $BACKEND_PID 2>/dev/null || true
    exit 0
}
trap cleanup SIGTERM SIGINT

# Lancer le backend Reflex en arrière-plan sur le port 8000
echo "📦 Démarrage du backend Reflex..."
reflex run --env prod --backend-only --backend-host 127.0.0.1 --backend-port 8000 &
BACKEND_PID=$!

# Attendre que le backend soit prêt
echo "⏳ Attente du backend..."
for i in {1..30}; do
    if curl -s http://127.0.0.1:8000/ping > /dev/null 2>&1; then
        echo "✅ Backend prêt!"
        break
    fi
    sleep 1
done

# Lancer Caddy (reverse proxy + frontend statique)
echo "🌐 Démarrage de Caddy sur le port $PORT..."
caddy run --config /app/Caddyfile --adapter caddyfile &
CADDY_PID=$!

# Attendre que l'un des processus se termine
wait -n $BACKEND_PID $CADDY_PID

# Si un processus se termine, arrêter l'autre
cleanup