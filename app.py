"""Nice Waste Management — application de pilotage du projet de modernisation de la collecte des déchets."""

import streamlit as st

from src.components import dashboard, maps, quartiers, risks, sources, stakeholders
from src.components.communication import CommunicationDashboard
from src.components.project_management import show_project_management
from src.utils.config import APP_CONFIG

PAGES = {
    "🏠 Synthèse exécutive": dashboard.show_dashboard,
    "📅 Pilotage de projet": show_project_management,
    "⚠️ Gestion des risques": risks.show_risk_analysis,
    "👥 Parties prenantes": stakeholders.show_stakeholders,
    "🗺️ Diagnostic par quartier": quartiers.show_quartiers,
    "📍 Cartographie": maps.show_maps,
    "📣 Communication & changement": lambda: CommunicationDashboard().show_communication(),
    "📚 Sources & méthodologie": sources.show_sources,
}


def main():
    st.set_page_config(page_title=APP_CONFIG["short_title"], page_icon="♻️", layout="wide")

    with st.sidebar:
        st.markdown(f"## ♻️ {APP_CONFIG['short_title']}")
        st.caption("Pilotage du projet de modernisation de la collecte des déchets à Nice")
        page = st.radio("Navigation", list(PAGES), label_visibility="collapsed")
        st.divider()
        st.caption(
            f"Cas d'étude réalisé par **{APP_CONFIG['author']}** · v{APP_CONFIG['version']}  \n"
            "Données de pilotage simulées — voir *Sources & méthodologie*."
        )

    PAGES[page]()


if __name__ == "__main__":
    main()
