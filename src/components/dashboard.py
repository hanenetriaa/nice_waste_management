# src/components/dashboard.py
import streamlit as st
import plotly.express as px
import pandas as pd
from ..data.quartiers_data import QUARTIERS_DATA

def show_dashboard():
    st.header("Tableau de Bord")
    
    # KPIs principaux
    col1, col2, col3, col4 = st.columns(4)
    with col1:
        st.metric("Volume Total Collecté", "1250 tonnes", "+2%")
    with col2:
        st.metric("Taux de Tri Moyen", "64%", "+3%")
    with col3:
        st.metric("Points de Collecte", "378", "+15")
    with col4:
        st.metric("Satisfaction", "72%", "-5%")

    # Graphiques
    df = pd.DataFrame(QUARTIERS_DATA)
    show_quartier_charts(df)

def show_quartier_charts(df):
    col1, col2 = st.columns(2)
    
    with col1:
        fig1 = px.bar(df,
                     x="Nom",
                     y="Taux_Tri",
                     title="Taux de Tri par Quartier",
                     color="Complexité_Collecte")
        st.plotly_chart(fig1)
    
    with col2:
        fig2 = px.scatter(df,
                         x="Population",
                         y="Points_Collecte",
                         title="Points de Collecte vs Population",
                         color="Densité",
                         text="Nom")
        st.plotly_chart(fig2)