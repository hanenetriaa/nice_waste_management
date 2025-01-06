import streamlit as st
from datetime import datetime

class SocialMediaManager:
    def __init__(self):
        self.platforms = ["Facebook", "Instagram", "Twitter", "LinkedIn"]
        self.scheduled_posts = []

    def show_social_media_dashboard(self):
        st.header("Gestion des Réseaux Sociaux")
        
        # Planification des posts
        with st.expander("Planifier un nouveau post"):
            platforms = st.multiselect(
                "Plateformes",
                self.platforms
            )
            
            post_content = st.text_area("Contenu du post")
            
            col1, col2 = st.columns(2)
            with col1:
                post_date = st.date_input("Date de publication")
            with col2:
                post_time = st.time_input("Heure")

            if st.button("Programmer"):
                self.schedule_post(platforms, post_content, post_date, post_time)
                st.success("Post programmé avec succès!")

        # Posts programmés
        st.subheader("Posts Programmés")
        if not self.scheduled_posts:
            st.info("Aucun post programmé")
        else:
            for post in self.scheduled_posts:
                with st.expander(f"Post prévu le {post['datetime'].strftime('%d/%m/%Y %H:%M')}"):
                    st.write("Plateformes:", ", ".join(post['platforms']))
                    st.write("Contenu:", post['content'])

    def schedule_post(self, platforms, content, date, time):
        self.scheduled_posts.append({
            "platforms": platforms,
            "content": content,
            "datetime": datetime.combine(date, time),
            "status": "Programmé"
        })