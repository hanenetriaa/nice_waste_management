import streamlit as st
from ..data.quartiers_data import QUARTIERS_DATA, STATISTIQUES_COMPLEMENTAIRES, CALENDRIER_COLLECTE

def show_quartiers():
    st.header("Analyse par Quartier")

    # Sélection d'un quartier
    quartiers = QUARTIERS_DATA["Nom"]
    quartier_selection = st.selectbox("Sélectionnez un quartier :", quartiers)

    # Recherche des données du quartier sélectionné
    index = quartiers.index(quartier_selection)
    quartier_data = {key: QUARTIERS_DATA[key][index] for key in QUARTIERS_DATA.keys()}

    # Affichage des informations générales
    st.subheader(f"Informations pour {quartier_selection}")
    st.write(f"**Population :** {quartier_data['Population']} habitants")
    st.write(f"**Points de collecte :** {quartier_data['Points_Collecte']}")
    st.write(f"**Type de zone :** {quartier_data['Type_Zone']}")
    st.write(f"**Densité :** {quartier_data['Densité']}")
    st.write(f"**Complexité de collecte :** {quartier_data['Complexité_Collecte']}")
    st.write(f"**Caractéristiques spécifiques :** {quartier_data['Caractéristiques_Spécifiques']}")
    st.write(f"**Défis principaux :** {quartier_data['Défis_Principaux']}")
    st.write(f"**Taux de tri :** {quartier_data['Taux_Tri']}%")
    st.write(f"**Volume moyen mensuel :** {quartier_data['Volume_Moyen_Mensuel']} tonnes")

    # Carte pour visualiser la position
    st.subheader("Localisation")
    st.map(
        data={
            "lat": [quartier_data["Latitude"]],
            "lon": [quartier_data["Longitude"]]
        },
        zoom=12
    )

    # Statistiques complémentaires
    st.subheader("Statistiques complémentaires")
    with st.expander("Équipements"):
        for key, value in STATISTIQUES_COMPLEMENTAIRES["Équipements"].items():
            st.write(f"- **{key.replace('_', ' ')} :** {value}")

    with st.expander("Performance Globale"):
        for key, value in STATISTIQUES_COMPLEMENTAIRES["Performance_Globale"].items():
            st.write(f"- **{key.replace('_', ' ')} :** {value}")

    # Calendrier de collecte
    st.subheader("Calendrier de collecte")
    for key, value in CALENDRIER_COLLECTE.items():
        st.write(f"- **{key.replace('_', ' ')} :** {value}")
