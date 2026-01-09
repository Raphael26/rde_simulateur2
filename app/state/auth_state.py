"""
Authentication State
Manages user authentication state for the application
"""

import reflex as rx
from typing import Optional
from ..services import auth_service


#class AuthState(rx.State):
#    """Authentication state management"""
#    
#    # User data
#    user_id: str = ""
#    user_email: str = ""
#    user_full_name: str = ""
#    user_avatar_url: str = ""
#    user_created_at: str = ""
#    
#    # Auth state
#    is_authenticated: bool = False
#    is_loading: bool = False
#    
#    # Form fields
#    login_email: str = ""
#    login_password: str = ""
#    register_email: str = ""
#    register_password: str = ""
#    register_password_confirm: str = ""
#    register_full_name: str = ""
#    forgot_email: str = ""
#    new_password: str = ""
#    new_password_confirm: str = ""
#    
#    # Error/Success messages
#    error_message: str = ""
#    success_message: str = ""
#    
#    # UI state
#    show_password: bool = False
#    
#    @rx.var
#    def user_initials(self) -> str:
#        """Get user initials for avatar"""
#        if self.user_full_name:
#            parts = self.user_full_name.split()
#            if len(parts) >= 2:
#                return (parts[0][0] + parts[1][0]).upper()
#            elif len(parts) == 1:
#                return parts[0][:2].upper()
#        elif self.user_email:
#            return self.user_email[:2].upper()
#        return "U"
#    
#    @rx.var
#    def display_name(self) -> str:
#        """Get display name for user"""
#        return self.user_full_name or self.user_email.split("@")[0] if self.user_email else "Utilisateur"
#    
#    def _clear_messages(self):
#        """Clear error and success messages"""
#        self.error_message = ""
#        self.success_message = ""
#    
#    def _clear_form_fields(self):
#        """Clear all form fields"""
#        self.login_email = ""
#        self.login_password = ""
#        self.register_email = ""
#        self.register_password = ""
#        self.register_password_confirm = ""
#        self.register_full_name = ""
#        self.forgot_email = ""
#        self.new_password = ""
#        self.new_password_confirm = ""
#    
#    def _set_user(self, user: auth_service.AuthUser):
#        """Set user data from AuthUser object"""
#        self.user_id = user.id
#        self.user_email = user.email or ""
#        self.user_full_name = user.full_name or ""
#        self.user_avatar_url = user.avatar_url or ""
#        self.user_created_at = user.created_at or ""
#        self.is_authenticated = True
#    
#    def _clear_user(self):
#        """Clear user data"""
#        self.user_id = ""
#        self.user_email = ""
#        self.user_full_name = ""
#        self.user_avatar_url = ""
#        self.user_created_at = ""
#        self.is_authenticated = False
#    
#    @rx.event
#    def toggle_password_visibility(self):
#        """Toggle password visibility"""
#        self.show_password = not self.show_password
#    
#    @rx.event
#    def set_login_email(self, value: str):
#        """Set login email"""
#        self.login_email = value
#        self._clear_messages()
#    
#    @rx.event
#    def set_login_password(self, value: str):
#        """Set login password"""
#        self.login_password = value
#        self._clear_messages()
#    
#    @rx.event
#    def set_register_email(self, value: str):
#        """Set register email"""
#        self.register_email = value
#        self._clear_messages()
#    
#    @rx.event
#    def set_register_password(self, value: str):
#        """Set register password"""
#        self.register_password = value
#        self._clear_messages()
#    
#    @rx.event
#    def set_register_password_confirm(self, value: str):
#        """Set register password confirmation"""
#        self.register_password_confirm = value
#        self._clear_messages()
#    
#    @rx.event
#    def set_register_full_name(self, value: str):
#        """Set register full name"""
#        self.register_full_name = value
#        self._clear_messages()
#    
#    @rx.event
#    def set_forgot_email(self, value: str):
#        """Set forgot password email"""
#        self.forgot_email = value
#        self._clear_messages()
#    
#    @rx.event
#    def set_new_password(self, value: str):
#        """Set new password"""
#        self.new_password = value
#        self._clear_messages()
#    
#    @rx.event
#    def set_new_password_confirm(self, value: str):
#        """Set new password confirmation"""
#        self.new_password_confirm = value
#        self._clear_messages()
#    
#    @rx.event
#    def check_auth(self):
#        """Check if user is authenticated on page load"""
#        user = auth_service.get_current_user()
#        if user:
#            self._set_user(user)
#        else:
#            self._clear_user()
#    
#    @rx.event
#    def login(self):
#        """Handle login form submission"""
#        self._clear_messages()
#        self.is_loading = True
#        yield
#        
#        if not self.login_email or not self.login_password:
#            self.error_message = "Veuillez remplir tous les champs."
#            self.is_loading = False
#            return
#        
#        user, error = auth_service.sign_in(self.login_email, self.login_password)
#        
#        if error:
#            self.error_message = error
#            self.is_loading = False
#            return
#        
#        if user:
#            self._set_user(user)
#            self._clear_form_fields()
#            self.is_loading = False
#            yield rx.redirect("/dashboard")
#        else:
#            self.error_message = "Erreur de connexion. Veuillez réessayer."
#            self.is_loading = False
#    
#    @rx.event
#    def register(self):
#        """Handle registration form submission"""
#        self._clear_messages()
#        self.is_loading = True
#        yield
#        
#        # Validation
#        if not self.register_email or not self.register_password:
#            self.error_message = "Veuillez remplir tous les champs obligatoires."
#            self.is_loading = False
#            return
#        
#        if self.register_password != self.register_password_confirm:
#            self.error_message = "Les mots de passe ne correspondent pas."
#            self.is_loading = False
#            return
#        
#        if len(self.register_password) < 6:
#            self.error_message = "Le mot de passe doit contenir au moins 6 caractères."
#            self.is_loading = False
#            return
#        
#        user, error = auth_service.sign_up(
#            email=self.register_email,
#            password=self.register_password,
#            full_name=self.register_full_name or None
#        )
#        
#        if error:
#            self.error_message = error
#            self.is_loading = False
#            return
#        
#        if user:
#            self._set_user(user)
#            self._clear_form_fields()
#            self.success_message = "Compte créé avec succès ! Vérifiez votre email pour confirmer votre inscription."
#            self.is_loading = False
#            yield rx.redirect("/dashboard")
#        else:
#            self.error_message = "Erreur lors de l'inscription. Veuillez réessayer."
#            self.is_loading = False
#    
#    @rx.event
#    def logout(self):
#        """Handle logout"""
#        self.is_loading = True
#        yield
#        
#        success, error = auth_service.sign_out()
#        
#        self._clear_user()
#        self._clear_form_fields()
#        self.is_loading = False
#        
#        yield rx.redirect("/")
#    
#    @rx.event
#    def request_password_reset(self):
#        """Handle forgot password form submission"""
#        self._clear_messages()
#        self.is_loading = True
#        yield
#        
#        if not self.forgot_email:
#            self.error_message = "Veuillez entrer votre adresse email."
#            self.is_loading = False
#            return
#        
#        success, error = auth_service.request_password_reset(self.forgot_email)
#        
#        # Always show success message to prevent email enumeration
#        self.success_message = "Si cette adresse email est associée à un compte, vous recevrez un lien de réinitialisation."
#        self._clear_form_fields()
#        self.is_loading = False
#    
#    @rx.event
#    def update_password(self):
#        """Handle password update"""
#        self._clear_messages()
#        self.is_loading = True
#        yield
#        
#        if not self.new_password:
#            self.error_message = "Veuillez entrer un nouveau mot de passe."
#            self.is_loading = False
#            return
#        
#        if self.new_password != self.new_password_confirm:
#            self.error_message = "Les mots de passe ne correspondent pas."
#            self.is_loading = False
#            return
#        
#        if len(self.new_password) < 6:
#            self.error_message = "Le mot de passe doit contenir au moins 6 caractères."
#            self.is_loading = False
#            return
#        
#        success, error = auth_service.update_password(self.new_password)
#        
#        if error:
#            self.error_message = error
#            self.is_loading = False
#            return
#        
#        self.success_message = "Mot de passe mis à jour avec succès."
#        self._clear_form_fields()
#        self.is_loading = False
#    
#    @rx.event
#    def update_profile(self, full_name: str):
#        """Update user profile"""
#        self._clear_messages()
#        self.is_loading = True
#        yield
#        
#        user, error = auth_service.update_user_metadata(full_name=full_name)
#        
#        if error:
#            self.error_message = error
#            self.is_loading = False
#            return
#        
#        if user:
#            self._set_user(user)
#            self.success_message = "Profil mis à jour avec succès."
#        
#        self.is_loading = False


class AuthState(rx.State):
    """État pour la gestion de l'authentification."""
    
    # Informations utilisateur
    user_id: str = ""
    user_email: str = ""
    is_authenticated: bool = False
    is_loading: bool = False
    error_message: str = ""
    success_message: str = ""
    
    # Champs de formulaire
    email: str = ""
    password: str = ""
    password_confirm: str = ""
    
    @rx.var
    def is_logged_in(self) -> bool:
        """Vérifie si l'utilisateur est connecté."""
        return self.is_authenticated and self.user_id != ""
    
    @rx.var
    def initials(self) -> str:
        """Retourne les initiales de l'utilisateur."""
        if self.user_email:
            return self.user_email[0:2].upper()
        return "U"
    
    @rx.var
    def display_name(self) -> str:
        """Retourne le nom d'affichage."""
        if self.user_email:
            return self.user_email.split("@")[0]
        return "Utilisateur"
    
    @rx.event
    def set_email(self, value: str):
        """Met à jour l'email."""
        self.email = value
        self.error_message = ""
    
    @rx.event
    def set_password(self, value: str):
        """Met à jour le mot de passe."""
        self.password = value
        self.error_message = ""
    
    @rx.event
    def set_password_confirm(self, value: str):
        """Met à jour la confirmation du mot de passe."""
        self.password_confirm = value
        self.error_message = ""
    
    @rx.event
    async def handle_login(self):
        """Gère la connexion de l'utilisateur."""
        self.is_loading = True
        self.error_message = ""
        yield
        
        try:
            if not self.email or not self.password:
                self.error_message = "Veuillez remplir tous les champs"
                self.is_loading = False
                return
            
            # Essayer Supabase
            supabase = None
            try:
                from ..services.supabase_service import supabase as sb_client
                supabase = sb_client
            except ImportError:
                pass
            
            if supabase:
                response = supabase.auth.sign_in_with_password({
                    "email": self.email,
                    "password": self.password
                })
                
                if response.user:
                    self.user_id = response.user.id
                    self.user_email = response.user.email
                    self.is_authenticated = True
                    self.error_message = ""
                    self.password = ""
                    self.is_loading = False
                    yield rx.redirect("/dashboard")
                    return
            else:
                # Mode démo sans Supabase
                if self.email and self.password:
                    self.user_id = "demo-user-123"
                    self.user_email = self.email
                    self.is_authenticated = True
                    self.error_message = ""
                    self.password = ""
                    self.is_loading = False
                    yield rx.redirect("/dashboard")
                    return
                    
        except Exception as e:
            self.error_message = f"Erreur de connexion: {str(e)}"
        
        self.is_loading = False
    
    @rx.event
    async def handle_register(self):
        """Gère l'inscription de l'utilisateur."""
        self.is_loading = True
        self.error_message = ""
        yield
        
        try:
            if not self.email or not self.password:
                self.error_message = "Veuillez remplir tous les champs"
                self.is_loading = False
                return
            
            if self.password != self.password_confirm:
                self.error_message = "Les mots de passe ne correspondent pas"
                self.is_loading = False
                return
            
            if len(self.password) < 6:
                self.error_message = "Le mot de passe doit contenir au moins 6 caractères"
                self.is_loading = False
                return
            
            # Essayer Supabase
            supabase = None
            try:
                from ..services.supabase_service import supabase as sb_client
                supabase = sb_client
            except ImportError:
                pass
            
            if supabase:
                response = supabase.auth.sign_up({
                    "email": self.email,
                    "password": self.password
                })
                
                if response.user:
                    self.success_message = "Compte créé ! Vérifiez votre email."
                    self.error_message = ""
                    self.password = ""
                    self.password_confirm = ""
                    self.is_loading = False
                    yield rx.redirect("/login")
                    return
            else:
                # Mode démo
                self.success_message = "Compte créé (mode démo)"
                self.is_loading = False
                yield rx.redirect("/login")
                return
                    
        except Exception as e:
            self.error_message = f"Erreur d'inscription: {str(e)}"
        
        self.is_loading = False
    
    @rx.event
    def handle_logout(self):
        """Gère la déconnexion de l'utilisateur."""
        try:
            supabase = None
            try:
                from ..services.supabase_service import supabase as sb_client
                supabase = sb_client
            except ImportError:
                pass
            
            if supabase:
                supabase.auth.sign_out()
        except Exception:
            pass
        
        # Réinitialiser l'état
        self.user_id = ""
        self.user_email = ""
        self.is_authenticated = False
        self.email = ""
        self.password = ""
        self.error_message = ""
        self.success_message = ""
        
        return rx.redirect("/")
    
    @rx.event
    async def check_auth(self):
        """Vérifie si l'utilisateur est déjà connecté."""
        try:
            supabase = None
            try:
                from ..services.supabase_service import supabase as sb_client
                supabase = sb_client
            except ImportError:
                pass
            
            if supabase:
                response = supabase.auth.get_user()
                if response and response.user:
                    self.user_id = response.user.id
                    self.user_email = response.user.email
                    self.is_authenticated = True
        except Exception:
            pass


def require_auth(page_component):
    """
    Decorator to require authentication for a page
    Redirects to login if not authenticated
    """
    def wrapper():
        return rx.cond(
            AuthState.is_authenticated,
            page_component(),
            rx.fragment(
                rx.script(
                    """
                    if (typeof window !== 'undefined') {
                        window.location.href = '/login';
                    }
                    """
                )
            )
        )
    return wrapper