#!/bin/bash
# Script de démarrage pour Railway

# Utiliser le port fourni par Railway, ou 8080 par défaut
PORT=${PORT:-8080}

echo "🚀 Démarrage de RDE Simulateur CEE sur le port $PORT"

# Lancer Reflex en mode production
exec reflex run --env prod --backend-only --backend-host 0.0.0.0 --backend-port $PORT