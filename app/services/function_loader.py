"""
FunctionLoader - Chargement et exécution dynamique de fonctions Python
Utilisé pour les calculs CEE basés sur les fichiers de configuration des fiches.
"""

import inspect
import ast
import types
from typing import Any, Dict


class FunctionLoader:
    """
    Utilitaire pour charger, inspecter et appeler dynamiquement une fonction Python
    définie dans une chaîne de code.

    Attributes:
        code_string (str): Le code brut contenant la fonction.
        function_name (str): Le nom de la première fonction définie.
        function (function): L'objet fonction chargé.
        signature (inspect.Signature): La signature de la fonction.
    """
    
    def __init__(self, code_string: str):
        """
        Initialise le FunctionLoader avec une chaîne de code.

        Args:
            code_string (str): Code Python contenant au moins une fonction.
        """
        self.code_string = code_string
        self.function_name = self._extract_function_name()
        self.function = self._load_function()
        self.signature = inspect.signature(self.function)

    def _extract_function_name(self) -> str:
        """
        Parse le code et retourne le nom de la première fonction définie.

        Returns:
            str: Le nom de la première fonction trouvée.
        
        Raises:
            ValueError: Si le parsing échoue ou si aucune fonction n'est trouvée.
        """
        try:
            parsed = ast.parse(self.code_string)
            for node in parsed.body:
                if isinstance(node, ast.FunctionDef):
                    return node.name
        except Exception as e:
            raise ValueError(f"Échec du parsing du code: {e}")

        raise ValueError("Aucune définition de fonction trouvée.")

    def _load_function(self) -> types.FunctionType:
        """
        Exécute le code et extrait l'objet fonction par son nom.

        Returns:
            function: L'objet fonction Python chargé.
        
        Raises:
            RuntimeError: Si l'exécution du code échoue.
            TypeError: Si l'objet extrait n'est pas une fonction.
        """
        local_namespace = {}

        try:
            exec(self.code_string, {}, local_namespace)
        except Exception as e:
            raise RuntimeError(f"Échec de l'exécution du code: {e}")

        func = local_namespace.get(self.function_name)

        if not isinstance(func, types.FunctionType):
            raise TypeError(f"{self.function_name} n'est pas une fonction valide.")

        return func

    def get_signature(self) -> str:
        """Retourne la signature de la fonction en tant que chaîne."""
        return str(self.signature)

    def get_parameters(self) -> Dict[str, Dict[str, Any]]:
        """
        Retourne des informations détaillées sur chaque paramètre de la fonction.

        Returns:
            dict: Dictionnaire où les clés sont les noms des paramètres,
                  et les valeurs sont des dicts contenant 'default', 'kind',
                  'annotation', et 'required'.
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

    def get_parameter_names(self) -> list:
        """
        Retourne la liste des noms de paramètres.
        
        Returns:
            list: Liste des noms de paramètres.
        """
        return list(self.signature.parameters.keys())

    def call_with_dict(self, arg_dict: Dict[str, Any]) -> Any:
        """
        Appelle la fonction avec un dictionnaire d'arguments nommés.

        Args:
            arg_dict (dict): Dictionnaire des noms d'arguments et leurs valeurs.

        Returns:
            Any: Le résultat de l'appel de la fonction.
        
        Raises:
            TypeError: Si l'appel de la fonction échoue.
        """
        try:
            return self.function(**arg_dict)
        except TypeError as e:
            raise TypeError(f"Erreur lors de l'appel de la fonction avec args {arg_dict}: {e}")

    def validate_args(self, arg_dict: Dict[str, Any]) -> tuple:
        """
        Valide les arguments avant l'appel de la fonction.
        
        Args:
            arg_dict (dict): Dictionnaire des arguments à valider.
        
        Returns:
            tuple: (is_valid: bool, missing_args: list, extra_args: list)
        """
        params = self.get_parameters()
        required_params = [name for name, info in params.items() if info["required"]]
        
        provided_args = set(arg_dict.keys())
        required_args = set(required_params)
        all_params = set(params.keys())
        
        missing = list(required_args - provided_args)
        extra = list(provided_args - all_params)
        
        is_valid = len(missing) == 0
        
        return is_valid, missing, extra


def extract_parameters_from_code(code_string: str) -> Dict[str, str]:
    """
    Extrait les paramètres d'une fonction depuis une chaîne de code.
    
    Args:
        code_string (str): Code Python contenant la fonction.
    
    Returns:
        dict: Dictionnaire {nom_param: ""} pour chaque paramètre.
    """
    try:
        tree = ast.parse(code_string)
        for node in ast.walk(tree):
            if isinstance(node, ast.FunctionDef):
                return {arg.arg: "" for arg in node.args.args}
    except Exception:
        pass
    return {}


def safe_execute_function(code_string: str, args: Dict[str, Any]) -> tuple:
    """
    Exécute une fonction de manière sécurisée.
    
    Args:
        code_string (str): Le code de la fonction.
        args (dict): Les arguments à passer à la fonction.
    
    Returns:
        tuple: (success: bool, result: Any, error: str)
    """
    try:
        loader = FunctionLoader(code_string)
        
        # Valider les arguments
        is_valid, missing, extra = loader.validate_args(args)
        
        if not is_valid:
            return False, None, f"Arguments manquants: {', '.join(missing)}"
        
        # Exécuter la fonction
        result = loader.call_with_dict(args)
        return True, result, ""
        
    except ValueError as e:
        return False, None, f"Erreur de parsing: {str(e)}"
    except RuntimeError as e:
        return False, None, f"Erreur d'exécution: {str(e)}"
    except TypeError as e:
        return False, None, f"Erreur d'appel: {str(e)}"
    except Exception as e:
        return False, None, f"Erreur inattendue: {str(e)}"