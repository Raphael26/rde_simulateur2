"""Service Supabase pour l'accès à la base de données"""
import os
from typing import Optional

try:
    from supabase import create_client, Client
    SUPABASE_AVAILABLE = True
except ImportError:
    SUPABASE_AVAILABLE = False
    Client = None

# Variables d'environnement
SUPABASE_URL = os.environ.get("SUPABASE_URL", "")
SUPABASE_KEY = os.environ.get("SUPABASE_KEY", "")

# Client Supabase global
supabase: Optional[Client] = None

def get_supabase_client() -> Optional[Client]:
    """Retourne le client Supabase ou None si non configuré."""
    global supabase
    
    if not SUPABASE_AVAILABLE:
        print("⚠️ Supabase SDK not installed. Run: pip install supabase")
        return None
    
    if not SUPABASE_URL or not SUPABASE_KEY:
        print("⚠️ SUPABASE_URL ou SUPABASE_KEY non configuré")
        return None
    
    if supabase is None:
        try:
            supabase = create_client(SUPABASE_URL, SUPABASE_KEY)
            print("✅ Supabase client créé avec succès!")
        except Exception as e:
            print(f"❌ Erreur création client Supabase: {e}")
            return None
    
    return supabase

# Initialiser au chargement du module
supabase = get_supabase_client()