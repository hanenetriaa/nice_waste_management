"""Calculs de pilotage : avancement prévu, statut des tâches et valeur acquise (EVM)."""

from __future__ import annotations

import pandas as pd

from src.data.project_data import ACTIONS, MILESTONES, PROJECT_INFO, TASKS


def reporting_date() -> pd.Timestamp:
    return pd.Timestamp(PROJECT_INFO["date_reporting"])


def planned_progress(start: pd.Timestamp, end: pd.Timestamp, at: pd.Timestamp) -> float:
    """Avancement prévu (en %) d'une tâche à une date donnée, en supposant une charge linéaire."""
    if at <= start:
        return 0.0
    if at >= end:
        return 100.0
    return round(100 * (at - start).days / max((end - start).days, 1), 1)


def task_status(row: pd.Series) -> str:
    if row["avancement"] >= 100:
        return "Terminé"
    if row["avancement_prevu"] - row["avancement"] > 5:
        return "En retard"
    if row["debut"] > row["date_reporting"]:
        return "À venir"
    return "En cours"


def tasks_dataframe() -> pd.DataFrame:
    df = pd.DataFrame(TASKS)
    df["debut"] = pd.to_datetime(df["debut"])
    df["fin"] = pd.to_datetime(df["fin"])
    df["date_reporting"] = reporting_date()
    df["avancement_prevu"] = [
        planned_progress(s, e, reporting_date()) for s, e in zip(df["debut"], df["fin"])
    ]
    df["statut"] = df.apply(task_status, axis=1)
    df["duree_jours"] = (df["fin"] - df["debut"]).dt.days + 1
    # Valeur acquise, tâche par tâche
    df["valeur_planifiee"] = df["budget"] * df["avancement_prevu"] / 100
    df["valeur_acquise"] = df["budget"] * df["avancement"] / 100
    return df.drop(columns="date_reporting")


def evm_summary(df: pd.DataFrame | None = None) -> dict:
    """Indicateurs de valeur acquise (Earned Value Management).

    BAC : budget à l'achèvement · PV : valeur planifiée · EV : valeur acquise · AC : coût réel
    SPI = EV / PV (délais) · CPI = EV / AC (coûts) · EAC = BAC / CPI (estimation à terminaison)
    """
    df = tasks_dataframe() if df is None else df
    bac = df["budget"].sum()
    pv = df["valeur_planifiee"].sum()
    ev = df["valeur_acquise"].sum()
    ac = df["cout_reel"].sum()
    spi = ev / pv if pv else 1.0
    cpi = ev / ac if ac else 1.0
    eac = bac / cpi if cpi else bac
    return {
        "BAC": bac, "PV": pv, "EV": ev, "AC": ac,
        "SPI": spi, "CPI": cpi, "EAC": eac, "VAC": bac - eac,
        "avancement_reel": 100 * ev / bac,
        "avancement_prevu": 100 * pv / bac,
        "reserve": PROJECT_INFO["reserve_aleas_keur"],
        "reserve_consommee": PROJECT_INFO["reserve_consommee_keur"],
    }


def project_weather(spi: float, cpi: float) -> tuple[str, str, str]:
    """Météo projet à partir des indices de performance : (icône, libellé, explication)."""
    worst = min(spi, cpi)
    if worst >= 0.95:
        return "☀️", "Sous contrôle", "Délais et coûts conformes au plan."
    if worst >= 0.85:
        return "⛅", "Sous surveillance", "Écart modéré : un plan d'actions correctif est en cours."
    return "🌧️", "En difficulté", "Écart important : arbitrage du COPIL nécessaire."


def milestones_dataframe() -> pd.DataFrame:
    df = pd.DataFrame(MILESTONES)
    df["prevu"] = pd.to_datetime(df["prevu"])
    df["reel"] = pd.to_datetime(df["reel"].replace("", None))
    df["ecart_jours"] = (df["reel"] - df["prevu"]).dt.days

    def _status(row):
        if pd.notna(row["reel"]):
            return "Atteint" if row["ecart_jours"] <= 0 else f"Atteint (+{int(row['ecart_jours'])} j)"
        return "À venir" if row["prevu"] >= reporting_date() else "En retard"

    df["statut"] = df.apply(_status, axis=1)
    return df


def actions_dataframe() -> pd.DataFrame:
    df = pd.DataFrame(ACTIONS)
    df["echeance"] = pd.to_datetime(df["echeance"])
    return df


def budget_curve(df: pd.DataFrame | None = None) -> pd.DataFrame:
    """Courbe en S : valeur planifiée cumulée semaine par semaine + EV / AC à la date de reporting."""
    df = tasks_dataframe() if df is None else df
    weeks = pd.date_range(df["debut"].min(), df["fin"].max() + pd.Timedelta(days=7), freq="W-FRI")
    rows = []
    for w in weeks:
        pv = sum(
            b * planned_progress(s, e, w) / 100
            for b, s, e in zip(df["budget"], df["debut"], df["fin"])
        )
        rows.append({"semaine": w, "Valeur planifiée (PV)": round(pv, 1)})
    return pd.DataFrame(rows)
