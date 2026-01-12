"""
État de gestion du profil utilisateur et du dashboard.
"""

#import reflex as rx
#from typing import List, Dict, Any, Optional
#from datetime import datetime, date, timedelta
#import json
#
#from ..models.simulation import Simulation
#from .auth_state import AuthState
#
#
#class UserState(AuthState):
#    """État utilisateur étendu avec gestion du dashboard et profil."""
#    
#    # ==================== Dashboard ====================
#    simulations: List[Dict[str, Any]] = []
#    filtered_simulations: List[Dict[str, Any]] = []
#    
#    # Filtres
#    filter_date_start: str = ""
#    filter_date_end: str = ""
#    filter_sector: str = ""
#    filter_typology: str = ""
#    filter_search: str = ""
#    
#    # Pagination
#    page_size: int = 10
#    current_page: int = 1
#    total_pages: int = 1
#    
#    # Tri
#    sort_column: str = "created_at"
#    sort_direction: str = "desc"
#    
#    # ==================== KPIs ====================
#    total_simulations: int = 0
#    simulations_this_month: int = 0
#    average_result: float = 0.0
#    last_simulation_date: str = ""
#    
#    # ==================== Profil ====================
#    edit_mode: bool = False
#    edit_full_name: str = ""
#    current_password: str = ""
#    profile_new_password: str = ""
#    profile_confirm_password: str = ""
#    profile_error: str = ""
#    profile_success: str = ""
#    
#    # ==================== Dashboard Methods ====================
#    
#    @rx.event
#    def load_simulations(self):
#        """Charge les simulations de l'utilisateur."""
#        if not self.user_id:
#            return
#        
#        try:
#            with rx.session() as session:
#                query = Simulation.select().where(
#                    Simulation.user_id == self.user_id,
#                    Simulation.is_deleted == False
#                )
#                results = session.exec(query).all()
#                
#                self.simulations = [
#                    {
#                        "id": sim.id,
#                        "name": sim.name,
#                        "created_at": sim.created_at.isoformat() if sim.created_at else "",
#                        "signature_date": sim.signature_date.isoformat() if sim.signature_date else "",
#                        "department": sim.department,
#                        "sector": sim.sector,
#                        "typology": sim.typology,
#                        "fiche_code": sim.fiche_code,
#                        "fiche_description": sim.fiche_description,
#                        "beneficiary_type": sim.beneficiary_type,
#                        "result_cumacs": sim.result_cumacs,
#                        "result_euros": sim.result_euros,
#                        "input_data": sim.input_data,
#                    }
#                    for sim in results
#                ]
#                
#                self._apply_filters()
#                self._calculate_kpis()
#                
#        except Exception as e:
#            print(f"❌ Erreur chargement simulations: {e}")
#            self.simulations = []
#    
#    def _apply_filters(self):
#        """Applique les filtres aux simulations."""
#        filtered = self.simulations.copy()
#        
#        # Filtre par date
#        if self.filter_date_start:
#            start = datetime.fromisoformat(self.filter_date_start)
#            filtered = [
#                s for s in filtered
#                if s["created_at"] and datetime.fromisoformat(s["created_at"]) >= start
#            ]
#        
#        if self.filter_date_end:
#            end = datetime.fromisoformat(self.filter_date_end)
#            filtered = [
#                s for s in filtered
#                if s["created_at"] and datetime.fromisoformat(s["created_at"]) <= end
#            ]
#        
#        # Filtre par secteur
#        if self.filter_sector:
#            filtered = [s for s in filtered if s["sector"] == self.filter_sector]
#        
#        # Filtre par typologie
#        if self.filter_typology:
#            filtered = [s for s in filtered if s["typology"] == self.filter_typology]
#        
#        # Recherche textuelle
#        if self.filter_search:
#            search = self.filter_search.lower()
#            filtered = [
#                s for s in filtered
#                if search in s["name"].lower()
#                or search in s["fiche_code"].lower()
#                or search in s["fiche_description"].lower()
#                or search in s["department"].lower()
#            ]
#        
#        # Tri
#        reverse = self.sort_direction == "desc"
#        if self.sort_column in ["created_at", "signature_date"]:
#            filtered.sort(key=lambda x: x.get(self.sort_column, ""), reverse=reverse)
#        elif self.sort_column in ["result_cumacs", "result_euros"]:
#            filtered.sort(key=lambda x: float(x.get(self.sort_column, 0)), reverse=reverse)
#        else:
#            filtered.sort(key=lambda x: str(x.get(self.sort_column, "")).lower(), reverse=reverse)
#        
#        self.filtered_simulations = filtered
#        self.total_pages = max(1, (len(filtered) + self.page_size - 1) // self.page_size)
#        self.current_page = min(self.current_page, self.total_pages)
#    
#    def _calculate_kpis(self):
#        """Calcule les KPIs du dashboard."""
#        self.total_simulations = len(self.filtered_simulations)
#        
#        # Simulations ce mois
#        now = datetime.now()
#        first_of_month = now.replace(day=1, hour=0, minute=0, second=0, microsecond=0)
#        self.simulations_this_month = len([
#            s for s in self.filtered_simulations
#            if s["created_at"] and datetime.fromisoformat(s["created_at"]) >= first_of_month
#        ])
#        
#        # Moyenne des résultats
#        if self.filtered_simulations:
#            total = sum(s["result_euros"] for s in self.filtered_simulations)
#            self.average_result = total / len(self.filtered_simulations)
#        else:
#            self.average_result = 0.0
#        
#        # Dernière simulation
#        if self.simulations:
#            sorted_sims = sorted(
#                self.simulations,
#                key=lambda x: x["created_at"],
#                reverse=True
#            )
#            if sorted_sims:
#                self.last_simulation_date = sorted_sims[0]["created_at"][:10]
#    
#    # ==================== Filtres ====================
#    
#    @rx.event
#    def set_filter_date_start(self, value: str):
#        self.filter_date_start = value
#        self._apply_filters()
#    
#    @rx.event
#    def set_filter_date_end(self, value: str):
#        self.filter_date_end = value
#        self._apply_filters()
#    
#    @rx.event
#    def set_filter_sector(self, value: str):
#        self.filter_sector = value
#        self._apply_filters()
#    
#    @rx.event
#    def set_filter_typology(self, value: str):
#        self.filter_typology = value
#        self._apply_filters()
#    
#    @rx.event
#    def set_filter_search(self, value: str):
#        self.filter_search = value
#        self._apply_filters()
#    
#    @rx.event
#    def clear_filters(self):
#        """Réinitialise tous les filtres."""
#        self.filter_date_start = ""
#        self.filter_date_end = ""
#        self.filter_sector = ""
#        self.filter_typology = ""
#        self.filter_search = ""
#        self._apply_filters()
#    
#    # ==================== Pagination ====================
#    
#    @rx.event
#    def set_page_size(self, value: str):
#        self.page_size = int(value)
#        self.current_page = 1
#        self._apply_filters()
#    
#    @rx.event
#    def go_to_page(self, page: int):
#        self.current_page = max(1, min(page, self.total_pages))
#    
#    @rx.event
#    def next_page(self):
#        if self.current_page < self.total_pages:
#            self.current_page += 1
#    
#    @rx.event
#    def previous_page(self):
#        if self.current_page > 1:
#            self.current_page -= 1
#    
#    # ==================== Tri ====================
#    
#    @rx.event
#    def sort_by(self, column: str):
#        if self.sort_column == column:
#            self.sort_direction = "asc" if self.sort_direction == "desc" else "desc"
#        else:
#            self.sort_column = column
#            self.sort_direction = "desc"
#        self._apply_filters()
#    
#    # ==================== Actions sur simulations ====================
#    
#    @rx.event
#    def delete_simulation(self, simulation_id: int):
#        """Supprime (soft delete) une simulation."""
#        try:
#            with rx.session() as session:
#                simulation = session.get(Simulation, simulation_id)
#                if simulation and simulation.user_id == self.user_id:
#                    simulation.is_deleted = True
#                    session.add(simulation)
#                    session.commit()
#                    
#            self.load_simulations()
#            return rx.toast("Simulation supprimée", duration=3000)
#            
#        except Exception as e:
#            print(f"❌ Erreur suppression: {e}")
#            return rx.toast("Erreur lors de la suppression", duration=5000)
#    
#    # ==================== Profil ====================
#    
#    @rx.event
#    def toggle_edit_mode(self):
#        self.edit_mode = not self.edit_mode
#        if self.edit_mode:
#            self.edit_full_name = self.user_full_name
#        self.profile_error = ""
#        self.profile_success = ""
#    
#    @rx.event
#    def set_edit_full_name(self, value: str):
#        self.edit_full_name = value
#    
#    @rx.event
#    def set_current_password(self, value: str):
#        self.current_password = value
#    
#    @rx.event
#    def set_profile_new_password(self, value: str):
#        self.profile_new_password = value
#    
#    @rx.event
#    def set_profile_confirm_password(self, value: str):
#        self.profile_confirm_password = value
#    
#    @rx.event
#    async def save_profile(self):
#        """Sauvegarde les modifications du profil."""
#        self.profile_error = ""
#        self.profile_success = ""
#        
#        if not self.edit_full_name.strip():
#            self.profile_error = "Le nom ne peut pas être vide"
#            return
#        
#        # TODO: Mettre à jour via Supabase Auth
#        # Pour l'instant, mise à jour locale
#        self.user_full_name = self.edit_full_name.strip()
#        self.edit_mode = False
#        self.profile_success = "Profil mis à jour"
#        yield rx.toast("Profil mis à jour", duration=3000)
#    
#    @rx.event
#    async def change_password(self):
#        """Change le mot de passe de l'utilisateur."""
#        self.profile_error = ""
#        self.profile_success = ""
#        
#        if not self.current_password:
#            self.profile_error = "Veuillez entrer votre mot de passe actuel"
#            return
#        
#        if self.profile_new_password != self.profile_confirm_password:
#            self.profile_error = "Les mots de passe ne correspondent pas"
#            return
#        
#        from ..services.auth_service import AuthService
#        
#        valid, msg = AuthService.validate_password(self.profile_new_password)
#        if not valid:
#            self.profile_error = msg
#            return
#        
#        result = AuthService.update_password(
#            self.profile_new_password,
#            self.access_token
#        )
#        
#        if result.success:
#            self.current_password = ""
#            self.profile_new_password = ""
#            self.profile_confirm_password = ""
#            self.profile_success = "Mot de passe mis à jour"
#            yield rx.toast("Mot de passe mis à jour", duration=3000)
#        else:
#            self.profile_error = result.message
#
#    @rx.var
#    def initials(self) -> str:
#        """Retourne les initiales de l'utilisateur."""
#        if self.user_email:
#            return self.user_email[0:2].upper()
#        return "U"
#
#    @rx.var
#    def display_name(self) -> str:
#        """Retourne le nom d'affichage."""
#        if self.user_email:
#            return self.user_email.split("@")[0]
#        return "Utilisateur"
#    
#    # ==================== Computed vars ====================
#    
#    @rx.var
#    def paginated_simulations(self) -> List[Dict[str, Any]]:
#        """Retourne les simulations de la page courante."""
#        start = (self.current_page - 1) * self.page_size
#        end = start + self.page_size
#        return self.filtered_simulations[start:end]
#    
#    @rx.var
#    def has_simulations(self) -> bool:
#        """Vérifie s'il y a des simulations."""
#        return len(self.simulations) > 0
#    
#    @rx.var
#    def formatted_average_result(self) -> str:
#        """Moyenne formatée en euros."""
#        return f"{self.average_result:,.2f} €".replace(",", " ")
#    
#    @rx.var
#    def available_sectors(self) -> List[str]:
#        """Liste des secteurs uniques dans les simulations."""
#        sectors = set(s["sector"] for s in self.simulations if s["sector"])
#        return sorted(list(sectors))
#    
#    @rx.var
#    def available_typologies(self) -> List[str]:
#        """Liste des typologies uniques dans les simulations."""
#        typologies = set(s["typology"] for s in self.simulations if s["typology"])
#        return sorted(list(typologies))



"""
État de gestion du profil utilisateur et du dashboard.
"""

import reflex as rx
from typing import List, Dict, Any, Optional
from datetime import datetime, date, timedelta
import json

from .auth_state import AuthState


class UserState(AuthState):
    """État utilisateur étendu avec gestion du dashboard et profil."""
    
    # ==================== Dashboard ====================
    simulations: List[Dict[str, Any]] = []
    filtered_simulations: List[Dict[str, Any]] = []
    
    # Filtres
    filter_date_start: str = ""
    filter_date_end: str = ""
    filter_sector: str = ""
    filter_typology: str = ""
    filter_search: str = ""
    
    # Pagination
    page_size: int = 10
    current_page: int = 1
    total_pages: int = 1
    
    # Tri
    sort_column: str = "created_at"
    sort_direction: str = "desc"
    
    # ==================== KPIs ====================
    total_simulations: int = 0
    simulations_this_month: int = 0
    average_result: float = 0.0
    last_simulation_date: str = ""
    
    # ==================== Profil ====================
    edit_mode: bool = False
    edit_full_name: str = ""
    current_password: str = ""
    profile_new_password: str = ""
    profile_confirm_password: str = ""
    profile_error: str = ""
    profile_success: str = ""
    
    # ==================== Helper Methods ====================
    
    def _get_supabase_client(self):
        """Récupère le client Supabase."""
        try:
            from ..services.supabase_service import get_service_client
            return get_service_client()
        except ImportError:
            pass
        try:
            from ..services.supabase_service import get_supabase_client
            return get_supabase_client()
        except ImportError:
            pass
        return None
    
    # ==================== Dashboard Methods ====================
    
    @rx.event
    async def load_simulations(self):
        """Charge les simulations de l'utilisateur depuis Supabase."""
        if not self.user_id:
            print("⚠️ Pas de user_id pour charger les simulations")
            self.simulations = []
            self._apply_filters()
            self._calculate_kpis()
            return
        
        try:
            client = self._get_supabase_client()
            
            if client:
                response = client.table("simulations")\
                    .select("*")\
                    .eq("user_id", self.user_id)\
                    .order("created_at", desc=True)\
                    .execute()
                
                if response.data:
                    self.simulations = [
                        {
                            "id": sim.get("id", ""),
                            "name": sim.get("name", "Sans nom"),
                            "created_at": sim.get("created_at", ""),
                            "signature_date": sim.get("date_signature", ""),
                            "department": sim.get("department", ""),
                            "sector": sim.get("sector", ""),
                            "typology": sim.get("typology", ""),
                            "fiche_code": sim.get("fiche_code", ""),
                            "fiche_description": sim.get("fiche_description", ""),
                            "beneficiary_type": sim.get("beneficiary_type", ""),
                            "result_cumacs": sim.get("result_cumacs", 0) or 0,
                            "result_euros": sim.get("result_euros", 0) or 0,
                            "input_data": sim.get("input_data", ""),
                        }
                        for sim in response.data
                    ]
                    print(f"✅ {len(self.simulations)} simulations chargées pour le profil")
                else:
                    self.simulations = []
                    print("ℹ️ Aucune simulation trouvée")
            else:
                print("⚠️ Client Supabase non disponible")
                self.simulations = []
            
            self._apply_filters()
            self._calculate_kpis()
                
        except Exception as e:
            print(f"❌ Erreur chargement simulations: {e}")
            self.simulations = []
            self._apply_filters()
            self._calculate_kpis()
    
    def _apply_filters(self):
        """Applique les filtres aux simulations."""
        filtered = self.simulations.copy()
        
        # Filtre par date
        if self.filter_date_start:
            try:
                start = datetime.fromisoformat(self.filter_date_start.replace("Z", "+00:00").replace("+00:00", ""))
                filtered = [
                    s for s in filtered
                    if s["created_at"] and datetime.fromisoformat(s["created_at"].replace("Z", "+00:00").replace("+00:00", "")) >= start
                ]
            except:
                pass
        
        if self.filter_date_end:
            try:
                end = datetime.fromisoformat(self.filter_date_end.replace("Z", "+00:00").replace("+00:00", ""))
                filtered = [
                    s for s in filtered
                    if s["created_at"] and datetime.fromisoformat(s["created_at"].replace("Z", "+00:00").replace("+00:00", "")) <= end
                ]
            except:
                pass
        
        # Filtre par secteur
        if self.filter_sector:
            filtered = [s for s in filtered if s.get("sector") == self.filter_sector]
        
        # Filtre par typologie
        if self.filter_typology:
            filtered = [s for s in filtered if s.get("typology") == self.filter_typology]
        
        # Recherche textuelle
        if self.filter_search:
            search = self.filter_search.lower()
            filtered = [
                s for s in filtered
                if search in (s.get("name") or "").lower()
                or search in (s.get("fiche_code") or "").lower()
                or search in (s.get("fiche_description") or "").lower()
                or search in (s.get("department") or "").lower()
            ]
        
        # Tri
        reverse = self.sort_direction == "desc"
        if self.sort_column in ["created_at", "signature_date"]:
            filtered.sort(key=lambda x: x.get(self.sort_column) or "", reverse=reverse)
        elif self.sort_column in ["result_cumacs", "result_euros"]:
            filtered.sort(key=lambda x: float(x.get(self.sort_column) or 0), reverse=reverse)
        else:
            filtered.sort(key=lambda x: str(x.get(self.sort_column) or "").lower(), reverse=reverse)
        
        self.filtered_simulations = filtered
        self.total_pages = max(1, (len(filtered) + self.page_size - 1) // self.page_size)
        self.current_page = min(self.current_page, self.total_pages)
    
    def _calculate_kpis(self):
        """Calcule les KPIs du dashboard."""
        self.total_simulations = len(self.simulations)
        
        # Simulations ce mois
        now = datetime.now()
        first_of_month = now.replace(day=1, hour=0, minute=0, second=0, microsecond=0)
        
        self.simulations_this_month = 0
        for s in self.simulations:
            try:
                if s.get("created_at"):
                    created = s["created_at"]
                    if isinstance(created, str):
                        created = datetime.fromisoformat(created.replace("Z", "+00:00").replace("+00:00", ""))
                    if created >= first_of_month:
                        self.simulations_this_month += 1
            except:
                pass
        
        # Moyenne des résultats
        if self.simulations:
            total = sum(s.get("result_euros") or 0 for s in self.simulations)
            self.average_result = total / len(self.simulations)
        else:
            self.average_result = 0.0
        
        # Dernière simulation
        if self.simulations:
            try:
                sorted_sims = sorted(
                    self.simulations,
                    key=lambda x: x.get("created_at") or "",
                    reverse=True
                )
                if sorted_sims and sorted_sims[0].get("created_at"):
                    self.last_simulation_date = sorted_sims[0]["created_at"][:10]
                else:
                    self.last_simulation_date = ""
            except:
                self.last_simulation_date = ""
        else:
            self.last_simulation_date = ""
    
    # ==================== Filtres ====================
    
    @rx.event
    def set_filter_date_start(self, value: str):
        self.filter_date_start = value
        self._apply_filters()
    
    @rx.event
    def set_filter_date_end(self, value: str):
        self.filter_date_end = value
        self._apply_filters()
    
    @rx.event
    def set_filter_sector(self, value: str):
        self.filter_sector = value
        self._apply_filters()
    
    @rx.event
    def set_filter_typology(self, value: str):
        self.filter_typology = value
        self._apply_filters()
    
    @rx.event
    def set_filter_search(self, value: str):
        self.filter_search = value
        self._apply_filters()
    
    @rx.event
    def clear_filters(self):
        """Réinitialise tous les filtres."""
        self.filter_date_start = ""
        self.filter_date_end = ""
        self.filter_sector = ""
        self.filter_typology = ""
        self.filter_search = ""
        self._apply_filters()
    
    # ==================== Pagination ====================
    
    @rx.event
    def set_page_size(self, value: str):
        self.page_size = int(value)
        self.current_page = 1
        self._apply_filters()
    
    @rx.event
    def go_to_page(self, page: int):
        self.current_page = max(1, min(page, self.total_pages))
    
    @rx.event
    def next_page(self):
        if self.current_page < self.total_pages:
            self.current_page += 1
    
    @rx.event
    def previous_page(self):
        if self.current_page > 1:
            self.current_page -= 1
    
    # ==================== Tri ====================
    
    @rx.event
    def sort_by(self, column: str):
        if self.sort_column == column:
            self.sort_direction = "asc" if self.sort_direction == "desc" else "desc"
        else:
            self.sort_column = column
            self.sort_direction = "desc"
        self._apply_filters()
    
    # ==================== Profil ====================
    
    @rx.event
    def toggle_edit_mode(self):
        self.edit_mode = not self.edit_mode
        if self.edit_mode:
            self.edit_full_name = self.user_full_name
        self.profile_error = ""
        self.profile_success = ""
    
    @rx.event
    def set_edit_full_name(self, value: str):
        self.edit_full_name = value
    
    @rx.event
    def set_current_password(self, value: str):
        self.current_password = value
    
    @rx.event
    def set_profile_new_password(self, value: str):
        self.profile_new_password = value
    
    @rx.event
    def set_profile_confirm_password(self, value: str):
        self.profile_confirm_password = value
    
    @rx.event
    async def save_profile(self):
        """Sauvegarde les modifications du profil."""
        self.profile_error = ""
        self.profile_success = ""
        
        if not self.edit_full_name.strip():
            self.profile_error = "Le nom ne peut pas être vide"
            return
        
        # TODO: Mettre à jour via Supabase Auth
        # Pour l'instant, mise à jour locale
        self.user_full_name = self.edit_full_name.strip()
        self.edit_mode = False
        self.profile_success = "Profil mis à jour"
        yield rx.toast.success("Profil mis à jour", duration=3000)
    
    @rx.event
    async def change_password(self):
        """Change le mot de passe de l'utilisateur."""
        self.profile_error = ""
        self.profile_success = ""
        
        if not self.current_password:
            self.profile_error = "Veuillez entrer votre mot de passe actuel"
            return
        
        if self.profile_new_password != self.profile_confirm_password:
            self.profile_error = "Les mots de passe ne correspondent pas"
            return
        
        try:
            from ..services.auth_service import AuthService
            
            valid, msg = AuthService.validate_password(self.profile_new_password)
            if not valid:
                self.profile_error = msg
                return
            
            result = AuthService.update_password(
                self.profile_new_password,
                self.access_token
            )
            
            if result.success:
                self.current_password = ""
                self.profile_new_password = ""
                self.profile_confirm_password = ""
                self.profile_success = "Mot de passe mis à jour"
                yield rx.toast.success("Mot de passe mis à jour", duration=3000)
            else:
                self.profile_error = result.message
        except Exception as e:
            self.profile_error = f"Erreur: {str(e)}"

    @rx.var
    def initials(self) -> str:
        """Retourne les initiales de l'utilisateur."""
        if self.user_full_name:
            parts = self.user_full_name.split()
            if len(parts) >= 2:
                return (parts[0][0] + parts[1][0]).upper()
            return self.user_full_name[0:2].upper()
        if self.user_email:
            return self.user_email[0:2].upper()
        return "U"

    @rx.var
    def display_name(self) -> str:
        """Retourne le nom d'affichage."""
        if self.user_full_name:
            return self.user_full_name
        if self.user_email:
            return self.user_email.split("@")[0]
        return "Utilisateur"
    
    # ==================== Computed vars ====================
    
    @rx.var
    def paginated_simulations(self) -> List[Dict[str, Any]]:
        """Retourne les simulations de la page courante."""
        start = (self.current_page - 1) * self.page_size
        end = start + self.page_size
        return self.filtered_simulations[start:end]
    
    @rx.var
    def has_simulations(self) -> bool:
        """Vérifie s'il y a des simulations."""
        return len(self.simulations) > 0
    
    @rx.var
    def formatted_average_result(self) -> str:
        """Moyenne formatée en euros."""
        return f"{self.average_result:,.2f} €".replace(",", " ")
    
    @rx.var
    def available_sectors(self) -> List[str]:
        """Liste des secteurs uniques dans les simulations."""
        sectors = set(s.get("sector") for s in self.simulations if s.get("sector"))
        return sorted(list(sectors))
    
    @rx.var
    def available_typologies(self) -> List[str]:
        """Liste des typologies uniques dans les simulations."""
        typologies = set(s.get("typology") for s in self.simulations if s.get("typology"))
        return sorted(list(typologies))
    
    @rx.var
    def total_simulations_str(self) -> str:
        """Nombre total de simulations en string."""
        return str(self.total_simulations)
    
    @rx.var
    def simulations_this_month_str(self) -> str:
        """Simulations ce mois en string."""
        return str(self.simulations_this_month)