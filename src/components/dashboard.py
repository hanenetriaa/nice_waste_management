"""Synthèse exécutive : la page qu'un sponsor ou un élu lit en 2 minutes."""

import pandas as pd
import plotly.express as px
import streamlit as st

from src.components.risks import risks_dataframe
from src.data.project_data import PROJECT_INFO, PROJECT_KPIS
from src.data.quartiers_data import QUARTIERS_DATA
from src.utils.config import COLORS
from src.utils.project_metrics import (
    evm_summary, milestones_dataframe, project_weather, reporting_date, tasks_dataframe,
)


def show_dashboard():
    tasks = tasks_dataframe()
    evm = evm_summary(tasks)
    icon, label, explanation = project_weather(evm["SPI"], evm["CPI"])

    st.header("Synthèse exécutive")
    st.caption(f"{PROJECT_INFO['nom']} · situation au {reporting_date():%d/%m/%Y} (scénario simulé)")

    left, right = st.columns([1, 3])
    with left:
        with st.container(border=True):
            st.markdown(
                f"<div style='text-align:center'><div style='font-size:3.2rem;line-height:1.1'>{icon}</div>"
                f"<div style='font-size:1.15rem;font-weight:600'>Météo projet : {label}</div>"
                f"<div style='color:#64748B;font-size:0.9rem'>{explanation}</div></div>",
                unsafe_allow_html=True,
            )
    with right:
        c = st.columns(4)
        c[0].metric("Avancement réel", f"{evm['avancement_reel']:.0f} %",
                    f"{evm['avancement_reel'] - evm['avancement_prevu']:+.1f} pt vs prévu")
        c[1].metric("Délais (SPI)", f"{evm['SPI']:.2f}", help="1 = conforme au planning")
        c[2].metric("Coûts (CPI)", f"{evm['CPI']:.2f}", help="1 = conforme au budget")
        c[3].metric("Budget consommé", f"{evm['AC']:,.0f} k€".replace(",", " "),
                    f"sur {evm['BAC']:,.0f} k€".replace(",", " "), delta_color="off")
        st.progress(evm["avancement_reel"] / 100,
                    text=f"Avancement global : {evm['avancement_reel']:.0f} % réalisé · {evm['avancement_prevu']:.0f} % prévu à date")

    col1, col2, col3 = st.columns(3)
    with col1:
        st.markdown("##### Prochains jalons")
        ms = milestones_dataframe()
        upcoming = ms[ms["reel"].isna()].head(3)
        for _, m in upcoming.iterrows():
            days = (m["prevu"] - reporting_date()).days
            st.markdown(f"◆ **{m['jalon']}**  \n{m['prevu']:%d/%m/%Y} · dans {days} jours")
    with col2:
        st.markdown("##### Risques à surveiller")
        risks = risks_dataframe().head(3)
        for _, r in risks.iterrows():
            st.markdown(f"🔴 **{r['id']}** {r['risque']}  \nCriticité {r['criticite']}/25 · {r['responsable']}")
    with col3:
        st.markdown("##### Points d'attention")
        late = tasks[tasks["statut"] == "En retard"]
        for _, t in late.iterrows():
            st.markdown(f"⚠️ **{t['id']}** {t['tache']} : {t['avancement']} % réalisé vs "
                        f"{t['avancement_prevu']:.0f} % prévu")
        st.markdown("✅ Pilote concluant : décision **GO** pour la généralisation (27/06)")

    st.divider()
    st.subheader("Indicateurs de réussite")
    kpi = pd.DataFrame(PROJECT_KPIS)
    kpi["progression"] = ((kpi["actuel"] - kpi["depart"]) / (kpi["cible"] - kpi["depart"])).clip(0, 1) * 100
    fig = px.bar(kpi, x="progression", y="indicateur", orientation="h", text=kpi["progression"].round(0).astype(int).astype(str) + " %",
                 range_x=[0, 100], color_discrete_sequence=[COLORS["primary"]],
                 hover_data={"depart": True, "actuel": True, "cible": True, "progression": False})
    fig.update_layout(height=280, margin=dict(t=10, b=10), xaxis_title="% du chemin parcouru vers la cible",
                      yaxis_title=None)
    fig.update_yaxes(categoryorder="total ascending")
    st.plotly_chart(fig, width="stretch")

    st.subheader("Contexte territorial")
    df = pd.DataFrame(QUARTIERS_DATA)
    c = st.columns(4)
    c[0].metric("Quartiers couverts", len(df))
    c[1].metric("Habitants concernés", f"{df['Population'].sum():,}".replace(",", " "))
    c[2].metric("Points de collecte", int(df["Points_Collecte"].sum()))
    c[3].metric("Volume mensuel collecté", f"{df['Volume_Moyen_Mensuel'].sum():,} t".replace(",", " "))

    col1, col2 = st.columns(2)
    with col1:
        fig1 = px.bar(df.sort_values("Taux_Tri"), x="Taux_Tri", y="Nom", orientation="h", color="Complexité_Collecte",
                      title="Taux de tri par quartier (%)",
                      color_discrete_map={"Faible": "#99F6E4", "Moyenne": "#2DD4BF", "Élevée": "#0F766E", "Très élevée": "#134E4A"},
                      labels={"Taux_Tri": "Taux de tri (%)", "Nom": "", "Complexité_Collecte": "Complexité de collecte"})
        fig1.update_layout(height=460, legend=dict(orientation="h", y=-0.15))
        st.plotly_chart(fig1, width="stretch")
    with col2:
        df["Habitants par point"] = (df["Population"] / df["Points_Collecte"]).round(0)
        fig2 = px.scatter(df, x="Population", y="Points_Collecte", size="Volume_Moyen_Mensuel", color="Taux_Tri",
                          text="Nom", title="Points de collecte vs population",
                          color_continuous_scale="Teal", hover_data=["Habitants par point"],
                          labels={"Points_Collecte": "Points de collecte", "Taux_Tri": "Taux de tri (%)"})
        fig2.update_traces(textposition="top center", textfont_size=10)
        fig2.update_layout(height=460)
        st.plotly_chart(fig2, width="stretch")
