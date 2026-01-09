"""
Profile Page
User profile management with personal info, security, and account settings
"""

import reflex as rx
from state.auth_state import AuthState
from styles.design_system import Colors, Typography, Borders, Shadows
from components.sidebar import sidebar
from components.header import header


class ProfileState(rx.State):
    """Profile page state"""
    edit_name: str = ""
    is_editing: bool = False
    show_delete_modal: bool = False
    error_message: str = ""
    success_message: str = ""
    
    @rx.event
    def start_editing(self):
        """Start editing profile"""
        self.edit_name = AuthState.user_full_name
        self.is_editing = True
        self.error_message = ""
        self.success_message = ""
    
    @rx.event
    def cancel_editing(self):
        """Cancel editing"""
        self.is_editing = False
        self.edit_name = ""
    
    @rx.event
    def set_edit_name(self, value: str):
        """Set edit name value"""
        self.edit_name = value
    
    @rx.event
    def save_profile(self):
        """Save profile changes"""
        if not self.edit_name.strip():
            self.error_message = "Le nom ne peut pas être vide."
            return
        
        # Call auth state update
        yield AuthState.update_profile(self.edit_name.strip())
        
        self.is_editing = False
        self.success_message = "Profil mis à jour avec succès."
    
    @rx.event
    def open_delete_modal(self):
        """Open account deletion confirmation"""
        self.show_delete_modal = True
    
    @rx.event
    def close_delete_modal(self):
        """Close deletion modal"""
        self.show_delete_modal = False


def profile_card(title: str, description: str, content: rx.Component) -> rx.Component:
    """Reusable profile card component"""
    return rx.box(
        rx.vstack(
            rx.hstack(
                rx.vstack(
                    rx.text(
                        title,
                        font_size="1.125rem",
                        font_weight="600",
                        color=Colors.TEXT_PRIMARY,
                    ),
                    rx.text(
                        description,
                        font_size="0.875rem",
                        color=Colors.TEXT_SECONDARY,
                    ),
                    spacing="1",
                    align="start",
                ),
                rx.spacer(),
                width="100%",
            ),
            rx.divider(margin_y="1rem"),
            content,
            spacing="0",
            width="100%",
        ),
        background="white",
        padding="1.5rem",
        border_radius=Borders.RADIUS_LG,
        border=f"1px solid {Colors.BORDER}",
    )


def personal_info_section() -> rx.Component:
    """Personal information section"""
    return profile_card(
        "Informations personnelles",
        "Gérez vos informations de profil",
        rx.vstack(
            # Avatar
            rx.hstack(
                rx.box(
                    rx.text(
                        AuthState.user_initials,
                        font_size="1.5rem",
                        font_weight="600",
                        color="white",
                    ),
                    display="flex",
                    align_items="center",
                    justify_content="center",
                    width="80px",
                    height="80px",
                    background=Colors.PRIMARY,
                    border_radius=Borders.RADIUS_FULL,
                ),
                rx.vstack(
                    rx.text(
                        AuthState.display_name,
                        font_size="1.25rem",
                        font_weight="600",
                        color=Colors.TEXT_PRIMARY,
                    ),
                    rx.text(
                        AuthState.user_email,
                        font_size="0.875rem",
                        color=Colors.TEXT_SECONDARY,
                    ),
                    spacing="1",
                    align="start",
                ),
                spacing="4",
                align="center",
            ),
            
            rx.divider(margin_y="1rem"),
            
            # Edit form or display
            rx.cond(
                ProfileState.is_editing,
                # Edit mode
                rx.vstack(
                    rx.box(
                        rx.text(
                            "Nom complet",
                            font_size="0.875rem",
                            font_weight="500",
                            color=Colors.TEXT_SECONDARY,
                            margin_bottom="0.5rem",
                        ),
                        rx.input(
                            value=ProfileState.edit_name,
                            on_change=ProfileState.set_edit_name,
                            size="3",
                            width="100%",
                        ),
                        width="100%",
                        max_width="400px",
                    ),
                    rx.hstack(
                        rx.button(
                            "Annuler",
                            variant="outline",
                            on_click=ProfileState.cancel_editing,
                        ),
                        rx.button(
                            "Enregistrer",
                            background=Colors.PRIMARY,
                            color="white",
                            on_click=ProfileState.save_profile,
                        ),
                        spacing="2",
                    ),
                    spacing="4",
                    width="100%",
                ),
                # Display mode
                rx.vstack(
                    rx.hstack(
                        rx.vstack(
                            rx.text("Nom", font_size="0.75rem", color=Colors.TEXT_MUTED),
                            rx.text(AuthState.user_full_name if AuthState.user_full_name else "Non renseigné", font_weight="500"),
                            spacing="1",
                        ),
                        rx.vstack(
                            rx.text("Email", font_size="0.75rem", color=Colors.TEXT_MUTED),
                            rx.text(AuthState.user_email, font_weight="500"),
                            spacing="1",
                        ),
                        rx.vstack(
                            rx.text("Membre depuis", font_size="0.75rem", color=Colors.TEXT_MUTED),
                            rx.text(AuthState.user_created_at[:10] if AuthState.user_created_at else "—", font_weight="500"),
                            spacing="1",
                        ),
                        spacing="6",
                        flex_wrap="wrap",
                    ),
                    rx.button(
                        rx.hstack(
                            rx.icon("pencil", size=16),
                            rx.text("Modifier"),
                            spacing="2",
                        ),
                        variant="outline",
                        on_click=ProfileState.start_editing,
                        margin_top="1rem",
                    ),
                    spacing="3",
                    width="100%",
                ),
            ),
            
            spacing="4",
            width="100%",
        ),
    )


def security_section() -> rx.Component:
    """Security settings section"""
    return profile_card(
        "Sécurité",
        "Gérez votre mot de passe et la sécurité de votre compte",
        rx.vstack(
            # Password change
            rx.hstack(
                rx.vstack(
                    rx.text("Mot de passe", font_weight="500"),
                    rx.text("Dernière modification : inconnue", font_size="0.875rem", color=Colors.TEXT_MUTED),
                    spacing="1",
                    align="start",
                ),
                rx.spacer(),
                rx.button(
                    "Changer le mot de passe",
                    variant="outline",
                ),
                width="100%",
                align="center",
            ),
            
            rx.divider(margin_y="1rem"),
            
            # Two-factor auth (placeholder)
            rx.hstack(
                rx.vstack(
                    rx.text("Authentification à deux facteurs", font_weight="500"),
                    rx.text("Ajoutez une couche de sécurité supplémentaire", font_size="0.875rem", color=Colors.TEXT_MUTED),
                    spacing="1",
                    align="start",
                ),
                rx.spacer(),
                rx.badge("Bientôt disponible", color_scheme="gray"),
                width="100%",
                align="center",
            ),
            
            spacing="4",
            width="100%",
        ),
    )


def preferences_section() -> rx.Component:
    """Preferences section"""
    return profile_card(
        "Préférences",
        "Personnalisez votre expérience",
        rx.vstack(
            # Email notifications
            rx.hstack(
                rx.vstack(
                    rx.text("Notifications par email", font_weight="500"),
                    rx.text("Recevez des alertes sur vos simulations", font_size="0.875rem", color=Colors.TEXT_MUTED),
                    spacing="1",
                    align="start",
                ),
                rx.spacer(),
                rx.switch(default_checked=True, color_scheme="teal"),
                width="100%",
                align="center",
            ),
            
            rx.divider(margin_y="1rem"),
            
            # Theme
            rx.hstack(
                rx.vstack(
                    rx.text("Thème", font_weight="500"),
                    rx.text("Choisissez l'apparence de l'application", font_size="0.875rem", color=Colors.TEXT_MUTED),
                    spacing="1",
                    align="start",
                ),
                rx.spacer(),
                rx.select(
                    ["Clair", "Sombre", "Système"],
                    default_value="Clair",
                    size="2",
                ),
                width="100%",
                align="center",
            ),
            
            spacing="4",
            width="100%",
        ),
    )


def danger_zone_section() -> rx.Component:
    """Danger zone section for account deletion"""
    return rx.box(
        rx.vstack(
            rx.hstack(
                rx.vstack(
                    rx.text(
                        "Zone dangereuse",
                        font_size="1.125rem",
                        font_weight="600",
                        color=Colors.ERROR,
                    ),
                    rx.text(
                        "Actions irréversibles sur votre compte",
                        font_size="0.875rem",
                        color=Colors.TEXT_SECONDARY,
                    ),
                    spacing="1",
                    align="start",
                ),
                rx.spacer(),
                width="100%",
            ),
            rx.divider(margin_y="1rem"),
            rx.hstack(
                rx.vstack(
                    rx.text("Supprimer le compte", font_weight="500"),
                    rx.text(
                        "Cette action supprimera définitivement votre compte et toutes vos données.",
                        font_size="0.875rem",
                        color=Colors.TEXT_MUTED,
                    ),
                    spacing="1",
                    align="start",
                ),
                rx.spacer(),
                rx.button(
                    "Supprimer mon compte",
                    color_scheme="red",
                    variant="outline",
                    on_click=ProfileState.open_delete_modal,
                ),
                width="100%",
                align="center",
            ),
            spacing="0",
            width="100%",
        ),
        background="white",
        padding="1.5rem",
        border_radius=Borders.RADIUS_LG,
        border=f"1px solid {Colors.ERROR}30",
    )


def delete_account_modal() -> rx.Component:
    """Delete account confirmation modal"""
    return rx.dialog.root(
        rx.dialog.content(
            rx.dialog.title(
                rx.hstack(
                    rx.icon("alert-triangle", size=24, color=Colors.ERROR),
                    rx.text("Supprimer votre compte ?"),
                    spacing="2",
                ),
            ),
            rx.dialog.description(
                rx.vstack(
                    rx.text(
                        "Cette action est irréversible. Toutes vos données seront définitivement supprimées :",
                        color=Colors.TEXT_SECONDARY,
                    ),
                    rx.box(
                        rx.vstack(
                            rx.text("• Toutes vos simulations", font_size="0.875rem"),
                            rx.text("• Votre historique", font_size="0.875rem"),
                            rx.text("• Vos préférences", font_size="0.875rem"),
                            spacing="1",
                            align="start",
                        ),
                        padding="1rem",
                        background=Colors.ERROR_LIGHT,
                        border_radius=Borders.RADIUS_MD,
                        width="100%",
                    ),
                    spacing="3",
                ),
            ),
            rx.hstack(
                rx.dialog.close(
                    rx.button(
                        "Annuler",
                        variant="outline",
                        on_click=ProfileState.close_delete_modal,
                    ),
                ),
                rx.button(
                    "Supprimer définitivement",
                    color_scheme="red",
                    on_click=AuthState.logout,  # For now, just logout
                ),
                spacing="3",
                justify="end",
                margin_top="1.5rem",
            ),
        ),
        open=ProfileState.show_delete_modal,
    )


def profile_content() -> rx.Component:
    """Main profile content"""
    return rx.box(
        rx.vstack(
            # Page header
            rx.hstack(
                rx.vstack(
                    rx.heading(
                        "Mon profil",
                        font_size="1.75rem",
                        font_weight="700",
                        color=Colors.TEXT_PRIMARY,
                    ),
                    rx.text(
                        "Gérez vos informations personnelles et vos préférences",
                        color=Colors.TEXT_SECONDARY,
                    ),
                    spacing="1",
                    align="start",
                ),
                width="100%",
            ),
            
            # Messages
            rx.cond(
                ProfileState.error_message != "",
                rx.callout(
                    ProfileState.error_message,
                    icon="alert-circle",
                    color="red",
                ),
            ),
            rx.cond(
                ProfileState.success_message != "",
                rx.callout(
                    ProfileState.success_message,
                    icon="check-circle",
                    color="green",
                ),
            ),
            
            # Sections
            personal_info_section(),
            security_section(),
            preferences_section(),
            danger_zone_section(),
            
            spacing="5",
            width="100%",
            max_width="800px",
            padding=["1.5rem", "2rem"],
        ),
        flex="1",
        min_height="100vh",
    )


def profile_page() -> rx.Component:
    """Profile page with sidebar layout"""
    return rx.hstack(
        sidebar(),
        rx.box(
            header(),
            profile_content(),
            delete_account_modal(),
            flex="1",
            margin_left="280px",
            background=Colors.BACKGROUND,
            min_height="100vh",
        ),
        spacing="0",
        width="100%",
        font_family=Typography.FONT_FAMILY,
    )


@rx.page(route="/profile", title="Mon profil - SimuPrime", on_load=AuthState.check_auth)
def profile() -> rx.Component:
    return rx.cond(
        AuthState.is_authenticated,
        profile_page(),
        rx.center(
            rx.vstack(
                rx.spinner(size="3"),
                rx.text("Vérification de l'authentification..."),
                spacing="3",
            ),
            min_height="100vh",
        ),
    )
