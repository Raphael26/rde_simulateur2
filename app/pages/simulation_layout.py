"""Layout commun pour les pages de simulation"""
import reflex as rx
from ..styles.design_system import Colors, Typography, Spacing, Borders
from ..components.sidebar import simulation_sidebar


def simulation_layout(
    title: str,
    subtitle: str,
    step: int,
    total_steps: int,
    content: rx.Component,
    back_url: str,
    next_url: str,
    can_continue: rx.Var,
    recap: rx.Component = None,
    on_next: rx.EventHandler = None,
) -> rx.Component:
    """Layout commun pour toutes les étapes de simulation."""
    
    progress_percent = f"{(step / total_steps) * 100}%"
    
    return rx.hstack(
        # Sidebar
        simulation_sidebar(current_step=step),
        
        # Contenu principal
        rx.box(
            rx.vstack(
                # Header
                rx.vstack(
                    rx.text(title, font_size=Typography.SIZE_2XL, font_weight=Typography.WEIGHT_BOLD, text_align="center"),
                    rx.text(f"Étape {step} sur {total_steps} : {subtitle}", color=Colors.GRAY_500, text_align="center"),
                    spacing="1",
                    align="center",
                    width="100%",
                ),
                
                # Progress bar
                rx.box(
                    rx.box(
                        width=progress_percent,
                        height="100%",
                        background=Colors.PRIMARY,
                        border_radius=Borders.RADIUS_FULL,
                        transition="width 0.3s ease",
                    ),
                    width="100%",
                    height="6px",
                    background=Colors.GRAY_200,
                    border_radius=Borders.RADIUS_FULL,
                    overflow="hidden",
                ),
                
                # Récap (optionnel)
                rx.cond(
                    recap is not None,
                    recap,
                    rx.fragment(),
                ) if recap else rx.fragment(),
                
                # Contenu principal
                content,
                
                # Navigation
                rx.hstack(
                    rx.button(
                        rx.hstack(rx.icon("chevron-left", size=18), rx.text("Retour"), spacing="2", align="center"),
                        variant="ghost",
                        on_click=rx.redirect(back_url),
                        size="3",
                    ),
                    rx.spacer(),
                    rx.button(
                        rx.hstack(rx.text("Continuer"), rx.icon("chevron-right", size=18), spacing="2", align="center"),
                        disabled=~can_continue,
                        on_click=on_next if on_next else rx.redirect(next_url),
                        size="3",
                        style={
                            "background": Colors.PRIMARY,
                            "color": Colors.WHITE,
                        },
                    ),
                    width="100%",
                ),
                
                spacing="5",
                align="center",
                padding=Spacing.XL,
                width="100%",
                max_width="800px",
            ),
            min_height="100vh",
            background=Colors.BG_PAGE,
            display="flex",
            justify_content="center",
            padding_top="40px",
            padding_x=Spacing.MD,
            margin_left="260px",  # Espace pour la sidebar
            width="100%",
        ),
        
        spacing="0",
        width="100%",
    )


def recap_bar(*items) -> rx.Component:
    """Barre de récap des sélections précédentes."""
    return rx.box(
        rx.hstack(
            *items,
            spacing="3",
            align="center",
            wrap="wrap",
            justify="center",
        ),
        padding=Spacing.MD,
        background=Colors.GRAY_50,
        border_radius=Borders.RADIUS_MD,
        border=f"1px solid {Colors.GRAY_200}",
        width="100%",
    )


def recap_item(icon: str, text: rx.Var, is_primary: bool = False) -> rx.Component:
    """Un item de récap."""
    return rx.hstack(
        rx.icon(icon, size=14, color=Colors.PRIMARY if is_primary else Colors.GRAY_400),
        rx.text(
            text,
            font_size=Typography.SIZE_SM,
            color=Colors.PRIMARY if is_primary else Colors.GRAY_600,
            font_weight=Typography.WEIGHT_MEDIUM if is_primary else Typography.WEIGHT_NORMAL,
        ),
        spacing="1",
        align="center",
    )


def recap_separator() -> rx.Component:
    """Séparateur entre items de récap."""
    return rx.box(width="1px", height="16px", background=Colors.GRAY_300)