import streamlit as st 

def complaint_form():
    st.header("Formulaire de Réclamation - Gestion des Déchets")

    st.subheader("Détails de la réclamation")
    name = st.text_input("Votre nom")
    email = st.text_input("Votre email")
    complaint = st.text_area("Veuillez décrire votre réclamation en détail")

    if st.button("Soumettre Réclamation"):
        if name and email and complaint:
            st.success("Votre réclamation a été soumise avec succès. Nous vous contacterons sous 48 heures.")
        else:
            st.warning("Veuillez remplir tous les champs avant de soumettre.")
