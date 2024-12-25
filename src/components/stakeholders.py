import streamlit as st
import pandas as pd
from ..data.stakeholders_data import STAKEHOLDERS_DATA, PHASES_PROJET

def show_stakeholders():
    st.header("Parties Prenantes du Projet")

    # Conversion des données des parties prenantes en DataFrame pour affichage
    df_stakeholders = pd.DataFrame(STAKEHOLDERS_DATA)

    # Affichage des données sous forme de tableau
    st.subheader("Données des Parties Prenantes")
    st.dataframe(df_stakeholders)

    # Graphique sur le niveau d'influence
    st.subheader("Niveau d'Influence par Groupe")
    influence_chart = df_stakeholders.groupby("Stakeholder Principal")["Niveau_Influence"].mean().sort_values()
    st.bar_chart(influence_chart)

    # Affichage des phases du projet
    st.subheader("Phases du Projet")
    for phase, details in PHASES_PROJET.items():
        with st.expander(phase):
            st.write(f"**Durée :** {details['Durée']}")
            st.write("**Objectifs :**")
            st.write("- " + "\n- ".join(details["Objectifs"]))
            st.write("**Livrables :**")
            st.write("- " + "\n- ".join(details["Livrables"]))

    # Sélection de la phase pour filtrer les données
    st.subheader("Données par Phase")
    phase_selected = st.selectbox(
        "Sélectionnez une phase du projet",
        list(PHASES_PROJET.keys())
    )

    # Filtrage et affichage des données pour la phase sélectionnée
    if phase_selected:
        phase_index = list(PHASES_PROJET.keys()).index(phase_selected)
        phase_column = df_stakeholders.columns[phase_index + 2]  # Les phases commencent après "Sous-Groupe"
        phase_data = df_stakeholders[["Stakeholder Principal", "Sous-Groupe", phase_column]]
        st.dataframe(phase_data)

    st.success("Analyse des parties prenantes terminée.")
