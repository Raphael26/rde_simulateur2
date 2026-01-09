"""
Services de l'application.
"""

from .supabase_client import (
    get_supabase_client,
    read_file_from_bucket,
    list_bucket_contents,
    upload_file_to_bucket,
    BUCKET_NAME,
)

from .supabase_service import supabase, get_supabase_client

from .auth_service import AuthService, AuthResult, auth_service

from .config_loader import ConfigLoader, FicheConfig, config_loader

from .calculation_engine import (
    FunctionLoader,
    CalculationEngine,
    CalculationResult,
    calculation_engine,
)

__all__ = [
    # Supabase
    "get_supabase_client",
    "read_file_from_bucket",
    "list_bucket_contents",
    "upload_file_to_bucket",
    "BUCKET_NAME",
    # Auth
    "AuthService",
    "AuthResult",
    "auth_service",
    # Config
    "ConfigLoader",
    "FicheConfig",
    "config_loader",
    # Calculation
    "FunctionLoader",
    "CalculationEngine",
    "CalculationResult",
    "calculation_engine",
]
