import streamlit as st
from src.components import dashboard, maps, stakeholders, risks, sources, quartiers, communication, feedback_form, complaint_form, preventive_analysis_form
from src.utils.config import APP_CONFIG

def main():
    st.set_page_config(
        page_title=APP_CONFIG["title"],
        page_icon="♻️",
        layout="wide"
    )
    
    st.title(APP_CONFIG["title"])

    # Menu principal avec selectbox
    main_menu = st.sidebar.selectbox("Menu Principal", ["Dashboard", "Gestion des Déchets", "Documentation"])

    if main_menu == "Dashboard":
        dashboard.show_dashboard()

    elif main_menu == "Gestion des Déchets":
        # Sous-menu Gestion des Déchets avec selectbox
        sub_menu = st.sidebar.selectbox("Gestion des Déchets", ["Études", "Actions"])
        
        if sub_menu == "Études":
            # Sous-menu Études avec selectbox
            study_menu = st.sidebar.selectbox("Études", ["Stakeholders", "Analyse des Risques", "Analyse par Quartier", "Cartographie"])
            
            if study_menu == "Stakeholders":
                stakeholders.show_stakeholders()
            elif study_menu == "Analyse des Risques":
                risks.show_risk_analysis()
            elif study_menu == "Analyse par Quartier":
                quartiers.show_quartiers()
            elif study_menu == "Cartographie":
                maps.show_maps()

        elif sub_menu == "Actions":
            # Sous-menu Actions avec selectbox
            action_menu = st.sidebar.selectbox("Actions", ["Communication", "Formulaires de Feedback", "Formulaires de Réclamation", "Analyse Préventive"])
            
            if action_menu == "Communication":
                communication.show_communication()
            elif action_menu == "Formulaires de Feedback":
                feedback_form.feedback_form()
            elif action_menu == "Formulaires de Réclamation":
                complaint_form.complaint_form()
            elif action_menu == "Analyse Préventive":
                preventive_analysis_form.preventive_analysis_form()

    elif main_menu == "Documentation":
        # Sous-menu Documentation avec selectbox
        doc_menu = st.sidebar.selectbox("Documentation", ["Sources"])
        
        if doc_menu == "Sources":
            sources.show_sources()

if __name__ == "__main__":
    main()
