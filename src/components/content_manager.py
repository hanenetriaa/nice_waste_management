import streamlit as st
import pandas as pd
from datetime import datetime
import plotly.express as px
from src.utils.image_generator import ImageGenerator

class ContentManager:
    def __init__(self):
        self.image_generator = ImageGenerator()
        self.content_library = []

    def show_content_dashboard(self):
        st.subheader("Gestionnaire de Contenu")

        tabs = st.tabs(["Création", "Bibliothèque", "Analytics"])

        with tabs[0]:
            self.show_content_creator()
        with tabs[1]:
            self.show_content_library()
        with tabs[2]:
            self.show_content_analytics()

    def show_content_creator(self):
        st.write("### Créer Nouveau Contenu")
        
        content_type = st.selectbox(
            "Type de contenu",
            ["Post Réseaux Sociaux", "Email", "Communiqué", "Affiche", "Guide"]
        )

        col1, col2 = st.columns(2)
        with col1:
            title = st.text_input("Titre")
            target = st.multiselect(
                "Public cible",
                ["Résidents", "Touristes", "Commerçants", "Jeunes", "Seniors"]
            )
            channels = st.multiselect(
                "Canaux de diffusion",
                ["Facebook", "Instagram", "Email", "Site web", "Application"]
            )

        with col2:
            tone = st.select_slider(
                "Ton",
                options=["Formel", "Professionnel", "Neutre", "Décontracté", "Engageant"]
            )
            scheduled_date = st.date_input("Date de publication")
            language = st.multiselect("Langues", ["Français", "English", "Italiano"])

        content = st.text_area("Contenu", height=200)

        if st.button("Générer une image"):
            prompt = f"Communication visuelle sur la gestion des déchets à Nice, style {tone.lower()}, pour {', '.join(target)}"
            image_url = self.image_generator.generate_image(prompt)
            st.image(image_url)

        if st.button("Sauvegarder"):
            self.content_library.append({
                "type": content_type,
                "title": title,
                "target": target,
                "channels": channels,
                "tone": tone,
                "date": scheduled_date,
                "content": content,
                "languages": language,
                "created_at": datetime.now()
            })
            st.success("Contenu sauvegardé!")

    def show_content_library(self):
        if not self.content_library:
            st.info("La bibliothèque est vide")
            return

        st.write("### Bibliothèque de Contenu")

        filter_type = st.multiselect(
            "Filtrer par type",
            list(set(c["type"] for c in self.content_library))
        )

        filtered_content = self.content_library
        if filter_type:
            filtered_content = [c for c in self.content_library if c["type"] in filter_type]

        for content in filtered_content:
            with st.expander(f"{content['title']} ({content['type']})"):
                col1, col2 = st.columns(2)
                with col1:
                    st.write("**Public:** " + ", ".join(content['target']))
                    st.write("**Canaux:** " + ", ".join(content['channels']))
                    st.write("**Date:** " + content['date'].strftime("%d/%m/%Y"))
                with col2:
                    st.write("**Ton:** " + content['tone'])
                    st.write("**Langues:** " + ", ".join(content['languages']))
                
                st.markdown("---")
                st.write(content['content'])

    def show_content_analytics(self):
        if not self.content_library:
            st.info("Pas de données à analyser")
            return

        st.write("### Analyse du Contenu")

        # Distribution par type
        type_dist = pd.DataFrame([
            {"Type": c["type"], "Count": 1} 
            for c in self.content_library
        ]).groupby("Type").sum().reset_index()

        fig1 = px.pie(
            type_dist,
            values='Count',
            names='Type',
            title='Distribution par Type de Contenu'
        )
        st.plotly_chart(fig1)

        # Timeline de publication
        timeline_data = pd.DataFrame([
            {
                "Date": c["date"],
                "Type": c["type"],
                "Title": c["title"]
            }
            for c in self.content_library
        ])

        fig2 = px.timeline(
            timeline_data,
            x_start="Date",
            x_end="Date",
            y="Type",
            color="Type",
            hover_data=["Title"]
        )
        st.plotly_chart(fig2)