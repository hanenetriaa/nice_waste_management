"""Module « Pilotage de projet » : charte, planning, budget (valeur acquise), RACI, gouvernance, décisions."""

import pandas as pd
import plotly.express as px
import plotly.graph_objects as go
import streamlit as st

from src.data.project_data import (
    DECISIONS, GOVERNANCE, LESSONS_LEARNED, PILOT_RESULTS, PROJECT_INFO, PROJECT_KPIS, RACI, RACI_ROLES,
)
from src.utils.config import COLORS, PHASE_COLORS, STATUS_COLORS
from src.utils.project_metrics import (
    actions_dataframe, budget_curve, evm_summary, milestones_dataframe, project_weather,
    reporting_date, tasks_dataframe,
)

DATE_FMT = "%d/%m/%Y"


def _fmt_date(d) -> str:
    return pd.Timestamp(d).strftime(DATE_FMT) if pd.notna(d) else "—"


def _add_today_line(fig, label="Date de reporting"):
    d = reporting_date()
    fig.add_shape(type="line", x0=d, x1=d, y0=0, y1=1, yref="paper",
                  line=dict(color=COLORS["danger"], width=2, dash="dash"))
    fig.add_annotation(x=d, y=1.02, yref="paper", text=f"{label} · {d.strftime(DATE_FMT)}",
                       showarrow=False, font=dict(color=COLORS["danger"], size=11))


def show_project_management():
    st.header("Pilotage de projet")
    st.caption(
        f"{PROJECT_INFO['nom']} · Chef de projet : {PROJECT_INFO['chef_de_projet']} · "
        f"Situation au **{reporting_date().strftime(DATE_FMT)}** (scénario simulé)"
    )

    tabs = st.tabs([
        "Cadrage & objectifs", "Planning & jalons", "Budget & valeur acquise",
        "Organisation (RACI)", "Décisions & actions",
    ])
    with tabs[0]:
        _show_charter()
    with tabs[1]:
        _show_planning()
    with tabs[2]:
        _show_budget()
    with tabs[3]:
        _show_organisation()
    with tabs[4]:
        _show_decisions()


# --------------------------------------------------------------------------- Cadrage
def _show_charter():
    st.subheader("Charte projet")
    st.markdown(f"**Objectif.** {PROJECT_INFO['objectif']}")

    col1, col2, col3 = st.columns([1.2, 1, 0.8])
    with col1:
        with st.container(border=True):
            st.markdown("**Dans le périmètre**")
            st.markdown("\n".join(f"- {p}" for p in PROJECT_INFO["perimetre_inclus"]))
    with col2:
        with st.container(border=True):
            st.markdown("**Hors périmètre**")
            st.markdown("\n".join(f"- {p}" for p in PROJECT_INFO["perimetre_exclu"]))
    with col3:
        with st.container(border=True):
            st.markdown("**Fiche d'identité**")
            st.markdown(
                f"- **Sponsor :** {PROJECT_INFO['sponsor']}\n"
                f"- **Durée :** 12 mois ({_fmt_date(PROJECT_INFO['debut'])} → {_fmt_date(PROJECT_INFO['fin'])})\n"
                f"- **Budget :** {evm_summary()['BAC']:,.0f} k€ + {PROJECT_INFO['reserve_aleas_keur']} k€ de réserve".replace(",", " ")
            )

    st.subheader("Indicateurs de réussite")
    st.caption("Chaque indicateur a une valeur de départ, une cible chiffrée et une échéance (fin 2025).")
    cols = st.columns(len(PROJECT_KPIS))
    for col, kpi in zip(cols, PROJECT_KPIS):
        span = kpi["cible"] - kpi["depart"]
        done = (kpi["actuel"] - kpi["depart"]) / span if span else 1
        with col:
            with st.container(border=True):
                st.markdown(f"**{kpi['indicateur']}**")
                st.markdown(
                    f"<span style='font-size:1.6rem;font-weight:600'>{kpi['actuel']:g}</span>"
                    f"<span style='color:#64748B'> / cible {kpi['cible']:g}</span>",
                    unsafe_allow_html=True,
                )
                st.progress(min(max(done, 0.0), 1.0), text=f"{done:.0%} du chemin parcouru")
                st.caption(f"Départ : {kpi['depart']:g}")

    st.subheader("Résultats du pilote (3 quartiers, après 3 mois)")
    df = pd.DataFrame(PILOT_RESULTS).melt(
        id_vars=["quartier", "indicateur"], value_vars=["avant", "apres"], var_name="moment", value_name="valeur"
    )
    df["moment"] = df["moment"].map({"avant": "Avant", "apres": "Après"})
    fig = px.bar(
        df, x="quartier", y="valeur", color="moment", barmode="group", facet_col="indicateur",
        color_discrete_map={"Avant": COLORS["muted"], "Après": COLORS["primary"]}, text="valeur",
    )
    fig.for_each_annotation(lambda a: a.update(text=a.text.split("=")[-1]))
    fig.update_yaxes(matches=None, showticklabels=True, title=None)
    fig.update_xaxes(title=None)
    fig.update_layout(height=360, legend_title=None, margin=dict(t=40, b=10))
    st.plotly_chart(fig, width="stretch")
    st.info(
        "Les résultats du pilote ont justifié la décision **GO** du COPIL du 27/06/2025 pour la généralisation "
        "aux 12 autres quartiers."
    )


# --------------------------------------------------------------------------- Planning
def _show_planning():
    df = tasks_dataframe()

    c1, c2, c3, c4 = st.columns(4)
    counts = df["statut"].value_counts()
    c1.metric("Tâches terminées", f"{counts.get('Terminé', 0)} / {len(df)}")
    c2.metric("En cours", counts.get("En cours", 0))
    c3.metric("En retard", counts.get("En retard", 0))
    c4.metric("À venir", counts.get("À venir", 0))

    color_by = st.radio("Colorer par", ["Statut", "Phase"], horizontal=True, label_visibility="collapsed")
    df["libelle"] = df["id"] + " · " + df["tache"]
    df["hover_avancement"] = df["avancement"].astype(str) + " % réalisé (prévu : " + df["avancement_prevu"].round(0).astype(int).astype(str) + " %)"

    fig = px.timeline(
        df, x_start="debut", x_end="fin", y="libelle",
        color="statut" if color_by == "Statut" else "phase",
        color_discrete_map=STATUS_COLORS if color_by == "Statut" else PHASE_COLORS,
        hover_data={"responsable": True, "hover_avancement": True, "predecesseurs": True, "libelle": False},
        labels={"hover_avancement": "Avancement", "responsable": "Responsable", "predecesseurs": "Dépend de",
                "statut": "Statut", "phase": "Phase"},
    )
    fig.update_traces(marker_line_width=0, opacity=0.9)

    ms = milestones_dataframe()
    fig.add_trace(go.Scatter(
        x=ms["prevu"], y=["◆ Jalons"] * len(ms), mode="markers", name="Jalon",
        marker=dict(symbol="diamond", size=13, color=["#0F766E" if s.startswith("Atteint") else "#94A3B8" for s in ms["statut"]],
                    line=dict(width=1, color="white")),
        text=ms["jalon"], hovertemplate="%{text}<br>%{x|%d/%m/%Y}<extra></extra>",
    ))
    order = ["◆ Jalons"] + df["libelle"].tolist()
    fig.update_yaxes(categoryorder="array", categoryarray=order[::-1], title=None, autorange=True)
    fig.update_xaxes(title=None, dtick="M1", tickformat="%b<br>%Y", tickangle=0)
    _add_today_line(fig)
    fig.update_layout(height=640, legend_title=None, margin=dict(l=10, r=10, t=40, b=10),
                      legend=dict(orientation="h", y=-0.06))
    st.plotly_chart(fig, width="stretch")

    st.subheader("Jalons")
    ms_view = ms.assign(prevu=ms["prevu"].map(_fmt_date), reel=ms["reel"].map(_fmt_date))
    st.dataframe(
        ms_view[["jalon", "prevu", "reel", "statut", "critere"]],
        column_config={"jalon": "Jalon", "prevu": "Date prévue", "reel": "Date réelle",
                       "statut": "Statut", "critere": "Critère d'atteinte"},
        hide_index=True, width="stretch",
    )

    with st.expander("Détail des tâches (WBS)"):
        view = df.assign(debut=df["debut"].map(_fmt_date), fin=df["fin"].map(_fmt_date))
        st.dataframe(
            view[["id", "tache", "phase", "responsable", "debut", "fin", "predecesseurs", "avancement", "statut"]],
            column_config={
                "id": "ID", "tache": "Tâche", "phase": "Phase", "responsable": "Responsable",
                "debut": "Début", "fin": "Fin", "predecesseurs": "Dépend de", "statut": "Statut",
                "avancement": st.column_config.ProgressColumn("Avancement", format="%d %%", min_value=0, max_value=100),
            },
            hide_index=True, width="stretch",
        )


# --------------------------------------------------------------------------- Budget
def _show_budget():
    df = tasks_dataframe()
    evm = evm_summary(df)

    st.markdown(
        "Le suivi budgétaire utilise la **méthode de la valeur acquise** (Earned Value Management) : "
        "on compare ce qui était prévu (PV), ce qui a réellement été produit (EV) et ce que cela a coûté (AC)."
    )
    c = st.columns(5)
    c[0].metric("Budget total (BAC)", f"{evm['BAC']:,.0f} k€".replace(",", " "))
    c[1].metric("Coût réel à date (AC)", f"{evm['AC']:,.0f} k€".replace(",", " "))
    c[2].metric("SPI — performance délais", f"{evm['SPI']:.2f}", f"{evm['SPI'] - 1:+.0%}", help="EV / PV. < 1 : en retard.")
    c[3].metric("CPI — performance coûts", f"{evm['CPI']:.2f}", f"{evm['CPI'] - 1:+.0%}", help="EV / AC. < 1 : dépassement.")
    c[4].metric("Estimation à terminaison (EAC)", f"{evm['EAC']:,.0f} k€".replace(",", " "),
                f"{evm['EAC'] - evm['BAC']:+,.0f} k€".replace(",", " "), delta_color="inverse",
                help="BAC / CPI : coût final si la performance actuelle se maintient.")

    col1, col2 = st.columns([1.4, 1])
    with col1:
        curve = budget_curve(df)
        fig = go.Figure()
        fig.add_trace(go.Scatter(x=curve["semaine"], y=curve["Valeur planifiée (PV)"], name="Valeur planifiée (PV)",
                                 line=dict(color=COLORS["muted"], width=3)))
        d = reporting_date()
        fig.add_trace(go.Scatter(x=[d], y=[evm["EV"]], name="Valeur acquise (EV)", mode="markers+text",
                                 marker=dict(size=13, color=COLORS["primary"]), text=[f"EV {evm['EV']:.0f}"],
                                 textposition="bottom right"))
        fig.add_trace(go.Scatter(x=[d], y=[evm["AC"]], name="Coût réel (AC)", mode="markers+text",
                                 marker=dict(size=13, color=COLORS["danger"], symbol="square"),
                                 text=[f"AC {evm['AC']:.0f}"], textposition="top left"))
        fig.add_hline(y=evm["BAC"], line_dash="dot", line_color=COLORS["secondary"],
                      annotation_text=f"Budget {evm['BAC']:.0f} k€", annotation_position="top left")
        _add_today_line(fig)
        fig.update_layout(title="Courbe en S du budget (k€ cumulés)", height=420, legend=dict(orientation="h", y=-0.15),
                          margin=dict(t=60, b=10), yaxis_title=None)
        st.plotly_chart(fig, width="stretch")
    with col2:
        by_phase = df.groupby("phase", as_index=False)[["budget", "valeur_acquise", "cout_reel"]].sum()
        long = by_phase.melt(id_vars="phase", var_name="mesure", value_name="k€")
        long["mesure"] = long["mesure"].map({"budget": "Budget", "valeur_acquise": "Valeur acquise", "cout_reel": "Coût réel"})
        fig2 = px.bar(long, y="phase", x="k€", color="mesure", barmode="group", orientation="h",
                      color_discrete_map={"Budget": "#CBD5E1", "Valeur acquise": COLORS["primary"], "Coût réel": COLORS["danger"]})
        fig2.update_layout(title="Budget par phase", height=420, legend_title=None, yaxis_title=None,
                           legend=dict(orientation="h", y=-0.15), margin=dict(t=60, b=10))
        fig2.update_yaxes(categoryorder="category descending")
        st.plotly_chart(fig2, width="stretch")

    reserve_left = evm["reserve"] - evm["reserve_consommee"]
    overrun = evm["EAC"] - evm["BAC"]
    k = lambda v: f"{v:,.0f}".replace(",", "\u202f")
    st.warning(
        f"**Analyse du chef de projet.** Le projet est légèrement en retard (SPI {evm['SPI']:.2f}) et en léger "
        f"dépassement (CPI {evm['CPI']:.2f}), principalement à cause de la pose des capteurs en zone dense (T06, T11). "
        f"Au rythme actuel, le coût final serait de {k(evm['EAC'])} k€, soit {k(overrun)} k€ au-dessus du budget, "
        f"alors qu'il reste {reserve_left} k€ de réserve. **Actions :** plan de rattrapage en cours (A13) et dossier "
        f"d'arbitrage préparé pour le COPIL de septembre (A16)."
    )

    with st.expander("Détail par tâche"):
        view = df[["id", "tache", "budget", "valeur_planifiee", "valeur_acquise", "cout_reel"]].copy()
        view["ecart_cout"] = view["valeur_acquise"] - view["cout_reel"]
        st.dataframe(
            view.round(1),
            column_config={"id": "ID", "tache": "Tâche", "budget": "Budget (k€)", "valeur_planifiee": "PV (k€)",
                           "valeur_acquise": "EV (k€)", "cout_reel": "AC (k€)", "ecart_cout": "Écart EV − AC (k€)"},
            hide_index=True, width="stretch",
        )


# --------------------------------------------------------------------------- Organisation
def _style_raci(val):
    styles = {
        "R": "background-color:#0F766E;color:white;font-weight:600",
        "A": "background-color:#1E3A8A;color:white;font-weight:600",
        "C": "background-color:#CCFBF1;color:#134E4A",
        "I": "background-color:#F1F5F9;color:#475569",
    }
    return styles.get(val, "")


def _show_organisation():
    st.subheader("Matrice RACI")
    st.caption("**R** Réalise · **A** Approuve (un seul responsable final par activité) · **C** Consulté · **I** Informé")
    raci = pd.DataFrame(RACI, index=RACI_ROLES).T
    raci.index.name = "Activité"
    styler = raci.style.map(_style_raci).set_properties(**{"text-align": "center"})
    st.dataframe(styler, width="stretch", height=(len(raci) + 1) * 36 + 3)

    a_count = (raci == "A").sum(axis=1)
    if (a_count == 1).all():
        st.success("Contrôle de cohérence : chaque activité a exactement un « A ».")
    else:
        st.error("Contrôle de cohérence : certaines activités n'ont pas exactement un « A ».")

    load = (raci.isin(["R", "A"])).sum().sort_values(ascending=True)
    fig = px.bar(load, orientation="h", labels={"value": "Activités en R ou A", "index": ""},
                 color_discrete_sequence=[COLORS["primary"]])
    fig.update_layout(title="Charge de responsabilité par acteur", showlegend=False, height=300,
                      margin=dict(t=50, b=10), yaxis_title=None)
    st.plotly_chart(fig, width="stretch")

    st.subheader("Gouvernance")
    st.dataframe(
        pd.DataFrame(GOVERNANCE),
        column_config={"instance": "Instance", "frequence": "Fréquence", "participants": "Participants", "role": "Rôle"},
        hide_index=True, width="stretch",
    )


# --------------------------------------------------------------------------- Décisions & actions
def _show_decisions():
    st.subheader("Plan d'actions")
    actions = actions_dataframe()
    late = actions[(actions["statut"] != "Fait") & (actions["echeance"] < reporting_date())]
    c1, c2, c3 = st.columns(3)
    c1.metric("Actions ouvertes", int((actions["statut"] != "Fait").sum()))
    c2.metric("Actions en retard", len(late))
    c3.metric("Actions soldées", int((actions["statut"] == "Fait").sum()))
    st.dataframe(
        actions.assign(echeance=actions["echeance"].map(_fmt_date)),
        column_config={"id": "ID", "action": "Action", "porteur": "Porteur", "echeance": "Échéance", "statut": "Statut"},
        hide_index=True, width="stretch",
    )

    st.subheader("Journal des décisions")
    for d in sorted(DECISIONS, key=lambda x: x["date"], reverse=True):
        with st.container(border=True):
            st.markdown(f"**{_fmt_date(d['date'])} · {d['instance']}** — {d['decision']}")
            st.caption(f"Impact : {d['impact']}")

    st.subheader("Retour d'expérience (à date)")
    st.markdown("\n".join(f"- {l}" for l in LESSONS_LEARNED))
