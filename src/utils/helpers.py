# src/utils/helpers.py
import pandas as pd

def calculate_kpis(data):
    """Calcule les KPIs principaux"""
    return {
        "moyenne_tri": data["Taux_Tri"].mean(),
        "total_points": data["Points_Collecte"].sum(),
        "total_population": data["Population"].sum()
    }

def filter_quartiers(df, filters):
    """Filtre les données des quartiers selon les critères"""
    for key, value in filters.items():
        if value:
            df = df[df[key].isin(value)]
    return df