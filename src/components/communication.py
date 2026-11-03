"""Module « Communication & conduite du changement »."""

import json
import os
import textwrap
from datetime import datetime

import pandas as pd
import plotly.express as px
import streamlit as st

from src.data.communication_data import (
    get_communication_objectives, get_crisis_plan, get_key_audiences, get_training_plan,
)
from src.data.communication_examples import COMMUNICATION_EXAMPLES
from src.utils.config import COLORS

STORAGE_PATH = os.path.join(os.path.dirname(__file__), "..", "data", "generated_content")
SUBFOLDERS = ("campaigns", "content", "feedback")


class CommunicationDashboard:
    def __init__(self):
        for sub in SUBFOLDERS:
            os.makedirs(os.path.join(STORAGE_PATH, sub), exist_ok=True)

    # ------------------------------------------------------------------ pages
    def show_communication(self):
        st.header("Communication & conduite du changement")
        st.caption("Un projet technique réussit seulement si les habitants et les agents adoptent les nouveaux usages.")

        tabs = st.tabs(["Plan de communication", "Indicateurs", "Campagnes", "Contenus", "Retours usagers"])
        with tabs[0]:
            self._show_plan()
        with tabs[1]:
            self._show_overview()
        with tabs[2]:
            self._show_campaigns()
        with tabs[3]:
            self._show_content_management()
        with tabs[4]:
            self._show_feedback()

    def _show_plan(self):
        st.subheader("Objectifs")
        cols = st.columns(3)
        for col, (verb, desc) in zip(cols, get_communication_objectives().items()):
            with col:
                with st.container(border=True):
                    st.markdown(f"**{verb}**")
                    st.caption(desc)

        st.subheader("Cibles, messages et canaux")
        audiences = pd.DataFrame(get_key_audiences()).T.reset_index().rename(columns={"index": "Cible"})
        st.dataframe(audiences, hide_index=True, use_container_width=True)

        st.subheader("Plan de formation")
        st.dataframe(pd.DataFrame(get_training_plan()), hide_index=True, use_container_width=True)
        st.subheader("Communication de crise")
        st.dataframe(pd.DataFrame(get_crisis_plan()), hide_index=True, use_container_width=True)

        st.subheader("Exemples de messages par cible")
        audience = st.selectbox("Cible", list(COMMUNICATION_EXAMPLES))
        for example in COMMUNICATION_EXAMPLES[audience]["Examples"]:
            with st.expander(f"{example['type']} — {example['title']}"):
                st.text(textwrap.dedent(example["content"]).strip())

    def _show_overview(self):
        st.subheader("Indicateurs de communication (pilote)")
        stats = {
            "Taux d'engagement": ("24 %", "+2,3 pt"),
            "Personnes touchées": ("45 k", "+1,2 k"),
            "Utilisateurs de l'app": ("4 800", "+1 900"),
            "Satisfaction": ("4,2 / 5", "+0,3"),
        }
        cols = st.columns(4)
        for col, (label, (value, delta)) in zip(cols, stats.items()):
            col.metric(label, value, delta)

        engagement = pd.DataFrame({
            "Mois": pd.date_range("2025-01-01", periods=7, freq="MS"),
            "Facebook": [45, 48, 52, 55, 58, 62, 65],
            "Instagram": [30, 32, 35, 38, 40, 42, 45],
            "Application": [0, 0, 0, 12, 25, 34, 41],
        }).melt(id_vars="Mois", var_name="Canal", value_name="Engagement")
        fig = px.line(engagement, x="Mois", y="Engagement", color="Canal", markers=True,
                      title="Engagement par canal (indice)",
                      color_discrete_sequence=[COLORS["secondary"], "#DB2777", COLORS["primary"]])
        fig.update_layout(height=380, legend_title=None, xaxis_title=None)
        st.plotly_chart(fig, use_container_width=True)
        st.caption("L'application citoyenne a été lancée en avril 2025 dans les quartiers pilotes.")

    def _show_campaigns(self):
        with st.expander("➕ Nouvelle campagne"):
            col1, col2 = st.columns(2)
            with col1:
                name = st.text_input("Nom de la campagne")
                audience = st.multiselect("Public cible", ["Résidents", "Touristes", "Commerçants", "Scolaires"])
            with col2:
                start = st.date_input("Date de début")
                end = st.date_input("Date de fin")
            description = st.text_area("Description", height=100)
            if st.button("Créer la campagne"):
                if not name:
                    st.error("Donnez un nom à la campagne.")
                elif end < start:
                    st.error("La date de fin doit être postérieure à la date de début.")
                else:
                    self._save("campaigns", {
                        "nom": name, "public_cible": audience, "debut": start.isoformat(), "fin": end.isoformat(),
                        "description": description, "status": "Planifiée",
                        "creation_date": datetime.now().strftime("%Y-%m-%d %H:%M:%S"),
                    })
                    st.success("Campagne créée.")

        campaigns = self._load("campaigns", "debut")
        if campaigns:
            df = pd.DataFrame(campaigns)
            df["debut"] = pd.to_datetime(df["debut"])
            df["fin"] = pd.to_datetime(df["fin"]) + pd.Timedelta(days=1)
            fig = px.timeline(df, x_start="debut", x_end="fin", y="nom", color="status",
                              color_discrete_map={"Terminée": COLORS["muted"], "En cours": COLORS["primary"],
                                                  "Planifiée": COLORS["secondary"]},
                              hover_data={"description": True})
            fig.update_yaxes(autorange="reversed", title=None)
            fig.update_layout(title="Calendrier des campagnes", height=300, legend_title=None)
            st.plotly_chart(fig, use_container_width=True)
            for c in campaigns:
                with st.expander(f"{c['nom']} · {c.get('status', '')}"):
                    st.markdown(f"**Public :** {', '.join(c.get('public_cible', []))}  \n"
                                f"**Période :** {c['debut']} → {c['fin']}  \n{c.get('description', '')}")

    def _show_content_management(self):
        with st.expander("➕ Nouveau contenu"):
            col1, col2 = st.columns(2)
            with col1:
                content_type = st.selectbox("Type", ["Post réseaux sociaux", "Newsletter", "Communiqué"])
                title = st.text_input("Titre")
                channels = st.multiselect("Canaux", ["Facebook", "Instagram", "Application", "Email", "Affichage"])
            with col2:
                tone = st.selectbox("Ton", ["Formel", "Neutre", "Décontracté"])
                target = st.multiselect("Cible", ["Tous", "Résidents", "Touristes", "Commerçants"])
            body = st.text_area("Contenu", height=150)
            if st.button("Enregistrer le contenu"):
                if body and title:
                    self._save("content", {
                        "type": content_type, "titre": title, "contenu": body, "canaux": channels,
                        "ton": tone, "cible": target, "creation_date": datetime.now().strftime("%Y-%m-%d %H:%M:%S"),
                    })
                    st.success("Contenu enregistré.")
                else:
                    st.error("Le titre et le contenu sont obligatoires.")

        for c in self._load("content", "creation_date"):
            with st.expander(f"{c.get('titre', 'Sans titre')} · {c.get('type', '')}"):
                st.caption(f"Canaux : {', '.join(c.get('canaux', []))} · Ton : {c.get('ton', '')} · "
                           f"Cible : {', '.join(c.get('cible', []))}")
                st.write(c.get("contenu", ""))

    def _show_feedback(self):
        feedbacks = self._load("feedback", "date")
        if feedbacks:
            df = pd.DataFrame(feedbacks)
            c1, c2 = st.columns([1, 2])
            c1.metric("Satisfaction moyenne", f"{df['satisfaction'].mean():.1f} / 5", f"{len(df)} retours",
                      delta_color="off")
            counts = df["type"].value_counts().reset_index()
            fig = px.bar(counts, x="count", y="type", orientation="h", color_discrete_sequence=[COLORS["primary"]],
                         labels={"count": "Nombre de retours", "type": ""})
            fig.update_layout(height=220, margin=dict(t=10, b=10))
            c2.plotly_chart(fig, use_container_width=True)

        with st.form("feedback_form", clear_on_submit=True):
            st.markdown("**Ajouter un retour**")
            satisfaction = st.slider("Satisfaction", 1, 5, 4)
            feedback_type = st.selectbox("Type", ["Général", "Application", "Collecte", "Suggestion"])
            comments = st.text_area("Commentaire")
            if st.form_submit_button("Envoyer"):
                self._save("feedback", {"satisfaction": satisfaction, "type": feedback_type, "commentaires": comments,
                                        "date": datetime.now().strftime("%Y-%m-%d %H:%M:%S")})
                st.success("Merci, votre retour est enregistré.")

        for f in feedbacks:
            with st.expander(f"{f['date'][:10]} · {f['type']} · {f['satisfaction']}/5"):
                st.write(f.get("commentaires") or "—")

    # ------------------------------------------------------------------ stockage JSON
    @staticmethod
    def _save(kind: str, data: dict):
        filename = f"user_{kind}_{datetime.now():%Y%m%d_%H%M%S}.json"
        with open(os.path.join(STORAGE_PATH, kind, filename), "w", encoding="utf-8") as f:
            json.dump(data, f, ensure_ascii=False, indent=2)

    @staticmethod
    def _load(kind: str, sort_key: str) -> list:
        folder = os.path.join(STORAGE_PATH, kind)
        items = []
        for name in sorted(os.listdir(folder)):
            if name.endswith(".json"):
                with open(os.path.join(folder, name), encoding="utf-8") as f:
                    items.append(json.load(f))
        return sorted(items, key=lambda x: x.get(sort_key, ""), reverse=True)
