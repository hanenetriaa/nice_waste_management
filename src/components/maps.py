# src/components/maps.py
import streamlit as st
import plotly.express as px
import pandas as pd
from ..data.quartiers_data import QUARTIERS_DATA

def show_maps():
    st.header("Cartographie des Quartiers")
    
    df = pd.DataFrame(QUARTIERS_DATA)
    
    # Filtres
    densite = st.multiselect(
        "Filtrer par densité",
        df["Densité"].unique(),
        default=df["Densité"].unique()
    )
    
    # Filtrage des données
    df_filtered = df[df["Densité"].isin(densite)]
    
    # Carte
    show_map(df_filtered)

def show_map(df):
    fig = px.scatter_mapbox(df,
                           lat="Latitude",
                           lon="Longitude",
                           size="Points_Collecte",
                           color="Complexité_Collecte",
                           hover_name="Nom",
                           hover_data=["Population", "Taux_Tri"],
                           zoom=12,
                           title="Distribution des Points de Collecte")
    
    fig.update_layout(mapbox_style="open-street-map")
    st.plotly_chart(fig)