"""Module « Parties prenantes » : grille pouvoir / intérêt, stratégie d'engagement et implication par phase."""

import numpy as np
import pandas as pd
import plotly.express as px
import streamlit as st

from src.data.stakeholders_data import PHASES_PROJET, STAKEHOLDERS_DATA

PHASE_COLUMNS = ["Phase Préparation (M1-M3)", "Phase Déploiement (M4-M6)", "Phase Opérationnelle (M7-M12)"]

STRATEGIES = {
    "Gérer étroitement": "Associer aux décisions, points réguliers, co-construction",
    "Satisfaire": "Consulter sur les sujets clés, reporting synthétique",
    "Tenir informé": "Communication régulière, ateliers, retours d'usage",
    "Surveiller": "Information générale, veille sur les attentes",
}


def _quadrant(influence: int, interest: int) -> str:
    high_inf, high_int = influence >= 4, interest >= 4
    if high_inf and high_int:
        return "Gérer étroitement"
    if high_inf:
        return "Satisfaire"
    if high_int:
        return "Tenir informé"
    return "Surveiller"


def show_stakeholders():
    st.header("Parties prenantes")
    df = pd.DataFrame(STAKEHOLDERS_DATA)
    df["Stratégie"] = [_quadrant(i, n) for i, n in zip(df["Niveau_Influence"], df["Niveau_Intérêt"])]
    df["Mode d'engagement"] = df["Stratégie"].map(STRATEGIES)

    st.subheader("Grille pouvoir / intérêt")
    st.caption("Chaque partie prenante est positionnée selon son influence sur le projet et son intérêt pour celui-ci. "
               "Le quadrant détermine la stratégie d'engagement.")

    rng = np.random.default_rng(7)  # léger décalage pour éviter les superpositions
    plot = df.assign(
        x=df["Niveau_Intérêt"] + rng.uniform(-0.28, 0.28, len(df)),
        y=df["Niveau_Influence"] + rng.uniform(-0.28, 0.28, len(df)),
    )
    fig = px.scatter(
        plot, x="x", y="y", color="Stakeholder Principal", text="Sous-Groupe",
        hover_data={"x": False, "y": False, "Niveau_Influence": True, "Niveau_Intérêt": True, "Stratégie": True},
        labels={"Stakeholder Principal": "Groupe"},
    )
    fig.update_traces(marker=dict(size=14, line=dict(width=1, color="white")), textposition="top center",
                      textfont=dict(size=10))
    quadrants = [
        (0.5, 3.5, 3.5, 5.5, "Satisfaire", "#FEF3C7"),
        (3.5, 5.5, 3.5, 5.5, "Gérer étroitement", "#CCFBF1"),
        (0.5, 3.5, 0.5, 3.5, "Surveiller", "#F1F5F9"),
        (3.5, 5.5, 0.5, 3.5, "Tenir informé", "#DBEAFE"),
    ]
    for x0, x1, y0, y1, label, color in quadrants:
        fig.add_shape(type="rect", x0=x0, x1=x1, y0=y0, y1=y1, fillcolor=color, line_width=0, layer="below")
        fig.add_annotation(x=(x0 + x1) / 2, y=y0 + 0.15, text=f"<b>{label}</b>", showarrow=False,
                           font=dict(color="#475569", size=12))
    fig.update_layout(height=560, xaxis=dict(title="Intérêt pour le projet →", range=[0.5, 5.5], dtick=1),
                      yaxis=dict(title="Influence sur le projet →", range=[0.5, 5.5], dtick=1),
                      legend=dict(orientation="h", y=-0.12), margin=dict(t=20, b=10))
    st.plotly_chart(fig, use_container_width=True)

    st.subheader("Stratégie d'engagement")
    counts = df["Stratégie"].value_counts()
    cols = st.columns(4)
    for col, (strategy, desc) in zip(cols, STRATEGIES.items()):
        with col:
            with st.container(border=True):
                st.markdown(f"**{strategy}** · {counts.get(strategy, 0)} acteurs")
                st.caption(desc)
                st.markdown("\n".join(f"- {s}" for s in df.loc[df["Stratégie"] == strategy, "Sous-Groupe"]))

    st.subheader("Implication par phase")
    st.dataframe(
        df[["Stakeholder Principal", "Sous-Groupe"] + PHASE_COLUMNS].replace("", "—"),
        column_config={"Stakeholder Principal": "Groupe", "Sous-Groupe": "Sous-groupe"},
        hide_index=True, use_container_width=True,
    )

    st.subheader("Phases du projet")
    cols = st.columns(len(PHASES_PROJET))
    for col, (phase, details) in zip(cols, PHASES_PROJET.items()):
        with col:
            with st.container(border=True):
                st.markdown(f"**{phase}** · {details['Durée']}")
                st.markdown("*Objectifs*\n" + "\n".join(f"- {o}" for o in details["Objectifs"]))
                st.markdown("*Livrables*\n" + "\n".join(f"- {l}" for l in details["Livrables"]))
