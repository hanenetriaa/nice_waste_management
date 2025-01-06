import streamlit as st
import pandas as pd
from datetime import datetime, timedelta

class CampaignManager:
    def __init__(self):
        self.campaigns = []
        
    def show_campaign_dashboard(self):
        st.subheader("Gestionnaire de Campagnes")
        
        # Création de nouvelle campagne
        with st.expander("Créer une nouvelle campagne"):
            self.create_campaign_form()
            
        # Liste des campagnes actives
        self.show_active_campaigns()
        
        # Analyse des performances
        self.show_campaign_analytics()
    
    def create_campaign_form(self):
        with st.form("new_campaign"):
            name = st.text_input("Nom de la campagne")
            campaign_type = st.selectbox(
                "Type de campagne",
                ["Sensibilisation", "Événement", "Urgence", "Saisonnière"]
            )
            target_audience = st.multiselect(
                "Public cible",
                ["Résidents", "Touristes", "Commerçants", "Jeunes", "Seniors"]
            )
            start_date = st.date_input("Date de début")
            end_date = st.date_input("Date de fin")
            
            channels = st.multiselect(
                "Canaux de communication",
                ["Réseaux sociaux", "Email", "Application", "Affichage", "Presse"]
            )
            
            budget = st.number_input("Budget (€)", min_value=0)
            
            if st.form_submit_button("Créer la campagne"):
                self.campaigns.append({
                    "name": name,
                    "type": campaign_type,
                    "audience": target_audience,
                    "start_date": start_date,
                    "end_date": end_date,
                    "channels": channels,
                    "budget": budget,
                    "status": "Active"
                })
                st.success("Campagne créée avec succès !")
    
    def show_active_campaigns(self):
        if not self.campaigns:
            st.info("Aucune campagne active")
            return
            
        st.subheader("Campagnes en cours")
        
        for idx, campaign in enumerate(self.campaigns):
            with st.expander(f"{campaign['name']} ({campaign['type']})"):
                col1, col2 = st.columns(2)
                
                with col1:
                    st.write("**Public cible:**", ", ".join(campaign['audience']))
                    st.write("**Canaux:**", ", ".join(campaign['channels']))
                    st.write("**Budget:**", f"{campaign['budget']}€")
                
                with col2:
                    st.write("**Début:**", campaign['start_date'])
                    st.write("**Fin:**", campaign['end_date'])
                    st.write("**Statut:**", campaign['status'])
                
                if st.button(f"Terminer la campagne {idx}"):
                    campaign['status'] = "Terminée"
                    st.success("Statut mis à jour")
    
    def show_campaign_analytics(self):
        if not self.campaigns:
            return
            
        st.subheader("Analyse des Performances")
        
        # Données simulées pour l'exemple
        performance_data = pd.DataFrame({
            'Campagne': [c['name'] for c in self.campaigns],
            'Engagement': [round(random.uniform(1, 5), 2) for _ in self.campaigns],
            'ROI': [f"{round(random.uniform(0.5, 3), 2)}x" for _ in self.campaigns]
        })
        
        st.dataframe(performance_data)