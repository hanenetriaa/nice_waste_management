# src/data/stakeholders_data.py

STAKEHOLDERS_DATA = {
    "Stakeholder Principal": [
        # Citoyens
        "Citoyens de Nice", "Citoyens de Nice", "Citoyens de Nice", "Citoyens de Nice", "Citoyens de Nice",
        # Opérationnels
        "Chauffeurs", "Chauffeurs", "Direction des Déchets", "Direction des Déchets",
        # Associations
        "Associations", "Associations", 
        # Technique
        "Équipe Technique", "Équipe Technique", "Équipe Technique",
        # Administration
        "Mairie", "Mairie"
    ],
    "Sous-Groupe": [
        # Citoyens
        "Population générale", "Personnes âgées", "Familles", "Touristes", "Personnes handicapées",
        # Opérationnels
        "Nouveaux chauffeurs", "Chauffeurs expérimentés", "Planification", "Opérations",
        # Associations
        "Quartiers", "Environnement",
        # Technique
        "Développement App", "Infrastructure", "Support",
        # Administration
        "Direction", "Communication"
    ],
    "Phase Préparation (M1-M3)": [
        "Consultation", "Analyse besoins", "Analyse besoins", "", "",
        "Formation initiale", "Planification", "Analyse système", "Organisation",
        "Consultation", "Planification",
        "Spécifications", "Installation capteurs", "Préparation",
        "Validation", "Stratégie"
    ],
    "Phase Déploiement (M4-M6)": [
        "Sensibilisation", "Installation", "Préparation", "Documentation", "Adaptation",
        "Formation terrain", "GPS", "Tests", "Formation",
        "Pilotes", "Préparation",
        "Développement", "Tests capteurs", "Configuration",
        "Suivi", "Campagne"
    ],
    "Phase Opérationnelle (M7-M12)": [
        "Utilisation", "Support", "Adaptation", "Multilangue", "Support",
        "Exploitation", "Optimisation", "Production", "Gestion",
        "Animation", "Communication",
        "Maintenance", "Optimisation", "Support continu",
        "Évaluation", "Diffusion"
    ],
    "Niveau_Influence": [
        5, 3, 4, 2, 3,
        4, 5, 5, 4,
        3, 4,
        5, 4, 3,
        5, 4
    ],
    "Impact_Projet": [
        "Direct", "Direct", "Direct", "Indirect", "Direct",
        "Direct", "Direct", "Direct", "Direct",
        "Indirect", "Indirect",
        "Direct", "Direct", "Direct",
        "Direct", "Direct"
    ]
}

# Détails des phases
PHASES_PROJET = {
    "Phase 1 - Préparation": {
        "Durée": "3 mois",
        "Objectifs": [
            "Analyse des besoins",
            "Formation initiale",
            "Installation infrastructure",
            "Consultation stakeholders"
        ],
        "Livrables": [
            "Plan de déploiement",
            "Rapport d'analyse",
            "Programme de formation"
        ]
    },
    "Phase 2 - Déploiement": {
        "Durée": "3 mois",
        "Objectifs": [
            "Installation équipements",
            "Formation terrain",
            "Tests système",
            "Communication"
        ],
        "Livrables": [
            "Rapport de déploiement",
            "Documentation technique",
            "Plan de communication"
        ]
    },
    "Phase 3 - Opérationnelle": {
        "Durée": "6 mois",
        "Objectifs": [
            "Exploitation système",
            "Support continu",
            "Optimisation",
            "Évaluation"
        ],
        "Livrables": [
            "Rapport d'exploitation",
            "Indicateurs de performance",
            "Plan d'amélioration continue"
        ]
    }
}