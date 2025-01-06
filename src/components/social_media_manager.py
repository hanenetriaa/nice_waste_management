import streamlit as st
from datetime import datetime, timedelta

class SocialMediaManager:
    def __init__(self):
        self.platforms = ["Facebook", "Instagram", "Twitter", "LinkedIn"]
        self.scheduled_posts = []

    def show_social_media_dashboard(self):
        st.header("Gestion des Réseaux Sociaux")
        
        tabs = st.tabs(["Publications", "Planification", "Analytics"])
        
        with tabs[0]:
            self.show_posts_manager()
        with tabs[1]:
            self.show_scheduler()
        with tabs[2]:
            self.show_social_analytics()

    def show_posts_manager(self):
        st.subheader("Gestionnaire de Publications")
        
        with st.form("new_post"):
            platform = st.multiselect(
                "Plateformes",
                self.platforms
            )
            
            content = st.text_area(
                "Contenu du post",
                height=150
            )
            
            col1, col2 = st.columns(2)
            with col1:
                include_image = st.checkbox("Inclure une image")
                if include_image:
                    image = st.file_uploader("Choisir une image")
            
            with col2:
                schedule_post = st.checkbox("Planifier")
                if schedule_post:
                    post_date = st.date_input("Date de publication")
                    post_time = st.time_input("Heure de publication")

            if st.form_submit_button("Programmer"):
                self.schedule_post(platform, content, post_date, post_time)
                st.success("Publication programmée!")

    def schedule_post(self, platforms, content, date, time):
        self.scheduled_posts.append({
            "platforms": platforms,
            "content": content,
            "datetime": datetime.combine(date, time),
            "status": "Scheduled"
        })

    def show_scheduler(self):
        st.subheader("Publications Programmées")
        
        if not self.scheduled_posts:
            st.info("Aucune publication programmée")
            return
            
        for post in self.scheduled_posts:
            with st.expander(f"Post prévu pour le {post['datetime'].strftime('%d/%m/%Y %H:%M')}"):
                st.write("**Plateformes:** " + ", ".join(post['platforms']))
                st.write("**Contenu:**")
                st.write(post['content'])
                st.write("**Status:** " + post['status'])

    def show_social_analytics(self):
        st.subheader("Analyse des Performances")
        
        platform = st.selectbox(
            "Plateforme",
            self.platforms
        )
        
        period = st.selectbox(
            "Période",
            ["7 derniers jours", "30 derniers jours", "3 derniers mois"]
        )
        
        # Exemple de métriques
        col1, col2, col3 = st.columns(3)
        with col1:
            st.metric("Engagement", "2.4K", "12%")
        with col2:
            st.metric("Portée", "15K", "8%")
        with col3:
            st.metric("Clics", "856", "-3%")