"""
Moteur de calcul dynamique pour les simulations.
Charge et exécute les fonctions de calcul définies dans les fichiers de configuration.
Basé sur le FunctionLoader existant.
"""

import inspect
import ast
import types
from typing import Any, Dict, Optional
from dataclasses import dataclass


@dataclass
class CalculationResult:
    """Résultat d'un calcul de simulation."""
    success: bool
    value: float
    error_message: str = ""
    cumacs: float = 0.0
    euros: float = 0.0


class FunctionLoader:
    """
    Utilitaire pour charger, inspecter et exécuter dynamiquement
    une fonction Python définie dans une chaîne de code.
    
    Attributes:
        code_string: Code source contenant la fonction
        function_name: Nom de la fonction extraite
        function: Objet fonction chargé
        signature: Signature de la fonction
    """
    
    def __init__(self, code_string: str):
        """
        Initialise le FunctionLoader avec une chaîne de code.
        
        Args:
            code_string: Code Python contenant au moins une fonction
        """
        self.code_string = code_string
        self.function_name = self._extract_function_name()
        self.function = self._load_function()
        self.signature = inspect.signature(self.function)
    
    def _extract_function_name(self) -> str:
        """
        Parse le code et retourne le nom de la première fonction définie.
        
        Returns:
            Nom de la fonction
            
        Raises:
            ValueError: Si aucune fonction n'est trouvée ou si le parsing échoue
        """
        try:
            parsed = ast.parse(self.code_string)
            for node in parsed.body:
                if isinstance(node, ast.FunctionDef):
                    return node.name
        except Exception as e:
            raise ValueError(f"Erreur de parsing du code: {e}")
        
        raise ValueError("Aucune définition de fonction trouvée dans le code")
    
    def _load_function(self) -> types.FunctionType:
        """
        Exécute le code et extrait l'objet fonction.
        
        Returns:
            Fonction Python chargée
            
        Raises:
            RuntimeError: Si l'exécution échoue
            TypeError: Si l'objet extrait n'est pas une fonction
        """
        local_namespace = {}
        
        # Namespace global avec les fonctions mathématiques courantes
        global_namespace = {
            'abs': abs,
            'min': min,
            'max': max,
            'sum': sum,
            'round': round,
            'pow': pow,
            'len': len,
            'int': int,
            'float': float,
            'str': str,
            'bool': bool,
            'list': list,
            'dict': dict,
            'range': range,
        }
        
        try:
            exec(self.code_string, global_namespace, local_namespace)
        except Exception as e:
            raise RuntimeError(f"Erreur d'exécution du code: {e}")
        
        func = local_namespace.get(self.function_name)
        
        if not isinstance(func, types.FunctionType):
            raise TypeError(f"{self.function_name} n'est pas une fonction valide")
        
        return func
    
    def get_signature(self) -> str:
        """Retourne la signature de la fonction sous forme de chaîne."""
        return str(self.signature)
    
    def get_parameters(self) -> Dict[str, Dict[str, Any]]:
        """
        Retourne les informations détaillées sur chaque paramètre.
        
        Returns:
            Dict avec nom du paramètre comme clé et infos comme valeur:
            - default: Valeur par défaut (None si requis)
            - kind: Type de paramètre
            - annotation: Annotation de type (si présente)
            - required: True si le paramètre est obligatoire
        """
        return {
            name: {
                "default": (
                    param.default if param.default is not inspect._empty else None
                ),
                "kind": str(param.kind),
                "annotation": (
                    str(param.annotation)
                    if param.annotation != inspect._empty
                    else None
                ),
                "required": (
                    param.default is inspect._empty
                    and param.kind in (
                        param.POSITIONAL_OR_KEYWORD,
                        param.KEYWORD_ONLY
                    )
                )
            }
            for name, param in self.signature.parameters.items()
        }
    
    def get_required_parameters(self) -> list:
        """
        Retourne la liste des paramètres obligatoires.
        
        Returns:
            Liste des noms de paramètres requis
        """
        params = self.get_parameters()
        return [name for name, info in params.items() if info["required"]]
    
    def call_with_dict(self, arg_dict: Dict[str, Any]) -> Any:
        """
        Appelle la fonction avec un dictionnaire d'arguments nommés.
        
        Args:
            arg_dict: Dictionnaire {nom_paramètre: valeur}
            
        Returns:
            Résultat de la fonction
            
        Raises:
            TypeError: Si les arguments sont invalides
        """
        try:
            return self.function(**arg_dict)
        except TypeError as e:
            raise TypeError(f"Erreur d'appel de la fonction avec {arg_dict}: {e}")
    
    def validate_args(self, arg_dict: Dict[str, Any]) -> tuple:
        """
        Valide que tous les arguments requis sont présents.
        
        Args:
            arg_dict: Dictionnaire d'arguments à valider
            
        Returns:
            Tuple (is_valid, missing_args)
        """
        required = self.get_required_parameters()
        missing = [p for p in required if p not in arg_dict or arg_dict[p] == ""]
        return (len(missing) == 0, missing)


class CalculationEngine:
    """
    Moteur de calcul pour les simulations CEE.
    Gère le chargement des fonctions et l'exécution des calculs.
    """
    
    # Taux de conversion cumacs → euros (configurable)
    CUMAC_TO_EURO_RATE = 0.0065
    
    def __init__(self):
        """Initialise le moteur de calcul."""
        self._function_loader: Optional[FunctionLoader] = None
        self._current_function_string: str = ""
    
    def load_function(self, function_string: str) -> bool:
        """
        Charge une fonction de calcul.
        
        Args:
            function_string: Code Python de la fonction
            
        Returns:
            True si le chargement réussit, False sinon
        """
        try:
            self._function_loader = FunctionLoader(function_string)
            self._current_function_string = function_string
            print(f"✅ Fonction chargée: {self._function_loader.function_name}")
            return True
        except Exception as e:
            print(f"❌ Erreur chargement fonction: {e}")
            self._function_loader = None
            return False
    
    def get_required_parameters(self) -> Dict[str, Dict[str, Any]]:
        """
        Retourne les paramètres requis pour la fonction chargée.
        
        Returns:
            Dict des paramètres avec leurs infos
        """
        if self._function_loader:
            return self._function_loader.get_parameters()
        return {}
    
    def calculate(self, parameters: Dict[str, Any]) -> CalculationResult:
        """
        Exécute le calcul avec les paramètres fournis.
        
        Args:
            parameters: Dict des valeurs des paramètres
            
        Returns:
            CalculationResult avec les valeurs calculées
        """
        if not self._function_loader:
            return CalculationResult(
                success=False,
                value=0.0,
                error_message="Aucune fonction de calcul chargée"
            )
        
        # Validation des arguments
        is_valid, missing = self._function_loader.validate_args(parameters)
        if not is_valid:
            return CalculationResult(
                success=False,
                value=0.0,
                error_message=f"Paramètres manquants: {', '.join(missing)}"
            )
        
        # Nettoyage des paramètres (conversion des types)
        clean_params = self._clean_parameters(parameters)
        
        try:
            result = self._function_loader.call_with_dict(clean_params)
            cumacs = float(result)
            euros = cumacs * self.CUMAC_TO_EURO_RATE
            
            return CalculationResult(
                success=True,
                value=cumacs,
                cumacs=cumacs,
                euros=euros
            )
            
        except Exception as e:
            return CalculationResult(
                success=False,
                value=0.0,
                error_message=str(e)
            )
    
    def _clean_parameters(self, parameters: Dict[str, Any]) -> Dict[str, Any]:
        """
        Nettoie et convertit les paramètres pour le calcul.
        
        Args:
            parameters: Paramètres bruts
            
        Returns:
            Paramètres nettoyés avec les bons types
        """
        clean = {}
        for key, value in parameters.items():
            # Ignorer les valeurs vides ou les dicts (non remplis)
            if value == "" or value is None or isinstance(value, dict):
                continue
            
            # Conversion booléenne
            if value == "Oui":
                clean[key] = True
            elif value == "Non":
                clean[key] = False
            else:
                # Tentative de conversion numérique
                try:
                    if isinstance(value, str):
                        if '.' in value or ',' in value:
                            clean[key] = float(value.replace(',', '.'))
                        else:
                            clean[key] = int(value)
                    else:
                        clean[key] = value
                except (ValueError, TypeError):
                    clean[key] = value
        
        return clean
    
    def extract_parameters_from_code(self, function_string: str) -> Dict[str, str]:
        """
        Extrait les noms des paramètres d'une fonction à partir de son code.
        
        Args:
            function_string: Code de la fonction
            
        Returns:
            Dict {nom_param: ""} pour initialisation
        """
        try:
            tree = ast.parse(function_string)
            for node in ast.walk(tree):
                if isinstance(node, ast.FunctionDef):
                    return {arg.arg: "" for arg in node.args.args}
        except Exception as e:
            print(f"⚠️ Erreur extraction paramètres: {e}")
        return {}


# Instance singleton
calculation_engine = CalculationEngine()
