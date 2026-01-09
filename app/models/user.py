"""
Modèle User pour la base de données.
"""

from typing import Optional
from datetime import datetime
import reflex as rx
from sqlmodel import Field


class User(rx.Model, table=True):
    """Modèle utilisateur pour la base de données locale."""
    
    __tablename__ = "users"
    
    id: Optional[int] = Field(default=None, primary_key=True)
    supabase_id: str = Field(unique=True, index=True)  # ID Supabase Auth
    email: str = Field(unique=True, index=True)
    full_name: str = Field(default="")
    created_at: datetime = Field(default_factory=datetime.utcnow)
    updated_at: datetime = Field(default_factory=datetime.utcnow)
    last_login: Optional[datetime] = Field(default=None)
    is_active: bool = Field(default=True)
    
    # Préférences utilisateur
    theme: str = Field(default="light")  # light ou dark
    notifications_enabled: bool = Field(default=True)


class UserSession(rx.Model, table=True):
    """Sessions utilisateur pour le tracking."""
    
    __tablename__ = "user_sessions"
    
    id: Optional[int] = Field(default=None, primary_key=True)
    user_id: int = Field(foreign_key="users.id")
    access_token: str = Field(index=True)
    refresh_token: Optional[str] = Field(default=None)
    created_at: datetime = Field(default_factory=datetime.utcnow)
    expires_at: Optional[datetime] = Field(default=None)
    ip_address: Optional[str] = Field(default=None)
    user_agent: Optional[str] = Field(default=None)
