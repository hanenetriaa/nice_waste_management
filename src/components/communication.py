import streamlit as st
import plotly.express as px
import pandas as pd
from textblob import TextBlob
import requests
import json
from datetime import datetime
from src.data.communication_data import get_key_audiences
from src.data.communication_examples import (
    COMMUNICATION_EXAMPLES, 
    GENERIC_STATS, 
    SEASONAL_MESSAGES
)

class CommunicationDashboard:
    def __init__(self):
        self.feedback_data = []
        
    def show_communication(self):
        st.title("Plan de Communication - Gestion des Déchets Nice")
        
        tabs = st.tabs([
            "Vue d'ensemble", 
            "Communication par Public", 
            "Analyses & Rapports",
            "Génération de Contenu"
        ])
        
        with tabs[0]:
            self.show_overview()
        with tabs[1]:
            self.show_audience_communication()
        with tabs[2]:
            self.show_analysis()
        with tabs[3]:
            self.show_content_generator()

    def show_overview(self):
        st.header("Vue d'ensemble de la Communication")
        
        # KPIs principaux
        cols = st.columns(4)
        with cols[0]:
            st.metric("Taux d'Engagement", "24%", "+2.3%", help="Mesure de l'interaction avec nos communications")
        with cols[1]:
            st.metric("Taux de Réponse", "89%", "+5%", help="Pourcentage de réponses aux communications")
        with cols[2]:
            st.metric("Portée", "45K", "+1.2K", help="Nombre de personnes touchées")
        with cols[3]:
            st.metric("Score de Satisfaction", "4.2/5", "+0.3", help="Évaluation moyenne des retours")

        # Graphique d'engagement
        st.subheader("Engagement par Canal")
        engagement_data = pd.DataFrame({
            'Date': pd.date_range(start='2024-01-01', periods=12, freq='M'),
            'Réseaux Sociaux': [45, 48, 52, 55, 58, 62, 65, 68, 70, 72, 75, 78],
            'Application': [30, 32, 35, 38, 40, 42, 45, 48, 50, 52, 55, 58],
            'Site Web': [20, 22, 25, 28, 30, 32, 35, 38, 40, 42, 45, 48]
        })
        
        fig = px.line(
            engagement_data.melt(
                id_vars=['Date'], 
                var_name='Canal', 
                value_name='Engagement'
            ),
            x='Date',
            y='Engagement',
            color='Canal',
            title="Évolution de l'Engagement par Canal"  # Utilisez des guillemets doubles pour le titre
        )
        fig.update_layout(
            xaxis_title="Date",
            yaxis_title="Taux d'Engagement (%)",
            hovermode='x unified'
        )
        st.plotly_chart(fig, use_container_width=True)

    def show_audience_communication(self):
        st.header("Communication par Public Cible")
        
        # Sélection du public
        audiences = get_key_audiences()
        selected_audience = st.selectbox(
            "Sélectionnez un public cible",
            list(audiences.keys())
        )

        if selected_audience in COMMUNICATION_EXAMPLES:
            examples = COMMUNICATION_EXAMPLES[selected_audience]["Examples"]
            
            # Affichage des exemples de communication
            for example in examples:
                with st.expander(f"{example['type']} - {example['title']}"):
                    st.markdown(example['content'])
                    
                    # Métriques de performance
                    cols = st.columns(3)
                    with cols[0]:
                        st.metric(
                            "Engagement",
                            "24%",
                            "+2.3%",
                            help="Taux d'interaction avec ce contenu"
                        )
                    with cols[1]:
                        st.metric(
                            "Portée",
                            "1.2K",
                            "+300",
                            help="Nombre de personnes touchées"
                        )
                    with cols[2]:
                        st.metric(
                            "Conversion",
                            "3.5%",
                            "+0.5%",
                            help="Taux de conversion des actions souhaitées"
                        )
                    
                    # Génération d'image si prompt existe
                    if 'image_prompt' in example:
                        with st.spinner("Génération de l'image..."):
                            image_url = self.generate_image(example['image_prompt'])
                            st.image(image_url, caption=example['title'])

    def show_content_generator(self):
        st.header("Générateur de Contenu")
        
        # Interface de génération
        col1, col2, col3 = st.columns(3)
        
        with col1:
            content_type = st.selectbox(
                "Type de contenu",
                ["Post Social Media", "Email Newsletter", "Communiqué de Presse"]
            )
        
        with col2:
            target_audience = st.selectbox(
                "Public cible",
                ["Citoyens", "Touristes", "Professionnels"]
            )
        
        with col3:
            tone = st.select_slider(
                "Ton de la communication",
                options=["Formel", "Neutre", "Décontracté"]
            )

        # Options supplémentaires selon le type de contenu
        if content_type == "Post Social Media":
            platform = st.selectbox(
                "Plateforme",
                ["Facebook", "Instagram", "Twitter", "LinkedIn"]
            )
            include_hashtags = st.checkbox("Inclure des hashtags", value=True)
            
        elif content_type == "Email Newsletter":
            include_images = st.checkbox("Inclure des visuels", value=True)
            include_cta = st.checkbox("Inclure un appel à l'action", value=True)
            
        elif content_type == "Communiqué de Presse":
            include_quotes = st.checkbox("Inclure des citations", value=True)
            include_stats = st.checkbox("Inclure des statistiques", value=True)

        # Bouton de génération
        if st.button("Générer le contenu", type="primary"):
            with st.spinner('Génération en cours...'):
                content = self.generate_content(
                    content_type, 
                    target_audience, 
                    tone,
                    locals()
                )
                
                # Affichage du contenu généré
                st.markdown("### Contenu Généré")
                st.markdown("---")
                st.markdown(f"""```{content}```""")
                
                # Options post-génération
                col1, col2 = st.columns(2)
                with col1:
                    if st.button("📋 Copier le contenu"):
                        st.code(content)
                        st.success("Contenu copié!")
                
                with col2:
                    if st.button("🖼️ Générer une image"):
                        image_prompt = f"Marketing image about waste management in Nice, {target_audience} focused, {tone.lower()} style"
                        st.image(self.generate_image(image_prompt))

    def generate_content(self, content_type, audience, tone, options=None):
        """Génère du contenu personnalisé selon les paramètres"""
        templates = {
            "Post Social Media": {
                "Citoyens": {
                    "Formel": """
                    📢 Information importante pour les Niçois

                    La Ville de Nice renforce son engagement environnemental avec de nouveaux points de collecte dans votre quartier.

                    ♻️ Objectifs :
                    • Optimisation du tri sélectif
                    • Réduction de notre empreinte carbone
                    • Amélioration du cadre de vie

                    📱 Téléchargez notre application pour localiser les points de collecte
                    🔗 nice.fr/tri-selectif

                    #NiceDurable #TriSelectif #EnvironnementNice
                    """,
                    "Neutre": """
                    🌿 Le tri sélectif à Nice, c'est simple !

                    Découvrez les nouveaux points de collecte près de chez vous.
                    Une question ? L'application mobile est là pour vous guider.

                    👉 Téléchargez-la maintenant : nice.fr/app

                    #Nice06 #TriSelectif
                    """,
                    "Décontracté": """
                    Hey Nice ! 🌟

                    On continue nos efforts pour une ville + propre ! 
                    Nouveau : points de collecte intelligents dans ton quartier 🎯

                    📱 Check l'app pour les trouver facilement
                    💪 Ensemble pour une Nice au top !

                    #NiceEnAction #TeamTri
                    """
                }
                # Ajoutez d'autres audiences...
            }
            # Ajoutez d'autres types de contenu...
        }

        try:
            content = templates[content_type][audience][tone]
            if options and options.get('include_hashtags', True):
                content += "\n#GestionDéchetsNice #VilleDeNice"
            return content
        except KeyError:
            return self._generate_fallback_content(content_type, audience, tone)

    def _generate_fallback_content(self, content_type, audience, tone):
        """Génère un contenu par défaut si le template n'existe pas"""
        current_date = datetime.now().strftime("%d/%m/%Y")
        return f"""
        === {content_type} ===
        Date: {current_date}
        Public cible: {audience}
        Ton: {tone}

        [Contenu personnalisé à venir]

        Pour plus d'informations sur la gestion des déchets à Nice :
        📱 Application mobile
        🌐 nice.fr/tri
        📞 0800 XXX XXX
        """

    def show_analysis(self):
        st.header("Analyse des Retours")
        
        # Données de sentiment
        sentiment_data = pd.DataFrame({
            'Sentiment': ['Positif', 'Neutre', 'Négatif'],
            'Pourcentage': [65, 25, 10]
        })
        
        # Graphique des sentiments
        fig = px.pie(
            sentiment_data,
            values='Pourcentage',
            names='Sentiment',
            title='Analyse des Sentiments',
            color='Sentiment',
            color_discrete_map={
                'Positif': '#2ecc71',
                'Neutre': '#3498db',
                'Négatif': '#e74c3c'
            }
        )
        st.plotly_chart(fig)
        
        # Formulaire de feedback
        st.subheader("Donnez votre avis")
        with st.form("feedback_form"):
            satisfaction = st.slider(
                "Niveau de satisfaction",
                1, 5, 3,
                help="1 = Très insatisfait, 5 = Très satisfait"
            )
            feedback = st.text_area(
                "Vos commentaires",
                placeholder="Partagez votre expérience..."
            )
            submitted = st.form_submit_button("Envoyer")
            
            if submitted:
                sentiment = self.analyze_sentiment(feedback)
                self.feedback_data.append({
                    'satisfaction': satisfaction,
                    'feedback': feedback,
                    'sentiment': sentiment,
                    'timestamp': datetime.now()
                })
                st.success("Merci pour votre retour !")
                self._update_analysis()

    def _update_analysis(self):
        """Met à jour les analyses basées sur les nouveaux feedbacks"""
        if not self.feedback_data:
            return
            
        # Calcul des moyennes et tendances
        recent_feedbacks = self.feedback_data[-10:]  # 10 derniers retours
        avg_satisfaction = sum(f['satisfaction'] for f in recent_feedbacks) / len(recent_feedbacks)
        sentiment_trend = sum(f['sentiment'] for f in recent_feedbacks) / len(recent_feedbacks)
        
        # Mise à jour des KPIs
        st.session_state['avg_satisfaction'] = avg_satisfaction
        st.session_state['sentiment_trend'] = sentiment_trend

    @staticmethod
    def analyze_sentiment(text):
        """Analyse le sentiment d'un texte"""
        if not text:
            return 0
        analysis = TextBlob(text)
        return analysis.sentiment.polarity

    @staticmethod
    def generate_image(prompt):
        """Génère une image basée sur un prompt"""
        # Placeholder - À remplacer par une vraie API d'IA
        encoded_prompt = prompt.replace(" ", "+")
        return f"https://placehold.co/600x400?text={encoded_prompt}"

def main():
    dashboard = CommunicationDashboard()
    dashboard.show_communication()

if __name__ == "__main__":
    main()