#!/bin/bash
# Script de démarrage pour Railway - RDE Simulateur CEE

set -e

# Utiliser le port fourni par Railway, ou 8080 par défaut
export PORT=${PORT:-8080}

echo "🚀 Démarrage de RDE Simulateur CEE sur le port $PORT"

# Lancer Reflex en mode production (frontend + backend ensemble)
exec reflex run --env prod --backend-host 0.0.0.0 --backend-port $PORT