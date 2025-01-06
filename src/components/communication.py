import streamlit as st
import plotly.express as px
import pandas as pd
import json
import os
from datetime import datetime

class CommunicationDashboard:
   def __init__(self):
       self.feedback_data = []
       self._initialize_data()
       # Définir le chemin du dossier de stockage
       self.storage_path = os.path.join(os.path.dirname(__file__), '..', 'data', 'generated_content')
       os.makedirs(self.storage_path, exist_ok=True)
       os.makedirs(os.path.join(self.storage_path, 'campaigns'), exist_ok=True)
       os.makedirs(os.path.join(self.storage_path, 'content'), exist_ok=True)
       os.makedirs(os.path.join(self.storage_path, 'feedback'), exist_ok=True)

   def _initialize_data(self):
       self.communication_stats = {
           "Engagement": {"value": "24%", "delta": "+2.3%"},
           "Réponses": {"value": "89%", "delta": "+5%"},
           "Portée": {"value": "45K", "delta": "+1.2K"},
           "Satisfaction": {"value": "4.2/5", "delta": "+0.3"}
       }

   def show_communication(self):
       st.header("Communication et Médias")
       
       tab1, tab2, tab3, tab4 = st.tabs([
           "Vue d'ensemble",
           "Campagnes",
           "Contenu",
           "Feedback"
       ])
       
       with tab1:
           self._show_overview()
       with tab2:
           self._show_campaigns()
       with tab3:
           self._show_content_management()
       with tab4:
           self._show_feedback()

   def _show_overview(self):
       st.subheader("Statistiques Générales")
       
       cols = st.columns(4)
       for i, (metric, data) in enumerate(self.communication_stats.items()):
           with cols[i]:
               st.metric(label=metric, value=data["value"], delta=data["delta"])

       engagement_data = pd.DataFrame({
           'Date': pd.date_range('2024-01-01', periods=12, freq='M'),
           'Facebook': [45, 48, 52, 55, 58, 62, 65, 68, 70, 72, 75, 78],
           'Instagram': [30, 32, 35, 38, 40, 42, 45, 48, 50, 52, 55, 58],
           'Application': [20, 22, 25, 28, 30, 32, 35, 38, 40, 42, 45, 48]
       })

       fig = px.line(
           engagement_data.melt(id_vars=['Date'], var_name='Canal', value_name='Engagement'),
           x='Date', y='Engagement', color='Canal',
           title="Engagement par Canal de Communication"
       )
       st.plotly_chart(fig, use_container_width=True)

   def _show_campaigns(self):
       st.subheader("Gestion des Campagnes")
       
       with st.expander("Nouvelle Campagne"):
           col1, col2 = st.columns(2)
           with col1:
               campaign_name = st.text_input("Nom de la campagne")
               target_audience = st.multiselect("Public cible", ["Résidents", "Touristes", "Commerçants"])
           with col2:
               start_date = st.date_input("Date de début")
               end_date = st.date_input("Date de fin")
               description = st.text_area("Description", height=100)
           
           if st.button("Créer la campagne"):
               campaign_data = {
                   "nom": campaign_name,
                   "public_cible": target_audience,
                   "debut": start_date.strftime("%Y-%m-%d"),
                   "fin": end_date.strftime("%Y-%m-%d"),
                   "description": description,
                   "status": "En cours",
                   "creation_date": datetime.now().strftime("%Y-%m-%d %H:%M:%S")
               }
               self._save_campaign(campaign_data)
               st.success("Campagne créée avec succès!")

       # Afficher les campagnes existantes
       st.subheader("Campagnes existantes")
       campaigns = self._load_campaigns()
       if campaigns:
           for campaign in campaigns:
               with st.expander(f"{campaign['nom']} ({campaign['status']})"):
                   st.write(f"**Public cible:** {', '.join(campaign['public_cible'])}")
                   st.write(f"**Période:** Du {campaign['debut']} au {campaign['fin']}")
                   st.write(f"**Description:** {campaign['description']}")
                   st.write(f"**Créé le:** {campaign['creation_date']}")

   def _show_content_management(self):
       st.subheader("Gestion du Contenu")
       
       content_type = st.selectbox("Type de contenu", ["Post Social Media", "Newsletter", "Communiqué"])
       
       col1, col2 = st.columns(2)
       with col1:
           title = st.text_input("Titre")
           content = st.text_area("Contenu", height=150)
           channels = st.multiselect("Canaux de diffusion", ["Facebook", "Instagram", "Application", "Email"])
       with col2:
           tone = st.selectbox("Ton", ["Formel", "Neutre", "Décontracté"])
           target = st.multiselect("Cible", ["Tous", "Résidents", "Touristes", "Commerçants"])
           uploaded_file = st.file_uploader("Média")

       if st.button("Générer et sauvegarder"):
           if content:
               content_data = {
                   "type": content_type,
                   "titre": title,
                   "contenu": content,
                   "canaux": channels,
                   "ton": tone,
                   "cible": target,
                   "media": uploaded_file.name if uploaded_file else None,
                   "creation_date": datetime.now().strftime("%Y-%m-%d %H:%M:%S")
               }
               self._save_content(content_data)
               st.success("Contenu sauvegardé avec succès!")

       # Afficher les contenus existants
       st.subheader("Contenus existants")
       contents = self._load_contents()
       if contents:
           for content in contents:
               with st.expander(f"{content['titre']} ({content['type']})"):
                   st.write(f"**Canaux:** {', '.join(content['canaux'])}")
                   st.write(f"**Ton:** {content['ton']}")
                   st.write(f"**Cible:** {', '.join(content['cible'])}")
                   st.write(f"**Contenu:**\n{content['contenu']}")
                   st.write(f"**Créé le:** {content['creation_date']}")

   def _show_feedback(self):
       st.subheader("Retours et Analyses")
       
       with st.form("feedback_form"):
           satisfaction = st.slider("Niveau de satisfaction", 1, 5, 3)
           feedback_type = st.selectbox("Type de retour", ["Général", "Fonctionnalité", "Bug", "Suggestion"])
           comments = st.text_area("Commentaires")
           
           if st.form_submit_button("Envoyer"):
               feedback_data = {
                   "satisfaction": satisfaction,
                   "type": feedback_type,
                   "commentaires": comments,
                   "date": datetime.now().strftime("%Y-%m-%d %H:%M:%S")
               }
               self._save_feedback(feedback_data)
               st.success("Feedback enregistré avec succès!")

       # Afficher les retours existants
       st.subheader("Retours précédents")
       feedbacks = self._load_feedbacks()
       if feedbacks:
           for feedback in feedbacks:
               with st.expander(f"Retour du {feedback['date']} - {feedback['type']}"):
                   st.write(f"**Satisfaction:** {feedback['satisfaction']}/5")
                   st.write(f"**Commentaires:** {feedback['commentaires']}")

   def _save_campaign(self, campaign_data):
       filename = f"campaign_{datetime.now().strftime('%Y%m%d_%H%M%S')}.json"
       filepath = os.path.join(self.storage_path, 'campaigns', filename)
       with open(filepath, 'w', encoding='utf-8') as f:
           json.dump(campaign_data, f, ensure_ascii=False, indent=4)

   def _save_content(self, content_data):
       filename = f"content_{datetime.now().strftime('%Y%m%d_%H%M%S')}.json"
       filepath = os.path.join(self.storage_path, 'content', filename)
       with open(filepath, 'w', encoding='utf-8') as f:
           json.dump(content_data, f, ensure_ascii=False, indent=4)

   def _save_feedback(self, feedback_data):
       filename = f"feedback_{datetime.now().strftime('%Y%m%d_%H%M%S')}.json"
       filepath = os.path.join(self.storage_path, 'feedback', filename)
       with open(filepath, 'w', encoding='utf-8') as f:
           json.dump(feedback_data, f, ensure_ascii=False, indent=4)

   def _load_campaigns(self):
       campaigns = []
       campaign_dir = os.path.join(self.storage_path, 'campaigns')
       for filename in os.listdir(campaign_dir):
           if filename.endswith('.json'):
               with open(os.path.join(campaign_dir, filename), 'r', encoding='utf-8') as f:
                   campaigns.append(json.load(f))
       return sorted(campaigns, key=lambda x: x['creation_date'], reverse=True)

   def _load_contents(self):
       contents = []
       content_dir = os.path.join(self.storage_path, 'content')
       for filename in os.listdir(content_dir):
           if filename.endswith('.json'):
               with open(os.path.join(content_dir, filename), 'r', encoding='utf-8') as f:
                   contents.append(json.load(f))
       return sorted(contents, key=lambda x: x['creation_date'], reverse=True)

   def _load_feedbacks(self):
       feedbacks = []
       feedback_dir = os.path.join(self.storage_path, 'feedback')
       for filename in os.listdir(feedback_dir):
           if filename.endswith('.json'):
               with open(os.path.join(feedback_dir, filename), 'r', encoding='utf-8') as f:
                   feedbacks.append(json.load(f))
       return sorted(feedbacks, key=lambda x: x['date'], reverse=True)

def main():
   dashboard = CommunicationDashboard()
   dashboard.show_communication()

if __name__ == "__main__":
   main()