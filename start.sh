#!/bin/bash
# Script de démarrage pour Railway - RDE Simulateur CEE

set -e

# Utiliser le port fourni par Railway, ou 8080 par défaut
export PORT=${PORT:-8080}

echo "🚀 Démarrage de RDE Simulateur CEE sur le port $PORT"
echo "📍 Backend Host: 0.0.0.0"
echo "📍 Backend Port: $PORT"

# Export du frontend avant le démarrage
echo "🔨 Export du frontend..."
reflex export --frontend-only

# Lancer Reflex en mode production
echo "🚀 Démarrage du serveur..."
exec reflex run --env prod --backend-host 0.0.0.0 --backend-port $PORT --frontend-port $PORT