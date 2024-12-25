# src/components/preventive_analysis_form.py
import streamlit as st

def preventive_analysis_form():
    st.header("Analyse Préventive - Gestion des Déchets")

    st.subheader("Évaluation du service de collecte")
    rating = st.slider("Évaluez la qualité de la collecte des déchets", 1, 5, 3)
    suggestions = st.text_area("Avez-vous des suggestions pour améliorer le service ?")

    if st.button("Soumettre Évaluation"):
        st.success(f"Merci pour votre évaluation ! Votre note : {rating}/5")
        if suggestions:
            st.write("Vos suggestions : ", suggestions)
