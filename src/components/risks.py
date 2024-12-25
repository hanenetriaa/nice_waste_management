import streamlit as st
import pandas as pd
import plotly.express as px
from ..data.risks_data import RISKS_DATA

def show_risk_analysis():
    st.header("Analyse des Risques")

    # Conversion des données des risques en DataFrame pour affichage
    df_risks = pd.DataFrame(RISKS_DATA)

    # Affichage du tableau des risques
    st.subheader("Tableau des Risques")
    st.dataframe(df_risks)

    # Visualisation : matrice des risques
    st.subheader("Matrice des Risques")
    fig = px.scatter(
        df_risks,
        x="Probabilité",
        y="Impact",
        size="Impact",
        color="Zone_Principale",
        hover_name="Risque",
        title="Matrice des Risques",
        labels={"Probabilité": "Probabilité", "Impact": "Impact"},
        size_max=30
    )
    fig.update_traces(marker=dict(line=dict(width=1, color='DarkSlateGrey')))
    st.plotly_chart(fig)

    # Statistiques clés
    st.subheader("Statistiques Clés")
    st.write(f"**Nombre total de risques identifiés :** {len(df_risks)}")
    avg_prob = df_risks['Probabilité'].mean()
    avg_impact = df_risks['Impact'].mean()
    st.metric(label="Probabilité Moyenne", value=f"{avg_prob:.2f}")
    st.metric(label="Impact Moyen", value=f"{avg_impact:.2f}")

    # Détails par zone principale
    st.subheader("Risques par Zone Principale")
    zone_selected = st.selectbox("Sélectionnez une zone principale :", df_risks["Zone_Principale"].unique())

    # Filtrer les données par zone sélectionnée
    filtered_data = df_risks[df_risks["Zone_Principale"] == zone_selected]
    st.write(f"**Risques dans la zone : {zone_selected}**")
    st.dataframe(filtered_data)

    st.success("Analyse des risques terminée.")
