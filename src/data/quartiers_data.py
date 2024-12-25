# src/data/quartiers_data.py

QUARTIERS_DATA = {
    "Nom": [
        "Vieux-Nice", "Jean-Médecin", "Cimiez", "Port", "Libération",
        "Riquier", "Saint-Roch", "Arenas", "Fabron", "Saint-Isidore",
        "L'Ariane", "Les Moulins", "Las Planas", "Pasteur", "Saint-Augustin"
    ],
    "Population": [
        25000, 35000, 22000, 18000, 28000,
        20000, 24000, 15000, 17000, 12000,
        12000, 10000, 8000, 15000, 13000
    ],
    "Points_Collecte": [
        45, 55, 35, 40, 42,
        38, 36, 30, 32, 25,
        30, 28, 25, 32, 30
    ],
    "Latitude": [
        43.6967, 43.7016, 43.7150, 43.6950, 43.7080,
        43.7050, 43.7100, 43.6650, 43.6850, 43.7200,
        43.7283, 43.6717, 43.7367, 43.7183, 43.6733
    ],
    "Longitude": [
        7.2738, 7.2683, 7.2700, 7.2850, 7.2600,
        7.2900, 7.2800, 7.2150, 7.2450, 7.1900,
        7.3100, 7.2100, 7.2833, 7.2917, 7.2083
    ],
    "Type_Zone": [
        "Touristique", "Commercial", "Résidentiel", "Maritime", "Mixte",
        "Résidentiel", "Mixte", "Activités", "Résidentiel", "Périurbain",
        "Sensible", "Sensible", "Sensible", "Sensible", "Mixte"
    ],
    "Densité": [
        "Très élevée", "Élevée", "Modérée", "Élevée", "Élevée",
        "Modérée", "Élevée", "Modérée", "Faible", "Faible",
        "Très élevée", "Très élevée", "Élevée", "Élevée", "Élevée"
    ],
    "Complexité_Collecte": [
        "Très élevée", "Élevée", "Moyenne", "Élevée", "Moyenne",
        "Moyenne", "Élevée", "Faible", "Moyenne", "Faible",
        "Très élevée", "Très élevée", "Élevée", "Élevée", "Moyenne"
    ],
    "Taux_Tri": [
        75, 68, 72, 70, 65,
        67, 64, 66, 69, 63,
        55, 58, 57, 60, 62
    ],
    "Caractéristiques_Spécifiques": [
        "Rues étroites, haute fréquentation touristique",
        "Zone piétonne, commerces nombreux",
        "Habitat collectif, espaces verts",
        "Activité portuaire, restaurants",
        "Marché quotidien, transports",
        "Proche port, résidentiel dense",
        "Mixité habitat/commerce",
        "Zone industrielle, aéroport",
        "Collines, villas",
        "Zone périphérique, stade",
        "Collectifs sociaux, accès difficile",
        "Grand ensemble, forte densité",
        "Relief marqué, accès complexe",
        "Zone dense, axes routiers",
        "Proximité aéroport, activités"
    ],
    "Défis_Principaux": [
        "Accès véhicules, horaires stricts",
        "Gestion flux commerciaux",
        "Topographie, dispersion points",
        "Coordination port/ville",
        "Gestion marchés/événements",
        "Stationnement gênant",
        "Diversité usages",
        "Activités industrielles",
        "Accès collines",
        "Distances importantes",
        "Infrastructures, sécurité",
        "Densité population",
        "Relief, enclavement",
        "Circulation dense",
        "Bruit aéroport"
    ],
    "Volume_Moyen_Mensuel": [
        120, 150, 90, 100, 110,
        85, 95, 70, 65, 50,
        80, 75, 60, 85, 70
    ]
}

# Statistiques complémentaires
STATISTIQUES_COMPLEMENTAIRES = {
    "Équipements": {
        "Conteneurs_Standards": 450,
        "Points_Tri_Selectif": 280,
        "Composteurs_Collectifs": 45,
        "Points_Collecte_Spéciaux": 30
    },
    "Performance_Globale": {
        "Taux_Moyen_Tri": 65.8,
        "Taux_Satisfaction": 72,
        "Volume_Total_Annuel": 156000,
        "Coût_Moyen_Tonne": 285
    }
}

# Calendrier collecte
CALENDRIER_COLLECTE = {
    "Matin": "06:00-11:00",
    "Après-midi": "15:00-19:00",
    "Soirée": "20:00-23:00",
    "Fréquence_Standard": "Quotidienne",
    "Fréquence_Tri": "Bi-hebdomadaire"
}