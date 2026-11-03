"""Configuration générale de l'application."""

APP_CONFIG = {
    "title": "Nice Waste Management — Pilotage du projet de modernisation de la collecte",
    "short_title": "Nice Waste Management",
    "version": "2.0.0",
    "author": "Hanene Triaa",
}

MAP_CONFIG = {
    "center_lat": 43.7102,
    "center_lon": 7.2620,
    "default_zoom": 11.5,
}

# Palette sobre et cohérente pour tous les graphiques
COLORS = {
    "primary": "#0F766E",
    "secondary": "#2563EB",
    "success": "#16A34A",
    "warning": "#D97706",
    "danger": "#DC2626",
    "muted": "#94A3B8",
}

# Couleurs de statut utilisées dans le pilotage (RAG : Red / Amber / Green)
STATUS_COLORS = {
    "Terminé": "#16A34A",
    "En cours": "#2563EB",
    "En retard": "#DC2626",
    "À venir": "#94A3B8",
}

PHASE_COLORS = {
    "1. Cadrage & préparation": "#0F766E",
    "2. Déploiement pilote": "#2563EB",
    "3. Généralisation": "#7C3AED",
    "4. Exploitation & bilan": "#D97706",
}

CRITICITY_COLORS = {
    "Critique": "#DC2626",
    "Élevée": "#F97316",
    "Modérée": "#EAB308",
    "Faible": "#16A34A",
}
