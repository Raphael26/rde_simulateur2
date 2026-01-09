"""
Service de connexion à Supabase.
Gère la connexion au client Supabase et les opérations sur le storage.
"""

import os
import json
from typing import Any, Optional
from dotenv import load_dotenv
from supabase import create_client, Client

load_dotenv()

# Configuration
SUPABASE_URL = os.getenv("SUPABASE_URL")
SUPABASE_KEY = os.getenv("SUPABASE_KEY")
BUCKET_NAME = "fiches-operations"

# Client Supabase global
_supabase_client: Optional[Client] = None


def get_supabase_client() -> Optional[Client]:
    """
    Retourne le client Supabase singleton.
    Initialise la connexion si nécessaire.
    """
    global _supabase_client
    
    if _supabase_client is not None:
        return _supabase_client
    
    if not SUPABASE_URL or not SUPABASE_KEY:
        print("❌ Variables d'environnement Supabase manquantes!")
        print("   Veuillez définir SUPABASE_URL et SUPABASE_KEY")
        return None
    
    try:
        _supabase_client = create_client(SUPABASE_URL, SUPABASE_KEY)
        print(f"✅ Client Supabase initialisé avec succès")
        return _supabase_client
    except Exception as e:
        print(f"❌ Erreur initialisation Supabase: {e}")
        return None


def read_file_from_bucket(
    bucket_name: str,
    file_path: str,
    file_type: str = "txt",
    encoding: str = "utf-8",
) -> Optional[Any]:
    """
    Lit un fichier depuis un bucket Supabase Storage.
    
    Args:
        bucket_name: Nom du bucket
        file_path: Chemin du fichier dans le bucket
        file_type: Type de fichier ('txt' ou 'json')
        encoding: Encodage du fichier texte
        
    Returns:
        Contenu du fichier (str ou dict) ou None en cas d'erreur
    """
    client = get_supabase_client()
    if client is None:
        return None
    
    try:
        print(f"📁 Lecture: {bucket_name}/{file_path}")
        raw = client.storage.from_(bucket_name).download(file_path)
        print(f"✅ Fichier téléchargé: {len(raw)} bytes")
        
        if file_type == "txt":
            return raw.decode(encoding)
        elif file_type == "json":
            return json.loads(raw.decode(encoding))
        else:
            return raw
            
    except Exception as e:
        print(f"❌ Erreur lecture fichier {file_path}: {e}")
        return None


def list_bucket_contents(bucket_name: str, folder: str = "") -> list:
    """
    Liste le contenu d'un bucket ou d'un dossier.
    
    Args:
        bucket_name: Nom du bucket
        folder: Dossier à lister (vide pour la racine)
        
    Returns:
        Liste des fichiers/dossiers
    """
    client = get_supabase_client()
    if client is None:
        return []
    
    try:
        contents = client.storage.from_(bucket_name).list(folder)
        return contents
    except Exception as e:
        print(f"❌ Erreur listing bucket: {e}")
        return []


def upload_file_to_bucket(
    bucket_name: str,
    file_path: str,
    file_content: bytes,
    content_type: str = "application/octet-stream"
) -> bool:
    """
    Upload un fichier vers un bucket Supabase Storage.
    
    Args:
        bucket_name: Nom du bucket
        file_path: Chemin de destination
        file_content: Contenu du fichier en bytes
        content_type: Type MIME du fichier
        
    Returns:
        True si succès, False sinon
    """
    client = get_supabase_client()
    if client is None:
        return False
    
    try:
        client.storage.from_(bucket_name).upload(
            file_path,
            file_content,
            {"content-type": content_type}
        )
        print(f"✅ Fichier uploadé: {file_path}")
        return True
    except Exception as e:
        print(f"❌ Erreur upload fichier: {e}")
        return False


# Test de connexion au démarrage
def test_connection():
    """Teste la connexion à Supabase."""
    client = get_supabase_client()
    if client:
        try:
            buckets = client.storage.list_buckets()
            bucket_names = [b.name for b in buckets]
            print(f"✅ Connexion Supabase OK - Buckets: {bucket_names}")
            return True
        except Exception as e:
            print(f"⚠️ Connexion Supabase partielle: {e}")
            return True
    return False
