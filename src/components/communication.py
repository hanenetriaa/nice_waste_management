# src/components/communication.py
import streamlit as st
from src.data.communication_data import get_key_audiences

def show_communication():
    st.title("Plan de Communication - Gestion des Déchets")
    
    # Afficher les Audiences Clés, Messages et Canaux
    st.header("Audiences Clés, Messages et Canaux")
    audiences = get_key_audiences()
    
    for audience, details in audiences.items():
        st.subheader(audience)
        st.write(f"**Message**: {details['Message']}")
        st.write(f"**Canaux**: {details['Canaux']}")
        
        # Vérifier si la clé "Exemples" existe dans les détails de l'audience
        if "Exemples" in details:
            st.write("**Exemples de Communication**:")
            for example in details["Exemples"]:
                st.write(f"- {example}")
        else:
            st.write("Aucun exemple spécifique de communication n'est défini pour cette audience.")
        
        # Afficher un exemple visuel (image, carte, post, etc.)
        if audience == "Mairie de Nice":
            st.image("https://via.placeholder.com/600x400?text=Affiche+Rapport+Stratégique", caption="Exemple de rapport pour la Mairie")
            st.write("Exemple d'affiche pour la Mairie expliquant les bénéfices écologiques du recyclage.")
        
        elif audience == "Citoyens de Nice":
            st.image("https://via.placeholder.com/600x400?text=Post+Facebook+Recyclage", caption="Exemple de post sur les réseaux sociaux")
            st.write("Exemple de post sur Facebook sensibilisant au recyclage.")
            st.markdown("[Cliquez ici pour voir l'exemple de post Facebook](https://www.facebook.com/)")

        elif audience == "Associations de Quartier":
            st.image("https://via.placeholder.com/600x400?text=Flyer+Recyclage+Quartier", caption="Exemple de flyer pour les Associations de Quartier")
            st.write("Flyer distribué aux associations pour promouvoir le tri sélectif.")
        
        elif audience == "Chauffeurs de Collecte et Agents de Tri":
            st.image("https://via.placeholder.com/600x400?text=Formation+Chauffeurs", caption="Exemple de formation pour chauffeurs")
            st.write("Exemple d'une formation en ligne pour les chauffeurs sur les nouveaux outils de collecte.")

        elif audience == "Touristes":
            st.image("https://via.placeholder.com/600x400?text=Brochure+Tourisme+Recyclage", caption="Exemple de brochure pour les touristes")
            st.write("Brochure multilingue distribuée dans les hôtels expliquant le tri sélectif à Nice.")
        
        # Ajout d'un formulaire pour le feedback des citoyens (interactif)
        if audience == "Citoyens de Nice":
            st.subheader("Donnez votre avis sur la campagne de recyclage")
            feedback = st.text_area("Quels sont vos retours sur la campagne de recyclage de Nice ?", "Écrivez ici...")
            if st.button("Envoyer votre feedback"):
                st.success("Merci pour votre retour !")
                
        # Ajouter un formulaire de réclamation pour les chauffeurs et agents
        if audience == "Chauffeurs de Collecte et Agents de Tri":
            st.subheader("Formulaire de Réclamation pour les Agents de Tri")
            name = st.text_input("Nom")
            issue = st.text_area("Décrivez le problème rencontré")
            if st.button("Soumettre la réclamation"):
                st.success("Réclamation soumise avec succès !")
        
        st.write("---")
