#"""
#Dashboard State - Gestion des simulations et KPIs du tableau de bord
#Charge les vraies données depuis Supabase
#"""
#
#import reflex as rx
#from typing import List, Dict, Any, Optional
#from datetime import datetime, timedelta
#
#
#class DashboardState(rx.State):
#    """État pour le tableau de bord avec chargement Supabase."""
#    
#    # Données
#    simulations: List[Dict[str, Any]] = []
#    is_loading: bool = False
#    error_message: str = ""
#    debug_info: str = ""  # Pour le débogage
#    
#    # Stockage local de l'user_id (synchronisé avec AuthState)
#    _current_user_id: str = ""
#    _current_user_email: str = ""
#    
#    def _get_supabase_client(self):
#        """Récupère le client Supabase de manière sécurisée."""
#        try:
#            # Essayer d'abord supabase_client.py
#            from ..services.supabase_client import get_supabase_client
#            client = get_supabase_client()
#            if client:
#                return client
#        except ImportError:
#            pass
#        
#        try:
#            # Fallback sur supabase_service.py
#            from ..services.supabase_service import get_supabase_client
#            client = get_supabase_client()
#            if client:
#                return client
#        except ImportError:
#            pass
#        
#        try:
#            # Dernier recours: variable globale
#            from ..services.supabase_service import supabase
#            if supabase:
#                return supabase
#        except ImportError:
#            pass
#        
#        return None
#    
#    async def _get_user_id(self) -> Optional[str]:
#        """Récupère l'ID de l'utilisateur connecté."""
#        # D'abord vérifier le cache local
#        if self._current_user_id:
#            return self._current_user_id
#        
#        # Essayer de récupérer depuis AuthState
#        try:
#            from .auth_state import AuthState
#            auth_state = await self.get_state(AuthState)
#            if auth_state.user_id:
#                self._current_user_id = auth_state.user_id
#                self._current_user_email = auth_state.user_email
#                return auth_state.user_id
#        except Exception as e:
#            print(f"⚠️ Erreur récupération AuthState: {e}")
#        
#        # Essayer de récupérer depuis Supabase directement
#        try:
#            client = self._get_supabase_client()
#            if client:
#                response = client.auth.get_user()
#                if response and response.user:
#                    self._current_user_id = response.user.id
#                    self._current_user_email = response.user.email or ""
#                    return response.user.id
#        except Exception as e:
#            print(f"⚠️ Erreur récupération user Supabase: {e}")
#        
#        return None
#    
#    # ==================== Computed Vars ====================
#    
#    @rx.var
#    def simulations_list(self) -> List[Dict[str, str]]:
#        """Liste des simulations formatée pour l'affichage dans le tableau."""
#        formatted = []
#        for sim in self.simulations:
#            # Gérer les différents noms de colonnes possibles
#            result_euros = sim.get("result_euros") or sim.get("result_eur") or 0
#            result_cumacs = sim.get("result_cumacs") or 0
#            fiche_code = sim.get("fiche_code") or sim.get("document_id") or ""
#            created_at = sim.get("created_at") or ""
#            
#            formatted.append({
#                "id": str(sim.get("id", "")),
#                "name": sim.get("name", "Sans nom"),
#                "fiche": fiche_code,
#                "sector": sim.get("sector", ""),
#                "department": sim.get("department", ""),
#                "euros": f"{float(result_euros):,.2f} €".replace(",", " "),
#                "date": created_at[:10] if created_at else "",
#            })
#        return formatted
#    
#    @rx.var
#    def has_simulations(self) -> bool:
#        """Vérifie s'il y a des simulations."""
#        return len(self.simulations) > 0
#    
#    @rx.var
#    def total_simulations_str(self) -> str:
#        """Nombre total de simulations."""
#        return str(len(self.simulations))
#    
#    @rx.var
#    def total_euros_str(self) -> str:
#        """Total des primes en euros."""
#        total = 0.0
#        for sim in self.simulations:
#            value = sim.get("result_euros") or sim.get("result_eur") or 0
#            total += float(value)
#        return f"{total:,.2f} €".replace(",", " ")
#    
#    @rx.var
#    def total_cumacs_str(self) -> str:
#        """Total des cumacs."""
#        total = 0.0
#        for sim in self.simulations:
#            value = sim.get("result_cumacs") or 0
#            total += float(value)
#        return f"{total:,.0f} kWh".replace(",", " ")
#    
#    @rx.var
#    def monthly_simulations_str(self) -> str:
#        """Nombre de simulations ce mois-ci."""
#        now = datetime.now()
#        first_of_month = now.replace(day=1, hour=0, minute=0, second=0, microsecond=0)
#        
#        count = 0
#        for sim in self.simulations:
#            created_at = sim.get("created_at")
#            if created_at:
#                try:
#                    # Gérer les différents formats de date
#                    if "T" in created_at:
#                        dt = datetime.fromisoformat(created_at.replace("Z", "+00:00").split("+")[0])
#                    else:
#                        dt = datetime.strptime(created_at[:10], "%Y-%m-%d")
#                    
#                    if dt >= first_of_month:
#                        count += 1
#                except Exception:
#                    pass
#        
#        return str(count)
#    
#    @rx.var
#    def last_simulation_date_str(self) -> str:
#        """Date de la dernière simulation."""
#        if not self.simulations:
#            return "—"
#        
#        latest = None
#        for sim in self.simulations:
#            created_at = sim.get("created_at")
#            if created_at:
#                try:
#                    if "T" in created_at:
#                        dt = datetime.fromisoformat(created_at.replace("Z", "+00:00").split("+")[0])
#                    else:
#                        dt = datetime.strptime(created_at[:10], "%Y-%m-%d")
#                    
#                    if latest is None or dt > latest:
#                        latest = dt
#                except Exception:
#                    pass
#        
#        if latest:
#            return latest.strftime("%d/%m/%Y")
#        return "—"
#    
#    # ==================== Event Handlers ====================
#    
#    @rx.event
#    async def load_simulations(self):
#        """Charge les simulations de l'utilisateur connecté depuis Supabase."""
#        self.is_loading = True
#        self.error_message = ""
#        self.debug_info = ""
#        yield
#        
#        try:
#            # Récupérer le client Supabase
#            client = self._get_supabase_client()
#            
#            if not client:
#                self.debug_info = "Client Supabase non disponible"
#                self.error_message = "Connexion à la base de données indisponible"
#                self.simulations = []
#                self.is_loading = False
#                return
#            
#            # Récupérer l'ID utilisateur
#            user_id = await self._get_user_id()
#            
#            if not user_id:
#                self.debug_info = "Utilisateur non connecté"
#                self.error_message = "Veuillez vous connecter pour voir vos simulations"
#                self.simulations = []
#                self.is_loading = False
#                return
#            
#            self.debug_info = f"Chargement pour user_id: {user_id[:8]}..."
#            
#            # Charger les simulations depuis Supabase
#            response = client.table("simulations")\
#                .select("*")\
#                .eq("user_id", user_id)\
#                .order("created_at", desc=True)\
#                .limit(50)\
#                .execute()
#            
#            if response.data:
#                self.simulations = response.data
#                self.debug_info = f"✅ {len(response.data)} simulation(s) chargée(s)"
#                print(f"✅ Dashboard: {len(response.data)} simulations chargées pour {user_id[:8]}...")
#            else:
#                self.simulations = []
#                self.debug_info = "Aucune simulation trouvée"
#                print(f"ℹ️ Dashboard: Aucune simulation pour {user_id[:8]}...")
#            
#        except Exception as e:
#            error_msg = str(e)
#            self.error_message = f"Erreur de chargement: {error_msg}"
#            self.debug_info = f"❌ Erreur: {error_msg}"
#            self.simulations = []
#            print(f"❌ Dashboard erreur: {e}")
#        
#        self.is_loading = False
#    
#    @rx.event
#    async def refresh_simulations(self):
#        """Rafraîchit la liste des simulations."""
#        # Réinitialiser le cache user_id pour forcer une nouvelle vérification
#        self._current_user_id = ""
#        yield DashboardState.load_simulations
#    
#    @rx.event
#    async def delete_simulation(self, simulation_id: str):
#        """Supprime une simulation."""
#        try:
#            client = self._get_supabase_client()
#            user_id = await self._get_user_id()
#            
#            if not client or not user_id:
#                yield rx.toast.error("Impossible de supprimer la simulation")
#                return
#            
#            # Supprimer de Supabase (soft delete ou hard delete selon ta config)
#            response = client.table("simulations")\
#                .delete()\
#                .eq("id", simulation_id)\
#                .eq("user_id", user_id)\
#                .execute()
#            
#            # Retirer de la liste locale
#            self.simulations = [s for s in self.simulations if str(s.get("id")) != simulation_id]
#            
#            yield rx.toast.success("Simulation supprimée")
#            
#        except Exception as e:
#            print(f"❌ Erreur suppression: {e}")
#            yield rx.toast.error("Erreur lors de la suppression")
#    
#    @rx.event
#    def view_simulation(self, simulation_id: str):
#        """Navigue vers les détails d'une simulation."""
#        return rx.redirect(f"/simulation/view/{simulation_id}")
#    
#    @rx.event
#    def duplicate_simulation(self, simulation_id: str):
#        """Duplique une simulation (TODO)."""
#        return rx.toast.info("Fonctionnalité à venir")


#"""État du dashboard"""
#import reflex as rx
#from typing import List, Dict, Any, Optional
#
#
#class DashboardState(rx.State):
#    """État pour le tableau de bord."""
#    
#    simulations: List[Dict[str, Any]] = []
#    is_loading: bool = False
#    error_message: str = ""
#    
#    # Simulation sélectionnée pour visualisation/export
#    selected_simulation_id: str = ""
#    
#    @rx.var
#    def simulations_list(self) -> List[Dict[str, str]]:
#        """Liste des simulations formatée pour l'affichage."""
#        formatted = []
#        for index, sim in enumerate(self.simulations, start=1):
#            # Formater la date
#            date_str = ""
#            if sim.get("created_at"):
#                try:
#                    date_str = sim["created_at"][:10]  # YYYY-MM-DD
#                    # Convertir en DD/MM/YYYY
#                    parts = date_str.split("-")
#                    if len(parts) == 3:
#                        date_str = f"{parts[2]}/{parts[1]}/{parts[0]}"
#                except:
#                    date_str = sim.get("created_at", "")[:10]
#            
#            formatted.append({
#                "id": sim.get("id", ""),
#                "number": str(index),
#                "name": sim.get("name", "Sans nom"),
#                "fiche": sim.get("fiche_code", ""),
#                "sector": sim.get("sector", ""),
#                "department": sim.get("department", ""),
#                "cumacs": f"{sim.get('result_cumacs', 0):,.0f}".replace(",", " "),
#                "euros": f"{sim.get('result_euros', 0):,.2f} €".replace(",", " "),
#                "date": date_str,
#            })
#        return formatted
#    
#    @rx.var
#    def has_simulations(self) -> bool:
#        """Vérifie s'il y a des simulations."""
#        return len(self.simulations) > 0
#    
#    @rx.var
#    def total_simulations_str(self) -> str:
#        """Nombre total de simulations."""
#        return str(len(self.simulations))
#    
#    @rx.var
#    def total_euros_str(self) -> str:
#        """Total des primes en euros."""
#        total = sum(sim.get("result_euros", 0) or 0 for sim in self.simulations)
#        return f"{total:,.2f} €".replace(",", " ")
#    
#    @rx.var
#    def total_cumacs_str(self) -> str:
#        """Total des cumacs."""
#        total = sum(sim.get("result_cumacs", 0) or 0 for sim in self.simulations)
#        return f"{total:,.0f} kWh".replace(",", " ")
#    
#    def _get_supabase_client(self):
#        """Récupère le client Supabase."""
#        try:
#            from ..services.supabase_service import get_service_client
#            return get_service_client()
#        except ImportError:
#            pass
#        try:
#            from ..services.supabase_service import get_supabase_client
#            return get_supabase_client()
#        except ImportError:
#            pass
#        return None
#    
#    @rx.event
#    async def load_simulations(self):
#        """Charge les simulations de l'utilisateur connecté."""
#        self.is_loading = True
#        self.error_message = ""
#        yield
#        
#        try:
#            client = self._get_supabase_client()
#            
#            # Récupérer l'utilisateur connecté
#            user_id = None
#            try:
#                from .auth_state import AuthState
#                auth_state = await self.get_state(AuthState)
#                user_id = getattr(auth_state, 'user_id', None)
#            except Exception as e:
#                print(f"⚠️ Erreur récupération user_id: {e}")
#            
#            if client and user_id:
#                response = client.table("simulations")\
#                    .select("*")\
#                    .eq("user_id", user_id)\
#                    .order("created_at", desc=True)\
#                    .limit(50)\
#                    .execute()
#                
#                if response.data:
#                    self.simulations = response.data
#                    print(f"✅ {len(response.data)} simulations chargées")
#                else:
#                    self.simulations = []
#            else:
#                # Pas de données si pas connecté
#                self.simulations = []
#                print("⚠️ Pas de client Supabase ou user_id")
#                
#        except Exception as e:
#            print(f"❌ Erreur chargement simulations: {e}")
#            self.error_message = str(e)
#            self.simulations = []
#        
#        self.is_loading = False
#    
#    def _get_simulation_by_id(self, simulation_id: str) -> Optional[Dict[str, Any]]:
#        """Récupère une simulation par son ID."""
#        for sim in self.simulations:
#            if sim.get("id") == simulation_id:
#                return sim
#        return None
#    
#    @rx.event
#    def view_simulation(self, simulation_id: str):
#        """Affiche les détails d'une simulation (TODO: créer page de détail)."""
#        sim = self._get_simulation_by_id(simulation_id)
#        if sim:
#            self.selected_simulation_id = simulation_id
#            return rx.toast.info(f"Simulation: {sim.get('name', 'Sans nom')}", duration=2000)
#        else:
#            return rx.toast.error("Simulation non trouvée")
#    
#    @rx.event
#    async def download_simulation_pdf(self, simulation_id: str):
#        """Télécharge le PDF d'une simulation."""
#        sim = self._get_simulation_by_id(simulation_id)
#        
#        if not sim:
#            yield rx.toast.error("Simulation non trouvée")
#            return
#        
#        try:
#            from reportlab.lib.pagesizes import A4
#            from reportlab.lib import colors
#            from reportlab.lib.styles import getSampleStyleSheet, ParagraphStyle
#            from reportlab.lib.units import cm
#            from reportlab.platypus import SimpleDocTemplate, Paragraph, Spacer, Table, TableStyle
#            from reportlab.lib.enums import TA_CENTER
#            from datetime import datetime
#            import io
#            import base64
#            
#            # Générer le PDF en mémoire
#            buffer = io.BytesIO()
#            
#            # Nom du fichier
#            safe_name = "".join(c if c.isalnum() or c in (' ', '-', '_') else '_' for c in (sim.get("name") or "simulation"))[:30]
#            safe_name = safe_name.replace(" ", "_")
#            filename = f"simulation_{safe_name}.pdf"
#            
#            # Créer le document
#            doc = SimpleDocTemplate(
#                buffer,
#                pagesize=A4,
#                rightMargin=2*cm,
#                leftMargin=2*cm,
#                topMargin=2*cm,
#                bottomMargin=2*cm
#            )
#            
#            # Styles
#            styles = getSampleStyleSheet()
#            
#            title_style = ParagraphStyle(
#                'CustomTitle',
#                parent=styles['Heading1'],
#                fontSize=24,
#                spaceAfter=30,
#                alignment=TA_CENTER,
#                textColor=colors.HexColor("#1a365d")
#            )
#            
#            subtitle_style = ParagraphStyle(
#                'CustomSubtitle',
#                parent=styles['Normal'],
#                fontSize=12,
#                spaceAfter=20,
#                alignment=TA_CENTER,
#                textColor=colors.HexColor("#718096")
#            )
#            
#            heading_style = ParagraphStyle(
#                'CustomHeading',
#                parent=styles['Heading2'],
#                fontSize=14,
#                spaceBefore=20,
#                spaceAfter=10,
#                textColor=colors.HexColor("#2d3748")
#            )
#            
#            # Contenu du PDF
#            story = []
#            
#            # En-tête
#            story.append(Paragraph("Rapport de Simulation CEE", title_style))
#            story.append(Paragraph(sim.get("name") or "Simulation", subtitle_style))
#            story.append(Paragraph(f"Généré le {datetime.now().strftime('%d/%m/%Y à %H:%M')}", subtitle_style))
#            story.append(Spacer(1, 20))
#            
#            # Résultats principaux
#            story.append(Paragraph("Résultats de la simulation", heading_style))
#            
#            result_euros = sim.get("result_euros", 0) or 0
#            result_cumacs = sim.get("result_cumacs", 0) or 0
#            
#            results_data = [
#                ["Indicateur", "Valeur"],
#                ["Prime CEE estimée", f"{result_euros:,.2f} €".replace(",", " ")],
#                ["Volume CEE", f"{result_cumacs:,.0f} kWh cumac".replace(",", " ")],
#            ]
#            
#            results_table = Table(results_data, colWidths=[8*cm, 8*cm])
#            results_table.setStyle(TableStyle([
#                ('BACKGROUND', (0, 0), (-1, 0), colors.HexColor("#22c55e")),
#                ('TEXTCOLOR', (0, 0), (-1, 0), colors.white),
#                ('ALIGN', (0, 0), (-1, -1), 'CENTER'),
#                ('FONTNAME', (0, 0), (-1, 0), 'Helvetica-Bold'),
#                ('FONTSIZE', (0, 0), (-1, 0), 12),
#                ('BOTTOMPADDING', (0, 0), (-1, 0), 12),
#                ('TOPPADDING', (0, 0), (-1, 0), 12),
#                ('BACKGROUND', (0, 1), (-1, -1), colors.HexColor("#f0fdf4")),
#                ('FONTSIZE', (0, 1), (-1, -1), 14),
#                ('FONTNAME', (0, 1), (-1, -1), 'Helvetica-Bold'),
#                ('BOTTOMPADDING', (0, 1), (-1, -1), 15),
#                ('TOPPADDING', (0, 1), (-1, -1), 15),
#                ('GRID', (0, 0), (-1, -1), 1, colors.HexColor("#86efac")),
#            ]))
#            story.append(results_table)
#            story.append(Spacer(1, 20))
#            
#            # Détails de l'opération
#            story.append(Paragraph("Détails de l'opération", heading_style))
#            
#            details_data = [
#                ["Paramètre", "Valeur"],
#                ["Fiche d'opération", sim.get("fiche_code") or "-"],
#                ["Secteur", sim.get("sector") or "-"],
#                ["Typologie", sim.get("typology") or "-"],
#                ["Type de bénéficiaire", sim.get("beneficiary_type") or "-"],
#            ]
#            
#            details_table = Table(details_data, colWidths=[6*cm, 10*cm])
#            details_table.setStyle(TableStyle([
#                ('BACKGROUND', (0, 0), (-1, 0), colors.HexColor("#5a7a91")),
#                ('TEXTCOLOR', (0, 0), (-1, 0), colors.white),
#                ('ALIGN', (0, 0), (0, -1), 'LEFT'),
#                ('ALIGN', (1, 0), (1, -1), 'LEFT'),
#                ('FONTNAME', (0, 0), (-1, 0), 'Helvetica-Bold'),
#                ('FONTSIZE', (0, 0), (-1, -1), 10),
#                ('BOTTOMPADDING', (0, 0), (-1, -1), 8),
#                ('TOPPADDING', (0, 0), (-1, -1), 8),
#                ('BACKGROUND', (0, 1), (0, -1), colors.HexColor("#f1f5f9")),
#                ('GRID', (0, 0), (-1, -1), 0.5, colors.HexColor("#cbd5e1")),
#            ]))
#            story.append(details_table)
#            story.append(Spacer(1, 20))
#            
#            # Localisation
#            story.append(Paragraph("Localisation et date", heading_style))
#            
#            location_data = [
#                ["Paramètre", "Valeur"],
#                ["Département", sim.get("department") or "-"],
#                ["Zone climatique", sim.get("zone_climatique") or "-"],
#                ["Date de signature", sim.get("date_signature") or "-"],
#            ]
#            
#            location_table = Table(location_data, colWidths=[6*cm, 10*cm])
#            location_table.setStyle(TableStyle([
#                ('BACKGROUND', (0, 0), (-1, 0), colors.HexColor("#5a7a91")),
#                ('TEXTCOLOR', (0, 0), (-1, 0), colors.white),
#                ('ALIGN', (0, 0), (0, -1), 'LEFT'),
#                ('ALIGN', (1, 0), (1, -1), 'LEFT'),
#                ('FONTNAME', (0, 0), (-1, 0), 'Helvetica-Bold'),
#                ('FONTSIZE', (0, 0), (-1, -1), 10),
#                ('BOTTOMPADDING', (0, 0), (-1, -1), 8),
#                ('TOPPADDING', (0, 0), (-1, -1), 8),
#                ('BACKGROUND', (0, 1), (0, -1), colors.HexColor("#f1f5f9")),
#                ('GRID', (0, 0), (-1, -1), 0.5, colors.HexColor("#cbd5e1")),
#            ]))
#            story.append(location_table)
#            story.append(Spacer(1, 20))
#            
#            # Note de bas de page
#            story.append(Spacer(1, 30))
#            footer_style = ParagraphStyle(
#                'Footer',
#                parent=styles['Normal'],
#                fontSize=8,
#                textColor=colors.HexColor("#718096"),
#                alignment=TA_CENTER
#            )
#            story.append(Paragraph(
#                "Ce document est une estimation indicative. Le montant réel de la prime CEE peut varier.",
#                footer_style
#            ))
#            story.append(Paragraph(
#                f"Document généré par RDE Consulting - {datetime.now().strftime('%d/%m/%Y %H:%M')}",
#                footer_style
#            ))
#            
#            # Construire le PDF
#            doc.build(story)
#            
#            # Récupérer les bytes du PDF
#            pdf_bytes = buffer.getvalue()
#            buffer.close()
#            
#            # Encoder en base64
#            pdf_base64 = base64.b64encode(pdf_bytes).decode('utf-8')
#            
#            print(f"✅ PDF généré pour simulation: {sim.get('name')}")
#            yield rx.toast.success("PDF généré !", duration=2000)
#            
#            # Télécharger
#            yield rx.download(
#                data=f"data:application/pdf;base64,{pdf_base64}",
#                filename=filename
#            )
#            
#        except ImportError as e:
#            print(f"❌ Module manquant: {e}")
#            yield rx.toast.error("Module PDF non disponible", duration=3000)
#        except Exception as e:
#            print(f"❌ Erreur export PDF: {e}")
#            yield rx.toast.error(f"Erreur: {str(e)[:50]}", duration=3000)


"""État du dashboard"""
import reflex as rx
from typing import List, Dict, Any, Optional


class DashboardState(rx.State):
    """État pour le tableau de bord."""
    
    simulations: List[Dict[str, Any]] = []
    is_loading: bool = False
    error_message: str = ""
    
    # Simulation sélectionnée pour visualisation/export
    selected_simulation_id: str = ""
    
    @rx.var
    def simulations_list(self) -> List[Dict[str, str]]:
        """Liste des simulations formatée pour l'affichage."""
        formatted = []
        for index, sim in enumerate(self.simulations, start=1):
            # Formater la date
            date_str = ""
            if sim.get("created_at"):
                try:
                    date_str = sim["created_at"][:10]  # YYYY-MM-DD
                    # Convertir en DD/MM/YYYY
                    parts = date_str.split("-")
                    if len(parts) == 3:
                        date_str = f"{parts[2]}/{parts[1]}/{parts[0]}"
                except:
                    date_str = sim.get("created_at", "")[:10]
            
            formatted.append({
                "id": sim.get("id", ""),
                "number": str(index),
                "name": sim.get("name", "Sans nom"),
                "fiche": sim.get("fiche_code", ""),
                "sector": sim.get("sector", ""),
                "department": sim.get("department", ""),
                "cumacs": f"{sim.get('result_cumacs', 0):,.0f}".replace(",", " "),
                "euros": f"{sim.get('result_euros', 0):,.2f} €".replace(",", " "),
                "date": date_str,
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
        total = sum(sim.get("result_euros", 0) or 0 for sim in self.simulations)
        return f"{total:,.2f} €".replace(",", " ")
    
    @rx.var
    def total_cumacs_str(self) -> str:
        """Total des cumacs."""
        total = sum(sim.get("result_cumacs", 0) or 0 for sim in self.simulations)
        return f"{total:,.0f} kWh".replace(",", " ")
    
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
    
    @rx.event
    async def load_simulations(self):
        """Charge les simulations de l'utilisateur connecté."""
        self.is_loading = True
        self.error_message = ""
        yield
        
        try:
            client = self._get_supabase_client()
            
            # Récupérer l'utilisateur connecté
            user_id = None
            try:
                from .auth_state import AuthState
                auth_state = await self.get_state(AuthState)
                user_id = getattr(auth_state, 'user_id', None)
            except Exception as e:
                print(f"⚠️ Erreur récupération user_id: {e}")
            
            if client and user_id:
                response = client.table("simulations")\
                    .select("*")\
                    .eq("user_id", user_id)\
                    .order("created_at", desc=True)\
                    .limit(50)\
                    .execute()
                
                if response.data:
                    self.simulations = response.data
                    print(f"✅ {len(response.data)} simulations chargées")
                else:
                    self.simulations = []
            else:
                # Pas de données si pas connecté
                self.simulations = []
                print("⚠️ Pas de client Supabase ou user_id")
                
        except Exception as e:
            print(f"❌ Erreur chargement simulations: {e}")
            self.error_message = str(e)
            self.simulations = []
        
        self.is_loading = False
    
    def _get_simulation_by_id(self, simulation_id: str) -> Optional[Dict[str, Any]]:
        """Récupère une simulation par son ID."""
        for sim in self.simulations:
            if sim.get("id") == simulation_id:
                return sim
        return None
    
    @rx.event
    async def download_simulation_pdf(self, simulation_id: str):
        """Télécharge le PDF d'une simulation."""
        sim = self._get_simulation_by_id(simulation_id)
        
        if not sim:
            yield rx.toast.error("Simulation non trouvée")
            return
        
        try:
            from reportlab.lib.pagesizes import A4
            from reportlab.lib import colors
            from reportlab.lib.styles import getSampleStyleSheet, ParagraphStyle
            from reportlab.lib.units import cm
            from reportlab.platypus import SimpleDocTemplate, Paragraph, Spacer, Table, TableStyle
            from reportlab.lib.enums import TA_CENTER
            from datetime import datetime
            import io
            import base64
            
            # Générer le PDF en mémoire
            buffer = io.BytesIO()
            
            # Nom du fichier
            safe_name = "".join(c if c.isalnum() or c in (' ', '-', '_') else '_' for c in (sim.get("name") or "simulation"))[:30]
            safe_name = safe_name.replace(" ", "_")
            filename = f"simulation_{safe_name}.pdf"
            
            # Créer le document
            doc = SimpleDocTemplate(
                buffer,
                pagesize=A4,
                rightMargin=2*cm,
                leftMargin=2*cm,
                topMargin=2*cm,
                bottomMargin=2*cm
            )
            
            # Styles
            styles = getSampleStyleSheet()
            
            title_style = ParagraphStyle(
                'CustomTitle',
                parent=styles['Heading1'],
                fontSize=24,
                spaceAfter=30,
                alignment=TA_CENTER,
                textColor=colors.HexColor("#1a365d")
            )
            
            subtitle_style = ParagraphStyle(
                'CustomSubtitle',
                parent=styles['Normal'],
                fontSize=12,
                spaceAfter=20,
                alignment=TA_CENTER,
                textColor=colors.HexColor("#718096")
            )
            
            heading_style = ParagraphStyle(
                'CustomHeading',
                parent=styles['Heading2'],
                fontSize=14,
                spaceBefore=20,
                spaceAfter=10,
                textColor=colors.HexColor("#2d3748")
            )
            
            # Contenu du PDF
            story = []
            
            # En-tête
            story.append(Paragraph("Rapport de Simulation CEE", title_style))
            story.append(Paragraph(sim.get("name") or "Simulation", subtitle_style))
            story.append(Paragraph(f"Généré le {datetime.now().strftime('%d/%m/%Y à %H:%M')}", subtitle_style))
            story.append(Spacer(1, 20))
            
            # Résultats principaux
            story.append(Paragraph("Résultats de la simulation", heading_style))
            
            result_euros = sim.get("result_euros", 0) or 0
            result_cumacs = sim.get("result_cumacs", 0) or 0
            
            results_data = [
                ["Indicateur", "Valeur"],
                ["Prime CEE estimée", f"{result_euros:,.2f} €".replace(",", " ")],
                ["Volume CEE", f"{result_cumacs:,.0f} kWh cumac".replace(",", " ")],
            ]
            
            results_table = Table(results_data, colWidths=[8*cm, 8*cm])
            results_table.setStyle(TableStyle([
                ('BACKGROUND', (0, 0), (-1, 0), colors.HexColor("#22c55e")),
                ('TEXTCOLOR', (0, 0), (-1, 0), colors.white),
                ('ALIGN', (0, 0), (-1, -1), 'CENTER'),
                ('FONTNAME', (0, 0), (-1, 0), 'Helvetica-Bold'),
                ('FONTSIZE', (0, 0), (-1, 0), 12),
                ('BOTTOMPADDING', (0, 0), (-1, 0), 12),
                ('TOPPADDING', (0, 0), (-1, 0), 12),
                ('BACKGROUND', (0, 1), (-1, -1), colors.HexColor("#f0fdf4")),
                ('FONTSIZE', (0, 1), (-1, -1), 14),
                ('FONTNAME', (0, 1), (-1, -1), 'Helvetica-Bold'),
                ('BOTTOMPADDING', (0, 1), (-1, -1), 15),
                ('TOPPADDING', (0, 1), (-1, -1), 15),
                ('GRID', (0, 0), (-1, -1), 1, colors.HexColor("#86efac")),
            ]))
            story.append(results_table)
            story.append(Spacer(1, 20))
            
            # Détails de l'opération
            story.append(Paragraph("Détails de l'opération", heading_style))
            
            details_data = [
                ["Paramètre", "Valeur"],
                ["Fiche d'opération", sim.get("fiche_code") or "-"],
                ["Secteur", sim.get("sector") or "-"],
                ["Typologie", sim.get("typology") or "-"],
                ["Type de bénéficiaire", sim.get("beneficiary_type") or "-"],
            ]
            
            details_table = Table(details_data, colWidths=[6*cm, 10*cm])
            details_table.setStyle(TableStyle([
                ('BACKGROUND', (0, 0), (-1, 0), colors.HexColor("#5a7a91")),
                ('TEXTCOLOR', (0, 0), (-1, 0), colors.white),
                ('ALIGN', (0, 0), (0, -1), 'LEFT'),
                ('ALIGN', (1, 0), (1, -1), 'LEFT'),
                ('FONTNAME', (0, 0), (-1, 0), 'Helvetica-Bold'),
                ('FONTSIZE', (0, 0), (-1, -1), 10),
                ('BOTTOMPADDING', (0, 0), (-1, -1), 8),
                ('TOPPADDING', (0, 0), (-1, -1), 8),
                ('BACKGROUND', (0, 1), (0, -1), colors.HexColor("#f1f5f9")),
                ('GRID', (0, 0), (-1, -1), 0.5, colors.HexColor("#cbd5e1")),
            ]))
            story.append(details_table)
            story.append(Spacer(1, 20))
            
            # Localisation
            story.append(Paragraph("Localisation et date", heading_style))
            
            location_data = [
                ["Paramètre", "Valeur"],
                ["Département", sim.get("department") or "-"],
                ["Zone climatique", sim.get("zone_climatique") or "-"],
                ["Date de signature", sim.get("date_signature") or "-"],
            ]
            
            location_table = Table(location_data, colWidths=[6*cm, 10*cm])
            location_table.setStyle(TableStyle([
                ('BACKGROUND', (0, 0), (-1, 0), colors.HexColor("#5a7a91")),
                ('TEXTCOLOR', (0, 0), (-1, 0), colors.white),
                ('ALIGN', (0, 0), (0, -1), 'LEFT'),
                ('ALIGN', (1, 0), (1, -1), 'LEFT'),
                ('FONTNAME', (0, 0), (-1, 0), 'Helvetica-Bold'),
                ('FONTSIZE', (0, 0), (-1, -1), 10),
                ('BOTTOMPADDING', (0, 0), (-1, -1), 8),
                ('TOPPADDING', (0, 0), (-1, -1), 8),
                ('BACKGROUND', (0, 1), (0, -1), colors.HexColor("#f1f5f9")),
                ('GRID', (0, 0), (-1, -1), 0.5, colors.HexColor("#cbd5e1")),
            ]))
            story.append(location_table)
            story.append(Spacer(1, 20))
            
            # Note de bas de page
            story.append(Spacer(1, 30))
            footer_style = ParagraphStyle(
                'Footer',
                parent=styles['Normal'],
                fontSize=8,
                textColor=colors.HexColor("#718096"),
                alignment=TA_CENTER
            )
            story.append(Paragraph(
                "Ce document est une estimation indicative. Le montant réel de la prime CEE peut varier.",
                footer_style
            ))
            story.append(Paragraph(
                f"Document généré par RDE Consulting - {datetime.now().strftime('%d/%m/%Y %H:%M')}",
                footer_style
            ))
            
            # Construire le PDF
            doc.build(story)
            
            # Récupérer les bytes du PDF
            pdf_bytes = buffer.getvalue()
            buffer.close()
            
            # Encoder en base64
            pdf_base64 = base64.b64encode(pdf_bytes).decode('utf-8')
            
            print(f"✅ PDF généré pour simulation: {sim.get('name')}")
            yield rx.toast.success("PDF généré !", duration=2000)
            
            # Télécharger
            yield rx.download(
                data=f"data:application/pdf;base64,{pdf_base64}",
                filename=filename
            )
            
        except ImportError as e:
            print(f"❌ Module manquant: {e}")
            yield rx.toast.error("Module PDF non disponible", duration=3000)
        except Exception as e:
            print(f"❌ Erreur export PDF: {e}")
            yield rx.toast.error(f"Erreur: {str(e)[:50]}", duration=3000)