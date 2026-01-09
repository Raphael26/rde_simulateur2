"""Page Step 4 - Sélection de la fiche CEE"""
#import reflex as rx
#from ..state import SimulationState
#from ..styles.design_system import Colors, Typography, Spacing, Borders, Shadows
#
#
#def fiche_item(fiche: dict) -> rx.Component:
#    """Un item de fiche cliquable."""
#    is_selected = SimulationState.selected_fiche == fiche["code"]
#    
#    return rx.box(
#        rx.hstack(
#            rx.box(
#                rx.icon(
#                    "file-text",
#                    size=20,
#                    color=rx.cond(is_selected, Colors.PRIMARY, Colors.GRAY_400),
#                ),
#                padding=Spacing.SM,
#                background=rx.cond(is_selected, Colors.PRIMARY_LIGHTER, Colors.GRAY_100),
#                border_radius=Borders.RADIUS_MD,
#            ),
#            rx.vstack(
#                rx.hstack(
#                    rx.text(
#                        fiche["code"],
#                        font_weight=Typography.WEIGHT_SEMIBOLD,
#                        font_size=Typography.SIZE_SM,
#                        color=rx.cond(is_selected, Colors.PRIMARY, Colors.GRAY_900),
#                    ),
#                    rx.cond(
#                        is_selected,
#                        rx.box(
#                            rx.text("Sélectionnée", font_size="10px", color=Colors.WHITE),
#                            padding=f"2px {Spacing.SM}",
#                            background=Colors.PRIMARY,
#                            border_radius=Borders.RADIUS_FULL,
#                        ),
#                        rx.fragment(),
#                    ),
#                    spacing="2",
#                    align="center",
#                ),
#                rx.text(
#                    fiche["description"],
#                    font_size=Typography.SIZE_XS,
#                    color=Colors.GRAY_500,
#                    no_of_lines=2,
#                ),
#                spacing="1",
#                align="start",
#                flex="1",
#            ),
#            rx.spacer(),
#            rx.cond(
#                is_selected,
#                rx.icon("check-circle", size=20, color=Colors.SUCCESS),
#                rx.icon("chevron-right", size=18, color=Colors.GRAY_300),
#            ),
#            spacing="3",
#            align="center",
#            width="100%",
#        ),
#        on_click=SimulationState.select_fiche(fiche["code"], fiche["description"]),
#        cursor="pointer",
#        padding=Spacing.MD,
#        background=rx.cond(is_selected, Colors.PRIMARY_LIGHTER, Colors.WHITE),
#        border=rx.cond(
#            is_selected,
#            f"2px solid {Colors.PRIMARY}",
#            f"1px solid {Colors.GRAY_200}",
#        ),
#        border_radius=Borders.RADIUS_LG,
#        _hover={
#            "border_color": Colors.PRIMARY,
#            "background": Colors.GRAY_50,
#        },
#        transition="all 0.2s ease",
#        width="100%",
#    )
#
#
#def fiches_content() -> rx.Component:
#    return rx.box(
#        rx.vstack(
#            # Header
#            rx.vstack(
#                rx.text("Sélection de la Fiche CEE", font_size=Typography.SIZE_2XL, font_weight=Typography.WEIGHT_BOLD),
#                rx.text("Étape 4 sur 6 : Choisissez l'opération standardisée", color=Colors.GRAY_500),
#                spacing="1",
#                align="center",
#            ),
#            
#            # Progress bar
#            rx.box(
#                rx.box(
#                    width="66.66%",
#                    height="100%",
#                    background=Colors.PRIMARY,
#                    border_radius=Borders.RADIUS_FULL,
#                ),
#                width="100%",
#                max_width="400px",
#                height="6px",
#                background=Colors.GRAY_200,
#                border_radius=Borders.RADIUS_FULL,
#                overflow="hidden",
#            ),
#            
#            # Récap étapes précédentes
#            rx.box(
#                rx.hstack(
#                    rx.hstack(
#                        rx.icon("map-pin", size=14, color=Colors.GRAY_400),
#                        rx.text(SimulationState.department, font_size=Typography.SIZE_SM, color=Colors.GRAY_600),
#                        spacing="1",
#                    ),
#                    rx.box(width="1px", height="16px", background=Colors.GRAY_300),
#                    rx.hstack(
#                        rx.icon("building-2", size=14, color=Colors.GRAY_400),
#                        rx.text(SimulationState.sector, font_size=Typography.SIZE_SM, color=Colors.GRAY_600),
#                        spacing="1",
#                    ),
#                    rx.box(width="1px", height="16px", background=Colors.GRAY_300),
#                    rx.hstack(
#                        rx.icon("layers", size=14, color=Colors.PRIMARY),
#                        rx.text(SimulationState.typology, font_size=Typography.SIZE_SM, color=Colors.PRIMARY, font_weight=Typography.WEIGHT_MEDIUM),
#                        spacing="1",
#                    ),
#                    spacing="3",
#                    align="center",
#                    wrap="wrap",
#                    justify="center",
#                ),
#                padding=Spacing.MD,
#                background=Colors.GRAY_50,
#                border_radius=Borders.RADIUS_MD,
#                border=f"1px solid {Colors.GRAY_200}",
#            ),
#            
#            # Préfixe des fiches
#            rx.box(
#                rx.hstack(
#                    rx.icon("filter", size=16, color=Colors.INFO),
#                    rx.text("Fiches ", font_size=Typography.SIZE_SM, color=Colors.GRAY_600),
#                    rx.text(
#                        f"{SimulationState.sector_abbr}-{SimulationState.typology_abbr}-",
#                        font_family="monospace",
#                        font_weight=Typography.WEIGHT_BOLD,
#                        color=Colors.INFO,
#                    ),
#                    rx.text("***", font_family="monospace", color=Colors.GRAY_400),
#                    spacing="1",
#                    align="center",
#                ),
#                padding=Spacing.SM,
#                background=Colors.INFO_LIGHT,
#                border_radius=Borders.RADIUS_MD,
#            ),
#            
#            # Zone de recherche et liste
#            rx.box(
#                rx.vstack(
#                    # Recherche
#                    rx.hstack(
#                        rx.icon("search", size=16, color=Colors.GRAY_400),
#                        rx.text("Rechercher une fiche", font_weight=Typography.WEIGHT_MEDIUM),
#                        spacing="2",
#                    ),
#                    rx.input(
#                        placeholder="Tapez un code ou mot-clé (ex: isolation, pompe...)",
#                        value=SimulationState.fiche_search,
#                        on_change=SimulationState.set_fiche_search,
#                        width="100%",
#                        size="3",
#                    ),
#                    
#                    # Compteur de résultats
#                    rx.hstack(
#                        rx.text(
#                            f"{SimulationState.filtered_fiches.length()} fiche(s) disponible(s)",
#                            font_size=Typography.SIZE_XS,
#                            color=Colors.GRAY_500,
#                        ),
#                        rx.spacer(),
#                        rx.cond(
#                            SimulationState.fiche_search != "",
#                            rx.button(
#                                rx.hstack(rx.icon("x", size=12), rx.text("Effacer"), spacing="1"),
#                                size="1",
#                                variant="ghost",
#                                on_click=SimulationState.set_fiche_search(""),
#                            ),
#                            rx.fragment(),
#                        ),
#                        width="100%",
#                    ),
#                    
#                    # Liste des fiches
#                    rx.cond(
#                        SimulationState.filtered_fiches.length() > 0,
#                        rx.scroll_area(
#                            rx.vstack(
#                                rx.foreach(SimulationState.filtered_fiches, fiche_item),
#                                spacing="2",
#                                width="100%",
#                            ),
#                            height="300px",
#                            width="100%",
#                            padding_right=Spacing.SM,
#                        ),
#                        rx.box(
#                            rx.vstack(
#                                rx.icon("file-x", size=40, color=Colors.GRAY_300),
#                                rx.text("Aucune fiche trouvée", font_weight=Typography.WEIGHT_MEDIUM, color=Colors.GRAY_500),
#                                rx.text(
#                                    "Essayez un autre terme de recherche",
#                                    font_size=Typography.SIZE_SM,
#                                    color=Colors.GRAY_400,
#                                ),
#                                spacing="2",
#                                align="center",
#                            ),
#                            padding=Spacing.XL,
#                            width="100%",
#                        ),
#                    ),
#                    
#                    spacing="3",
#                    width="100%",
#                ),
#                padding=Spacing.LG,
#                background=Colors.WHITE,
#                border_radius=Borders.RADIUS_LG,
#                box_shadow=Shadows.SM,
#                width="100%",
#                max_width="550px",
#            ),
#            
#            # Fiche sélectionnée
#            rx.cond(
#                SimulationState.selected_fiche != "",
#                rx.box(
#                    rx.hstack(
#                        rx.box(
#                            rx.icon("check-circle", size=18, color=Colors.SUCCESS),
#                            padding="8px",
#                            background=Colors.SUCCESS_LIGHT,
#                            border_radius=Borders.RADIUS_FULL,
#                        ),
#                        rx.vstack(
#                            rx.text("Fiche sélectionnée", font_size=Typography.SIZE_XS, color=Colors.GRAY_500),
#                            rx.text(SimulationState.selected_fiche, font_weight=Typography.WEIGHT_BOLD, color=Colors.SUCCESS),
#                            rx.text(
#                                SimulationState.selected_fiche_description,
#                                font_size=Typography.SIZE_XS,
#                                color=Colors.GRAY_600,
#                                no_of_lines=1,
#                            ),
#                            spacing="0",
#                            align="start",
#                        ),
#                        spacing="3",
#                        align="center",
#                        width="100%",
#                    ),
#                    padding=Spacing.MD,
#                    background=Colors.WHITE,
#                    border=f"1px solid {Colors.SUCCESS}",
#                    border_radius=Borders.RADIUS_LG,
#                    width="100%",
#                    max_width="550px",
#                ),
#                rx.fragment(),
#            ),
#            
#            # Navigation
#            rx.hstack(
#                rx.button(
#                    rx.hstack(rx.icon("chevron-left", size=18), rx.text("Retour"), spacing="2"),
#                    variant="ghost",
#                    on_click=rx.redirect("/simulation/typology"),
#                    size="3",
#                ),
#                rx.spacer(),
#                rx.button(
#                    rx.hstack(rx.text("Continuer"), rx.icon("chevron-right", size=18), spacing="2"),
#                    disabled=SimulationState.selected_fiche == "",
#                    on_click=rx.redirect("/simulation/form"),
#                    size="3",
#                    style={
#                        "background": Colors.PRIMARY,
#                        "color": Colors.WHITE,
#                    },
#                ),
#                width="100%",
#                max_width="550px",
#            ),
#            
#            spacing="6",
#            align="center",
#            padding=Spacing.XL,
#            width="100%",
#        ),
#        min_height="100vh",
#        background=Colors.BG_PAGE,
#        display="flex",
#        justify_content="center",
#        padding_top="40px",
#    )
#
#
#@rx.page(route="/simulation/fiches", title="Fiche CEE - SimuPrime", on_load=SimulationState.load_fiches)
#def step4_fiches_page() -> rx.Component:
#    return fiches_content()


"""Page Step 4 - Sélection de la fiche CEE"""
import reflex as rx
from ..state import SimulationState
from ..styles.design_system import Colors, Typography, Spacing, Borders, Shadows
from .simulation_layout import simulation_layout, recap_bar, recap_item


def fiche_item(fiche: dict) -> rx.Component:
    """Un item de fiche cliquable."""
    is_selected = SimulationState.selected_fiche == fiche["code"]
    
    return rx.box(
        rx.hstack(
            rx.box(
                rx.icon(
                    "file-text",
                    size=20,
                    color=rx.cond(is_selected, Colors.PRIMARY, Colors.GRAY_400),
                ),
                padding=Spacing.SM,
                background=rx.cond(is_selected, Colors.PRIMARY_LIGHTER, Colors.GRAY_100),
                border_radius=Borders.RADIUS_MD,
            ),
            rx.vstack(
                rx.hstack(
                    rx.text(
                        fiche["code"],
                        font_weight=Typography.WEIGHT_SEMIBOLD,
                        font_size=Typography.SIZE_SM,
                        color=rx.cond(is_selected, Colors.PRIMARY, Colors.GRAY_900),
                    ),
                    rx.cond(
                        is_selected,
                        rx.box(
                            rx.text("Sélectionnée", font_size="10px", color=Colors.WHITE),
                            padding=f"2px {Spacing.SM}",
                            background=Colors.PRIMARY,
                            border_radius=Borders.RADIUS_FULL,
                        ),
                        rx.fragment(),
                    ),
                    spacing="2",
                    align="center",
                ),
                rx.text(
                    fiche["description"],
                    font_size=Typography.SIZE_XS,
                    color=Colors.GRAY_500,
                    no_of_lines=2,
                ),
                spacing="1",
                align="start",
                flex="1",
            ),
            rx.spacer(),
            rx.cond(
                is_selected,
                rx.icon("check-circle", size=20, color=Colors.SUCCESS),
                rx.icon("chevron-right", size=18, color=Colors.GRAY_300),
            ),
            spacing="3",
            align="center",
            width="100%",
        ),
        on_click=SimulationState.select_fiche(fiche["code"], fiche["description"]),
        cursor="pointer",
        padding=Spacing.MD,
        background=rx.cond(is_selected, Colors.PRIMARY_LIGHTER, Colors.WHITE),
        border=rx.cond(
            is_selected,
            f"2px solid {Colors.PRIMARY}",
            f"1px solid {Colors.GRAY_200}",
        ),
        border_radius=Borders.RADIUS_LG,
        _hover={
            "border_color": Colors.PRIMARY,
            "background": Colors.GRAY_50,
        },
        transition="all 0.2s ease",
        width="100%",
    )


def step4_recap() -> rx.Component:
    """Récap des étapes précédentes."""
    return recap_bar(
        recap_item("map-pin", SimulationState.department),
        rx.box(width="1px", height="16px", background=Colors.GRAY_300),
        recap_item("building-2", SimulationState.sector),
        rx.box(width="1px", height="16px", background=Colors.GRAY_300),
        recap_item("layers", SimulationState.typology, is_primary=True),
    )


def step4_content() -> rx.Component:
    return rx.vstack(
        # Préfixe des fiches
        rx.box(
            rx.hstack(
                rx.icon("filter", size=16, color=Colors.INFO),
                rx.text("Fiches ", font_size=Typography.SIZE_SM, color=Colors.GRAY_600),
                rx.text(
                    f"{SimulationState.sector_abbr}-{SimulationState.typology_abbr}-",
                    font_family="monospace",
                    font_weight=Typography.WEIGHT_BOLD,
                    color=Colors.INFO,
                ),
                rx.text("***", font_family="monospace", color=Colors.GRAY_400),
                spacing="1",
                align="center",
            ),
            padding=Spacing.MD,
            background=Colors.INFO_LIGHT,
            border_radius=Borders.RADIUS_MD,
            width="100%",
        ),
        
        # Recherche et liste
        rx.box(
            rx.vstack(
                rx.input(
                    placeholder="Rechercher une fiche (ex: isolation, pompe...)",
                    value=SimulationState.fiche_search,
                    on_change=SimulationState.set_fiche_search,
                    width="100%",
                    size="3",
                ),
                
                # Compteur
                rx.hstack(
                    rx.text(
                        f"{SimulationState.filtered_fiches.length()} fiche(s) disponible(s)",
                        font_size=Typography.SIZE_XS,
                        color=Colors.GRAY_500,
                    ),
                    rx.spacer(),
                    rx.cond(
                        SimulationState.fiche_search != "",
                        rx.button(
                            rx.hstack(rx.icon("x", size=12), rx.text("Effacer"), spacing="1"),
                            size="1",
                            variant="ghost",
                            on_click=SimulationState.set_fiche_search(""),
                        ),
                        rx.fragment(),
                    ),
                    width="100%",
                ),
                
                # Liste des fiches
                rx.cond(
                    SimulationState.filtered_fiches.length() > 0,
                    rx.scroll_area(
                        rx.vstack(
                            rx.foreach(SimulationState.filtered_fiches, fiche_item),
                            spacing="2",
                            width="100%",
                        ),
                        height="350px",
                        width="100%",
                        padding_right=Spacing.SM,
                    ),
                    rx.box(
                        rx.vstack(
                            rx.icon("file-x", size=40, color=Colors.GRAY_300),
                            rx.text("Aucune fiche trouvée", font_weight=Typography.WEIGHT_MEDIUM, color=Colors.GRAY_500),
                            spacing="2",
                            align="center",
                        ),
                        padding=Spacing.XL,
                        width="100%",
                    ),
                ),
                
                spacing="3",
                width="100%",
            ),
            padding=Spacing.LG,
            background=Colors.WHITE,
            border_radius=Borders.RADIUS_LG,
            box_shadow=Shadows.SM,
            width="100%",
        ),
        
        # Fiche sélectionnée
        rx.cond(
            SimulationState.selected_fiche != "",
            rx.box(
                rx.hstack(
                    rx.icon("check-circle", size=18, color=Colors.SUCCESS),
                    rx.text(SimulationState.selected_fiche, font_weight=Typography.WEIGHT_BOLD, color=Colors.SUCCESS),
                    rx.text(" - ", color=Colors.GRAY_400),
                    rx.text(SimulationState.selected_fiche_description, font_size=Typography.SIZE_SM, color=Colors.GRAY_600, no_of_lines=1),
                    spacing="2",
                    align="center",
                    width="100%",
                ),
                padding=Spacing.MD,
                background=Colors.SUCCESS_LIGHT,
                border_radius=Borders.RADIUS_LG,
                width="100%",
            ),
            rx.fragment(),
        ),
        
        spacing="4",
        width="100%",
    )


@rx.page(route="/simulation/fiches", title="Fiche CEE - SimuPrime", on_load=SimulationState.load_fiches)
def step4_fiches_page() -> rx.Component:
    return simulation_layout(
        title="Sélection de la Fiche CEE",
        subtitle="Choisissez l'opération standardisée",
        step=4,
        total_steps=6,
        content=step4_content(),
        recap=step4_recap(),
        back_url="/simulation/typology",
        next_url="/simulation/form",
        can_continue=SimulationState.selected_fiche != "",
    )