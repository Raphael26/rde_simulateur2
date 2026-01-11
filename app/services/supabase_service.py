"""
Service Supabase amélioré pour l'authentification et l'accès aux données.
Gère la connexion, l'authentification et les opérations CRUD.
"""

#import os
#from typing import Optional, Any, Dict
#from dotenv import load_dotenv
#
## Charger les variables d'environnement
#load_dotenv()
#
## Configuration
#SUPABASE_URL = os.getenv("SUPABASE_URL", "")
#SUPABASE_KEY = os.getenv("SUPABASE_KEY", "")  # Clé anon (publique)
#SUPABASE_SERVICE_KEY = os.getenv("SUPABASE_SERVICE_KEY", "")  # Clé service (optionnelle, pour admin)
#
## Client Supabase global
#_supabase_client = None
#_supabase_available = False
#
## Vérifier si Supabase est disponible
#try:
#    from supabase import create_client, Client
#    _supabase_available = True
#except ImportError:
#    print("⚠️ Supabase SDK non installé. Exécutez: pip install supabase")
#    Client = None
#
#
#def get_supabase_client() -> Optional[Any]:
#    """
#    Retourne le client Supabase singleton.
#    Initialise la connexion si nécessaire.
#    
#    Returns:
#        Client Supabase ou None si non configuré
#    """
#    global _supabase_client
#    
#    if not _supabase_available:
#        print("❌ Supabase SDK non disponible")
#        return None
#    
#    if _supabase_client is not None:
#        return _supabase_client
#    
#    if not SUPABASE_URL or not SUPABASE_KEY:
#        print("❌ Variables d'environnement Supabase manquantes!")
#        print("   Veuillez définir SUPABASE_URL et SUPABASE_KEY dans votre fichier .env")
#        return None
#    
#    try:
#        _supabase_client = create_client(SUPABASE_URL, SUPABASE_KEY)
#        print(f"✅ Client Supabase initialisé avec succès")
#        return _supabase_client
#    except Exception as e:
#        print(f"❌ Erreur initialisation Supabase: {e}")
#        return None
#
#
#def check_supabase_connection() -> Dict[str, Any]:
#    """
#    Vérifie la connexion à Supabase et retourne le statut.
#    
#    Returns:
#        Dict avec 'connected', 'message', et 'details'
#    """
#    result = {
#        "connected": False,
#        "message": "",
#        "details": {}
#    }
#    
#    if not _supabase_available:
#        result["message"] = "Supabase SDK non installé"
#        return result
#    
#    if not SUPABASE_URL or not SUPABASE_KEY:
#        result["message"] = "Variables d'environnement manquantes"
#        result["details"] = {
#            "SUPABASE_URL": "✓" if SUPABASE_URL else "✗ Manquant",
#            "SUPABASE_KEY": "✓" if SUPABASE_KEY else "✗ Manquant",
#        }
#        return result
#    
#    client = get_supabase_client()
#    if not client:
#        result["message"] = "Impossible de créer le client Supabase"
#        return result
#    
#    try:
#        # Tester la connexion avec une requête simple
#        response = client.table("simulations").select("id").limit(1).execute()
#        result["connected"] = True
#        result["message"] = "Connexion Supabase OK"
#        return result
#    except Exception as e:
#        result["message"] = f"Erreur de connexion: {str(e)}"
#        return result
#
#
## ============================================
## FONCTIONS D'AUTHENTIFICATION
## ============================================
#
#def sign_up(email: str, password: str, full_name: str = "") -> Dict[str, Any]:
#    """
#    Inscrit un nouvel utilisateur.
#    
#    Args:
#        email: Adresse email
#        password: Mot de passe
#        full_name: Nom complet (optionnel)
#    
#    Returns:
#        Dict avec 'success', 'user', 'session', 'error'
#    """
#    client = get_supabase_client()
#    if not client:
#        return {"success": False, "error": "Service indisponible"}
#    
#    try:
#        options = {}
#        if full_name:
#            options["data"] = {"full_name": full_name}
#        
#        response = client.auth.sign_up({
#            "email": email,
#            "password": password,
#            "options": options if options else None
#        })
#        
#        if response.user:
#            return {
#                "success": True,
#                "user": response.user,
#                "session": response.session,
#                "error": None
#            }
#        else:
#            return {"success": False, "error": "Erreur lors de l'inscription"}
#            
#    except Exception as e:
#        error_str = str(e)
#        if "User already registered" in error_str:
#            return {"success": False, "error": "Cette adresse email est déjà utilisée"}
#        return {"success": False, "error": error_str}
#
#
#def sign_in(email: str, password: str) -> Dict[str, Any]:
#    """
#    Connecte un utilisateur.
#    
#    Args:
#        email: Adresse email
#        password: Mot de passe
#    
#    Returns:
#        Dict avec 'success', 'user', 'session', 'error'
#    """
#    client = get_supabase_client()
#    if not client:
#        return {"success": False, "error": "Service indisponible"}
#    
#    try:
#        response = client.auth.sign_in_with_password({
#            "email": email,
#            "password": password
#        })
#        
#        if response.user and response.session:
#            return {
#                "success": True,
#                "user": response.user,
#                "session": response.session,
#                "error": None
#            }
#        else:
#            return {"success": False, "error": "Identifiants incorrects"}
#            
#    except Exception as e:
#        error_str = str(e)
#        if "Invalid login credentials" in error_str:
#            return {"success": False, "error": "Email ou mot de passe incorrect"}
#        if "Email not confirmed" in error_str:
#            return {"success": False, "error": "Veuillez confirmer votre email"}
#        return {"success": False, "error": error_str}
#
#
#def sign_out() -> Dict[str, Any]:
#    """
#    Déconnecte l'utilisateur actuel.
#    
#    Returns:
#        Dict avec 'success' et 'error'
#    """
#    client = get_supabase_client()
#    if not client:
#        return {"success": True, "error": None}  # Pas de client = déjà déconnecté
#    
#    try:
#        client.auth.sign_out()
#        return {"success": True, "error": None}
#    except Exception as e:
#        print(f"⚠️ Erreur déconnexion: {e}")
#        return {"success": True, "error": None}  # On considère comme déconnecté
#
#
#def get_current_user() -> Dict[str, Any]:
#    """
#    Récupère l'utilisateur actuellement connecté.
#    
#    Returns:
#        Dict avec 'user', 'session', ou None si non connecté
#    """
#    client = get_supabase_client()
#    if not client:
#        return {"user": None, "session": None}
#    
#    try:
#        response = client.auth.get_session()
#        if response and response.user:
#            return {
#                "user": response.user,
#                "session": response
#            }
#        return {"user": None, "session": None}
#    except Exception as e:
#        print(f"⚠️ Erreur récupération session: {e}")
#        return {"user": None, "session": None}
#
#
#def reset_password(email: str) -> Dict[str, Any]:
#    """
#    Envoie un email de réinitialisation de mot de passe.
#    
#    Args:
#        email: Adresse email
#    
#    Returns:
#        Dict avec 'success' et 'message'
#    """
#    client = get_supabase_client()
#    if not client:
#        return {"success": False, "message": "Service indisponible"}
#    
#    try:
#        client.auth.reset_password_for_email(email)
#        # Message générique pour ne pas révéler si l'email existe
#        return {
#            "success": True,
#            "message": "Si cette adresse existe, vous recevrez un email de réinitialisation."
#        }
#    except Exception as e:
#        print(f"⚠️ Erreur reset password: {e}")
#        return {
#            "success": True,
#            "message": "Si cette adresse existe, vous recevrez un email de réinitialisation."
#        }
#
#
## ============================================
## FONCTIONS CRUD POUR LES SIMULATIONS
## ============================================
#
#def create_simulation(user_id: str, data: Dict[str, Any]) -> Dict[str, Any]:
#    """
#    Crée une nouvelle simulation.
#    
#    Args:
#        user_id: ID de l'utilisateur
#        data: Données de la simulation
#    
#    Returns:
#        Dict avec 'success', 'data', 'error'
#    """
#    client = get_supabase_client()
#    if not client:
#        return {"success": False, "error": "Service indisponible"}
#    
#    try:
#        # S'assurer que user_id est dans les données
#        data["user_id"] = user_id
#        
#        response = client.table("simulations").insert(data).execute()
#        
#        if response.data:
#            return {"success": True, "data": response.data[0], "error": None}
#        else:
#            return {"success": False, "error": "Erreur lors de la création"}
#            
#    except Exception as e:
#        return {"success": False, "error": str(e)}
#
#
#def get_user_simulations(user_id: str, limit: int = 50) -> Dict[str, Any]:
#    """
#    Récupère les simulations d'un utilisateur.
#    
#    Args:
#        user_id: ID de l'utilisateur
#        limit: Nombre maximum de résultats
#    
#    Returns:
#        Dict avec 'success', 'data', 'error'
#    """
#    client = get_supabase_client()
#    if not client:
#        return {"success": False, "data": [], "error": "Service indisponible"}
#    
#    try:
#        response = client.table("simulations")\
#            .select("*")\
#            .eq("user_id", user_id)\
#            .eq("is_deleted", False)\
#            .order("created_at", desc=True)\
#            .limit(limit)\
#            .execute()
#        
#        return {"success": True, "data": response.data or [], "error": None}
#        
#    except Exception as e:
#        return {"success": False, "data": [], "error": str(e)}
#
#
#def delete_simulation(simulation_id: str, user_id: str) -> Dict[str, Any]:
#    """
#    Supprime une simulation (soft delete).
#    
#    Args:
#        simulation_id: ID de la simulation
#        user_id: ID de l'utilisateur (pour vérification)
#    
#    Returns:
#        Dict avec 'success' et 'error'
#    """
#    client = get_supabase_client()
#    if not client:
#        return {"success": False, "error": "Service indisponible"}
#    
#    try:
#        # Soft delete (marquer comme supprimé)
#        response = client.table("simulations")\
#            .update({"is_deleted": True})\
#            .eq("id", simulation_id)\
#            .eq("user_id", user_id)\
#            .execute()
#        
#        return {"success": True, "error": None}
#        
#    except Exception as e:
#        return {"success": False, "error": str(e)}
#
#
## ============================================
## INITIALISATION
## ============================================
#
## Créer le client au chargement du module
#supabase = get_supabase_client()
#
## Afficher le statut de connexion
#if __name__ == "__main__":
#    status = check_supabase_connection()
#    print(f"\n{'='*50}")
#    print("STATUT SUPABASE")
#    print(f"{'='*50}")
#    print(f"Connecté: {status['connected']}")
#    print(f"Message: {status['message']}")
#    if status['details']:
#        print("Détails:")
#        for key, value in status['details'].items():
#            print(f"  - {key}: {value}")
#    print(f"{'='*50}\n")


"""
Service Supabase amélioré pour l'authentification et l'accès aux données.
Gère la connexion, l'authentification et les opérations CRUD.

Deux clients disponibles :
- get_supabase_client() : client anon pour l'authentification
- get_service_client() : client service_role pour les opérations DB (bypass RLS)
"""

import os
from typing import Optional, Any, Dict
from dotenv import load_dotenv

# Charger les variables d'environnement
load_dotenv()

# Configuration
SUPABASE_URL = os.getenv("SUPABASE_URL", "")
SUPABASE_KEY = os.getenv("SUPABASE_KEY", "")  # Clé anon (publique)
SUPABASE_SERVICE_KEY = os.getenv("SUPABASE_SERVICE_KEY", "")  # Clé service (pour bypass RLS)

# Clients Supabase globaux
_supabase_client = None
_service_client = None
_supabase_available = False

# Vérifier si Supabase est disponible
try:
    from supabase import create_client, Client
    _supabase_available = True
except ImportError:
    print("⚠️ Supabase SDK non installé. Exécutez: pip install supabase")
    Client = None


def get_supabase_client() -> Optional[Any]:
    """
    Retourne le client Supabase singleton avec clé anon.
    Utilisé pour l'authentification (sign_in, sign_up, etc.)
    
    Returns:
        Client Supabase ou None si non configuré
    """
    global _supabase_client
    
    if not _supabase_available:
        print("❌ Supabase SDK non disponible")
        return None
    
    if _supabase_client is not None:
        return _supabase_client
    
    if not SUPABASE_URL or not SUPABASE_KEY:
        print("❌ Variables d'environnement Supabase manquantes!")
        print("   Veuillez définir SUPABASE_URL et SUPABASE_KEY dans votre fichier .env")
        return None
    
    try:
        _supabase_client = create_client(SUPABASE_URL, SUPABASE_KEY)
        print(f"✅ Client Supabase (anon) initialisé avec succès")
        return _supabase_client
    except Exception as e:
        print(f"❌ Erreur initialisation Supabase: {e}")
        return None


def get_service_client() -> Optional[Any]:
    """
    Retourne le client Supabase avec clé service_role.
    Utilisé pour les opérations de base de données (bypass RLS).
    
    ⚠️ IMPORTANT: Ce client bypass RLS !
    Toujours vérifier l'authentification dans le code avant d'utiliser.
    
    Returns:
        Client Supabase service ou None si non configuré
    """
    global _service_client
    
    if not _supabase_available:
        print("❌ Supabase SDK non disponible")
        return None
    
    if _service_client is not None:
        return _service_client
    
    if not SUPABASE_URL:
        print("❌ SUPABASE_URL manquant")
        return None
    
    # Utiliser service_key si disponible, sinon fallback sur anon key
    key_to_use = SUPABASE_SERVICE_KEY or SUPABASE_KEY
    
    if not key_to_use:
        print("❌ Aucune clé Supabase configurée")
        return None
    
    try:
        _service_client = create_client(SUPABASE_URL, key_to_use)
        if SUPABASE_SERVICE_KEY:
            print(f"✅ Client Supabase (service_role) initialisé - RLS bypassé")
        else:
            print(f"⚠️ Client Supabase (anon) initialisé - RLS actif")
        return _service_client
    except Exception as e:
        print(f"❌ Erreur initialisation service client: {e}")
        return None


def check_supabase_connection() -> Dict[str, Any]:
    """
    Vérifie la connexion à Supabase et retourne le statut.
    
    Returns:
        Dict avec 'connected', 'message', et 'details'
    """
    result = {
        "connected": False,
        "message": "",
        "details": {}
    }
    
    if not _supabase_available:
        result["message"] = "Supabase SDK non installé"
        return result
    
    if not SUPABASE_URL or not SUPABASE_KEY:
        result["message"] = "Variables d'environnement manquantes"
        result["details"] = {
            "SUPABASE_URL": "✓" if SUPABASE_URL else "✗ Manquant",
            "SUPABASE_KEY": "✓" if SUPABASE_KEY else "✗ Manquant",
            "SUPABASE_SERVICE_KEY": "✓" if SUPABASE_SERVICE_KEY else "✗ Non configuré (optionnel)",
        }
        return result
    
    client = get_supabase_client()
    if not client:
        result["message"] = "Impossible de créer le client Supabase"
        return result
    
    try:
        # Tester la connexion avec une requête simple
        response = client.table("simulations").select("id").limit(1).execute()
        result["connected"] = True
        result["message"] = "Connexion Supabase OK"
        result["details"] = {
            "service_key_configured": bool(SUPABASE_SERVICE_KEY),
        }
        return result
    except Exception as e:
        result["message"] = f"Erreur de connexion: {str(e)}"
        return result


# ============================================
# FONCTIONS D'AUTHENTIFICATION
# ============================================

def sign_up(email: str, password: str, full_name: str = "") -> Dict[str, Any]:
    """
    Inscrit un nouvel utilisateur.
    
    Args:
        email: Adresse email
        password: Mot de passe
        full_name: Nom complet (optionnel)
    
    Returns:
        Dict avec 'success', 'user', 'session', 'error'
    """
    client = get_supabase_client()
    if not client:
        return {"success": False, "error": "Service indisponible"}
    
    try:
        options = {}
        if full_name:
            options["data"] = {"full_name": full_name}
        
        response = client.auth.sign_up({
            "email": email,
            "password": password,
            "options": options if options else None
        })
        
        if response.user:
            return {
                "success": True,
                "user": response.user,
                "session": response.session,
                "error": None
            }
        else:
            return {"success": False, "error": "Erreur lors de l'inscription"}
            
    except Exception as e:
        error_str = str(e)
        if "User already registered" in error_str:
            return {"success": False, "error": "Cette adresse email est déjà utilisée"}
        return {"success": False, "error": error_str}


def sign_in(email: str, password: str) -> Dict[str, Any]:
    """
    Connecte un utilisateur.
    
    Args:
        email: Adresse email
        password: Mot de passe
    
    Returns:
        Dict avec 'success', 'user', 'session', 'error'
    """
    client = get_supabase_client()
    if not client:
        return {"success": False, "error": "Service indisponible"}
    
    try:
        response = client.auth.sign_in_with_password({
            "email": email,
            "password": password
        })
        
        if response.user and response.session:
            return {
                "success": True,
                "user": response.user,
                "session": response.session,
                "error": None
            }
        else:
            return {"success": False, "error": "Identifiants incorrects"}
            
    except Exception as e:
        error_str = str(e)
        if "Invalid login credentials" in error_str:
            return {"success": False, "error": "Email ou mot de passe incorrect"}
        if "Email not confirmed" in error_str:
            return {"success": False, "error": "Veuillez confirmer votre email"}
        return {"success": False, "error": error_str}


def sign_out() -> Dict[str, Any]:
    """
    Déconnecte l'utilisateur actuel.
    
    Returns:
        Dict avec 'success' et 'error'
    """
    client = get_supabase_client()
    if not client:
        return {"success": True, "error": None}  # Pas de client = déjà déconnecté
    
    try:
        client.auth.sign_out()
        return {"success": True, "error": None}
    except Exception as e:
        print(f"⚠️ Erreur déconnexion: {e}")
        return {"success": True, "error": None}  # On considère comme déconnecté


def get_current_user() -> Dict[str, Any]:
    """
    Récupère l'utilisateur actuellement connecté.
    
    Returns:
        Dict avec 'user', 'session', ou None si non connecté
    """
    client = get_supabase_client()
    if not client:
        return {"user": None, "session": None}
    
    try:
        response = client.auth.get_session()
        if response and response.user:
            return {
                "user": response.user,
                "session": response
            }
        return {"user": None, "session": None}
    except Exception as e:
        print(f"⚠️ Erreur récupération session: {e}")
        return {"user": None, "session": None}


def reset_password(email: str) -> Dict[str, Any]:
    """
    Envoie un email de réinitialisation de mot de passe.
    
    Args:
        email: Adresse email
    
    Returns:
        Dict avec 'success' et 'message'
    """
    client = get_supabase_client()
    if not client:
        return {"success": False, "message": "Service indisponible"}
    
    try:
        client.auth.reset_password_for_email(email)
        # Message générique pour ne pas révéler si l'email existe
        return {
            "success": True,
            "message": "Si cette adresse existe, vous recevrez un email de réinitialisation."
        }
    except Exception as e:
        print(f"⚠️ Erreur reset password: {e}")
        return {
            "success": True,
            "message": "Si cette adresse existe, vous recevrez un email de réinitialisation."
        }


# ============================================
# FONCTIONS CRUD POUR LES SIMULATIONS
# ============================================

def create_simulation(user_id: str, data: Dict[str, Any]) -> Dict[str, Any]:
    """
    Crée une nouvelle simulation.
    Utilise le service client pour bypasser RLS.
    
    Args:
        user_id: ID de l'utilisateur
        data: Données de la simulation
    
    Returns:
        Dict avec 'success', 'data', 'error'
    """
    # Utiliser le service client pour bypasser RLS
    client = get_service_client()
    if not client:
        return {"success": False, "error": "Service indisponible"}
    
    try:
        # S'assurer que user_id est dans les données
        data["user_id"] = user_id
        
        response = client.table("simulations").insert(data).execute()
        
        if response.data:
            return {"success": True, "data": response.data[0], "error": None}
        else:
            return {"success": False, "error": "Erreur lors de la création"}
            
    except Exception as e:
        return {"success": False, "error": str(e)}


def get_user_simulations(user_id: str, limit: int = 50) -> Dict[str, Any]:
    """
    Récupère les simulations d'un utilisateur.
    Utilise le service client pour bypasser RLS.
    
    Args:
        user_id: ID de l'utilisateur
        limit: Nombre maximum de résultats
    
    Returns:
        Dict avec 'success', 'data', 'error'
    """
    # Utiliser le service client pour bypasser RLS
    client = get_service_client()
    if not client:
        return {"success": False, "data": [], "error": "Service indisponible"}
    
    try:
        response = client.table("simulations")\
            .select("*")\
            .eq("user_id", user_id)\
            .order("created_at", desc=True)\
            .limit(limit)\
            .execute()
        
        return {"success": True, "data": response.data or [], "error": None}
        
    except Exception as e:
        return {"success": False, "data": [], "error": str(e)}


def delete_simulation(simulation_id: str, user_id: str) -> Dict[str, Any]:
    """
    Supprime une simulation.
    Utilise le service client pour bypasser RLS.
    
    Args:
        simulation_id: ID de la simulation
        user_id: ID de l'utilisateur (pour vérification)
    
    Returns:
        Dict avec 'success' et 'error'
    """
    # Utiliser le service client pour bypasser RLS
    client = get_service_client()
    if not client:
        return {"success": False, "error": "Service indisponible"}
    
    try:
        # Supprimer la simulation
        response = client.table("simulations")\
            .delete()\
            .eq("id", simulation_id)\
            .eq("user_id", user_id)\
            .execute()
        
        return {"success": True, "error": None}
        
    except Exception as e:
        return {"success": False, "error": str(e)}


# ============================================
# INITIALISATION
# ============================================

# Créer le client au chargement du module
supabase = get_supabase_client()

# Afficher le statut de connexion
if __name__ == "__main__":
    status = check_supabase_connection()
    print(f"\n{'='*50}")
    print("STATUT SUPABASE")
    print(f"{'='*50}")
    print(f"Connecté: {status['connected']}")
    print(f"Message: {status['message']}")
    if status['details']:
        print("Détails:")
        for key, value in status['details'].items():
            print(f"  - {key}: {value}")
    print(f"{'='*50}\n")