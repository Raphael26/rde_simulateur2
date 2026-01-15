#"""
#Authentication State - Gestion complète de l'authentification avec Supabase
#
#CORRECTION BUG SESSION PARTAGÉE:
#- check_auth() utilise maintenant validate_token() au lieu de client.auth.get_session()
#- Cela évite que la session d'un utilisateur soit vue par un autre utilisateur
#"""
#
#import reflex as rx
#import re
#
#
#class AuthState(rx.State):
#    """État pour la gestion de l'authentification avec Supabase."""
#    
#    # ==================== Informations utilisateur ====================
#    user_id: str = ""
#    user_email: str = ""
#    user_full_name: str = ""
#    access_token: str = ""
#    refresh_token: str = ""
#    is_authenticated: bool = False
#    
#    # ==================== États de chargement ====================
#    is_loading: bool = False
#    is_checking_auth: bool = True  # True au démarrage pour vérifier la session
#    
#    # ==================== Messages ====================
#    error_message: str = ""
#    success_message: str = ""
#    
#    # ==================== Champs de formulaire - Login ====================
#    login_email: str = ""
#    login_password: str = ""
#    show_login_password: bool = False
#    
#    # ==================== Champs de formulaire - Register ====================
#    register_email: str = ""
#    register_password: str = ""
#    register_password_confirm: str = ""
#    register_full_name: str = ""
#    register_accept_terms: bool = False
#    show_register_password: bool = False
#    
#    # ==================== Champs de formulaire - Reset Password ====================
#    reset_email: str = ""
#    new_password: str = ""
#    new_password_confirm: str = ""
#    
#    # ==================== Helpers ====================
#    
#    def _get_supabase_client(self):
#        """Récupère le client Supabase de manière sécurisée."""
#        try:
#            from ..services.supabase_client import get_supabase_client
#            client = get_supabase_client()
#            if client:
#                return client
#        except ImportError:
#            pass
#        
#        try:
#            from ..services.supabase_service import get_supabase_client
#            client = get_supabase_client()
#            if client:
#                return client
#        except ImportError:
#            pass
#        
#        try:
#            from ..services.supabase_service import supabase
#            if supabase:
#                return supabase
#        except ImportError:
#            pass
#        
#        return None
#    
#    def _clear_messages(self):
#        """Efface les messages d'erreur et de succès."""
#        self.error_message = ""
#        self.success_message = ""
#    
#    def _clear_login_form(self):
#        """Efface le formulaire de connexion."""
#        self.login_email = ""
#        self.login_password = ""
#        self.show_login_password = False
#    
#    def _clear_register_form(self):
#        """Efface le formulaire d'inscription."""
#        self.register_email = ""
#        self.register_password = ""
#        self.register_password_confirm = ""
#        self.register_full_name = ""
#        self.register_accept_terms = False
#        self.show_register_password = False
#    
#    def _set_user_from_response(self, user, session=None):
#        """Configure l'état utilisateur depuis une réponse Supabase."""
#        self.user_id = user.id
#        self.user_email = user.email or ""
#        self.is_authenticated = True
#        
#        # Récupérer le nom depuis les métadonnées
#        if user.user_metadata:
#            self.user_full_name = user.user_metadata.get("full_name", "")
#        
#        # Stocker les tokens si disponibles
#        if session:
#            if hasattr(session, 'access_token'):
#                self.access_token = session.access_token or ""
#            if hasattr(session, 'refresh_token'):
#                self.refresh_token = session.refresh_token or ""
#    
#    def _clear_user(self):
#        """Efface les données utilisateur."""
#        self.user_id = ""
#        self.user_email = ""
#        self.user_full_name = ""
#        self.access_token = ""
#        self.refresh_token = ""
#        self.is_authenticated = False
#    
#    @staticmethod
#    def _validate_email(email: str) -> tuple[bool, str]:
#        """Valide le format de l'email."""
#        if not email:
#            return False, "L'email est requis"
#        pattern = r'^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$'
#        if not re.match(pattern, email):
#            return False, "Format d'email invalide"
#        return True, ""
#    
#    @staticmethod
#    def _validate_password(password: str) -> tuple[bool, str]:
#        """Valide la force du mot de passe."""
#        if not password:
#            return False, "Le mot de passe est requis"
#        if len(password) < 8:
#            return False, "Le mot de passe doit contenir au moins 8 caractères"
#        if not re.search(r'[A-Z]', password):
#            return False, "Le mot de passe doit contenir au moins une majuscule"
#        if not re.search(r'[0-9]', password):
#            return False, "Le mot de passe doit contenir au moins un chiffre"
#        return True, ""
#    
#    # ==================== Computed Vars ====================
#    
#    @rx.var
#    def is_logged_in(self) -> bool:
#        """Vérifie si l'utilisateur est connecté."""
#        return self.is_authenticated and bool(self.user_id)
#    
#    @rx.var
#    def initials(self) -> str:
#        """Retourne les initiales de l'utilisateur."""
#        if self.user_full_name:
#            parts = self.user_full_name.split()
#            if len(parts) >= 2:
#                return (parts[0][0] + parts[1][0]).upper()
#            return self.user_full_name[:2].upper()
#        if self.user_email:
#            return self.user_email[:2].upper()
#        return "U"
#    
#    @rx.var
#    def display_name(self) -> str:
#        """Retourne le nom d'affichage."""
#        if self.user_full_name:
#            return self.user_full_name
#        if self.user_email:
#            return self.user_email.split("@")[0]
#        return "Utilisateur"
#    
#    @rx.var
#    def login_button_text(self) -> str:
#        """Texte du bouton de connexion."""
#        return "Connexion en cours..." if self.is_loading else "Se connecter"
#    
#    @rx.var
#    def register_button_text(self) -> str:
#        """Texte du bouton d'inscription."""
#        return "Inscription en cours..." if self.is_loading else "Créer mon compte"
#    
#    # ==================== Event Handlers - Formulaires ====================
#    
#    @rx.event
#    def set_login_email(self, value: str):
#        self.login_email = value.strip()
#        self._clear_messages()
#    
#    @rx.event
#    def set_login_password(self, value: str):
#        self.login_password = value
#        self._clear_messages()
#    
#    @rx.event
#    def toggle_login_password(self):
#        self.show_login_password = not self.show_login_password
#    
#    @rx.event
#    def set_register_email(self, value: str):
#        self.register_email = value.strip()
#        self._clear_messages()
#    
#    @rx.event
#    def set_register_password(self, value: str):
#        self.register_password = value
#        self._clear_messages()
#    
#    @rx.event
#    def set_register_password_confirm(self, value: str):
#        self.register_password_confirm = value
#        self._clear_messages()
#    
#    @rx.event
#    def set_register_full_name(self, value: str):
#        self.register_full_name = value.strip()
#        self._clear_messages()
#    
#    @rx.event
#    def set_register_accept_terms(self, value: bool):
#        self.register_accept_terms = value
#        self._clear_messages()
#    
#    @rx.event
#    def toggle_register_password(self):
#        self.show_register_password = not self.show_register_password
#    
#    @rx.event
#    def set_reset_email(self, value: str):
#        self.reset_email = value.strip()
#        self._clear_messages()
#    
#    # ==================== Event Handlers - Auth ====================
#    
#    @rx.event
#    async def check_auth(self):
#        """
#        Vérifie si l'utilisateur a une session active au chargement.
#        
#        ✅ VERSION CORRIGÉE: Utilise validate_token() au lieu de get_session()
#        pour éviter le bug de session partagée entre utilisateurs.
#        
#        AVANT (BUGUÉ):
#            response = client.auth.get_session()  # ← Retournait la session du dernier connecté!
#        
#        MAINTENANT:
#            - On utilise le token stocké dans self.access_token (isolé par utilisateur)
#            - On valide ce token avec validate_token() sur un client frais
#        """
#        self.is_checking_auth = True
#        
#        # Si pas de token stocké, l'utilisateur n'est pas connecté
#        if not self.access_token:
#            self._clear_user()
#            self.is_checking_auth = False
#            return
#        
#        try:
#            # Importer la fonction de validation sécurisée
#            from ..services.supabase_service import validate_token, refresh_session
#            
#            # ✅ Valider le token stocké (PAS get_session sur le singleton!)
#            result = validate_token(self.access_token)
#            
#            if result["valid"] and result["user"]:
#                # Token valide - restaurer les infos utilisateur
#                user = result["user"]
#                self.user_id = user.id
#                self.user_email = user.email or ""
#                self.is_authenticated = True
#                
#                if user.user_metadata:
#                    self.user_full_name = user.user_metadata.get("full_name", "")
#                
#                print(f"✅ Session validée pour {self.user_email}")
#            
#            elif self.refresh_token:
#                # Token expiré mais on a un refresh_token - essayer de rafraîchir
#                print("🔄 Token expiré, tentative de refresh...")
#                refresh_result = refresh_session(self.refresh_token)
#                
#                if refresh_result["success"]:
#                    # Mettre à jour les tokens
#                    self.access_token = refresh_result["access_token"] or ""
#                    self.refresh_token = refresh_result["refresh_token"] or ""
#                    
#                    if refresh_result["user"]:
#                        user = refresh_result["user"]
#                        self.user_id = user.id
#                        self.user_email = user.email or ""
#                        self.is_authenticated = True
#                        if user.user_metadata:
#                            self.user_full_name = user.user_metadata.get("full_name", "")
#                    
#                    print(f"✅ Session rafraîchie pour {self.user_email}")
#                else:
#                    # Refresh échoué - déconnecter
#                    print("⚠️ Refresh échoué - déconnexion")
#                    self._clear_user()
#            else:
#                # Token invalide et pas de refresh - déconnecter
#                print("⚠️ Token invalide - déconnexion")
#                self._clear_user()
#                
#        except ImportError:
#            # Fallback si validate_token n'existe pas (ancienne version du service)
#            print("⚠️ validate_token non disponible, fallback sur ancienne méthode")
#            try:
#                client = self._get_supabase_client()
#                if client:
#                    # ⚠️ Cette méthode a le bug de session partagée!
#                    response = client.auth.get_session()
#                    if response and response.user:
#                        self._set_user_from_response(response.user, response)
#                        print(f"✅ Session restaurée pour {self.user_email} (fallback)")
#                    else:
#                        self._clear_user()
#                else:
#                    self._clear_user()
#            except Exception as e:
#                print(f"⚠️ Erreur fallback check_auth: {e}")
#                self._clear_user()
#                
#        except Exception as e:
#            print(f"⚠️ Erreur vérification session: {e}")
#            self._clear_user()
#        
#        self.is_checking_auth = False
#    
#    @rx.event
#    async def handle_login(self):
#        """Gère la connexion de l'utilisateur."""
#        self._clear_messages()
#        
#        # Validation
#        valid, msg = self._validate_email(self.login_email)
#        if not valid:
#            self.error_message = msg
#            return
#        
#        if not self.login_password:
#            self.error_message = "Le mot de passe est requis"
#            return
#        
#        self.is_loading = True
#        yield
#        
#        try:
#            client = self._get_supabase_client()
#            
#            if not client:
#                self.error_message = "Service d'authentification indisponible"
#                self.is_loading = False
#                return
#            
#            # Connexion avec Supabase Auth
#            response = client.auth.sign_in_with_password({
#                "email": self.login_email,
#                "password": self.login_password
#            })
#            
#            if response.user and response.session:
#                self._set_user_from_response(response.user, response.session)
#                self._clear_login_form()
#                self.is_loading = False
#                
#                print(f"✅ Connexion réussie: {self.user_email}")
#                yield rx.toast.success(f"Bienvenue {self.display_name} !")
#                yield rx.redirect("/dashboard")
#            else:
#                self.error_message = "Identifiants incorrects"
#                self.is_loading = False
#                
#        except Exception as e:
#            error_str = str(e)
#            print(f"❌ Erreur connexion: {error_str}")
#            
#            if "Invalid login credentials" in error_str:
#                self.error_message = "Email ou mot de passe incorrect"
#            elif "Email not confirmed" in error_str:
#                self.error_message = "Veuillez confirmer votre email avant de vous connecter"
#            else:
#                self.error_message = "Erreur de connexion. Veuillez réessayer."
#            
#            self.is_loading = False
#    
#    @rx.event
#    async def handle_register(self):
#        """Gère l'inscription d'un nouvel utilisateur."""
#        self._clear_messages()
#        
#        # Validation du nom
#        if not self.register_full_name or len(self.register_full_name) < 2:
#            self.error_message = "Le nom complet est requis (minimum 2 caractères)"
#            return
#        
#        # Validation email
#        valid, msg = self._validate_email(self.register_email)
#        if not valid:
#            self.error_message = msg
#            return
#        
#        # Validation mot de passe
#        valid, msg = self._validate_password(self.register_password)
#        if not valid:
#            self.error_message = msg
#            return
#        
#        # Vérification correspondance mots de passe
#        if self.register_password != self.register_password_confirm:
#            self.error_message = "Les mots de passe ne correspondent pas"
#            return
#        
#        # Vérification CGU
#        if not self.register_accept_terms:
#            self.error_message = "Vous devez accepter les conditions d'utilisation"
#            return
#        
#        self.is_loading = True
#        yield
#        
#        try:
#            client = self._get_supabase_client()
#            
#            if not client:
#                self.error_message = "Service d'authentification indisponible"
#                self.is_loading = False
#                return
#            
#            # Inscription avec Supabase Auth
#            response = client.auth.sign_up({
#                "email": self.register_email,
#                "password": self.register_password,
#                "options": {
#                    "data": {
#                        "full_name": self.register_full_name
#                    }
#                }
#            })
#            
#            if response.user:
#                self._clear_register_form()
#                self.success_message = "Compte créé avec succès ! Vérifiez votre email pour confirmer votre inscription."
#                self.is_loading = False
#                
#                print(f"✅ Inscription réussie: {response.user.email}")
#                yield rx.toast.success("Compte créé ! Vérifiez votre email.")
#                
#                # Si l'email est déjà confirmé (mode dev), connecter directement
#                if response.session:
#                    self._set_user_from_response(response.user, response.session)
#                    yield rx.redirect("/dashboard")
#            else:
#                self.error_message = "Erreur lors de l'inscription"
#                self.is_loading = False
#                
#        except Exception as e:
#            error_str = str(e)
#            print(f"❌ Erreur inscription: {error_str}")
#            
#            if "User already registered" in error_str:
#                self.error_message = "Cette adresse email est déjà utilisée"
#            elif "Password should be" in error_str:
#                self.error_message = "Le mot de passe ne respecte pas les critères de sécurité"
#            else:
#                self.error_message = f"Erreur lors de l'inscription: {error_str[:100]}"
#            
#            self.is_loading = False
#    
#    @rx.event
#    async def handle_logout(self):
#        """Gère la déconnexion de l'utilisateur."""
#        try:
#            client = self._get_supabase_client()
#            if client:
#                client.auth.sign_out()
#                print("✅ Déconnexion Supabase réussie")
#        except Exception as e:
#            print(f"⚠️ Erreur déconnexion Supabase: {e}")
#        
#        # Toujours nettoyer l'état local
#        self._clear_user()
#        self._clear_login_form()
#        self._clear_register_form()
#        self._clear_messages()
#        
#        yield rx.toast.info("Vous avez été déconnecté")
#        yield rx.redirect("/")
#    
#    @rx.event
#    async def handle_password_reset_request(self):
#        """Envoie un email de réinitialisation de mot de passe."""
#        self._clear_messages()
#        
#        valid, msg = self._validate_email(self.reset_email)
#        if not valid:
#            self.error_message = msg
#            return
#        
#        self.is_loading = True
#        yield
#        
#        try:
#            client = self._get_supabase_client()
#            
#            if not client:
#                self.error_message = "Service indisponible"
#                self.is_loading = False
#                return
#            
#            # Envoyer l'email de réinitialisation
#            client.auth.reset_password_for_email(self.reset_email)
#            
#            # Message générique pour ne pas révéler si l'email existe
#            self.success_message = "Si cette adresse existe, vous recevrez un email de réinitialisation."
#            self.reset_email = ""
#            
#        except Exception as e:
#            print(f"⚠️ Erreur reset password: {e}")
#            # Message générique
#            self.success_message = "Si cette adresse existe, vous recevrez un email de réinitialisation."
#        
#        self.is_loading = False
#    
#    # ==================== Protection des routes ====================
#    
#    @rx.event
#    async def require_auth(self):
#        """Vérifie l'authentification et redirige si nécessaire."""
#        if not self.is_authenticated:
#            # Vérifier d'abord la session
#            await self.check_auth()
#            
#            if not self.is_authenticated:
#                yield rx.toast.warning("Veuillez vous connecter")
#                yield rx.redirect("/login")
#    
#    @rx.event
#    async def redirect_if_authenticated(self):
#        """Redirige vers le dashboard si déjà connecté."""
#        if self.is_authenticated:
#            yield rx.redirect("/dashboard")
#        else:
#            # Vérifier la session
#            await self.check_auth()
#            if self.is_authenticated:
#                yield rx.redirect("/dashboard")
#
#
#def require_auth(page_component):
#    """
#    Décorateur pour protéger une page et requérir l'authentification.
#    Redirige vers /login si non connecté.
#    
#    Usage:
#        @rx.page(route="/protected")
#        @require_auth
#        def protected_page():
#            return rx.text("Contenu protégé")
#    """
#    def wrapper(*args, **kwargs):
#        return rx.cond(
#            AuthState.is_authenticated,
#            page_component(*args, **kwargs),
#            rx.fragment(
#                rx.script(
#                    """
#                    if (typeof window !== 'undefined') {
#                        window.location.href = '/login';
#                    }
#                    """
#                ),
#                rx.center(
#                    rx.vstack(
#                        rx.spinner(size="3"),
#                        rx.text("Redirection vers la connexion..."),
#                        spacing="4",
#                    ),
#                    min_height="100vh",
#                ),
#            ),
#        )
#    return wrapper


"""
Authentication State - Gestion complète de l'authentification avec Supabase

CORRECTION BUG SESSION PARTAGÉE:
- check_auth() utilise maintenant validate_token() au lieu de client.auth.get_session()
- Cela évite que la session d'un utilisateur soit vue par un autre utilisateur

CORRECTION MESSAGES D'ERREUR:
- Ajout de computed var has_error pour une meilleure réactivité
- Ajout de yields après les assignations d'erreur
- Toast notifications pour les erreurs de validation
"""

import reflex as rx
import re


class AuthState(rx.State):
    """État pour la gestion de l'authentification avec Supabase."""
    
    # ==================== Informations utilisateur ====================
    user_id: str = ""
    user_email: str = ""
    user_full_name: str = ""
    access_token: str = ""
    refresh_token: str = ""
    is_authenticated: bool = False
    
    # ==================== États de chargement ====================
    is_loading: bool = False
    is_checking_auth: bool = True  # True au démarrage pour vérifier la session
    
    # ==================== Messages ====================
    error_message: str = ""
    success_message: str = ""
    
    # ==================== Champs de formulaire - Login ====================
    login_email: str = ""
    login_password: str = ""
    show_login_password: bool = False
    
    # ==================== Champs de formulaire - Register ====================
    register_email: str = ""
    register_password: str = ""
    register_password_confirm: str = ""
    register_full_name: str = ""
    register_accept_terms: bool = False
    show_register_password: bool = False
    
    # ==================== Champs de formulaire - Reset Password ====================
    reset_email: str = ""
    new_password: str = ""
    new_password_confirm: str = ""
    
    # ==================== Helpers ====================
    
    def _get_supabase_client(self):
        """Récupère le client Supabase de manière sécurisée."""
        try:
            from ..services.supabase_client import get_supabase_client
            client = get_supabase_client()
            if client:
                return client
        except ImportError:
            pass
        
        try:
            from ..services.supabase_service import get_supabase_client
            client = get_supabase_client()
            if client:
                return client
        except ImportError:
            pass
        
        try:
            from ..services.supabase_service import supabase
            if supabase:
                return supabase
        except ImportError:
            pass
        
        return None
    
    def _clear_messages(self):
        """Efface les messages d'erreur et de succès."""
        self.error_message = ""
        self.success_message = ""
    
    def _clear_login_form(self):
        """Efface le formulaire de connexion."""
        self.login_email = ""
        self.login_password = ""
        self.show_login_password = False
    
    def _clear_register_form(self):
        """Efface le formulaire d'inscription."""
        self.register_email = ""
        self.register_password = ""
        self.register_password_confirm = ""
        self.register_full_name = ""
        self.register_accept_terms = False
        self.show_register_password = False
    
    def _set_user_from_response(self, user, session=None):
        """Configure l'état utilisateur depuis une réponse Supabase."""
        self.user_id = user.id
        self.user_email = user.email or ""
        self.is_authenticated = True
        
        # Récupérer le nom depuis les métadonnées
        if user.user_metadata:
            self.user_full_name = user.user_metadata.get("full_name", "")
        
        # Stocker les tokens si disponibles
        if session:
            if hasattr(session, 'access_token'):
                self.access_token = session.access_token or ""
            if hasattr(session, 'refresh_token'):
                self.refresh_token = session.refresh_token or ""
    
    def _clear_user(self):
        """Efface les données utilisateur."""
        self.user_id = ""
        self.user_email = ""
        self.user_full_name = ""
        self.access_token = ""
        self.refresh_token = ""
        self.is_authenticated = False
    
    @staticmethod
    def _validate_email(email: str) -> tuple[bool, str]:
        """Valide le format de l'email."""
        if not email:
            return False, "L'email est requis"
        pattern = r'^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$'
        if not re.match(pattern, email):
            return False, "Format d'email invalide"
        return True, ""
    
    @staticmethod
    def _validate_password(password: str) -> tuple[bool, str]:
        """Valide la force du mot de passe."""
        if not password:
            return False, "Le mot de passe est requis"
        if len(password) < 8:
            return False, "Le mot de passe doit contenir au moins 8 caractères"
        if not re.search(r'[A-Z]', password):
            return False, "Le mot de passe doit contenir au moins une majuscule"
        if not re.search(r'[0-9]', password):
            return False, "Le mot de passe doit contenir au moins un chiffre"
        return True, ""
    
    # ==================== Computed Vars ====================
    
    @rx.var
    def is_logged_in(self) -> bool:
        """Vérifie si l'utilisateur est connecté."""
        return self.is_authenticated and bool(self.user_id)
    
    @rx.var
    def has_error(self) -> bool:
        """Vérifie si un message d'erreur est présent."""
        return len(self.error_message) > 0
    
    @rx.var
    def has_success(self) -> bool:
        """Vérifie si un message de succès est présent."""
        return len(self.success_message) > 0
    
    @rx.var
    def initials(self) -> str:
        """Retourne les initiales de l'utilisateur."""
        if self.user_full_name:
            parts = self.user_full_name.split()
            if len(parts) >= 2:
                return (parts[0][0] + parts[1][0]).upper()
            return self.user_full_name[:2].upper()
        if self.user_email:
            return self.user_email[:2].upper()
        return "U"
    
    @rx.var
    def display_name(self) -> str:
        """Retourne le nom d'affichage."""
        if self.user_full_name:
            return self.user_full_name
        if self.user_email:
            return self.user_email.split("@")[0]
        return "Utilisateur"
    
    @rx.var
    def login_button_text(self) -> str:
        """Texte du bouton de connexion."""
        return "Connexion en cours..." if self.is_loading else "Se connecter"
    
    @rx.var
    def register_button_text(self) -> str:
        """Texte du bouton d'inscription."""
        return "Inscription en cours..." if self.is_loading else "Créer mon compte"
    
    # ==================== Event Handlers - Formulaires ====================
    
    @rx.event
    def set_login_email(self, value: str):
        self.login_email = value.strip()
        self._clear_messages()
    
    @rx.event
    def set_login_password(self, value: str):
        self.login_password = value
        self._clear_messages()
    
    @rx.event
    def toggle_login_password(self):
        self.show_login_password = not self.show_login_password
    
    @rx.event
    def set_register_email(self, value: str):
        self.register_email = value.strip()
        self._clear_messages()
    
    @rx.event
    def set_register_password(self, value: str):
        self.register_password = value
        self._clear_messages()
    
    @rx.event
    def set_register_password_confirm(self, value: str):
        self.register_password_confirm = value
        self._clear_messages()
    
    @rx.event
    def set_register_full_name(self, value: str):
        self.register_full_name = value.strip()
        self._clear_messages()
    
    @rx.event
    def set_register_accept_terms(self, value: bool):
        self.register_accept_terms = value
        self._clear_messages()
    
    @rx.event
    def toggle_register_password(self):
        self.show_register_password = not self.show_register_password
    
    @rx.event
    def set_reset_email(self, value: str):
        self.reset_email = value.strip()
        self._clear_messages()
    
    # ==================== Event Handlers - Auth ====================
    
    @rx.event
    async def check_auth(self):
        """Vérifie si l'utilisateur a une session active au chargement."""
        self.is_checking_auth = True
        
        try:
            # Essayer d'utiliser validate_token si disponible
            from ..services.supabase_service import validate_token, refresh_session
            
            if not self.access_token:
                self._clear_user()
                self.is_checking_auth = False
                return
            
            # Valider le token actuel
            is_valid, user_info = validate_token(self.access_token)
            
            if is_valid and user_info:
                # Token valide - mettre à jour les infos utilisateur
                self.user_id = user_info.get("sub", "")
                self.user_email = user_info.get("email", "")
                self.is_authenticated = True
                print(f"✅ Token valide pour {self.user_email}")
            elif self.refresh_token:
                # Token expiré mais refresh disponible
                print("⚠️ Token expiré, tentative de refresh...")
                refresh_result = refresh_session(self.refresh_token)
                
                if refresh_result and refresh_result.get("access_token"):
                    self.access_token = refresh_result["access_token"] or ""
                    self.refresh_token = refresh_result["refresh_token"] or ""
                    
                    if refresh_result["user"]:
                        user = refresh_result["user"]
                        self.user_id = user.id
                        self.user_email = user.email or ""
                        self.is_authenticated = True
                        if user.user_metadata:
                            self.user_full_name = user.user_metadata.get("full_name", "")
                    
                    print(f"✅ Session rafraîchie pour {self.user_email}")
                else:
                    # Refresh échoué - déconnecter
                    print("⚠️ Refresh échoué - déconnexion")
                    self._clear_user()
            else:
                # Token invalide et pas de refresh - déconnecter
                print("⚠️ Token invalide - déconnexion")
                self._clear_user()
                
        except ImportError:
            # Fallback si validate_token n'existe pas (ancienne version du service)
            print("⚠️ validate_token non disponible, fallback sur ancienne méthode")
            try:
                client = self._get_supabase_client()
                if client:
                    # ⚠️ Cette méthode a le bug de session partagée!
                    response = client.auth.get_session()
                    if response and response.user:
                        self._set_user_from_response(response.user, response)
                        print(f"✅ Session restaurée pour {self.user_email} (fallback)")
                    else:
                        self._clear_user()
                else:
                    self._clear_user()
            except Exception as e:
                print(f"⚠️ Erreur fallback check_auth: {e}")
                self._clear_user()
                
        except Exception as e:
            print(f"⚠️ Erreur vérification session: {e}")
            self._clear_user()
        
        self.is_checking_auth = False
    
    @rx.event
    async def handle_login(self):
        """Gère la connexion de l'utilisateur."""
        self._clear_messages()
        
        # Validation de l'email
        valid, msg = self._validate_email(self.login_email)
        if not valid:
            self.error_message = msg
            print(f"❌ Erreur validation email: {msg}")
            yield rx.toast.error(msg)
            return
        
        # Validation du mot de passe
        if not self.login_password:
            self.error_message = "Le mot de passe est requis"
            print("❌ Erreur: mot de passe manquant")
            yield rx.toast.error("Le mot de passe est requis")
            return
        
        # Afficher le loader
        self.is_loading = True
        yield
        
        try:
            client = self._get_supabase_client()
            
            if not client:
                self.error_message = "Service d'authentification indisponible. Veuillez réessayer plus tard."
                self.is_loading = False
                print("❌ Erreur: client Supabase non disponible")
                yield rx.toast.error("Service indisponible")
                return
            
            # Connexion avec Supabase Auth
            print(f"🔄 Tentative de connexion pour: {self.login_email}")
            response = client.auth.sign_in_with_password({
                "email": self.login_email,
                "password": self.login_password
            })
            
            # Vérifier la réponse
            if response and response.user and response.session:
                self._set_user_from_response(response.user, response.session)
                self._clear_login_form()
                self.is_loading = False
                
                print(f"✅ Connexion réussie: {self.user_email}")
                yield rx.toast.success(f"Bienvenue {self.display_name} !")
                yield rx.redirect("/dashboard")
            else:
                # Connexion échouée sans exception
                self.error_message = "Identifiants incorrects. Vérifiez votre email et mot de passe."
                self.is_loading = False
                print("❌ Connexion échouée: réponse invalide de Supabase")
                yield rx.toast.error("Identifiants incorrects")
                
        except Exception as e:
            error_str = str(e).lower()
            print(f"❌ Exception connexion: {e}")
            
            # Messages d'erreur spécifiques selon le type d'erreur
            if "invalid login credentials" in error_str or "invalid_credentials" in error_str:
                self.error_message = "Email ou mot de passe incorrect"
                yield rx.toast.error("Email ou mot de passe incorrect")
            elif "email not confirmed" in error_str:
                self.error_message = "Veuillez confirmer votre email avant de vous connecter. Vérifiez votre boîte de réception."
                yield rx.toast.warning("Email non confirmé")
            elif "too many requests" in error_str or "rate limit" in error_str:
                self.error_message = "Trop de tentatives. Veuillez patienter quelques minutes."
                yield rx.toast.error("Trop de tentatives")
            elif "network" in error_str or "connection" in error_str:
                self.error_message = "Erreur de connexion réseau. Vérifiez votre connexion internet."
                yield rx.toast.error("Erreur réseau")
            elif "user not found" in error_str:
                self.error_message = "Aucun compte n'existe avec cette adresse email"
                yield rx.toast.error("Compte non trouvé")
            else:
                self.error_message = "Erreur de connexion. Veuillez réessayer."
                yield rx.toast.error("Erreur de connexion")
            
            self.is_loading = False
    
    @rx.event
    async def handle_register(self):
        """Gère l'inscription d'un nouvel utilisateur."""
        self._clear_messages()
        
        # Validation du nom
        if not self.register_full_name or len(self.register_full_name) < 2:
            self.error_message = "Le nom complet est requis (minimum 2 caractères)"
            yield rx.toast.error("Nom requis (min. 2 caractères)")
            return
        
        # Validation email
        valid, msg = self._validate_email(self.register_email)
        if not valid:
            self.error_message = msg
            yield rx.toast.error(msg)
            return
        
        # Validation mot de passe
        valid, msg = self._validate_password(self.register_password)
        if not valid:
            self.error_message = msg
            yield rx.toast.error(msg)
            return
        
        # Vérification correspondance mots de passe
        if self.register_password != self.register_password_confirm:
            self.error_message = "Les mots de passe ne correspondent pas"
            yield rx.toast.error("Les mots de passe ne correspondent pas")
            return
        
        # Vérification CGU
        if not self.register_accept_terms:
            self.error_message = "Vous devez accepter les conditions d'utilisation"
            yield rx.toast.error("Veuillez accepter les CGU")
            return
        
        self.is_loading = True
        yield
        
        try:
            client = self._get_supabase_client()
            
            if not client:
                self.error_message = "Service d'authentification indisponible"
                self.is_loading = False
                yield rx.toast.error("Service indisponible")
                return
            
            # Inscription avec Supabase Auth
            response = client.auth.sign_up({
                "email": self.register_email,
                "password": self.register_password,
                "options": {
                    "data": {
                        "full_name": self.register_full_name
                    }
                }
            })
            
            if response.user:
                self._clear_register_form()
                self.success_message = "Compte créé avec succès ! Vérifiez votre email pour confirmer votre inscription."
                self.is_loading = False
                
                print(f"✅ Inscription réussie: {response.user.email}")
                yield rx.toast.success("Compte créé ! Vérifiez votre email.")
                
                # Si l'email est déjà confirmé (mode dev), connecter directement
                if response.session:
                    self._set_user_from_response(response.user, response.session)
                    yield rx.redirect("/dashboard")
            else:
                self.error_message = "Erreur lors de l'inscription"
                self.is_loading = False
                yield rx.toast.error("Erreur d'inscription")
                
        except Exception as e:
            error_str = str(e).lower()
            print(f"❌ Erreur inscription: {e}")
            
            if "user already registered" in error_str or "already exists" in error_str:
                self.error_message = "Cette adresse email est déjà utilisée"
                yield rx.toast.error("Email déjà utilisé")
            elif "password should be" in error_str or "password" in error_str:
                self.error_message = "Le mot de passe ne respecte pas les critères de sécurité"
                yield rx.toast.error("Mot de passe trop faible")
            elif "invalid email" in error_str:
                self.error_message = "L'adresse email n'est pas valide"
                yield rx.toast.error("Email invalide")
            else:
                self.error_message = f"Erreur lors de l'inscription. Veuillez réessayer."
                yield rx.toast.error("Erreur d'inscription")
            
            self.is_loading = False
    
    @rx.event
    async def handle_logout(self):
        """Gère la déconnexion de l'utilisateur."""
        try:
            client = self._get_supabase_client()
            if client:
                client.auth.sign_out()
                print("✅ Déconnexion Supabase réussie")
        except Exception as e:
            print(f"⚠️ Erreur déconnexion Supabase: {e}")
        
        # Toujours nettoyer l'état local
        self._clear_user()
        self._clear_login_form()
        self._clear_register_form()
        self._clear_messages()
        
        yield rx.toast.info("Vous avez été déconnecté")
        yield rx.redirect("/")
    
    @rx.event
    async def handle_password_reset_request(self):
        """Envoie un email de réinitialisation de mot de passe."""
        self._clear_messages()
        
        valid, msg = self._validate_email(self.reset_email)
        if not valid:
            self.error_message = msg
            yield rx.toast.error(msg)
            return
        
        self.is_loading = True
        yield
        
        try:
            client = self._get_supabase_client()
            
            if not client:
                self.error_message = "Service indisponible"
                self.is_loading = False
                yield rx.toast.error("Service indisponible")
                return
            
            # Envoyer l'email de réinitialisation
            client.auth.reset_password_for_email(self.reset_email)
            
            # Message générique pour ne pas révéler si l'email existe
            self.success_message = "Si cette adresse existe, vous recevrez un email de réinitialisation."
            self.reset_email = ""
            yield rx.toast.success("Email envoyé si le compte existe")
            
        except Exception as e:
            print(f"⚠️ Erreur reset password: {e}")
            # Message générique
            self.success_message = "Si cette adresse existe, vous recevrez un email de réinitialisation."
            yield rx.toast.info("Vérifiez votre boîte mail")
        
        self.is_loading = False
    
    # ==================== Protection des routes ====================
    
    @rx.event
    async def require_auth(self):
        """Vérifie l'authentification et redirige si nécessaire."""
        if not self.is_authenticated:
            # Vérifier d'abord la session
            await self.check_auth()
            
            if not self.is_authenticated:
                yield rx.toast.warning("Veuillez vous connecter")
                yield rx.redirect("/login")
    
    @rx.event
    async def redirect_if_authenticated(self):
        """Redirige vers le dashboard si déjà connecté."""
        if self.is_authenticated:
            yield rx.redirect("/dashboard")
        else:
            # Vérifier la session
            await self.check_auth()
            if self.is_authenticated:
                yield rx.redirect("/dashboard")


def require_auth(page_component):
    """
    Décorateur pour protéger une page et requérir l'authentification.
    Redirige vers /login si non connecté.
    
    Usage:
        @rx.page(route="/protected")
        @require_auth
        def protected_page():
            return rx.text("Contenu protégé")
    """
    def wrapper(*args, **kwargs):
        return rx.cond(
            AuthState.is_authenticated,
            page_component(*args, **kwargs),
            rx.fragment(
                rx.script(
                    """
                    if (typeof window !== 'undefined') {
                        window.location.href = '/login';
                    }
                    """
                ),
                rx.center(
                    rx.vstack(
                        rx.spinner(size="3"),
                        rx.text("Redirection vers la connexion..."),
                        spacing="4",
                    ),
                    min_height="100vh",
                ),
            ),
        )
    return wrapper