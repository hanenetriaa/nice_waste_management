# src/components/feedback_form.py
import streamlit as st

def feedback_form():
    st.header("Formulaire de Feedback - Gestion des Déchets")

    st.subheader("Vos impressions sur le projet")
    feedback = st.text_area("Merci de nous faire part de vos retours concernant le tri sélectif et la gestion des déchets dans votre quartier.")
    
    if st.button("Envoyer Feedback"):
        if feedback:
            st.success("Merci pour votre retour ! Nous l'examinerons et apporterons les améliorations nécessaires.")
        else:
            st.warning("Veuillez fournir vos commentaires avant d'envoyer.")
