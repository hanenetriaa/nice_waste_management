"""Module « Gestion des risques » : matrice de criticité, registre et plan de réponse."""

import pandas as pd
import plotly.graph_objects as go
import streamlit as st

from src.data.risks_data import RISKS, criticity_level
from src.utils.config import CRITICITY_COLORS

LEVEL_SCALE = {"Faible": 0, "Modérée": 1, "Élevée": 2, "Critique": 3}


def risks_dataframe() -> pd.DataFrame:
    df = pd.DataFrame(RISKS)
    df["criticite"] = df["probabilite"] * df["impact"]
    df["niveau"] = df["criticite"].map(criticity_level)
    df["criticite_residuelle"] = df["prob_residuelle"] * df["impact_residuel"]
    df["niveau_residuel"] = df["criticite_residuelle"].map(criticity_level)
    return df.sort_values("criticite", ascending=False)


def _heatmap(df: pd.DataFrame, prob_col: str, impact_col: str, title: str) -> go.Figure:
    z, text = [], []
    for impact in range(1, 6):
        z_row, t_row = [], []
        for prob in range(1, 6):
            z_row.append(LEVEL_SCALE[criticity_level(prob * impact)])
            ids = df[(df[prob_col] == prob) & (df[impact_col] == impact)]["id"].tolist()
            t_row.append("<br>".join(" ".join(ids[i:i + 2]) for i in range(0, len(ids), 2)))
        z.append(z_row)
        text.append(t_row)

    colors = [CRITICITY_COLORS[k] for k in LEVEL_SCALE]
    colorscale = [[i / 3, c] for i, c in enumerate(colors)]
    fig = go.Figure(go.Heatmap(
        z=z, x=[1, 2, 3, 4, 5], y=[1, 2, 3, 4, 5], text=text, texttemplate="<b>%{text}</b>",
        textfont=dict(size=13, color="white"), colorscale=colorscale, zmin=0, zmax=3, showscale=False,
        xgap=3, ygap=3, opacity=0.85,
        hovertemplate="Probabilité %{x} × Impact %{y}<br>%{text}<extra></extra>",
    ))
    fig.update_layout(
        title=title, height=430, margin=dict(t=50, l=10, r=10, b=10),
        xaxis=dict(title="Probabilité →", tickvals=[1, 2, 3, 4, 5], ticktext=["1 Rare", "2", "3", "4", "5 Quasi certain"]),
        yaxis=dict(title="Impact →", tickvals=[1, 2, 3, 4, 5], ticktext=["1 Mineur", "2", "3", "4", "5 Majeur"]),
    )
    return fig


def show_risk_analysis():
    st.header("Gestion des risques")
    df = risks_dataframe()

    c = st.columns(4)
    c[0].metric("Risques identifiés", len(df))
    c[1].metric("Critiques (brut)", int((df["niveau"] == "Critique").sum()))
    c[2].metric("Critiques après plan de réponse", int((df["niveau_residuel"] == "Critique").sum()))
    reduction = 1 - df["criticite_residuelle"].sum() / df["criticite"].sum()
    c[3].metric("Réduction de l'exposition", f"{reduction:.0%}", help="Somme des criticités résiduelles vs brutes")

    col1, col2 = st.columns(2)
    with col1:
        st.plotly_chart(_heatmap(df, "probabilite", "impact", "Avant plan de réponse"), use_container_width=True)
    with col2:
        st.plotly_chart(_heatmap(df, "prob_residuelle", "impact_residuel", "Après plan de réponse (résiduel)"),
                        use_container_width=True)
    st.caption(" · ".join(f"<span style='color:{c}'>■</span> {k}" for k, c in CRITICITY_COLORS.items()),
               unsafe_allow_html=True)

    st.subheader("Registre des risques")
    f1, f2, f3 = st.columns(3)
    cats = f1.multiselect("Catégorie", sorted(df["categorie"].unique()), placeholder="Toutes")
    owners = f2.multiselect("Responsable", sorted(df["responsable"].unique()), placeholder="Tous")
    levels = f3.multiselect("Niveau brut", list(CRITICITY_COLORS), placeholder="Tous")
    view = df.copy()
    if cats:
        view = view[view["categorie"].isin(cats)]
    if owners:
        view = view[view["responsable"].isin(owners)]
    if levels:
        view = view[view["niveau"].isin(levels)]

    st.dataframe(
        view[["id", "risque", "categorie", "criticite", "niveau", "strategie", "reponse",
              "responsable", "criticite_residuelle", "statut", "tendance"]],
        column_config={
            "id": "ID", "risque": st.column_config.TextColumn("Risque", width="large"), "categorie": "Catégorie",
            "criticite": st.column_config.ProgressColumn("Criticité", min_value=0, max_value=25, format="%d"),
            "niveau": "Niveau", "strategie": "Stratégie", "reponse": st.column_config.TextColumn("Plan de réponse", width="large"),
            "responsable": "Responsable", "criticite_residuelle": st.column_config.ProgressColumn(
                "Résiduelle", min_value=0, max_value=25, format="%d"),
            "statut": "Statut", "tendance": "Tendance",
        },
        hide_index=True, use_container_width=True,
    )
    st.caption(
        "Stratégies de réponse : **Réduire** (diminuer probabilité ou impact) · **Transférer** (contrat, assurance) · "
        "**Accepter** · **Éviter**. Le registre est revu chaque semaine en comité projet."
    )
