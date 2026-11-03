"""Données de pilotage du projet de modernisation de la collecte des déchets à Nice.

Scénario de cas d'étude : projet de 12 mois (janvier → décembre 2025) visant à
équiper la ville de capteurs de remplissage, optimiser les tournées de collecte,
lancer une application citoyenne et accompagner le changement.

Les chiffres de planning, budget et avancement sont SIMULÉS pour illustrer une
démarche de pilotage ; ils ne proviennent pas de la Métropole Nice Côte d'Azur.
"""

PROJECT_INFO = {
    "nom": "Modernisation de la collecte des déchets — Ville de Nice",
    "sponsor": "Élu délégué à l'environnement (COPIL)",
    "chef_de_projet": "Hanene Triaa",
    "debut": "2025-01-06",
    "fin": "2025-12-19",
    "date_reporting": "2025-07-11",
    "reserve_aleas_keur": 120,
    "reserve_consommee_keur": 57,
    "objectif": (
        "Augmenter le taux de tri, réduire les kilomètres parcourus par les camions "
        "et améliorer la satisfaction des habitants grâce à des conteneurs connectés, "
        "des tournées optimisées et une application citoyenne."
    ),
    "perimetre_inclus": [
        "15 quartiers de Nice, déploiement en 2 temps (pilote sur 3 quartiers puis généralisation)",
        "Capteurs de remplissage sur les conteneurs de tri et d'ordures ménagères",
        "Optimisation des tournées à partir des données capteurs",
        "Application citoyenne (signalements, points de collecte, horaires) en FR/EN/IT",
        "Formation des chauffeurs et agents, campagnes de sensibilisation",
    ],
    "perimetre_exclu": [
        "Renouvellement de la flotte de camions",
        "Collecte des encombrants et déchetteries",
        "Communes de la Métropole hors Nice",
    ],
}

# Organigramme des tâches (WBS). Budgets et coûts en k€.
# "avancement" = % réalisé à la date de reporting.
TASKS = [
    # Phase 1
    {"id": "T01", "tache": "Note de cadrage & charte projet", "phase": "1. Cadrage & préparation",
     "debut": "2025-01-06", "fin": "2025-01-24", "responsable": "Chef de projet",
     "avancement": 100, "budget": 15, "cout_reel": 14, "predecesseurs": ""},
    {"id": "T02", "tache": "Diagnostic territorial des 15 quartiers", "phase": "1. Cadrage & préparation",
     "debut": "2025-01-13", "fin": "2025-02-21", "responsable": "Chef de projet",
     "avancement": 100, "budget": 45, "cout_reel": 48, "predecesseurs": "T01"},
    {"id": "T03", "tache": "Cartographie & consultation des parties prenantes", "phase": "1. Cadrage & préparation",
     "debut": "2025-01-20", "fin": "2025-02-28", "responsable": "Chef de projet",
     "avancement": 100, "budget": 30, "cout_reel": 27, "predecesseurs": "T01"},
    {"id": "T04", "tache": "Cahier des charges capteurs & appel d'offres", "phase": "1. Cadrage & préparation",
     "debut": "2025-02-03", "fin": "2025-03-21", "responsable": "Direction des Déchets",
     "avancement": 100, "budget": 60, "cout_reel": 62, "predecesseurs": "T02"},
    {"id": "T05", "tache": "Spécifications de l'application citoyenne", "phase": "1. Cadrage & préparation",
     "debut": "2025-02-17", "fin": "2025-03-28", "responsable": "Équipe technique (DSI)",
     "avancement": 100, "budget": 40, "cout_reel": 38, "predecesseurs": "T03"},
    # Phase 2
    {"id": "T06", "tache": "Installation des capteurs — 3 quartiers pilotes", "phase": "2. Déploiement pilote",
     "debut": "2025-03-31", "fin": "2025-05-16", "responsable": "Prestataire capteurs",
     "avancement": 100, "budget": 380, "cout_reel": 410, "predecesseurs": "T04"},
    {"id": "T07", "tache": "Développement de l'application citoyenne (MVP)", "phase": "2. Déploiement pilote",
     "debut": "2025-03-31", "fin": "2025-06-13", "responsable": "Équipe technique (DSI)",
     "avancement": 100, "budget": 220, "cout_reel": 236, "predecesseurs": "T05"},
    {"id": "T08", "tache": "Formation des chauffeurs des quartiers pilotes", "phase": "2. Déploiement pilote",
     "debut": "2025-04-22", "fin": "2025-05-30", "responsable": "Direction des Déchets",
     "avancement": 100, "budget": 35, "cout_reel": 33, "predecesseurs": "T06"},
    {"id": "T09", "tache": "Campagne de sensibilisation pilote", "phase": "2. Déploiement pilote",
     "debut": "2025-05-05", "fin": "2025-06-20", "responsable": "Communication",
     "avancement": 100, "budget": 60, "cout_reel": 55, "predecesseurs": "T03"},
    {"id": "T10", "tache": "Bilan du pilote & décision Go / No-Go", "phase": "2. Déploiement pilote",
     "debut": "2025-06-16", "fin": "2025-06-27", "responsable": "Chef de projet",
     "avancement": 100, "budget": 10, "cout_reel": 10, "predecesseurs": "T06, T07"},
    # Phase 3
    {"id": "T11", "tache": "Installation des capteurs — 12 quartiers restants", "phase": "3. Généralisation",
     "debut": "2025-06-30", "fin": "2025-10-10", "responsable": "Prestataire capteurs",
     "avancement": 4, "budget": 900, "cout_reel": 62, "predecesseurs": "T10"},
    {"id": "T12", "tache": "Optimisation des tournées (algorithme + paramétrage)", "phase": "3. Généralisation",
     "debut": "2025-06-30", "fin": "2025-09-05", "responsable": "Équipe technique (DSI)",
     "avancement": 18, "budget": 120, "cout_reel": 24, "predecesseurs": "T10"},
    {"id": "T13", "tache": "Ouverture de l'application à toute la ville", "phase": "3. Généralisation",
     "debut": "2025-07-07", "fin": "2025-09-26", "responsable": "Équipe technique (DSI)",
     "avancement": 6, "budget": 150, "cout_reel": 10, "predecesseurs": "T07, T10"},
    {"id": "T14", "tache": "Formation de l'ensemble des chauffeurs", "phase": "3. Généralisation",
     "debut": "2025-07-21", "fin": "2025-10-17", "responsable": "Direction des Déchets",
     "avancement": 0, "budget": 80, "cout_reel": 0, "predecesseurs": "T11"},
    {"id": "T15", "tache": "Campagne grand public & réseau d'ambassadeurs du tri", "phase": "3. Généralisation",
     "debut": "2025-09-01", "fin": "2025-10-31", "responsable": "Communication",
     "avancement": 0, "budget": 140, "cout_reel": 0, "predecesseurs": "T09"},
    {"id": "T16", "tache": "Plan de collecte renforcé été (zones touristiques)", "phase": "3. Généralisation",
     "debut": "2025-06-23", "fin": "2025-08-29", "responsable": "Direction des Déchets",
     "avancement": 28, "budget": 70, "cout_reel": 21, "predecesseurs": ""},
    # Phase 4
    {"id": "T17", "tache": "Exploitation & support de niveau 1", "phase": "4. Exploitation & bilan",
     "debut": "2025-11-03", "fin": "2025-12-12", "responsable": "Direction des Déchets",
     "avancement": 0, "budget": 90, "cout_reel": 0, "predecesseurs": "T11, T13"},
    {"id": "T18", "tache": "Évaluation des indicateurs & retour d'expérience", "phase": "4. Exploitation & bilan",
     "debut": "2025-11-24", "fin": "2025-12-12", "responsable": "Chef de projet",
     "avancement": 0, "budget": 25, "cout_reel": 0, "predecesseurs": "T17"},
    {"id": "T19", "tache": "Clôture & rapport final au COPIL", "phase": "4. Exploitation & bilan",
     "debut": "2025-12-08", "fin": "2025-12-19", "responsable": "Chef de projet",
     "avancement": 0, "budget": 10, "cout_reel": 0, "predecesseurs": "T18"},
]

MILESTONES = [
    {"jalon": "COPIL de lancement", "prevu": "2025-01-06", "reel": "2025-01-06", "critere": "Charte projet signée par le sponsor"},
    {"jalon": "Validation du cadrage", "prevu": "2025-02-28", "reel": "2025-02-28", "critere": "Périmètre, budget et quartiers pilotes validés"},
    {"jalon": "Attribution du marché capteurs", "prevu": "2025-03-21", "reel": "2025-03-28", "critere": "Contrat notifié au prestataire"},
    {"jalon": "MVP de l'application livré", "prevu": "2025-06-13", "reel": "2025-06-13", "critere": "Recette utilisateurs validée"},
    {"jalon": "Go / No-Go généralisation", "prevu": "2025-06-27", "reel": "2025-06-27", "critere": "Indicateurs pilotes ≥ objectifs intermédiaires"},
    {"jalon": "50 % des capteurs installés", "prevu": "2025-08-22", "reel": "", "critere": "Recette terrain sur 6 quartiers"},
    {"jalon": "Application ouverte à toute la ville", "prevu": "2025-09-26", "reel": "", "critere": "Tests de charge OK, support en place"},
    {"jalon": "Fin de la généralisation", "prevu": "2025-10-31", "reel": "", "critere": "15 quartiers équipés, chauffeurs formés"},
    {"jalon": "Clôture du projet", "prevu": "2025-12-19", "reel": "", "critere": "Rapport final validé en COPIL"},
]

# Matrice RACI : R = Réalise, A = Approuve (un seul A par activité), C = Consulté, I = Informé
RACI_ROLES = [
    "Chef de projet", "COPIL", "Dir. Déchets", "DSI", "Communication", "Prestataire", "Associations",
]
RACI = {
    "Cadrage & charte projet":            ["R", "A", "C", "C", "I", "",  "I"],
    "Diagnostic territorial":             ["A", "I", "R", "C", "I", "",  "C"],
    "Appel d'offres capteurs":            ["R", "I", "A", "C", "",  "",  ""],
    "Installation des capteurs":          ["A", "I", "C", "C", "I", "R", "I"],
    "Développement de l'application":     ["A", "I", "C", "R", "C", "C", "C"],
    "Formation des chauffeurs":           ["C", "",  "A", "C", "",  "R", ""],
    "Campagnes de sensibilisation":       ["A", "I", "C", "",  "R", "",  "C"],
    "Décision Go / No-Go":                ["R", "A", "C", "C", "I", "I", "I"],
    "Suivi budgétaire & reporting":       ["R", "A", "C", "C", "",  "",  ""],
    "Gestion des risques":                ["A", "I", "R", "R", "C", "C", "C"],
}

GOVERNANCE = [
    {"instance": "Comité de pilotage (COPIL)", "frequence": "Mensuelle",
     "participants": "Élu délégué, DGS, Direction des Déchets, Chef de projet",
     "role": "Arbitrages budget / périmètre / planning, décisions Go / No-Go"},
    {"instance": "Comité projet", "frequence": "Hebdomadaire",
     "participants": "Chef de projet, référents DSI, Déchets, Communication",
     "role": "Suivi du planning, des risques et du plan d'actions"},
    {"instance": "Comité technique", "frequence": "Toutes les 2 semaines",
     "participants": "DSI, prestataire capteurs, Chef de projet",
     "role": "Intégration capteurs / application / algorithme de tournées"},
    {"instance": "Point terrain", "frequence": "Hebdomadaire (pendant le déploiement)",
     "participants": "Chefs d'équipe, chauffeurs référents, Chef de projet",
     "role": "Remontées du terrain, ajustements opérationnels"},
    {"instance": "Comité usagers", "frequence": "Trimestrielle",
     "participants": "Associations de quartier, conseils de quartier",
     "role": "Retours d'usage, co-construction des campagnes"},
]

DECISIONS = [
    {"date": "2025-01-06", "instance": "COPIL", "decision": "Périmètre validé : 15 quartiers, approche pilote sur 3 quartiers avant généralisation",
     "impact": "Réduit le risque de déploiement à grande échelle"},
    {"date": "2025-02-28", "instance": "COPIL", "decision": "Quartiers pilotes : Vieux-Nice (touristique), L'Ariane (sensible), Cimiez (résidentiel)",
     "impact": "Pilote représentatif des 3 grands types de zones"},
    {"date": "2025-03-28", "instance": "COPIL", "decision": "Attribution du marché capteurs avec 1 semaine de décalage acceptée",
     "impact": "Absorbé par la marge du chemin critique"},
    {"date": "2025-05-20", "instance": "Comité projet", "decision": "Ajout de l'anglais et de l'italien dans l'application",
     "impact": "+12 k€ pris sur la réserve pour aléas"},
    {"date": "2025-06-27", "instance": "COPIL", "decision": "GO pour la généralisation, sous réserve d'un plan de rattrapage sur la pose des capteurs",
     "impact": "Lancement de la phase 3 à la date prévue"},
    {"date": "2025-07-08", "instance": "COPIL", "decision": "Renfort de 2 équipes de pose en zone dense",
     "impact": "+45 k€ pris sur la réserve ; objectif : rattraper le retard d'ici fin août"},
]

ACTIONS = [
    {"id": "A11", "action": "Diffuser le retour d'expérience du pilote aux équipes", "porteur": "Chef de projet",
     "echeance": "2025-07-04", "statut": "Fait"},
    {"id": "A12", "action": "Sécuriser les créneaux de pose avec la police municipale (Vieux-Nice, Port)", "porteur": "Chef de projet",
     "echeance": "2025-07-18", "statut": "En cours"},
    {"id": "A13", "action": "Mettre en œuvre le plan de rattrapage (2 équipes supplémentaires)", "porteur": "Prestataire capteurs",
     "echeance": "2025-07-25", "statut": "En cours"},
    {"id": "A14", "action": "Recruter 10 ambassadeurs du tri via les associations", "porteur": "Communication",
     "echeance": "2025-08-29", "statut": "À faire"},
    {"id": "A15", "action": "Réaliser les tests de charge de l'application", "porteur": "Équipe technique (DSI)",
     "echeance": "2025-09-12", "statut": "À faire"},
    {"id": "A16", "action": "Préparer le dossier d'arbitrage budgétaire pour le COPIL de septembre", "porteur": "Chef de projet",
     "echeance": "2025-09-05", "statut": "À faire"},
]

# Indicateurs de réussite (objectifs SMART) : valeur de départ, actuelle et cible fin 2025
PROJECT_KPIS = [
    {"indicateur": "Taux de tri moyen (%)", "depart": 64.7, "actuel": 66.0, "cible": 70.0, "sens": "hausse"},
    {"indicateur": "Conteneurs qui débordent (%)", "depart": 18.0, "actuel": 13.0, "cible": 8.0, "sens": "baisse"},
    {"indicateur": "Kilomètres parcourus par les camions (indice)", "depart": 100, "actuel": 96, "cible": 85, "sens": "baisse"},
    {"indicateur": "Satisfaction des habitants (%)", "depart": 72, "actuel": 75, "cible": 80, "sens": "hausse"},
    {"indicateur": "Utilisateurs actifs de l'application", "depart": 0, "actuel": 4800, "cible": 20000, "sens": "hausse"},
]

# Résultats du pilote (avant / après 3 mois) dans les 3 quartiers pilotes
PILOT_RESULTS = [
    {"quartier": "Vieux-Nice", "indicateur": "Taux de tri (%)", "avant": 75, "apres": 79},
    {"quartier": "L'Ariane", "indicateur": "Taux de tri (%)", "avant": 55, "apres": 61},
    {"quartier": "Cimiez", "indicateur": "Taux de tri (%)", "avant": 72, "apres": 75},
    {"quartier": "Vieux-Nice", "indicateur": "Débordements (%)", "avant": 24, "apres": 10},
    {"quartier": "L'Ariane", "indicateur": "Débordements (%)", "avant": 21, "apres": 9},
    {"quartier": "Cimiez", "indicateur": "Débordements (%)", "avant": 12, "apres": 6},
    {"quartier": "Vieux-Nice", "indicateur": "Km par tournée (indice)", "avant": 100, "apres": 91},
    {"quartier": "L'Ariane", "indicateur": "Km par tournée (indice)", "avant": 100, "apres": 87},
    {"quartier": "Cimiez", "indicateur": "Km par tournée (indice)", "avant": 100, "apres": 88},
]

LESSONS_LEARNED = [
    "Impliquer les chauffeurs dès les spécifications : leurs retours ont modifié 30 % des écrans de l'application embarquée.",
    "La pose en zone dense prend 2 fois plus de temps que prévu (stationnement, horaires) : planifier avec la police municipale.",
    "Les associations sont le meilleur relais dans les quartiers sensibles : +6 points de tri à L'Ariane.",
    "Prévoir le multilingue dès le départ dans une ville touristique.",
]
