# src/data/communication_data.py

from datetime import datetime, timedelta

def get_training_plan():
    return [
        {"Équipe": "Agents de terrain", "Formation nécessaire": "Formation sur l’utilisation des capteurs et logiciels associés", "Canaux de Formation": "Sessions pratiques sur le terrain et en ligne"},
        {"Équipe": "Équipes de communication", "Formation nécessaire": "Gestion des réseaux sociaux, interactions citoyennes", "Canaux de Formation": "Ateliers et formations en ligne, webinaires"},
        {"Équipe": "Responsables locaux", "Formation nécessaire": "Animation de réunions et ateliers citoyens", "Canaux de Formation": "Réunions participatives, ateliers"}
    ]

def get_key_audiences():
    return {
        "Mairie de Nice": {
            "Message": "Bénéfices stratégiques pour la ville en matière d’écologie et d’efficacité.",
            "Canaux": "Rapports mensuels, réunions stratégiques.",
            "Fréquence": "Mensuelle"
        },
        "Citoyens de Nice": {
            "Message": "Agissons ensemble pour une ville plus propre et durable.",
            "Canaux": "Réseaux sociaux, brochures, ateliers locaux, application mobile.",
            "Fréquence": "Bimensuelle"
        },
        "Associations de Quartier": {
            "Message": "Devenez des ambassadeurs du tri sélectif dans votre quartier.",
            "Canaux": "Réunions participatives, campagnes locales.",
            "Fréquence": "Trimestrielle"
        },
        "Chauffeurs de Collecte et Agents de Tri": {
            "Message": "Des outils modernes pour faciliter votre travail quotidien.",
            "Canaux": "Sessions de formation, plateforme intranet dédiée.",
            "Fréquence": "Bimensuelle"
        },
        "Touristes": {
            "Message": "Nice, une destination écoresponsable.",
            "Canaux": "Brochures multilingues, affichages dans les hôtels et lieux touristiques.",
            "Fréquence": "Continuellement"
        }
    }

def get_key_events():
    return [
        {"Événement": "Lancement du projet", "Date": datetime(2024, 1, 15)},
        {"Événement": "Semaine Européenne de la Réduction des Déchets", "Date": datetime(2024, 3, 25)},
        {"Événement": "Journées portes ouvertes", "Date": datetime(2024, 6, 10)}
    ]

def get_crisis_plan():
    return [
        {"Situation": "Panne des capteurs", "Responsable": "Direction des déchets", "Actions": "Communication interne, alerte sur l’application citoyenne", "Délai de réponse": "24h"},
        {"Situation": "Non-conformité des données", "Responsable": "Direction des données", "Actions": "Audit immédiat des capteurs et mise à jour des informations", "Délai de réponse": "24h"}
    ]

def get_revision_schedule():
    current_date = datetime.now()
    next_revision = current_date + timedelta(weeks=26)
    return f"Prochaine révision prévue pour le : {next_revision.strftime('%d %B %Y')}"

def get_feedback_and_improvement():
    return {
        "Feedback et Amélioration": {
            "Boucle de retour": "Sondages réguliers auprès des citoyens, chauffeurs, et agents de tri pour recueillir des retours.",
            "Analyse": "Rapports trimestriels pour ajuster les stratégies.",
            "KPI de succès": [
                "% d’augmentation du recyclage",
                "Réduction du temps moyen de collecte",
                "Satisfaction citoyenne > 80 %"
            ]
        }
    }

def get_strategic_objectives():
    return {
        "Réduction des déchets non triés et augmentation du taux de recyclage": "Mise en place de technologies pour faciliter le tri et augmenter les volumes recyclés.",
        "Optimisation des trajets de collecte pour réduire les émissions de CO₂": "Utilisation de données de capteurs pour optimiser les trajets de collecte.",
        "Amélioration de la satisfaction des citoyens grâce à des services modernisés et accessibles": "Offrir des services innovants et accessibles à tous."
    }

def get_communication_objectives():
    return {
        "Informer": "Sensibiliser les citoyens et parties prenantes sur les nouvelles pratiques et technologies.",
        "Impliquer": "Encourager l’adoption des nouvelles initiatives par un engagement actif des citoyens et des associations locales.",
        "Fidéliser": "Renforcer la confiance des parties prenantes dans les capacités du projet à atteindre ses objectifs écologiques et sociaux."
    }
