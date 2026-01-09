"""
Modèle Document (fiches d'opération) pour la base de données.
"""

from typing import Optional
from datetime import datetime
import reflex as rx
from sqlmodel import Field


class Document(rx.Model, table=True):
    """Modèle de fiche d'opération CEE."""
    
    __tablename__ = "documents"
    
    id: Optional[int] = Field(default=None, primary_key=True)
    code: str = Field(unique=True, index=True)  # Ex: BAR-TH-101
    title: str = Field(default="")
    description: str = Field(default="")
    
    # Classification
    sector: str = Field(index=True)  # Ex: Résidentiel
    sector_abbr: str = Field(default="")  # Ex: BAR
    typology: str = Field(index=True)  # Ex: Thermique
    typology_abbr: str = Field(default="")  # Ex: TH
    
    # Configuration
    config_loaded: bool = Field(default=False)
    
    # Métadonnées
    icon: str = Field(default="file-text")
    is_active: bool = Field(default=True)
    display_order: int = Field(default=0)
    
    created_at: datetime = Field(default_factory=datetime.utcnow)
    updated_at: datetime = Field(default_factory=datetime.utcnow)


class Sector(rx.Model, table=True):
    """Modèle de secteur."""
    
    __tablename__ = "sectors"
    
    id: Optional[int] = Field(default=None, primary_key=True)
    name: str = Field(unique=True)
    abbr: str = Field(unique=True)  # Abréviation
    icon: str = Field(default="folder")
    display_order: int = Field(default=0)
    is_active: bool = Field(default=True)


class Typology(rx.Model, table=True):
    """Modèle de typologie."""
    
    __tablename__ = "typologies"
    
    id: Optional[int] = Field(default=None, primary_key=True)
    name: str = Field(index=True)
    abbr: str = Field(index=True)
    sector_id: Optional[int] = Field(default=None, foreign_key="sectors.id")
    icon: str = Field(default="tag")
    display_order: int = Field(default=0)
    is_active: bool = Field(default=True)


class MprArticle(rx.Model, table=True):
    """Articles MaPrimeRénov' liés aux fiches."""
    
    __tablename__ = "mpr_articles"
    
    id: Optional[int] = Field(default=None, primary_key=True)
    pdf_file: str = Field(index=True)  # Code de la fiche
    link_article: str = Field(default="")  # URL Légifrance
    description: str = Field(default="")
    created_at: datetime = Field(default_factory=datetime.utcnow)
