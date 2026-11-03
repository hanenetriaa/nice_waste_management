"""Registre des risques du projet.

Probabilité et impact sont notés de 1 (très faible) à 5 (très fort).
Criticité = probabilité × impact. Les colonnes « résiduelles » estiment le niveau
de risque une fois le plan de réponse appliqué.
"""

RISKS = [
    {"id": "R01", "risque": "Accès difficile aux conteneurs dans les quartiers denses", "categorie": "Opérationnel",
     "zone": "Quartiers denses", "probabilite": 4, "impact": 5, "strategie": "Réduire",
     "reponse": "Créneaux de pose négociés avec la police municipale, véhicules plus petits",
     "responsable": "Direction des Déchets", "statut": "Ouvert", "tendance": "↗", "prob_residuelle": 3, "impact_residuel": 3},
    {"id": "R02", "risque": "Résistance des habitants au changement des habitudes de tri", "categorie": "Humain",
     "zone": "Tous quartiers", "probabilite": 5, "impact": 4, "strategie": "Réduire",
     "reponse": "Ambassadeurs du tri, ateliers de quartier, messages positifs et chiffrés",
     "responsable": "Communication", "statut": "Ouvert", "tendance": "↘", "prob_residuelle": 3, "impact_residuel": 3},
    {"id": "R03", "risque": "Vandalisme sur les conteneurs et capteurs", "categorie": "Technique",
     "zone": "Zones sensibles", "probabilite": 4, "impact": 4, "strategie": "Transférer",
     "reponse": "Capteurs encastrés, garantie de remplacement incluse dans le marché",
     "responsable": "Prestataire capteurs", "statut": "Ouvert", "tendance": "→", "prob_residuelle": 3, "impact_residuel": 2},
    {"id": "R04", "risque": "Augmentation des dépôts sauvages", "categorie": "Opérationnel",
     "zone": "Zones sensibles", "probabilite": 5, "impact": 5, "strategie": "Réduire",
     "reponse": "Signalement dans l'application, brigade d'intervention rapide sous 48 h",
     "responsable": "Direction des Déchets", "statut": "Ouvert", "tendance": "→", "prob_residuelle": 3, "impact_residuel": 4},
    {"id": "R05", "risque": "Conflits d'usage avec les commerces (horaires, encombrement)", "categorie": "Humain",
     "zone": "Zones commerciales", "probabilite": 4, "impact": 3, "strategie": "Réduire",
     "reponse": "Concertation avec les associations de commerçants, collecte dédiée",
     "responsable": "Chef de projet", "statut": "Ouvert", "tendance": "↘", "prob_residuelle": 2, "impact_residuel": 2},
    {"id": "R06", "risque": "Non-respect des horaires de sortie des bacs", "categorie": "Humain",
     "zone": "Centre-ville", "probabilite": 5, "impact": 3, "strategie": "Réduire",
     "reponse": "Rappels par notification dans l'application, affichage dans les halls",
     "responsable": "Communication", "statut": "Ouvert", "tendance": "→", "prob_residuelle": 3, "impact_residuel": 2},
    {"id": "R07", "risque": "Débordements en été liés à l'afflux touristique", "categorie": "Opérationnel",
     "zone": "Zones touristiques", "probabilite": 5, "impact": 5, "strategie": "Réduire",
     "reponse": "Plan de collecte renforcé été (T16), passages déclenchés par les capteurs",
     "responsable": "Direction des Déchets", "statut": "Ouvert", "tendance": "↘", "prob_residuelle": 3, "impact_residuel": 3},
    {"id": "R08", "risque": "Communication peu efficace auprès des touristes", "categorie": "Humain",
     "zone": "Zones touristiques", "probabilite": 3, "impact": 3, "strategie": "Réduire",
     "reponse": "Application et supports en FR / EN / IT, relais dans les hôtels",
     "responsable": "Communication", "statut": "Maîtrisé", "tendance": "↘", "prob_residuelle": 2, "impact_residuel": 2},
    {"id": "R09", "risque": "Retard du prestataire dans la pose des capteurs", "categorie": "Planning",
     "zone": "Tous quartiers", "probabilite": 4, "impact": 4, "strategie": "Réduire",
     "reponse": "Pénalités contractuelles, 2 équipes supplémentaires (décision COPIL du 08/07)",
     "responsable": "Chef de projet", "statut": "Ouvert", "tendance": "↗", "prob_residuelle": 3, "impact_residuel": 3},
    {"id": "R10", "risque": "Dépassement du budget", "categorie": "Financier",
     "zone": "Projet", "probabilite": 3, "impact": 4, "strategie": "Réduire",
     "reponse": "Suivi mensuel de la valeur acquise, réserve pour aléas de 120 k€, arbitrages COPIL",
     "responsable": "Chef de projet", "statut": "Ouvert", "tendance": "↗", "prob_residuelle": 2, "impact_residuel": 3},
    {"id": "R11", "risque": "Défaillance technique des capteurs (batterie, réseau)", "categorie": "Technique",
     "zone": "Tous quartiers", "probabilite": 3, "impact": 4, "strategie": "Transférer",
     "reponse": "Engagement de disponibilité de 98 % dans le contrat, supervision en temps réel",
     "responsable": "Équipe technique (DSI)", "statut": "Ouvert", "tendance": "→", "prob_residuelle": 2, "impact_residuel": 3},
    {"id": "R12", "risque": "Mauvaise coordination entre services municipaux", "categorie": "Organisationnel",
     "zone": "Projet", "probabilite": 3, "impact": 3, "strategie": "Réduire",
     "reponse": "Comité projet hebdomadaire, matrice RACI partagée",
     "responsable": "Chef de projet", "statut": "Maîtrisé", "tendance": "↘", "prob_residuelle": 2, "impact_residuel": 2},
]


def criticity_level(score: int) -> str:
    if score >= 20:
        return "Critique"
    if score >= 12:
        return "Élevée"
    if score >= 6:
        return "Modérée"
    return "Faible"
