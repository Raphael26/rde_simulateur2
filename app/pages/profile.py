#"""
#Page Profil Utilisateur
#Design moderne avec sections pour les informations, modifications et sécurité
#"""
#
#import reflex as rx
#from ..state.auth_state import AuthState
#from ..state.user_state import UserState
#from ..styles.design_system import Colors, Typography, Spacing, Borders, Shadows
#from ..components.sidebar import sidebar
#
#
#class ProfileState(AuthState):
#    """État étendu pour la gestion du profil."""
#    
#    # Mode édition
#    is_editing: bool = False
#    
#    # Champs de formulaire - Profil
#    edit_full_name: str = ""
#    edit_phone: str = ""
#    edit_company: str = ""
#    
#    # Champs de formulaire - Mot de passe
#    current_password: str = ""
#    new_password: str = ""
#    confirm_new_password: str = ""
#    show_current_password: bool = False
#    show_new_password: bool = False
#    
#    # États
#    is_saving_profile: bool = False
#    is_changing_password: bool = False
#    profile_success: str = ""
#    profile_error: str = ""
#    password_success: str = ""
#    password_error: str = ""
#    
#    # ==================== Computed Vars ====================
#    
#    @rx.var
#    def member_since(self) -> str:
#        """Date d'inscription formatée."""
#        # Pour l'instant, retourne une valeur par défaut
#        # À améliorer avec la vraie date depuis Supabase
#        return "Janvier 2026"
#    
#    @rx.var
#    def simulations_count(self) -> str:
#        """Nombre de simulations."""
#        return "0"
#    
#    # ==================== Event Handlers ====================
#    
#    @rx.event
#    def start_editing(self):
#        """Active le mode édition."""
#        self.is_editing = True
#        self.edit_full_name = self.user_full_name
#        self.profile_error = ""
#        self.profile_success = ""
#    
#    @rx.event
#    def cancel_editing(self):
#        """Annule le mode édition."""
#        self.is_editing = False
#        self.edit_full_name = ""
#        self.edit_phone = ""
#        self.edit_company = ""
#        self.profile_error = ""
#    
#    @rx.event
#    def set_edit_full_name(self, value: str):
#        self.edit_full_name = value
#        self.profile_error = ""
#    
#    @rx.event
#    def set_edit_phone(self, value: str):
#        self.edit_phone = value
#    
#    @rx.event
#    def set_edit_company(self, value: str):
#        self.edit_company = value
#    
#    @rx.event
#    def set_current_password(self, value: str):
#        self.current_password = value
#        self.password_error = ""
#    
#    @rx.event
#    def set_new_password(self, value: str):
#        self.new_password = value
#        self.password_error = ""
#    
#    @rx.event
#    def set_confirm_new_password(self, value: str):
#        self.confirm_new_password = value
#        self.password_error = ""
#    
#    @rx.event
#    def toggle_current_password(self):
#        self.show_current_password = not self.show_current_password
#    
#    @rx.event
#    def toggle_new_password(self):
#        self.show_new_password = not self.show_new_password
#    
#    @rx.event
#    async def save_profile(self):
#        """Sauvegarde les modifications du profil."""
#        self.profile_error = ""
#        self.profile_success = ""
#        
#        # Validation
#        if not self.edit_full_name or len(self.edit_full_name.strip()) < 2:
#            self.profile_error = "Le nom doit contenir au moins 2 caractères"
#            return
#        
#        self.is_saving_profile = True
#        yield
#        
#        try:
#            client = self._get_supabase_client()
#            
#            if client:
#                # Mettre à jour les métadonnées utilisateur dans Supabase Auth
#                response = client.auth.update_user({
#                    "data": {
#                        "full_name": self.edit_full_name.strip(),
#                        "phone": self.edit_phone.strip() if self.edit_phone else None,
#                        "company": self.edit_company.strip() if self.edit_company else None,
#                    }
#                })
#                
#                if response.user:
#                    self.user_full_name = self.edit_full_name.strip()
#                    self.is_editing = False
#                    self.profile_success = "Profil mis à jour avec succès"
#                    yield rx.toast.success("Profil mis à jour !")
#                else:
#                    self.profile_error = "Erreur lors de la mise à jour"
#            else:
#                # Mode démo sans Supabase
#                self.user_full_name = self.edit_full_name.strip()
#                self.is_editing = False
#                self.profile_success = "Profil mis à jour (mode démo)"
#                yield rx.toast.success("Profil mis à jour !")
#                
#        except Exception as e:
#            self.profile_error = f"Erreur: {str(e)[:50]}"
#            print(f"❌ Erreur mise à jour profil: {e}")
#        
#        self.is_saving_profile = False
#    
#    @rx.event
#    async def change_password(self):
#        """Change le mot de passe de l'utilisateur."""
#        self.password_error = ""
#        self.password_success = ""
#        
#        # Validations
#        if not self.current_password:
#            self.password_error = "Veuillez entrer votre mot de passe actuel"
#            return
#        
#        if not self.new_password:
#            self.password_error = "Veuillez entrer un nouveau mot de passe"
#            return
#        
#        if len(self.new_password) < 8:
#            self.password_error = "Le nouveau mot de passe doit contenir au moins 8 caractères"
#            return
#        
#        if self.new_password != self.confirm_new_password:
#            self.password_error = "Les mots de passe ne correspondent pas"
#            return
#        
#        if self.current_password == self.new_password:
#            self.password_error = "Le nouveau mot de passe doit être différent de l'ancien"
#            return
#        
#        self.is_changing_password = True
#        yield
#        
#        try:
#            client = self._get_supabase_client()
#            
#            if client:
#                # Mettre à jour le mot de passe
#                response = client.auth.update_user({
#                    "password": self.new_password
#                })
#                
#                if response.user:
#                    self.current_password = ""
#                    self.new_password = ""
#                    self.confirm_new_password = ""
#                    self.password_success = "Mot de passe modifié avec succès"
#                    yield rx.toast.success("Mot de passe modifié !")
#                else:
#                    self.password_error = "Erreur lors du changement de mot de passe"
#            else:
#                self.password_error = "Service d'authentification non disponible"
#                
#        except Exception as e:
#            error_str = str(e)
#            if "same_password" in error_str.lower():
#                self.password_error = "Le nouveau mot de passe doit être différent"
#            else:
#                self.password_error = "Erreur lors du changement de mot de passe"
#            print(f"❌ Erreur changement mot de passe: {e}")
#        
#        self.is_changing_password = False
#
#
## ============================================
## COMPOSANTS UI
## ============================================
#
#def profile_header() -> rx.Component:
#    """En-tête du profil avec avatar et infos principales."""
#    return rx.box(
#        rx.hstack(
#            # Avatar
#            rx.box(
#                rx.text(
#                    ProfileState.initials,
#                    font_size="2rem",
#                    font_weight="700",
#                    color=Colors.WHITE,
#                ),
#                width="100px",
#                height="100px",
#                background=f"linear-gradient(135deg, {Colors.PRIMARY} 0%, #2d6b62 100%)",
#                border_radius="50%",
#                display="flex",
#                align_items="center",
#                justify_content="center",
#                box_shadow=Shadows.LG,
#            ),
#            
#            # Infos
#            rx.vstack(
#                rx.text(
#                    ProfileState.display_name,
#                    font_size="1.75rem",
#                    font_weight="700",
#                    color=Colors.GRAY_900,
#                ),
#                rx.hstack(
#                    rx.icon("mail", size=16, color=Colors.GRAY_400),
#                    rx.text(
#                        ProfileState.user_email,
#                        font_size=Typography.SIZE_BASE,
#                        color=Colors.GRAY_500,
#                    ),
#                    spacing="2",
#                ),
#                rx.hstack(
#                    rx.box(
#                        rx.hstack(
#                            rx.icon("calendar", size=14, color=Colors.PRIMARY),
#                            rx.text(
#                                f"Membre depuis {ProfileState.member_since}",
#                                font_size=Typography.SIZE_SM,
#                            ),
#                            spacing="1",
#                        ),
#                        padding="0.25rem 0.75rem",
#                        background=Colors.PRIMARY_LIGHTER,
#                        border_radius=Borders.RADIUS_FULL,
#                        color=Colors.PRIMARY,
#                    ),
#                    rx.box(
#                        rx.hstack(
#                            rx.icon("file-text", size=14, color=Colors.INFO),
#                            rx.text(
#                                f"{ProfileState.simulations_count} simulations",
#                                font_size=Typography.SIZE_SM,
#                            ),
#                            spacing="1",
#                        ),
#                        padding="0.25rem 0.75rem",
#                        background=f"{Colors.INFO}15",
#                        border_radius=Borders.RADIUS_FULL,
#                        color=Colors.INFO,
#                    ),
#                    spacing="2",
#                    margin_top="0.5rem",
#                ),
#                spacing="1",
#                align_items="start",
#            ),
#            
#            spacing="6",
#            align="center",
#            width="100%",
#        ),
#        padding="2rem",
#        background=Colors.WHITE,
#        border_radius=Borders.RADIUS_2XL,
#        box_shadow=Shadows.MD,
#        border=f"1px solid {Colors.GRAY_100}",
#        width="100%",
#    )
#
#
#def section_card(title: str, icon: str, children: rx.Component, action: rx.Component = None) -> rx.Component:
#    """Carte de section avec titre et contenu."""
#    header_content = [
#        rx.hstack(
#            rx.box(
#                rx.icon(icon, size=20, color=Colors.PRIMARY),
#                padding="0.5rem",
#                background=Colors.PRIMARY_LIGHTER,
#                border_radius=Borders.RADIUS_MD,
#            ),
#            rx.text(
#                title,
#                font_size=Typography.SIZE_LG,
#                font_weight="600",
#                color=Colors.GRAY_900,
#            ),
#            spacing="3",
#            align="center",
#        ),
#        rx.spacer(),
#    ]
#    
#    if action is not None:
#        header_content.append(action)
#    
#    return rx.box(
#        rx.vstack(
#            rx.hstack(
#                *header_content,
#                width="100%",
#                align="center",
#            ),
#            rx.divider(margin_y="1rem"),
#            children,
#            spacing="0",
#            width="100%",
#        ),
#        padding="1.5rem",
#        background=Colors.WHITE,
#        border_radius=Borders.RADIUS_XL,
#        box_shadow=Shadows.SM,
#        border=f"1px solid {Colors.GRAY_100}",
#        width="100%",
#    )
#
#
#def info_row(label: str, value: rx.Var, icon: str = None) -> rx.Component:
#    """Ligne d'information."""
#    return rx.hstack(
#        rx.hstack(
#            rx.icon(icon, size=16, color=Colors.GRAY_400) if icon else rx.box(),
#            rx.text(
#                label,
#                font_size=Typography.SIZE_SM,
#                color=Colors.GRAY_500,
#                min_width="120px",
#            ),
#            spacing="2",
#        ),
#        rx.text(
#            value,
#            font_size=Typography.SIZE_BASE,
#            color=Colors.GRAY_900,
#            font_weight="500",
#        ),
#        spacing="4",
#        width="100%",
#        padding_y="0.75rem",
#        border_bottom=f"1px solid {Colors.GRAY_100}",
#    )
#
#
#def form_field(
#    label: str,
#    value: rx.Var,
#    on_change,
#    placeholder: str = "",
#    icon: str = None,
#    field_type: str = "text",
#) -> rx.Component:
#    """Champ de formulaire stylisé."""
#    return rx.vstack(
#        rx.text(
#            label,
#            font_size=Typography.SIZE_SM,
#            font_weight="500",
#            color=Colors.GRAY_700,
#        ),
#        rx.box(
#            rx.hstack(
#                rx.icon(icon, size=18, color=Colors.GRAY_400) if icon else rx.box(),
#                rx.input(
#                    placeholder=placeholder,
#                    type=field_type,
#                    value=value,
#                    on_change=on_change,
#                    width="100%",
#                    border="none",
#                    outline="none",
#                    background="transparent",
#                    font_size=Typography.SIZE_BASE,
#                    _focus={"outline": "none"},
#                ),
#                spacing="3",
#                width="100%",
#                padding="0.75rem 1rem",
#            ),
#            border=f"2px solid {Colors.GRAY_200}",
#            border_radius=Borders.RADIUS_LG,
#            background=Colors.WHITE,
#            _focus_within={
#                "border_color": Colors.PRIMARY,
#                "box_shadow": f"0 0 0 3px {Colors.PRIMARY}20",
#            },
#            transition="all 0.2s ease",
#            width="100%",
#        ),
#        spacing="1",
#        width="100%",
#    )
#
#
#def personal_info_section() -> rx.Component:
#    """Section des informations personnelles."""
#    
#    # Contenu en mode lecture
#    view_content = rx.vstack(
#        info_row("Nom complet", ProfileState.display_name, "user"),
#        info_row("Email", ProfileState.user_email, "mail"),
#        rx.hstack(
#            rx.text(
#                "L'adresse email ne peut pas être modifiée",
#                font_size=Typography.SIZE_XS,
#                color=Colors.GRAY_400,
#            ),
#            rx.icon("info", size=12, color=Colors.GRAY_400),
#            spacing="1",
#            margin_top="0.5rem",
#        ),
#        spacing="0",
#        width="100%",
#    )
#    
#    # Contenu en mode édition
#    edit_content = rx.vstack(
#        # Message de succès
#        rx.cond(
#            ProfileState.profile_success != "",
#            rx.box(
#                rx.hstack(
#                    rx.icon("check-circle", size=16, color=Colors.SUCCESS),
#                    rx.text(ProfileState.profile_success, font_size=Typography.SIZE_SM, color=Colors.SUCCESS),
#                    spacing="2",
#                ),
#                padding="0.75rem",
#                background=Colors.SUCCESS_LIGHT,
#                border_radius=Borders.RADIUS_MD,
#                width="100%",
#                margin_bottom="1rem",
#            ),
#            rx.box(),
#        ),
#        
#        # Message d'erreur
#        rx.cond(
#            ProfileState.profile_error != "",
#            rx.box(
#                rx.hstack(
#                    rx.icon("alert-circle", size=16, color="#dc2626"),
#                    rx.text(ProfileState.profile_error, font_size=Typography.SIZE_SM, color="#dc2626"),
#                    spacing="2",
#                ),
#                padding="0.75rem",
#                background="#fef2f2",
#                border_radius=Borders.RADIUS_MD,
#                width="100%",
#                margin_bottom="1rem",
#            ),
#            rx.box(),
#        ),
#        
#        form_field(
#            "Nom complet",
#            ProfileState.edit_full_name,
#            ProfileState.set_edit_full_name,
#            "Votre nom complet",
#            "user",
#        ),
#        # Email (lecture seule)
#        rx.vstack(
#            rx.text(
#                "Adresse email",
#                font_size=Typography.SIZE_SM,
#                font_weight="500",
#                color=Colors.GRAY_700,
#            ),
#            rx.box(
#                rx.hstack(
#                    rx.icon("mail", size=18, color=Colors.GRAY_400),
#                    rx.text(
#                        ProfileState.user_email,
#                        font_size=Typography.SIZE_BASE,
#                        color=Colors.GRAY_400,
#                    ),
#                    rx.icon("lock", size=14, color=Colors.GRAY_300),
#                    spacing="3",
#                    width="100%",
#                    padding="0.75rem 1rem",
#                ),
#                border=f"2px solid {Colors.GRAY_200}",
#                border_radius=Borders.RADIUS_LG,
#                background=Colors.GRAY_50,
#                width="100%",
#            ),
#            rx.text(
#                "L'adresse email ne peut pas être modifiée",
#                font_size="11px",
#                color=Colors.GRAY_400,
#                margin_top="0.25rem",
#            ),
#            spacing="1",
#            width="100%",
#        ),
#        rx.hstack(
#            rx.button(
#                rx.hstack(rx.icon("x", size=16), rx.text("Annuler"), spacing="2"),
#                variant="outline",
#                on_click=ProfileState.cancel_editing,
#                style={
#                    "border": f"2px solid {Colors.GRAY_300}",
#                    "color": Colors.GRAY_600,
#                },
#            ),
#            rx.button(
#                rx.cond(
#                    ProfileState.is_saving_profile,
#                    rx.hstack(rx.spinner(size="1"), rx.text("Enregistrement..."), spacing="2"),
#                    rx.hstack(rx.icon("check", size=16), rx.text("Enregistrer"), spacing="2"),
#                ),
#                on_click=ProfileState.save_profile,
#                disabled=ProfileState.is_saving_profile,
#                style={
#                    "background": Colors.PRIMARY,
#                    "color": Colors.WHITE,
#                },
#            ),
#            spacing="3",
#            margin_top="1rem",
#            justify="end",
#            width="100%",
#        ),
#        spacing="4",
#        width="100%",
#    )
#    
#    # Bouton d'édition
#    edit_button = rx.cond(
#        ProfileState.is_editing,
#        rx.box(),
#        rx.button(
#            rx.hstack(rx.icon("pencil", size=16), rx.text("Modifier"), spacing="2"),
#            variant="outline",
#            size="2",
#            on_click=ProfileState.start_editing,
#            style={
#                "border": f"2px solid {Colors.PRIMARY}",
#                "color": Colors.PRIMARY,
#                "_hover": {"background": Colors.PRIMARY_LIGHTER},
#            },
#        ),
#    )
#    
#    return section_card(
#        "Informations personnelles",
#        "user-circle",
#        rx.cond(ProfileState.is_editing, edit_content, view_content),
#        edit_button,
#    )
#
#
#def security_section() -> rx.Component:
#    """Section sécurité pour changer le mot de passe."""
#    return section_card(
#        "Sécurité",
#        "shield",
#        rx.vstack(
#            # Message de succès
#            rx.cond(
#                ProfileState.password_success != "",
#                rx.box(
#                    rx.hstack(
#                        rx.icon("check-circle", size=16, color=Colors.SUCCESS),
#                        rx.text(ProfileState.password_success, font_size=Typography.SIZE_SM, color=Colors.SUCCESS),
#                        spacing="2",
#                    ),
#                    padding="0.75rem",
#                    background=Colors.SUCCESS_LIGHT,
#                    border_radius=Borders.RADIUS_MD,
#                    width="100%",
#                    margin_bottom="1rem",
#                ),
#                rx.box(),
#            ),
#            
#            # Message d'erreur
#            rx.cond(
#                ProfileState.password_error != "",
#                rx.box(
#                    rx.hstack(
#                        rx.icon("alert-circle", size=16, color="#dc2626"),
#                        rx.text(ProfileState.password_error, font_size=Typography.SIZE_SM, color="#dc2626"),
#                        spacing="2",
#                    ),
#                    padding="0.75rem",
#                    background="#fef2f2",
#                    border_radius=Borders.RADIUS_MD,
#                    width="100%",
#                    margin_bottom="1rem",
#                ),
#                rx.box(),
#            ),
#            
#            rx.text(
#                "Changer le mot de passe",
#                font_size=Typography.SIZE_BASE,
#                font_weight="600",
#                color=Colors.GRAY_700,
#                margin_bottom="1rem",
#            ),
#            
#            # Mot de passe actuel
#            rx.vstack(
#                rx.text(
#                    "Mot de passe actuel",
#                    font_size=Typography.SIZE_SM,
#                    font_weight="500",
#                    color=Colors.GRAY_700,
#                ),
#                rx.box(
#                    rx.hstack(
#                        rx.icon("lock", size=18, color=Colors.GRAY_400),
#                        rx.input(
#                            placeholder="••••••••",
#                            type=rx.cond(ProfileState.show_current_password, "text", "password"),
#                            value=ProfileState.current_password,
#                            on_change=ProfileState.set_current_password,
#                            width="100%",
#                            border="none",
#                            outline="none",
#                            background="transparent",
#                            font_size=Typography.SIZE_BASE,
#                            _focus={"outline": "none"},
#                        ),
#                        rx.icon_button(
#                            rx.cond(
#                                ProfileState.show_current_password,
#                                rx.icon("eye-off", size=18),
#                                rx.icon("eye", size=18),
#                            ),
#                            variant="ghost",
#                            size="1",
#                            cursor="pointer",
#                            on_click=ProfileState.toggle_current_password,
#                            color=Colors.GRAY_400,
#                        ),
#                        spacing="3",
#                        width="100%",
#                        padding="0.75rem 1rem",
#                    ),
#                    border=f"2px solid {Colors.GRAY_200}",
#                    border_radius=Borders.RADIUS_LG,
#                    background=Colors.WHITE,
#                    _focus_within={
#                        "border_color": Colors.PRIMARY,
#                        "box_shadow": f"0 0 0 3px {Colors.PRIMARY}20",
#                    },
#                    transition="all 0.2s ease",
#                    width="100%",
#                ),
#                spacing="1",
#                width="100%",
#            ),
#            
#            # Nouveau mot de passe
#            rx.vstack(
#                rx.text(
#                    "Nouveau mot de passe",
#                    font_size=Typography.SIZE_SM,
#                    font_weight="500",
#                    color=Colors.GRAY_700,
#                ),
#                rx.box(
#                    rx.hstack(
#                        rx.icon("key", size=18, color=Colors.GRAY_400),
#                        rx.input(
#                            placeholder="••••••••",
#                            type=rx.cond(ProfileState.show_new_password, "text", "password"),
#                            value=ProfileState.new_password,
#                            on_change=ProfileState.set_new_password,
#                            width="100%",
#                            border="none",
#                            outline="none",
#                            background="transparent",
#                            font_size=Typography.SIZE_BASE,
#                            _focus={"outline": "none"},
#                        ),
#                        rx.icon_button(
#                            rx.cond(
#                                ProfileState.show_new_password,
#                                rx.icon("eye-off", size=18),
#                                rx.icon("eye", size=18),
#                            ),
#                            variant="ghost",
#                            size="1",
#                            cursor="pointer",
#                            on_click=ProfileState.toggle_new_password,
#                            color=Colors.GRAY_400,
#                        ),
#                        spacing="3",
#                        width="100%",
#                        padding="0.75rem 1rem",
#                    ),
#                    border=f"2px solid {Colors.GRAY_200}",
#                    border_radius=Borders.RADIUS_LG,
#                    background=Colors.WHITE,
#                    _focus_within={
#                        "border_color": Colors.PRIMARY,
#                        "box_shadow": f"0 0 0 3px {Colors.PRIMARY}20",
#                    },
#                    transition="all 0.2s ease",
#                    width="100%",
#                ),
#                rx.text(
#                    "Minimum 8 caractères",
#                    font_size="11px",
#                    color=Colors.GRAY_400,
#                    margin_top="0.25rem",
#                ),
#                spacing="1",
#                width="100%",
#            ),
#            
#            # Confirmer nouveau mot de passe
#            rx.vstack(
#                rx.text(
#                    "Confirmer le nouveau mot de passe",
#                    font_size=Typography.SIZE_SM,
#                    font_weight="500",
#                    color=Colors.GRAY_700,
#                ),
#                rx.box(
#                    rx.hstack(
#                        rx.icon("key", size=18, color=Colors.GRAY_400),
#                        rx.input(
#                            placeholder="••••••••",
#                            type=rx.cond(ProfileState.show_new_password, "text", "password"),
#                            value=ProfileState.confirm_new_password,
#                            on_change=ProfileState.set_confirm_new_password,
#                            width="100%",
#                            border="none",
#                            outline="none",
#                            background="transparent",
#                            font_size=Typography.SIZE_BASE,
#                            _focus={"outline": "none"},
#                        ),
#                        rx.cond(
#                            (ProfileState.confirm_new_password != "") & 
#                            (ProfileState.new_password == ProfileState.confirm_new_password),
#                            rx.icon("check-circle", size=18, color=Colors.SUCCESS),
#                            rx.box(width="18px"),
#                        ),
#                        spacing="3",
#                        width="100%",
#                        padding="0.75rem 1rem",
#                    ),
#                    border=f"2px solid {Colors.GRAY_200}",
#                    border_radius=Borders.RADIUS_LG,
#                    background=Colors.WHITE,
#                    _focus_within={
#                        "border_color": Colors.PRIMARY,
#                        "box_shadow": f"0 0 0 3px {Colors.PRIMARY}20",
#                    },
#                    transition="all 0.2s ease",
#                    width="100%",
#                ),
#                spacing="1",
#                width="100%",
#            ),
#            
#            # Bouton de changement
#            rx.hstack(
#                rx.button(
#                    rx.cond(
#                        ProfileState.is_changing_password,
#                        rx.hstack(rx.spinner(size="1"), rx.text("Modification..."), spacing="2"),
#                        rx.hstack(rx.icon("refresh-cw", size=16), rx.text("Changer le mot de passe"), spacing="2"),
#                    ),
#                    on_click=ProfileState.change_password,
#                    disabled=ProfileState.is_changing_password,
#                    style={
#                        "background": Colors.PRIMARY,
#                        "color": Colors.WHITE,
#                    },
#                ),
#                justify="end",
#                width="100%",
#                margin_top="1rem",
#            ),
#            
#            spacing="4",
#            width="100%",
#        ),
#    )
#
#
#def danger_zone_section() -> rx.Component:
#    """Section zone de danger pour la suppression de compte."""
#    return rx.box(
#        rx.vstack(
#            rx.hstack(
#                rx.hstack(
#                    rx.box(
#                        rx.icon("alert-triangle", size=20, color="#dc2626"),
#                        padding="0.5rem",
#                        background="#fef2f2",
#                        border_radius=Borders.RADIUS_MD,
#                    ),
#                    rx.text(
#                        "Zone de danger",
#                        font_size=Typography.SIZE_LG,
#                        font_weight="600",
#                        color="#dc2626",
#                    ),
#                    spacing="3",
#                    align="center",
#                ),
#                width="100%",
#            ),
#            rx.divider(margin_y="1rem"),
#            rx.hstack(
#                rx.vstack(
#                    rx.text(
#                        "Supprimer le compte",
#                        font_size=Typography.SIZE_BASE,
#                        font_weight="600",
#                        color=Colors.GRAY_900,
#                    ),
#                    rx.text(
#                        "Cette action est irréversible. Toutes vos données seront supprimées.",
#                        font_size=Typography.SIZE_SM,
#                        color=Colors.GRAY_500,
#                    ),
#                    spacing="1",
#                    align_items="start",
#                ),
#                rx.spacer(),
#                rx.alert_dialog.root(
#                    rx.alert_dialog.trigger(
#                        rx.button(
#                            rx.hstack(rx.icon("trash-2", size=16), rx.text("Supprimer"), spacing="2"),
#                            variant="outline",
#                            color_scheme="red",
#                        ),
#                    ),
#                    rx.alert_dialog.content(
#                        rx.alert_dialog.title("Supprimer votre compte ?"),
#                        rx.alert_dialog.description(
#                            "Cette action est irréversible. Toutes vos simulations et données seront définitivement supprimées.",
#                        ),
#                        rx.hstack(
#                            rx.alert_dialog.cancel(
#                                rx.button("Annuler", variant="soft", color_scheme="gray"),
#                            ),
#                            rx.alert_dialog.action(
#                                rx.button(
#                                    "Supprimer définitivement",
#                                    color_scheme="red",
#                                ),
#                            ),
#                            spacing="3",
#                            justify="end",
#                        ),
#                        style={"max_width": "450px"},
#                    ),
#                ),
#                width="100%",
#                align="center",
#            ),
#            spacing="0",
#            width="100%",
#        ),
#        padding="1.5rem",
#        background=Colors.WHITE,
#        border_radius=Borders.RADIUS_XL,
#        box_shadow=Shadows.SM,
#        border="1px solid #fecaca",
#        width="100%",
#    )
#
#
#def profile_content() -> rx.Component:
#    """Contenu principal de la page profil."""
#    return rx.vstack(
#        # Header
#        rx.hstack(
#            rx.vstack(
#                rx.text(
#                    "Mon Profil",
#                    font_size="1.75rem",
#                    font_weight="700",
#                    color=Colors.GRAY_900,
#                ),
#                rx.text(
#                    "Gérez vos informations personnelles et vos paramètres de sécurité",
#                    font_size=Typography.SIZE_BASE,
#                    color=Colors.GRAY_500,
#                ),
#                spacing="1",
#                align_items="start",
#            ),
#            rx.spacer(),
#            rx.button(
#                rx.hstack(rx.icon("arrow-left", size=18), rx.text("Retour au dashboard"), spacing="2"),
#                variant="outline",
#                on_click=rx.redirect("/dashboard"),
#                style={
#                    "border": f"2px solid {Colors.GRAY_300}",
#                    "color": Colors.GRAY_600,
#                },
#            ),
#            width="100%",
#            align="center",
#            margin_bottom="1.5rem",
#        ),
#        
#        # Contenu en 2 colonnes
#        rx.hstack(
#            # Colonne gauche
#            rx.vstack(
#                profile_header(),
#                personal_info_section(),
#                spacing="5",
#                width="60%",
#            ),
#            
#            # Colonne droite
#            rx.vstack(
#                security_section(),
#                danger_zone_section(),
#                spacing="5",
#                width="40%",
#            ),
#            
#            spacing="5",
#            width="100%",
#            align="start",
#        ),
#        
#        spacing="0",
#        width="100%",
#        max_width="1100px",
#    )
#
#
#@rx.page(
#    route="/profile",
#    title="Mon Profil - RDE Consulting",
#    on_load=[AuthState.require_auth, UserState.load_simulations],
#)
#def profile_page() -> rx.Component:
#    """Page de profil utilisateur."""
#    return rx.cond(
#        AuthState.is_authenticated,
#        rx.hstack(
#            sidebar(current_page="profile"),
#            rx.box(
#                profile_content(),
#                min_height="100vh",
#                background=Colors.BG_PAGE,
#                padding="40px",
#                flex="1",
#            ),
#            spacing="0",
#            width="100%",
#            align="stretch",
#        ),
#        rx.center(
#            rx.vstack(
#                rx.spinner(size="3"),
#                rx.text("Chargement...", color=Colors.GRAY_500),
#                spacing="4",
#            ),
#            min_height="100vh",
#            background=Colors.BG_PAGE,
#        ),
#    )


"""
Page Profil Utilisateur
Design moderne avec sections pour les informations, modifications et sécurité
"""

import reflex as rx
from ..state.auth_state import AuthState
from ..state.user_state import UserState
from ..styles.design_system import Colors, Typography, Spacing, Borders, Shadows
from ..components.sidebar import sidebar


class ProfileState(AuthState):
    """État étendu pour la gestion du profil."""
    
    # Mode édition
    is_editing: bool = False
    
    # Champs de formulaire - Profil
    edit_full_name: str = ""
    edit_phone: str = ""
    edit_company: str = ""
    
    # Champs de formulaire - Mot de passe (renommés pour éviter conflit avec AuthState)
    profile_current_password: str = ""
    profile_new_password: str = ""
    profile_confirm_password: str = ""
    profile_show_current_password: bool = False
    profile_show_new_password: bool = False
    
    # États
    is_saving_profile: bool = False
    is_changing_password: bool = False
    profile_success: str = ""
    profile_error: str = ""
    password_success: str = ""
    password_error: str = ""
    
    # ==================== Computed Vars ====================
    
    @rx.var
    def member_since(self) -> str:
        """Date d'inscription formatée."""
        # Pour l'instant, retourne une valeur par défaut
        # À améliorer avec la vraie date depuis Supabase
        return "Janvier 2026"
    
    @rx.var
    def simulations_count(self) -> str:
        """Nombre de simulations."""
        return "0"
    
    # ==================== Event Handlers ====================
    
    @rx.event
    def start_editing(self):
        """Active le mode édition."""
        self.is_editing = True
        self.edit_full_name = self.user_full_name
        self.profile_error = ""
        self.profile_success = ""
    
    @rx.event
    def cancel_editing(self):
        """Annule le mode édition."""
        self.is_editing = False
        self.edit_full_name = ""
        self.edit_phone = ""
        self.edit_company = ""
        self.profile_error = ""
    
    @rx.event
    def set_edit_full_name(self, value: str):
        self.edit_full_name = value
        self.profile_error = ""
    
    @rx.event
    def set_edit_phone(self, value: str):
        self.edit_phone = value
    
    @rx.event
    def set_edit_company(self, value: str):
        self.edit_company = value
    
    @rx.event
    def set_profile_current_password(self, value: str):
        self.profile_current_password = value
        self.password_error = ""
    
    @rx.event
    def set_profile_new_password(self, value: str):
        self.profile_new_password = value
        self.password_error = ""
    
    @rx.event
    def set_profile_confirm_password(self, value: str):
        self.profile_confirm_password = value
        self.password_error = ""
    
    @rx.event
    def toggle_profile_current_password(self):
        self.profile_show_current_password = not self.profile_show_current_password
    
    @rx.event
    def toggle_profile_new_password(self):
        self.profile_show_new_password = not self.profile_show_new_password
    
    @rx.event
    async def save_profile(self):
        """Sauvegarde les modifications du profil."""
        self.profile_error = ""
        self.profile_success = ""
        
        # Validation
        if not self.edit_full_name or len(self.edit_full_name.strip()) < 2:
            self.profile_error = "Le nom doit contenir au moins 2 caractères"
            return
        
        self.is_saving_profile = True
        yield
        
        try:
            client = self._get_supabase_client()
            
            if client:
                # Mettre à jour les métadonnées utilisateur dans Supabase Auth
                response = client.auth.update_user({
                    "data": {
                        "full_name": self.edit_full_name.strip(),
                        "phone": self.edit_phone.strip() if self.edit_phone else None,
                        "company": self.edit_company.strip() if self.edit_company else None,
                    }
                })
                
                if response.user:
                    self.user_full_name = self.edit_full_name.strip()
                    self.is_editing = False
                    self.profile_success = "Profil mis à jour avec succès"
                    yield rx.toast.success("Profil mis à jour !")
                else:
                    self.profile_error = "Erreur lors de la mise à jour"
            else:
                # Mode démo sans Supabase
                self.user_full_name = self.edit_full_name.strip()
                self.is_editing = False
                self.profile_success = "Profil mis à jour (mode démo)"
                yield rx.toast.success("Profil mis à jour !")
                
        except Exception as e:
            self.profile_error = f"Erreur: {str(e)[:50]}"
            print(f"❌ Erreur mise à jour profil: {e}")
        
        self.is_saving_profile = False
    
    @rx.event
    async def change_password(self):
        """Change le mot de passe de l'utilisateur."""
        self.password_error = ""
        self.password_success = ""
        
        # Validations
        if not self.profile_current_password:
            self.password_error = "Veuillez entrer votre mot de passe actuel"
            return
        
        if not self.profile_new_password:
            self.password_error = "Veuillez entrer un nouveau mot de passe"
            return
        
        if len(self.profile_new_password) < 8:
            self.password_error = "Le nouveau mot de passe doit contenir au moins 8 caractères"
            return
        
        if self.profile_new_password != self.profile_confirm_password:
            self.password_error = "Les mots de passe ne correspondent pas"
            return
        
        if self.profile_current_password == self.profile_new_password:
            self.password_error = "Le nouveau mot de passe doit être différent de l'ancien"
            return
        
        self.is_changing_password = True
        yield
        
        try:
            client = self._get_supabase_client()
            
            if client:
                # Mettre à jour le mot de passe
                response = client.auth.update_user({
                    "password": self.profile_new_password
                })
                
                if response.user:
                    self.profile_current_password = ""
                    self.profile_new_password = ""
                    self.profile_confirm_password = ""
                    self.password_success = "Mot de passe modifié avec succès"
                    yield rx.toast.success("Mot de passe modifié !")
                else:
                    self.password_error = "Erreur lors du changement de mot de passe"
            else:
                self.password_error = "Service d'authentification non disponible"
                
        except Exception as e:
            error_str = str(e)
            if "same_password" in error_str.lower():
                self.password_error = "Le nouveau mot de passe doit être différent"
            else:
                self.password_error = "Erreur lors du changement de mot de passe"
            print(f"❌ Erreur changement mot de passe: {e}")
        
        self.is_changing_password = False


# ============================================
# COMPOSANTS UI
# ============================================

def profile_header() -> rx.Component:
    """En-tête du profil avec avatar et infos principales."""
    return rx.box(
        rx.hstack(
            # Avatar
            rx.box(
                rx.text(
                    ProfileState.initials,
                    font_size="2rem",
                    font_weight="700",
                    color=Colors.WHITE,
                ),
                width="100px",
                height="100px",
                background=f"linear-gradient(135deg, {Colors.PRIMARY} 0%, #2d6b62 100%)",
                border_radius="50%",
                display="flex",
                align_items="center",
                justify_content="center",
                box_shadow=Shadows.LG,
            ),
            
            # Infos
            rx.vstack(
                rx.text(
                    ProfileState.display_name,
                    font_size="1.75rem",
                    font_weight="700",
                    color=Colors.GRAY_900,
                ),
                rx.hstack(
                    rx.icon("mail", size=16, color=Colors.GRAY_400),
                    rx.text(
                        ProfileState.user_email,
                        font_size=Typography.SIZE_BASE,
                        color=Colors.GRAY_500,
                    ),
                    spacing="2",
                ),
                rx.hstack(
                    rx.box(
                        rx.hstack(
                            rx.icon("calendar", size=14, color=Colors.PRIMARY),
                            rx.text(
                                f"Membre depuis {ProfileState.member_since}",
                                font_size=Typography.SIZE_SM,
                            ),
                            spacing="1",
                        ),
                        padding="0.25rem 0.75rem",
                        background=Colors.PRIMARY_LIGHTER,
                        border_radius=Borders.RADIUS_FULL,
                        color=Colors.PRIMARY,
                    ),
                    rx.box(
                        rx.hstack(
                            rx.icon("file-text", size=14, color=Colors.INFO),
                            rx.text(
                                f"{ProfileState.simulations_count} simulations",
                                font_size=Typography.SIZE_SM,
                            ),
                            spacing="1",
                        ),
                        padding="0.25rem 0.75rem",
                        background=f"{Colors.INFO}15",
                        border_radius=Borders.RADIUS_FULL,
                        color=Colors.INFO,
                    ),
                    spacing="2",
                    margin_top="0.5rem",
                ),
                spacing="1",
                align_items="start",
            ),
            
            spacing="5",
            align="center",
            width="100%",
        ),
        padding="1.5rem",
        background=Colors.WHITE,
        border_radius=Borders.RADIUS_XL,
        box_shadow=Shadows.SM,
        width="100%",
    )


def info_row(label: str, value: rx.Var, icon: str = None) -> rx.Component:
    """Ligne d'information du profil."""
    return rx.hstack(
        rx.hstack(
            rx.icon(icon, size=16, color=Colors.GRAY_400) if icon else rx.box(),
            rx.text(
                label,
                font_size=Typography.SIZE_SM,
                color=Colors.GRAY_500,
                min_width="120px",
            ),
            spacing="2",
        ),
        rx.text(
            value,
            font_size=Typography.SIZE_BASE,
            color=Colors.GRAY_900,
            font_weight="500",
        ),
        spacing="4",
        width="100%",
        padding_y="0.75rem",
        border_bottom=f"1px solid {Colors.GRAY_100}",
    )


def form_field(
    label: str,
    value: rx.Var,
    on_change,
    placeholder: str = "",
    icon: str = None,
    field_type: str = "text",
) -> rx.Component:
    """Champ de formulaire stylisé."""
    return rx.vstack(
        rx.text(
            label,
            font_size=Typography.SIZE_SM,
            font_weight="500",
            color=Colors.GRAY_700,
        ),
        rx.box(
            rx.hstack(
                rx.icon(icon, size=18, color=Colors.GRAY_400) if icon else rx.box(),
                rx.input(
                    placeholder=placeholder,
                    type=field_type,
                    value=value,
                    on_change=on_change,
                    width="100%",
                    border="none",
                    outline="none",
                    background="transparent",
                    font_size=Typography.SIZE_BASE,
                    _focus={"outline": "none"},
                ),
                spacing="3",
                width="100%",
                padding="0.75rem 1rem",
            ),
            border=f"2px solid {Colors.GRAY_200}",
            border_radius=Borders.RADIUS_LG,
            background=Colors.WHITE,
            _focus_within={
                "border_color": Colors.PRIMARY,
                "box_shadow": f"0 0 0 3px {Colors.PRIMARY}20",
            },
            transition="all 0.2s ease",
            width="100%",
        ),
        spacing="1",
        width="100%",
    )


def personal_info_section() -> rx.Component:
    """Section des informations personnelles."""
    return rx.box(
        rx.vstack(
            # Header de section
            rx.hstack(
                rx.hstack(
                    rx.box(
                        rx.icon("user", size=20, color=Colors.PRIMARY),
                        padding="0.5rem",
                        background=Colors.PRIMARY_LIGHTER,
                        border_radius=Borders.RADIUS_MD,
                    ),
                    rx.text(
                        "Informations personnelles",
                        font_size=Typography.SIZE_LG,
                        font_weight="600",
                        color=Colors.GRAY_900,
                    ),
                    spacing="3",
                    align="center",
                ),
                rx.spacer(),
                rx.cond(
                    ProfileState.is_editing,
                    rx.hstack(
                        rx.button(
                            rx.hstack(rx.icon("x", size=16), rx.text("Annuler"), spacing="2"),
                            variant="outline",
                            on_click=ProfileState.cancel_editing,
                            style={
                                "border": f"2px solid {Colors.GRAY_300}",
                                "color": Colors.GRAY_600,
                            },
                        ),
                        rx.button(
                            rx.cond(
                                ProfileState.is_saving_profile,
                                rx.hstack(rx.spinner(size="1"), rx.text("Enregistrement..."), spacing="2"),
                                rx.hstack(rx.icon("save", size=16), rx.text("Enregistrer"), spacing="2"),
                            ),
                            on_click=ProfileState.save_profile,
                            disabled=ProfileState.is_saving_profile,
                            style={
                                "background": Colors.PRIMARY,
                                "color": Colors.WHITE,
                            },
                        ),
                        spacing="2",
                    ),
                    rx.button(
                        rx.hstack(rx.icon("edit-2", size=16), rx.text("Modifier"), spacing="2"),
                        variant="outline",
                        on_click=ProfileState.start_editing,
                        style={
                            "border": f"2px solid {Colors.PRIMARY}",
                            "color": Colors.PRIMARY,
                        },
                    ),
                ),
                width="100%",
                align="center",
            ),
            
            rx.divider(margin_y="1rem"),
            
            # Messages
            rx.cond(
                ProfileState.profile_error != "",
                rx.box(
                    rx.hstack(
                        rx.icon("alert-circle", size=16, color="#dc2626"),
                        rx.text(ProfileState.profile_error, color="#dc2626", font_size=Typography.SIZE_SM),
                        spacing="2",
                    ),
                    padding="0.75rem 1rem",
                    background="#fef2f2",
                    border_radius=Borders.RADIUS_MD,
                    width="100%",
                    margin_bottom="1rem",
                ),
            ),
            rx.cond(
                ProfileState.profile_success != "",
                rx.box(
                    rx.hstack(
                        rx.icon("check-circle", size=16, color=Colors.SUCCESS),
                        rx.text(ProfileState.profile_success, color=Colors.SUCCESS, font_size=Typography.SIZE_SM),
                        spacing="2",
                    ),
                    padding="0.75rem 1rem",
                    background=f"{Colors.SUCCESS}10",
                    border_radius=Borders.RADIUS_MD,
                    width="100%",
                    margin_bottom="1rem",
                ),
            ),
            
            # Contenu conditionnel
            rx.cond(
                ProfileState.is_editing,
                # Mode édition
                rx.vstack(
                    form_field(
                        "Nom complet",
                        ProfileState.edit_full_name,
                        ProfileState.set_edit_full_name,
                        "Votre nom complet",
                        "user",
                    ),
                    form_field(
                        "Téléphone",
                        ProfileState.edit_phone,
                        ProfileState.set_edit_phone,
                        "+33 6 12 34 56 78",
                        "phone",
                    ),
                    form_field(
                        "Entreprise",
                        ProfileState.edit_company,
                        ProfileState.set_edit_company,
                        "Nom de votre entreprise",
                        "building-2",
                    ),
                    spacing="4",
                    width="100%",
                ),
                # Mode lecture
                rx.vstack(
                    info_row("Nom complet", ProfileState.display_name, "user"),
                    info_row("Email", ProfileState.user_email, "mail"),
                    spacing="0",
                    width="100%",
                ),
            ),
            
            spacing="0",
            width="100%",
        ),
        padding="1.5rem",
        background=Colors.WHITE,
        border_radius=Borders.RADIUS_XL,
        box_shadow=Shadows.SM,
        width="100%",
    )


def security_section() -> rx.Component:
    """Section sécurité pour le changement de mot de passe."""
    return rx.box(
        rx.vstack(
            # Header
            rx.hstack(
                rx.hstack(
                    rx.box(
                        rx.icon("shield", size=20, color=Colors.PRIMARY),
                        padding="0.5rem",
                        background=Colors.PRIMARY_LIGHTER,
                        border_radius=Borders.RADIUS_MD,
                    ),
                    rx.text(
                        "Sécurité",
                        font_size=Typography.SIZE_LG,
                        font_weight="600",
                        color=Colors.GRAY_900,
                    ),
                    spacing="3",
                    align="center",
                ),
                width="100%",
            ),
            
            rx.divider(margin_y="1rem"),
            
            # Messages
            rx.cond(
                ProfileState.password_error != "",
                rx.box(
                    rx.hstack(
                        rx.icon("alert-circle", size=16, color="#dc2626"),
                        rx.text(ProfileState.password_error, color="#dc2626", font_size=Typography.SIZE_SM),
                        spacing="2",
                    ),
                    padding="0.75rem 1rem",
                    background="#fef2f2",
                    border_radius=Borders.RADIUS_MD,
                    width="100%",
                    margin_bottom="1rem",
                ),
            ),
            rx.cond(
                ProfileState.password_success != "",
                rx.box(
                    rx.hstack(
                        rx.icon("check-circle", size=16, color=Colors.SUCCESS),
                        rx.text(ProfileState.password_success, color=Colors.SUCCESS, font_size=Typography.SIZE_SM),
                        spacing="2",
                    ),
                    padding="0.75rem 1rem",
                    background=f"{Colors.SUCCESS}10",
                    border_radius=Borders.RADIUS_MD,
                    width="100%",
                    margin_bottom="1rem",
                ),
            ),
            
            # Champs mot de passe
            rx.vstack(
                rx.text(
                    "Changer de mot de passe",
                    font_size=Typography.SIZE_BASE,
                    font_weight="600",
                    color=Colors.GRAY_900,
                    margin_bottom="0.5rem",
                ),
                
                # Mot de passe actuel
                rx.vstack(
                    rx.text(
                        "Mot de passe actuel",
                        font_size=Typography.SIZE_SM,
                        font_weight="500",
                        color=Colors.GRAY_700,
                    ),
                    rx.box(
                        rx.hstack(
                            rx.icon("lock", size=18, color=Colors.GRAY_400),
                            rx.input(
                                placeholder="••••••••",
                                type=rx.cond(ProfileState.profile_show_current_password, "text", "password"),
                                value=ProfileState.profile_current_password,
                                on_change=ProfileState.set_profile_current_password,
                                width="100%",
                                border="none",
                                outline="none",
                                background="transparent",
                                font_size=Typography.SIZE_BASE,
                                _focus={"outline": "none"},
                            ),
                            rx.icon_button(
                                rx.cond(
                                    ProfileState.profile_show_current_password,
                                    rx.icon("eye-off", size=18),
                                    rx.icon("eye", size=18),
                                ),
                                variant="ghost",
                                size="1",
                                cursor="pointer",
                                on_click=ProfileState.toggle_profile_current_password,
                                color=Colors.GRAY_400,
                            ),
                            spacing="3",
                            width="100%",
                            padding="0.75rem 1rem",
                        ),
                        border=f"2px solid {Colors.GRAY_200}",
                        border_radius=Borders.RADIUS_LG,
                        background=Colors.WHITE,
                        _focus_within={
                            "border_color": Colors.PRIMARY,
                            "box_shadow": f"0 0 0 3px {Colors.PRIMARY}20",
                        },
                        transition="all 0.2s ease",
                        width="100%",
                    ),
                    spacing="1",
                    width="100%",
                ),
                
                # Nouveau mot de passe
                rx.vstack(
                    rx.text(
                        "Nouveau mot de passe",
                        font_size=Typography.SIZE_SM,
                        font_weight="500",
                        color=Colors.GRAY_700,
                    ),
                    rx.box(
                        rx.hstack(
                            rx.icon("key", size=18, color=Colors.GRAY_400),
                            rx.input(
                                placeholder="••••••••",
                                type=rx.cond(ProfileState.profile_show_new_password, "text", "password"),
                                value=ProfileState.profile_new_password,
                                on_change=ProfileState.set_profile_new_password,
                                width="100%",
                                border="none",
                                outline="none",
                                background="transparent",
                                font_size=Typography.SIZE_BASE,
                                _focus={"outline": "none"},
                            ),
                            rx.icon_button(
                                rx.cond(
                                    ProfileState.profile_show_new_password,
                                    rx.icon("eye-off", size=18),
                                    rx.icon("eye", size=18),
                                ),
                                variant="ghost",
                                size="1",
                                cursor="pointer",
                                on_click=ProfileState.toggle_profile_new_password,
                                color=Colors.GRAY_400,
                            ),
                            spacing="3",
                            width="100%",
                            padding="0.75rem 1rem",
                        ),
                        border=f"2px solid {Colors.GRAY_200}",
                        border_radius=Borders.RADIUS_LG,
                        background=Colors.WHITE,
                        _focus_within={
                            "border_color": Colors.PRIMARY,
                            "box_shadow": f"0 0 0 3px {Colors.PRIMARY}20",
                        },
                        transition="all 0.2s ease",
                        width="100%",
                    ),
                    rx.text(
                        "Minimum 8 caractères",
                        font_size="11px",
                        color=Colors.GRAY_400,
                        margin_top="0.25rem",
                    ),
                    spacing="1",
                    width="100%",
                ),
                
                # Confirmer nouveau mot de passe
                rx.vstack(
                    rx.text(
                        "Confirmer le nouveau mot de passe",
                        font_size=Typography.SIZE_SM,
                        font_weight="500",
                        color=Colors.GRAY_700,
                    ),
                    rx.box(
                        rx.hstack(
                            rx.icon("key", size=18, color=Colors.GRAY_400),
                            rx.input(
                                placeholder="••••••••",
                                type="password",
                                value=ProfileState.profile_confirm_password,
                                on_change=ProfileState.set_profile_confirm_password,
                                width="100%",
                                border="none",
                                outline="none",
                                background="transparent",
                                font_size=Typography.SIZE_BASE,
                                _focus={"outline": "none"},
                            ),
                            rx.cond(
                                (ProfileState.profile_confirm_password != "") & 
                                (ProfileState.profile_new_password == ProfileState.profile_confirm_password),
                                rx.icon("check-circle", size=18, color=Colors.SUCCESS),
                                rx.box(width="18px"),
                            ),
                            spacing="3",
                            width="100%",
                            padding="0.75rem 1rem",
                        ),
                        border=f"2px solid {Colors.GRAY_200}",
                        border_radius=Borders.RADIUS_LG,
                        background=Colors.WHITE,
                        _focus_within={
                            "border_color": Colors.PRIMARY,
                            "box_shadow": f"0 0 0 3px {Colors.PRIMARY}20",
                        },
                        transition="all 0.2s ease",
                        width="100%",
                    ),
                    spacing="1",
                    width="100%",
                ),
                
                # Bouton de changement
                rx.hstack(
                    rx.button(
                        rx.cond(
                            ProfileState.is_changing_password,
                            rx.hstack(rx.spinner(size="1"), rx.text("Modification..."), spacing="2"),
                            rx.hstack(rx.icon("refresh-cw", size=16), rx.text("Changer le mot de passe"), spacing="2"),
                        ),
                        on_click=ProfileState.change_password,
                        disabled=ProfileState.is_changing_password,
                        style={
                            "background": Colors.PRIMARY,
                            "color": Colors.WHITE,
                        },
                    ),
                    justify="end",
                    width="100%",
                    margin_top="1rem",
                ),
                
                spacing="4",
                width="100%",
            ),
        ),
    )


def danger_zone_section() -> rx.Component:
    """Section zone de danger pour la suppression de compte."""
    return rx.box(
        rx.vstack(
            rx.hstack(
                rx.hstack(
                    rx.box(
                        rx.icon("alert-triangle", size=20, color="#dc2626"),
                        padding="0.5rem",
                        background="#fef2f2",
                        border_radius=Borders.RADIUS_MD,
                    ),
                    rx.text(
                        "Zone de danger",
                        font_size=Typography.SIZE_LG,
                        font_weight="600",
                        color="#dc2626",
                    ),
                    spacing="3",
                    align="center",
                ),
                width="100%",
            ),
            rx.divider(margin_y="1rem"),
            rx.hstack(
                rx.vstack(
                    rx.text(
                        "Supprimer le compte",
                        font_size=Typography.SIZE_BASE,
                        font_weight="600",
                        color=Colors.GRAY_900,
                    ),
                    rx.text(
                        "Cette action est irréversible. Toutes vos données seront supprimées.",
                        font_size=Typography.SIZE_SM,
                        color=Colors.GRAY_500,
                    ),
                    spacing="1",
                    align_items="start",
                ),
                rx.spacer(),
                rx.alert_dialog.root(
                    rx.alert_dialog.trigger(
                        rx.button(
                            rx.hstack(rx.icon("trash-2", size=16), rx.text("Supprimer"), spacing="2"),
                            variant="outline",
                            color_scheme="red",
                        ),
                    ),
                    rx.alert_dialog.content(
                        rx.alert_dialog.title("Supprimer votre compte ?"),
                        rx.alert_dialog.description(
                            "Cette action est irréversible. Toutes vos simulations et données seront définitivement supprimées.",
                        ),
                        rx.hstack(
                            rx.alert_dialog.cancel(
                                rx.button("Annuler", variant="soft", color_scheme="gray"),
                            ),
                            rx.alert_dialog.action(
                                rx.button(
                                    "Supprimer définitivement",
                                    color_scheme="red",
                                ),
                            ),
                            spacing="3",
                            justify="end",
                        ),
                        style={"max_width": "450px"},
                    ),
                ),
                width="100%",
                align="center",
            ),
            spacing="0",
            width="100%",
        ),
        padding="1.5rem",
        background=Colors.WHITE,
        border_radius=Borders.RADIUS_XL,
        box_shadow=Shadows.SM,
        border="1px solid #fecaca",
        width="100%",
    )


def profile_content() -> rx.Component:
    """Contenu principal de la page profil."""
    return rx.vstack(
        # Header
        rx.hstack(
            rx.vstack(
                rx.text(
                    "Mon Profil",
                    font_size="1.75rem",
                    font_weight="700",
                    color=Colors.GRAY_900,
                ),
                rx.text(
                    "Gérez vos informations personnelles et vos paramètres de sécurité",
                    font_size=Typography.SIZE_BASE,
                    color=Colors.GRAY_500,
                ),
                spacing="1",
                align_items="start",
            ),
            rx.spacer(),
            rx.button(
                rx.hstack(rx.icon("arrow-left", size=18), rx.text("Retour au dashboard"), spacing="2"),
                variant="outline",
                on_click=rx.redirect("/dashboard"),
                style={
                    "border": f"2px solid {Colors.GRAY_300}",
                    "color": Colors.GRAY_600,
                },
            ),
            width="100%",
            align="center",
            margin_bottom="1.5rem",
        ),
        
        # Contenu en 2 colonnes
        rx.hstack(
            # Colonne gauche
            rx.vstack(
                profile_header(),
                personal_info_section(),
                spacing="5",
                width="60%",
            ),
            
            # Colonne droite
            rx.vstack(
                security_section(),
                danger_zone_section(),
                spacing="5",
                width="40%",
            ),
            
            spacing="5",
            width="100%",
            align="start",
        ),
        
        spacing="0",
        width="100%",
        max_width="1100px",
    )


@rx.page(
    route="/profile",
    title="Mon Profil - RDE Consulting",
    on_load=[AuthState.require_auth, UserState.load_simulations],
)
def profile_page() -> rx.Component:
    """Page de profil utilisateur."""
    return rx.cond(
        AuthState.is_authenticated,
        rx.hstack(
            sidebar(current_page="profile"),
            rx.box(
                profile_content(),
                min_height="100vh",
                background=Colors.BG_PAGE,
                padding="40px",
                flex="1",
            ),
            spacing="0",
            width="100%",
            align="stretch",
        ),
        rx.center(
            rx.vstack(
                rx.spinner(size="3"),
                rx.text("Chargement...", color=Colors.GRAY_500),
                spacing="4",
            ),
            min_height="100vh",
            background=Colors.BG_PAGE,
        ),
    )