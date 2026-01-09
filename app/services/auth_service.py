"""
Service d'authentification avec Supabase Auth.
Gère l'inscription, la connexion, la déconnexion et la réinitialisation de mot de passe.
"""

import os
import re
from typing import Optional, Tuple, Dict, Any
from dataclasses import dataclass
from dotenv import load_dotenv
from .supabase_client import get_supabase_client

load_dotenv()


@dataclass
class AuthResult:
    """Résultat d'une opération d'authentification."""
    success: bool
    message: str
    user_id: Optional[str] = None
    email: Optional[str] = None
    access_token: Optional[str] = None
    refresh_token: Optional[str] = None
    user_data: Optional[Dict[str, Any]] = None


class AuthService:
    """Service d'authentification Supabase."""
    
    # Regex pour validation email
    EMAIL_REGEX = re.compile(r'^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$')
    
    # Critères mot de passe
    MIN_PASSWORD_LENGTH = 8
    
    @staticmethod
    def validate_email(email: str) -> Tuple[bool, str]:
        """Valide le format de l'email."""
        if not email:
            return False, "L'email est requis"
        if not AuthService.EMAIL_REGEX.match(email):
            return False, "Format d'email invalide"
        return True, ""
    
    @staticmethod
    def validate_password(password: str) -> Tuple[bool, str]:
        """
        Valide la force du mot de passe.
        Critères: min 8 caractères, 1 majuscule, 1 chiffre, 1 caractère spécial.
        """
        if not password:
            return False, "Le mot de passe est requis"
        
        if len(password) < AuthService.MIN_PASSWORD_LENGTH:
            return False, f"Le mot de passe doit contenir au moins {AuthService.MIN_PASSWORD_LENGTH} caractères"
        
        if not re.search(r'[A-Z]', password):
            return False, "Le mot de passe doit contenir au moins une majuscule"
        
        if not re.search(r'[0-9]', password):
            return False, "Le mot de passe doit contenir au moins un chiffre"
        
        if not re.search(r'[!@#$%^&*(),.?":{}|<>]', password):
            return False, "Le mot de passe doit contenir au moins un caractère spécial (!@#$%^&*...)"
        
        return True, ""
    
    @staticmethod
    def validate_passwords_match(password: str, confirm_password: str) -> Tuple[bool, str]:
        """Vérifie que les deux mots de passe correspondent."""
        if password != confirm_password:
            return False, "Les mots de passe ne correspondent pas"
        return True, ""
    
    @staticmethod
    def register(
        email: str,
        password: str,
        confirm_password: str,
        full_name: str,
        accept_terms: bool = False
    ) -> AuthResult:
        """
        Inscrit un nouvel utilisateur.
        
        Args:
            email: Adresse email
            password: Mot de passe
            confirm_password: Confirmation du mot de passe
            full_name: Nom complet
            accept_terms: Acceptation des CGU
            
        Returns:
            AuthResult avec le statut de l'opération
        """
        # Validation des CGU
        if not accept_terms:
            return AuthResult(
                success=False,
                message="Vous devez accepter les conditions d'utilisation"
            )
        
        # Validation du nom
        if not full_name or len(full_name.strip()) < 2:
            return AuthResult(
                success=False,
                message="Le nom complet est requis (minimum 2 caractères)"
            )
        
        # Validation email
        valid, msg = AuthService.validate_email(email)
        if not valid:
            return AuthResult(success=False, message=msg)
        
        # Validation mot de passe
        valid, msg = AuthService.validate_password(password)
        if not valid:
            return AuthResult(success=False, message=msg)
        
        # Vérification correspondance mots de passe
        valid, msg = AuthService.validate_passwords_match(password, confirm_password)
        if not valid:
            return AuthResult(success=False, message=msg)
        
        # Inscription via Supabase
        client = get_supabase_client()
        if client is None:
            return AuthResult(
                success=False,
                message="Service d'authentification indisponible"
            )
        
        try:
            response = client.auth.sign_up({
                "email": email,
                "password": password,
                "options": {
                    "data": {
                        "full_name": full_name.strip()
                    }
                }
            })
            
            if response.user:
                return AuthResult(
                    success=True,
                    message="Inscription réussie ! Vérifiez votre email pour confirmer votre compte.",
                    user_id=response.user.id,
                    email=response.user.email,
                    access_token=response.session.access_token if response.session else None,
                    refresh_token=response.session.refresh_token if response.session else None
                )
            else:
                return AuthResult(
                    success=False,
                    message="Erreur lors de l'inscription"
                )
                
        except Exception as e:
            error_msg = str(e)
            if "User already registered" in error_msg:
                return AuthResult(
                    success=False,
                    message="Cette adresse email est déjà utilisée"
                )
            print(f"❌ Erreur inscription: {e}")
            return AuthResult(
                success=False,
                message=f"Erreur lors de l'inscription: {error_msg}"
            )
    
    @staticmethod
    def login(email: str, password: str) -> AuthResult:
        """
        Connecte un utilisateur.
        
        Args:
            email: Adresse email
            password: Mot de passe
            
        Returns:
            AuthResult avec le statut de l'opération
        """
        # Validation email
        valid, msg = AuthService.validate_email(email)
        if not valid:
            return AuthResult(success=False, message=msg)
        
        if not password:
            return AuthResult(success=False, message="Le mot de passe est requis")
        
        client = get_supabase_client()
        if client is None:
            return AuthResult(
                success=False,
                message="Service d'authentification indisponible"
            )
        
        try:
            response = client.auth.sign_in_with_password({
                "email": email,
                "password": password
            })
            
            if response.user and response.session:
                user_metadata = response.user.user_metadata or {}
                return AuthResult(
                    success=True,
                    message="Connexion réussie",
                    user_id=response.user.id,
                    email=response.user.email,
                    access_token=response.session.access_token,
                    refresh_token=response.session.refresh_token,
                    user_data={
                        "full_name": user_metadata.get("full_name", ""),
                        "created_at": str(response.user.created_at) if response.user.created_at else None
                    }
                )
            else:
                return AuthResult(
                    success=False,
                    message="Identifiants incorrects"
                )
                
        except Exception as e:
            error_msg = str(e)
            if "Invalid login credentials" in error_msg:
                return AuthResult(
                    success=False,
                    message="Email ou mot de passe incorrect"
                )
            print(f"❌ Erreur connexion: {e}")
            return AuthResult(
                success=False,
                message="Erreur lors de la connexion"
            )
    
    @staticmethod
    def logout(access_token: Optional[str] = None) -> AuthResult:
        """
        Déconnecte l'utilisateur.
        
        Returns:
            AuthResult avec le statut de l'opération
        """
        client = get_supabase_client()
        if client is None:
            return AuthResult(success=True, message="Déconnexion effectuée")
        
        try:
            client.auth.sign_out()
            return AuthResult(
                success=True,
                message="Déconnexion réussie"
            )
        except Exception as e:
            print(f"⚠️ Erreur déconnexion: {e}")
            return AuthResult(
                success=True,
                message="Déconnexion effectuée"
            )
    
    @staticmethod
    def reset_password_request(email: str) -> AuthResult:
        """
        Envoie un email de réinitialisation de mot de passe.
        
        Args:
            email: Adresse email
            
        Returns:
            AuthResult avec le statut de l'opération
        """
        # Validation email
        valid, msg = AuthService.validate_email(email)
        if not valid:
            return AuthResult(success=False, message=msg)
        
        client = get_supabase_client()
        if client is None:
            return AuthResult(
                success=False,
                message="Service indisponible"
            )
        
        try:
            # URL de redirection après clic sur le lien
            redirect_url = os.getenv("APP_URL", "http://localhost:3000") + "/reset-password"
            
            client.auth.reset_password_for_email(
                email,
                {"redirect_to": redirect_url}
            )
            
            return AuthResult(
                success=True,
                message="Si cette adresse existe, vous recevrez un email de réinitialisation."
            )
            
        except Exception as e:
            print(f"❌ Erreur reset password: {e}")
            # On ne révèle pas si l'email existe ou non
            return AuthResult(
                success=True,
                message="Si cette adresse existe, vous recevrez un email de réinitialisation."
            )
    
    @staticmethod
    def update_password(new_password: str, access_token: str) -> AuthResult:
        """
        Met à jour le mot de passe de l'utilisateur.
        
        Args:
            new_password: Nouveau mot de passe
            access_token: Token d'accès de l'utilisateur
            
        Returns:
            AuthResult avec le statut de l'opération
        """
        # Validation mot de passe
        valid, msg = AuthService.validate_password(new_password)
        if not valid:
            return AuthResult(success=False, message=msg)
        
        client = get_supabase_client()
        if client is None:
            return AuthResult(
                success=False,
                message="Service indisponible"
            )
        
        try:
            response = client.auth.update_user({
                "password": new_password
            })
            
            if response.user:
                return AuthResult(
                    success=True,
                    message="Mot de passe mis à jour avec succès"
                )
            else:
                return AuthResult(
                    success=False,
                    message="Erreur lors de la mise à jour"
                )
                
        except Exception as e:
            print(f"❌ Erreur update password: {e}")
            return AuthResult(
                success=False,
                message="Erreur lors de la mise à jour du mot de passe"
            )
    
    @staticmethod
    def get_user(access_token: str) -> AuthResult:
        """
        Récupère les informations de l'utilisateur connecté.
        
        Args:
            access_token: Token d'accès
            
        Returns:
            AuthResult avec les données utilisateur
        """
        client = get_supabase_client()
        if client is None:
            return AuthResult(
                success=False,
                message="Service indisponible"
            )
        
        try:
            response = client.auth.get_user(access_token)
            
            if response.user:
                user_metadata = response.user.user_metadata or {}
                return AuthResult(
                    success=True,
                    message="Utilisateur récupéré",
                    user_id=response.user.id,
                    email=response.user.email,
                    user_data={
                        "full_name": user_metadata.get("full_name", ""),
                        "created_at": str(response.user.created_at) if response.user.created_at else None
                    }
                )
            else:
                return AuthResult(
                    success=False,
                    message="Utilisateur non trouvé"
                )
                
        except Exception as e:
            print(f"❌ Erreur get user: {e}")
            return AuthResult(
                success=False,
                message="Session expirée"
            )


# Instance singleton
auth_service = AuthService()
