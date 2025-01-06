import streamlit as st
from src.components import (
    dashboard,
    maps,
    stakeholders,
    risks,
    sources,
    quartiers
)
from src.components.communication import CommunicationDashboard
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
            action_menu = st.sidebar.selectbox(
                "Actions",
                ["Communication"]
            )

            if action_menu == "Communication":
                communication_dashboard = CommunicationDashboard()
                communication_dashboard.show_communication()

    elif main_menu == "Documentation":
        doc_menu = st.sidebar.selectbox(
            "Documentation",
            ["Sources"]
        )

        if doc_menu == "Sources":
            sources.show_sources()

if __name__ == "__main__":
    main()