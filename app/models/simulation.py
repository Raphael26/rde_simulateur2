"""
Modèle Simulation pour la base de données.
"""

from typing import Optional
from datetime import datetime, date
import reflex as rx
from sqlmodel import Field


class Simulation(rx.Model, table=True):
    """Modèle de simulation enregistrée."""
    
    __tablename__ = "simulations"
    
    id: Optional[int] = Field(default=None, primary_key=True)
    user_id: str = Field(index=True)  # ID Supabase Auth de l'utilisateur
    
    # Métadonnées
    name: str = Field(default="Ma simulation")
    created_at: datetime = Field(default_factory=datetime.utcnow)
    updated_at: datetime = Field(default_factory=datetime.utcnow)
    
    # Données de la simulation
    signature_date: date = Field(default_factory=date.today)
    department: str = Field(default="")
    sector: str = Field(default="")
    typology: str = Field(default="")
    fiche_code: str = Field(default="")
    fiche_description: str = Field(default="")
    beneficiary_type: str = Field(default="")  # particulier ou personne_morale
    
    # Paramètres d'entrée (JSON stringifié)
    input_data: str = Field(default="{}")
    
    # Résultats
    result_cumacs: float = Field(default=0.0)
    result_euros: float = Field(default=0.0)
    
    # Statut
    is_draft: bool = Field(default=False)
    is_deleted: bool = Field(default=False)


class SimulationTemplate(rx.Model, table=True):
    """Templates de simulation sauvegardés par l'utilisateur."""
    
    __tablename__ = "simulation_templates"
    
    id: Optional[int] = Field(default=None, primary_key=True)
    user_id: str = Field(index=True)
    name: str = Field(default="Mon template")
    description: str = Field(default="")
    
    # Configuration du template
    sector: str = Field(default="")
    typology: str = Field(default="")
    fiche_code: str = Field(default="")
    
    # Valeurs par défaut (JSON)
    default_values: str = Field(default="{}")
    
    created_at: datetime = Field(default_factory=datetime.utcnow)
    updated_at: datetime = Field(default_factory=datetime.utcnow)
