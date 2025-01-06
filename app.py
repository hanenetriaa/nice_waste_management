import streamlit as st
import nltk
nltk.download('punkt')
from src.components import (
    dashboard,
    maps,
    stakeholders,
    risks,
    sources,
    quartiers
)
from src.components.communication import CommunicationDashboard
from src.components.content_manager import ContentManager
from src.components.campaign_manager import CampaignManager
from src.components.performance_analyzer import PerformanceAnalyzer
from src.integrations.social_media_manager import SocialMediaManager
from src.utils.config import APP_CONFIG

def main():
    st.set_page_config(
        page_title=APP_CONFIG["title"],
        page_icon="♻️",
        layout="wide"
    )
    
    st.title(APP_CONFIG["title"])

    # Menu principal
    main_menu = st.sidebar.selectbox(
        "Menu Principal",
        ["Dashboard", "Gestion des Déchets", "Documentation"]
    )

    if main_menu == "Dashboard":
        dashboard.show_dashboard()
        
    elif main_menu == "Gestion des Déchets":
        sub_menu = st.sidebar.selectbox(
            "Gestion des Déchets",
            ["Études", "Actions"]
        )

        if sub_menu == "Études":
            study_menu = st.sidebar.selectbox(
                "Études",
                ["Stakeholders", "Analyse des Risques", "Analyse par Quartier", "Cartographie"]
            )

            if study_menu == "Stakeholders":
                stakeholders.show_stakeholders()
            elif study_menu == "Analyse des Risques":
                risks.show_risk_analysis()
            elif study_menu == "Analyse par Quartier":
                quartiers.show_quartiers()
            elif study_menu == "Cartographie":
                maps.show_maps()
                
        elif sub_menu == "Actions":
            if st.sidebar.selectbox("Actions", ["Communication"]) == "Communication":
                comm_sub_menu = st.sidebar.selectbox(
                    "Options Communication",
                    [
                        "Vue d'ensemble",
                        "Gestion des Campagnes", 
                        "Gestion de Contenu",
                        "Réseaux Sociaux",
                        "Analyses de Performance"
                    ]
                )

                if comm_sub_menu == "Vue d'ensemble":
                    comm_dashboard = CommunicationDashboard()
                    comm_dashboard.show_communication()
                elif comm_sub_menu == "Gestion des Campagnes":
                    campaign_mgr = CampaignManager()
                    campaign_mgr.show_campaign_dashboard()
                elif comm_sub_menu == "Gestion de Contenu":
                    content_mgr = ContentManager()
                    content_mgr.show_content_dashboard()
                elif comm_sub_menu == "Réseaux Sociaux":
                    social_mgr = SocialMediaManager()
                    social_mgr.show_social_media_dashboard()
                elif comm_sub_menu == "Analyses de Performance":
                    perf_analyzer = PerformanceAnalyzer()
                    perf_analyzer.show_performance_dashboard()

    elif main_menu == "Documentation":
        doc_menu = st.sidebar.selectbox(
            "Documentation",
            ["Sources"]
        )

        if doc_menu == "Sources":
            sources.show_sources()

if __name__ == "__main__":
    main()