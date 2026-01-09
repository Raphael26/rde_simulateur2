"""Page Step 1 - Date et Département"""
#import reflex as rx
#from ..state import SimulationState
#from ..styles.design_system import Colors, Typography, Spacing, Borders, Shadows
#
#
#def department_item(dept: str) -> rx.Component:
#    """Un item de département cliquable."""
#    return rx.box(
#        rx.hstack(
#            rx.icon("map-pin", size=14, color=Colors.GRAY_400),
#            rx.text(dept, font_size=Typography.SIZE_SM),
#            spacing="2",
#            align="center",
#        ),
#        on_click=SimulationState.select_department(dept),
#        padding="10px 12px",
#        cursor="pointer",
#        _hover={"background": Colors.PRIMARY_LIGHTER},
#        width="100%",
#        border_bottom=f"1px solid {Colors.GRAY_100}",
#    )
#
#
#def date_department_content() -> rx.Component:
#    return rx.box(
#        # Overlay pour fermer le dropdown quand on clique ailleurs
#        rx.cond(
#            SimulationState.show_department_dropdown,
#            rx.box(
#                position="fixed",
#                top="0",
#                left="0",
#                right="0",
#                bottom="0",
#                z_index="999",
#                on_click=SimulationState.close_department_dropdown,
#            ),
#            rx.fragment(),
#        ),
#        rx.vstack(
#            # Header
#            rx.vstack(
#                rx.text("Nouvelle Simulation", font_size=Typography.SIZE_2XL, font_weight=Typography.WEIGHT_BOLD),
#                rx.text("Étape 1 sur 6 : Date et Département", color=Colors.GRAY_500),
#                spacing="1",
#                align="center",
#            ),
#            
#            # Progress bar
#            rx.box(
#                rx.box(
#                    width="16.66%",
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
#            # Formulaire
#            rx.vstack(
#                # Date de signature
#                rx.box(
#                    rx.vstack(
#                        rx.hstack(
#                            rx.icon("calendar", size=16, color=Colors.PRIMARY),
#                            rx.text("Date de signature", font_weight=Typography.WEIGHT_MEDIUM, color=Colors.GRAY_700),
#                            spacing="2",
#                        ),
#                        rx.input(
#                            type="date",
#                            value=SimulationState.date_signature,
#                            on_change=SimulationState.set_date_signature,
#                            width="100%",
#                            size="3",
#                        ),
#                        spacing="2",
#                        align="start",
#                        width="100%",
#                    ),
#                    width="100%",
#                    padding=Spacing.LG,
#                    background=Colors.WHITE,
#                    border_radius=Borders.RADIUS_LG,
#                    box_shadow=Shadows.SM,
#                ),
#                
#                # Département avec recherche
#                rx.box(
#                    rx.vstack(
#                        rx.hstack(
#                            rx.icon("map-pin", size=16, color=Colors.PRIMARY),
#                            rx.text("Département", font_weight=Typography.WEIGHT_MEDIUM, color=Colors.GRAY_700),
#                            spacing="2",
#                        ),
#                        
#                        # Input avec dropdown
#                        rx.cond(
#                            SimulationState.department != "",
#                            # Département sélectionné
#                            rx.box(
#                                rx.hstack(
#                                    rx.hstack(
#                                        rx.icon("check-circle", size=16, color=Colors.SUCCESS),
#                                        rx.text(SimulationState.department, font_weight=Typography.WEIGHT_MEDIUM),
#                                        spacing="2",
#                                    ),
#                                    rx.spacer(),
#                                    rx.box(
#                                        rx.icon("x", size=16, color=Colors.GRAY_400),
#                                        cursor="pointer",
#                                        on_click=SimulationState.clear_department,
#                                        padding="4px",
#                                        border_radius=Borders.RADIUS_FULL,
#                                        _hover={"background": Colors.GRAY_100},
#                                    ),
#                                    width="100%",
#                                    align="center",
#                                ),
#                                padding=Spacing.MD,
#                                background=Colors.SUCCESS_LIGHT,
#                                border=f"1px solid {Colors.SUCCESS}",
#                                border_radius=Borders.RADIUS_MD,
#                                width="100%",
#                            ),
#                            # Input de recherche
#                            rx.box(
#                                rx.input(
#                                    placeholder="Tapez pour rechercher (ex: Paris, Lyon...)",
#                                    value=SimulationState.department_search,
#                                    on_change=SimulationState.set_department_search,
#                                    on_focus=SimulationState.open_department_dropdown,
#                                    width="100%",
#                                    size="3",
#                                ),
#                                # Dropdown
#                                rx.cond(
#                                    (SimulationState.show_department_dropdown) & (SimulationState.filtered_departments.length() > 0),
#                                    rx.box(
#                                        rx.foreach(
#                                            SimulationState.filtered_departments,
#                                            department_item,
#                                        ),
#                                        position="absolute",
#                                        top="100%",
#                                        left="0",
#                                        right="0",
#                                        background=Colors.WHITE,
#                                        border=f"1px solid {Colors.GRAY_200}",
#                                        border_radius=Borders.RADIUS_MD,
#                                        box_shadow=Shadows.LG,
#                                        max_height="250px",
#                                        overflow_y="auto",
#                                        z_index="1000",
#                                        margin_top="4px",
#                                    ),
#                                    rx.fragment(),
#                                ),
#                                position="relative",
#                                width="100%",
#                            ),
#                        ),
#                        
#                        # Hint
#                        rx.cond(
#                            SimulationState.department == "",
#                            rx.text("Commencez à taper pour voir les suggestions", font_size=Typography.SIZE_XS, color=Colors.GRAY_400),
#                            rx.fragment(),
#                        ),
#                        
#                        spacing="2",
#                        align="start",
#                        width="100%",
#                    ),
#                    width="100%",
#                    padding=Spacing.LG,
#                    background=Colors.WHITE,
#                    border_radius=Borders.RADIUS_LG,
#                    box_shadow=Shadows.SM,
#                ),
#                
#                # Info zone climatique
#                rx.cond(
#                    SimulationState.department != "",
#                    rx.box(
#                        rx.hstack(
#                            rx.box(
#                                rx.icon("thermometer", size=18, color=Colors.INFO),
#                                padding="8px",
#                                background=Colors.INFO_LIGHT,
#                                border_radius=Borders.RADIUS_FULL,
#                            ),
#                            rx.vstack(
#                                rx.text("Zone climatique détectée", font_size=Typography.SIZE_XS, color=Colors.GRAY_500),
#                                rx.text(SimulationState.zone_climatique, font_weight=Typography.WEIGHT_SEMIBOLD, color=Colors.INFO),
#                                spacing="0",
#                                align="start",
#                            ),
#                            spacing="3",
#                            align="center",
#                        ),
#                        width="100%",
#                        padding=Spacing.MD,
#                        background=Colors.WHITE,
#                        border=f"1px solid {Colors.INFO}",
#                        border_radius=Borders.RADIUS_LG,
#                    ),
#                    rx.fragment(),
#                ),
#                
#                spacing="4",
#                width="100%",
#                max_width="400px",
#            ),
#            
#            # Navigation
#            rx.hstack(
#                rx.button(
#                    rx.hstack(rx.icon("chevron-left", size=18), rx.text("Accueil"), spacing="2"),
#                    variant="ghost",
#                    on_click=rx.redirect("/"),
#                    size="3",
#                ),
#                rx.spacer(),
#                rx.button(
#                    rx.hstack(rx.text("Continuer"), rx.icon("chevron-right", size=18), spacing="2"),
#                    disabled=~SimulationState.can_continue_step1,
#                    on_click=rx.redirect("/simulation/sector"),
#                    size="3",
#                    style={
#                        "background": Colors.PRIMARY,
#                        "color": Colors.WHITE,
#                    },
#                ),
#                width="100%",
#                max_width="400px",
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
#@rx.page(route="/simulation/date-department", title="Date et Département - SimuPrime")
#def date_department_page() -> rx.Component:
#    return date_department_content()

"""Page Step 1 - Date et Département"""
import reflex as rx
from ..state import SimulationState
from ..styles.design_system import Colors, Typography, Spacing, Borders, Shadows
from .simulation_layout import simulation_layout


def department_item(dept: str) -> rx.Component:
    """Un item de département cliquable."""
    return rx.box(
        rx.hstack(
            rx.icon("map-pin", size=14, color=Colors.GRAY_400),
            rx.text(dept, font_size=Typography.SIZE_SM),
            spacing="2",
            align="center",
        ),
        on_click=SimulationState.select_department(dept),
        padding="10px 12px",
        cursor="pointer",
        _hover={"background": Colors.PRIMARY_LIGHTER},
        width="100%",
        border_bottom=f"1px solid {Colors.GRAY_100}",
    )


def step1_content() -> rx.Component:
    return rx.vstack(
        # Overlay pour fermer le dropdown
        rx.cond(
            SimulationState.show_department_dropdown,
            rx.box(
                position="fixed",
                top="0",
                left="0",
                right="0",
                bottom="0",
                z_index="999",
                on_click=SimulationState.close_department_dropdown,
            ),
            rx.fragment(),
        ),
        
        # Date de signature
        rx.box(
            rx.vstack(
                rx.hstack(
                    rx.icon("calendar", size=16, color=Colors.PRIMARY),
                    rx.text("Date de signature", font_weight=Typography.WEIGHT_MEDIUM, color=Colors.GRAY_700),
                    spacing="2",
                ),
                rx.input(
                    type="date",
                    value=SimulationState.date_signature,
                    on_change=SimulationState.set_date_signature,
                    width="100%",
                    size="3",
                ),
                spacing="2",
                align="start",
                width="100%",
            ),
            padding=Spacing.LG,
            background=Colors.WHITE,
            border_radius=Borders.RADIUS_LG,
            box_shadow=Shadows.SM,
            width="100%",
        ),
        
        # Département
        rx.box(
            rx.vstack(
                rx.hstack(
                    rx.icon("map-pin", size=16, color=Colors.PRIMARY),
                    rx.text("Département", font_weight=Typography.WEIGHT_MEDIUM, color=Colors.GRAY_700),
                    spacing="2",
                ),
                
                rx.cond(
                    SimulationState.department != "",
                    # Département sélectionné
                    rx.box(
                        rx.hstack(
                            rx.hstack(
                                rx.icon("check-circle", size=16, color=Colors.SUCCESS),
                                rx.text(SimulationState.department, font_weight=Typography.WEIGHT_MEDIUM),
                                spacing="2",
                            ),
                            rx.spacer(),
                            rx.box(
                                rx.icon("x", size=16, color=Colors.GRAY_400),
                                cursor="pointer",
                                on_click=SimulationState.clear_department,
                                padding="4px",
                                border_radius=Borders.RADIUS_FULL,
                                _hover={"background": Colors.GRAY_100},
                            ),
                            width="100%",
                            align="center",
                        ),
                        padding=Spacing.MD,
                        background=Colors.SUCCESS_LIGHT,
                        border=f"1px solid {Colors.SUCCESS}",
                        border_radius=Borders.RADIUS_MD,
                        width="100%",
                    ),
                    # Input de recherche
                    rx.box(
                        rx.input(
                            placeholder="Tapez pour rechercher (ex: Paris, Lyon...)",
                            value=SimulationState.department_search,
                            on_change=SimulationState.set_department_search,
                            on_focus=SimulationState.open_department_dropdown,
                            width="100%",
                            size="3",
                        ),
                        rx.cond(
                            (SimulationState.show_department_dropdown) & (SimulationState.filtered_departments.length() > 0),
                            rx.box(
                                rx.foreach(SimulationState.filtered_departments, department_item),
                                position="absolute",
                                top="100%",
                                left="0",
                                right="0",
                                background=Colors.WHITE,
                                border=f"1px solid {Colors.GRAY_200}",
                                border_radius=Borders.RADIUS_MD,
                                box_shadow=Shadows.LG,
                                max_height="250px",
                                overflow_y="auto",
                                z_index="1000",
                                margin_top="4px",
                            ),
                            rx.fragment(),
                        ),
                        position="relative",
                        width="100%",
                    ),
                ),
                
                # Hint
                rx.cond(
                    SimulationState.department == "",
                    rx.text("Commencez à taper pour voir les suggestions", font_size=Typography.SIZE_XS, color=Colors.GRAY_400),
                    rx.fragment(),
                ),
                
                spacing="2",
                align="start",
                width="100%",
            ),
            padding=Spacing.LG,
            background=Colors.WHITE,
            border_radius=Borders.RADIUS_LG,
            box_shadow=Shadows.SM,
            width="100%",
        ),
        
        # Zone climatique
        rx.cond(
            SimulationState.department != "",
            rx.box(
                rx.hstack(
                    rx.box(
                        rx.icon("thermometer", size=18, color=Colors.INFO),
                        padding="8px",
                        background=Colors.INFO_LIGHT,
                        border_radius=Borders.RADIUS_FULL,
                    ),
                    rx.vstack(
                        rx.text("Zone climatique détectée", font_size=Typography.SIZE_XS, color=Colors.GRAY_500),
                        rx.text(SimulationState.zone_climatique, font_weight=Typography.WEIGHT_SEMIBOLD, color=Colors.INFO),
                        spacing="0",
                        align="start",
                    ),
                    spacing="3",
                    align="center",
                ),
                padding=Spacing.MD,
                background=Colors.WHITE,
                border=f"1px solid {Colors.INFO}",
                border_radius=Borders.RADIUS_LG,
                width="100%",
            ),
            rx.fragment(),
        ),
        
        spacing="4",
        width="100%",
    )


@rx.page(route="/simulation/date-department", title="Date et Département - SimuPrime")
def date_department_page() -> rx.Component:
    return simulation_layout(
        title="Nouvelle Simulation",
        subtitle="Date et Département",
        step=1,
        total_steps=6,
        content=step1_content(),
        back_url="/",
        next_url="/simulation/sector",
        can_continue=SimulationState.can_continue_step1,
    )