"""
Dashboard State
Manages simulation history, KPIs, and dashboard functionality
"""

#import reflex as rx
#from typing import List, Dict, Any
#from datetime import datetime, timedelta
#from services.supabase_client import get_supabase, select_records, delete_record
#from ..services.supabase_service import supabase
#
#
#class SimulationRecord(rx.Base):
#    """Model for a simulation record"""
#    id: str = ""
#    name: str = ""
#    created_at: str = ""
#    signature_date: str = ""
#    department: str = ""
#    sector: str = ""
#    typology: str = ""
#    document_id: str = ""
#    beneficiary_type: str = ""
#    result_eur: float = 0.0
#    result_cumacs: float = 0.0


#class DashboardState(rx.State):
#    """Dashboard state management"""
#    
#    # Simulation data
#    simulations: List[Dict[str, Any]] = []
#    filtered_simulations: List[Dict[str, Any]] = []
#    selected_simulation: Dict[str, Any] = {}
#    
#    # Loading states
#    is_loading: bool = False
#    is_deleting: bool = False
#    
#    # KPIs
#    total_simulations: int = 0
#    total_eur: float = 0.0
#    total_cumacs: float = 0.0
#    monthly_count: int = 0
#    average_result: float = 0.0
#    last_simulation_date: str = ""
#    
#    # Filters
#    filter_sector: str = ""
#    filter_typology: str = ""
#    filter_date_start: str = ""
#    filter_date_end: str = ""
#    filter_search: str = ""
#    
#    # Pagination
#    current_page: int = 1
#    items_per_page: int = 10
#    total_pages: int = 1
#    
#    # Sort
#    sort_column: str = "created_at"
#    sort_ascending: bool = False
#    
#    # Modal states
#    show_delete_modal: bool = False
#    simulation_to_delete: str = ""
#    
#    # Messages
#    error_message: str = ""
#    success_message: str = ""
#    
#    @rx.var
#    def paginated_simulations(self) -> List[Dict[str, Any]]:
#        """Get current page of simulations"""
#        start = (self.current_page - 1) * self.items_per_page
#        end = start + self.items_per_page
#        return self.filtered_simulations[start:end]
#    
#    @rx.var
#    def has_simulations(self) -> bool:
#        """Check if there are any simulations"""
#        return len(self.simulations) > 0
#    
#    @rx.var
#    def showing_range(self) -> str:
#        """Get display text for pagination"""
#        if not self.filtered_simulations:
#            return "0 résultat"
#        start = (self.current_page - 1) * self.items_per_page + 1
#        end = min(self.current_page * self.items_per_page, len(self.filtered_simulations))
#        total = len(self.filtered_simulations)
#        return f"{start}-{end} sur {total}"
#    
#    def _clear_messages(self):
#        """Clear error and success messages"""
#        self.error_message = ""
#        self.success_message = ""
#    
#    def _calculate_kpis(self):
#        """Calculate KPIs from filtered simulations"""
#        if not self.simulations:
#            self.total_simulations = 0
#            self.total_eur = 0.0
#            self.total_cumacs = 0.0
#            self.monthly_count = 0
#            self.average_result = 0.0
#            self.last_simulation_date = "—"
#            return
#        
#        self.total_simulations = len(self.simulations)
#        
#        # Sum results
#        self.total_eur = sum(s.get("result_eur", 0) or 0 for s in self.simulations)
#        self.total_cumacs = sum(s.get("result_cumacs", 0) or 0 for s in self.simulations)
#        
#        # Average
#        if self.total_simulations > 0:
#            self.average_result = self.total_eur / self.total_simulations
#        else:
#            self.average_result = 0.0
#        
#        # Monthly count (last 30 days)
#        now = datetime.now()
#        thirty_days_ago = now - timedelta(days=30)
#        self.monthly_count = sum(
#            1 for s in self.simulations
#            if s.get("created_at") and datetime.fromisoformat(s["created_at"].replace("Z", "+00:00").replace("+00:00", "")) > thirty_days_ago
#        )
#        
#        # Last simulation date
#        if self.simulations:
#            dates = [s.get("created_at") for s in self.simulations if s.get("created_at")]
#            if dates:
#                latest = max(dates)
#                try:
#                    dt = datetime.fromisoformat(latest.replace("Z", "+00:00").replace("+00:00", ""))
#                    self.last_simulation_date = dt.strftime("%d/%m/%Y")
#                except:
#                    self.last_simulation_date = "—"
#            else:
#                self.last_simulation_date = "—"
#        else:
#            self.last_simulation_date = "—"
#    
#    def _apply_filters(self):
#        """Apply all filters to simulations"""
#        filtered = self.simulations.copy()
#        
#        # Sector filter
#        if self.filter_sector:
#            filtered = [s for s in filtered if s.get("sector") == self.filter_sector]
#        
#        # Typology filter
#        if self.filter_typology:
#            filtered = [s for s in filtered if s.get("typology") == self.filter_typology]
#        
#        # Date range filter
#        if self.filter_date_start:
#            try:
#                start_date = datetime.strptime(self.filter_date_start, "%Y-%m-%d")
#                filtered = [
#                    s for s in filtered
#                    if s.get("created_at") and datetime.fromisoformat(s["created_at"].replace("Z", "+00:00").replace("+00:00", "")) >= start_date
#                ]
#            except:
#                pass
#        
#        if self.filter_date_end:
#            try:
#                end_date = datetime.strptime(self.filter_date_end, "%Y-%m-%d")
#                filtered = [
#                    s for s in filtered
#                    if s.get("created_at") and datetime.fromisoformat(s["created_at"].replace("Z", "+00:00").replace("+00:00", "")) <= end_date
#                ]
#            except:
#                pass
#        
#        # Text search
#        if self.filter_search:
#            search_lower = self.filter_search.lower()
#            filtered = [
#                s for s in filtered
#                if search_lower in (s.get("name", "") or "").lower()
#                or search_lower in (s.get("document_id", "") or "").lower()
#                or search_lower in (s.get("department", "") or "").lower()
#            ]
#        
#        # Sort
#        if self.sort_column and filtered:
#            try:
#                filtered.sort(
#                    key=lambda x: x.get(self.sort_column) or "",
#                    reverse=not self.sort_ascending
#                )
#            except:
#                pass
#        
#        self.filtered_simulations = filtered
#        self.total_pages = max(1, (len(filtered) + self.items_per_page - 1) // self.items_per_page)
#        
#        # Reset to page 1 if current page is out of range
#        if self.current_page > self.total_pages:
#            self.current_page = 1
#    
#    @rx.event
#    def load_simulations(self):
#        """Load simulations from database"""
#        self._clear_messages()
#        self.is_loading = True
#        yield
#        
#        try:
#            # Get current user's simulations
#            # Note: In production, filter by user_id
#            from state.auth_state import AuthState
#            
#            # For now, load all simulations (would need to filter by user_id in production)
#            records = select_records(
#                "simulations",
#                order_by="created_at",
#                ascending=False
#            )
#            
#            self.simulations = records
#            self._apply_filters()
#            self._calculate_kpis()
#            
#        except Exception as e:
#            print(f"❌ Error loading simulations: {e}")
#            self.error_message = "Erreur lors du chargement des simulations."
#            self.simulations = []
#            self.filtered_simulations = []
#        
#        self.is_loading = False
#    
#    @rx.event
#    def set_filter_sector(self, value: str):
#        """Set sector filter"""
#        self.filter_sector = value
#        self.current_page = 1
#        self._apply_filters()
#    
#    @rx.event
#    def set_filter_typology(self, value: str):
#        """Set typology filter"""
#        self.filter_typology = value
#        self.current_page = 1
#        self._apply_filters()
#    
#    @rx.event
#    def set_filter_date_start(self, value: str):
#        """Set start date filter"""
#        self.filter_date_start = value
#        self.current_page = 1
#        self._apply_filters()
#    
#    @rx.event
#    def set_filter_date_end(self, value: str):
#        """Set end date filter"""
#        self.filter_date_end = value
#        self.current_page = 1
#        self._apply_filters()
#    
#    @rx.event
#    def set_filter_search(self, value: str):
#        """Set search filter"""
#        self.filter_search = value
#        self.current_page = 1
#        self._apply_filters()
#    
#    @rx.event
#    def clear_filters(self):
#        """Clear all filters"""
#        self.filter_sector = ""
#        self.filter_typology = ""
#        self.filter_date_start = ""
#        self.filter_date_end = ""
#        self.filter_search = ""
#        self.current_page = 1
#        self._apply_filters()
#    
#    @rx.event
#    def set_sort(self, column: str):
#        """Set sort column and direction"""
#        if self.sort_column == column:
#            self.sort_ascending = not self.sort_ascending
#        else:
#            self.sort_column = column
#            self.sort_ascending = False
#        self._apply_filters()
#    
#    @rx.event
#    def set_items_per_page(self, value: str):
#        """Set items per page"""
#        try:
#            self.items_per_page = int(value)
#            self.current_page = 1
#            self._apply_filters()
#        except:
#            pass
#    
#    @rx.event
#    def go_to_page(self, page: int):
#        """Go to specific page"""
#        if 1 <= page <= self.total_pages:
#            self.current_page = page
#    
#    @rx.event
#    def next_page(self):
#        """Go to next page"""
#        if self.current_page < self.total_pages:
#            self.current_page += 1
#    
#    @rx.event
#    def prev_page(self):
#        """Go to previous page"""
#        if self.current_page > 1:
#            self.current_page -= 1
#    
#    @rx.event
#    def open_delete_modal(self, simulation_id: str):
#        """Open delete confirmation modal"""
#        self.simulation_to_delete = simulation_id
#        self.show_delete_modal = True
#    
#    @rx.event
#    def close_delete_modal(self):
#        """Close delete confirmation modal"""
#        self.simulation_to_delete = ""
#        self.show_delete_modal = False
#    
#    @rx.event
#    def confirm_delete(self):
#        """Confirm and execute deletion"""
#        if not self.simulation_to_delete:
#            return
#        
#        self._clear_messages()
#        self.is_deleting = True
#        yield
#        
#        try:
#            success = delete_record("simulations", self.simulation_to_delete)
#            
#            if success:
#                # Remove from local state
#                self.simulations = [s for s in self.simulations if s.get("id") != self.simulation_to_delete]
#                self._apply_filters()
#                self._calculate_kpis()
#                self.success_message = "Simulation supprimée avec succès."
#            else:
#                self.error_message = "Erreur lors de la suppression."
#        except Exception as e:
#            print(f"❌ Error deleting simulation: {e}")
#            self.error_message = "Erreur lors de la suppression."
#        
#        self.is_deleting = False
#        self.close_delete_modal()
#    
#    @rx.event
#    def view_simulation(self, simulation_id: str):
#        """View simulation details"""
#        for s in self.simulations:
#            if s.get("id") == simulation_id:
#                self.selected_simulation = s
#                return rx.redirect(f"/simulation/{simulation_id}")
#        return rx.toast.error("Simulation non trouvée")
#    
#    @rx.event
#    def export_simulations(self):
#        """Export simulations to CSV"""
#        # This would generate a CSV file for download
#        # Implementation depends on specific requirements
#        yield rx.toast.info("Export en cours de développement...")


"""État du dashboard"""
import reflex as rx
from typing import List, Dict, Any


class DashboardState(rx.State):
    """État pour le tableau de bord."""
    
    simulations: List[Dict[str, Any]] = []
    is_loading: bool = False
    error_message: str = ""
    
    @rx.var
    def simulations_list(self) -> List[Dict[str, str]]:
        """Liste des simulations formatée pour l'affichage."""
        formatted = []
        for sim in self.simulations:
            formatted.append({
                "name": sim.get("name", "Sans nom"),
                "fiche": sim.get("fiche_code", ""),
                "sector": sim.get("sector", ""),
                "department": sim.get("department", ""),
                "euros": f"{sim.get('result_euros', 0):,.2f} €".replace(",", " "),
                "date": sim.get("created_at", "")[:10] if sim.get("created_at") else "",
            })
        return formatted
    
    @rx.var
    def has_simulations(self) -> bool:
        """Vérifie s'il y a des simulations."""
        return len(self.simulations) > 0
    
    @rx.var
    def total_simulations_str(self) -> str:
        """Nombre total de simulations."""
        return str(len(self.simulations))
    
    @rx.var
    def total_euros_str(self) -> str:
        """Total des primes en euros."""
        total = sum(sim.get("result_euros", 0) for sim in self.simulations)
        return f"{total:,.2f} €".replace(",", " ")
    
    @rx.var
    def total_cumacs_str(self) -> str:
        """Total des cumacs."""
        total = sum(sim.get("result_cumacs", 0) for sim in self.simulations)
        return f"{total:,.0f} kWh".replace(",", " ")
    
    @rx.event
    async def load_simulations(self):
        """Charge les simulations de l'utilisateur connecté."""
        self.is_loading = True
        self.error_message = ""
        yield
        
        try:
            # Essayer d'importer Supabase
            supabase = None
            try:
                from ..services.supabase_service import supabase as sb_client
                supabase = sb_client
            except ImportError:
                pass
            
            # Récupérer l'utilisateur connecté
            user_id = None
            try:
                from .auth_state import AuthState
                auth_state = await self.get_state(AuthState)
                user_id = getattr(auth_state, 'user_id', None)
            except Exception:
                pass
            
            if supabase and user_id:
                response = supabase.table("simulations").select("*").eq("user_id", user_id).order("created_at", desc=True).limit(20).execute()
                if response.data:
                    self.simulations = response.data
                else:
                    self.simulations = []
            else:
                # Données de démo
                self.simulations = [
                    {"name": "Isolation Dupont", "fiche_code": "BAR-EN-101", "sector": "Résidentiel", "department": "Paris (75)", "result_euros": 812.50, "result_cumacs": 125000, "created_at": "2026-01-09"},
                    {"name": "PAC Martin", "fiche_code": "BAR-TH-104", "sector": "Résidentiel", "department": "Lyon (69)", "result_euros": 1170.00, "result_cumacs": 180000, "created_at": "2026-01-08"},
                    {"name": "Chaudière Bernard", "fiche_code": "BAR-TH-106", "sector": "Résidentiel", "department": "Marseille (13)", "result_euros": 494.00, "result_cumacs": 76000, "created_at": "2026-01-07"},
                ]
        except Exception as e:
            self.error_message = str(e)
            self.simulations = [
                {"name": "Isolation Dupont", "fiche_code": "BAR-EN-101", "sector": "Résidentiel", "department": "Paris (75)", "result_euros": 812.50, "result_cumacs": 125000, "created_at": "2026-01-09"},
                {"name": "PAC Martin", "fiche_code": "BAR-TH-104", "sector": "Résidentiel", "department": "Lyon (69)", "result_euros": 1170.00, "result_cumacs": 180000, "created_at": "2026-01-08"},
                {"name": "Chaudière Bernard", "fiche_code": "BAR-TH-106", "sector": "Résidentiel", "department": "Marseille (13)", "result_euros": 494.00, "result_cumacs": 76000, "created_at": "2026-01-07"},
            ]
        
        self.is_loading = False