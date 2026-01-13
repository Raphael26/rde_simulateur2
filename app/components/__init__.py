"""
Composants réutilisables de l'application.
"""

from .sidebar import sidebar, mobile_menu, sidebar_item, simulation_sidebar
from .header import header, page_header
from .kpi_card import kpi_card, kpi_grid, mini_kpi, result_card
from .selector_grid import selector_card, selector_grid, typology_card, beneficiary_card
from .stepper import step_indicator, simulation_stepper, progress_bar, step_navigation
from .simulation_table import simulation_table, simulation_row
from .dynamic_form import form_field, dynamic_form_field, simulator_form, form_summary

__all__ = [
    # Sidebar
    "sidebar",
    "mobile_menu",
    "sidebar_item",
    "simulation_sidebar",
    # Header
    "header",
    "page_header",
    # KPI
    "kpi_card",
    "kpi_grid",
    "mini_kpi",
    "result_card",
    # Selector
    "selector_card",
    "selector_grid",
    "typology_card",
    "beneficiary_card",
    # Stepper
    "step_indicator",
    "simulation_stepper",
    "progress_bar",
    "step_navigation",
    # Table
    "simulation_table",
    "simulation_row",
    # Form
    "form_field",
    "dynamic_form_field",
    "simulator_form",
    "form_summary",
]
