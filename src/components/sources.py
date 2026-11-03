import streamlit as st

def show_sources():
    st.header("Sources et Documentation")

    # Sources principales
    sources_data = {
        "Données Démographiques": {
            "source": "INSEE - Population légale 2021",
            "lien": "https://www.insee.fr/fr/statistiques/6683035?geo=COM-06088",
            "description": "Données démographiques officielles pour Nice et ses quartiers",
            "dernière_mise_à_jour": "2021"
        },
        "Gestion des Déchets": {
            "source": "Métropole Nice Côte d'Azur - Rapport annuel 2023",
            "lien": "https://www.nicecotedazur.org/environnement/propreté/collecte-des-déchets",
            "description": "Rapport annuel sur la gestion des déchets dans la métropole",
            "dernière_mise_à_jour": "2023"
        },
        "Données Quartiers": {
            "source": "Mairie de Nice - Open Data",
            "lien": "https://opendata.nicecotedazur.org/",
            "description": "Données ouvertes sur les quartiers de Nice",
            "dernière_mise_à_jour": "2024"
        },
        "Plans d'Urbanisme": {
            "source": "PLU Nice",
            "lien": "https://www.nice.fr/fr/urbanisme",
            "description": "Plan Local d'Urbanisme et données territoriales",
            "dernière_mise_à_jour": "2023"
        },
        "Statistiques Environnementales": {
            "source": "ADEME - Observatoire des déchets",
            "lien": "https://www.ademe.fr/",
            "description": "Données nationales sur la gestion des déchets",
            "dernière_mise_à_jour": "2023"
        }
    }

    # Documentation technique
    documentation_data = {
        "Méthodologie": [
            "Analyse des flux de déchets",
            "Calcul des indicateurs de performance",
            "Méthodologie d'échantillonnage",
            "Protocoles de mesure"
        ],
        "Standards Techniques": [
            "Normes ISO 14001 - Management environnemental",
            "Réglementation européenne sur les déchets",
            "Standards locaux de collecte"
        ],
        "Outils Utilisés": [
            "Systèmes de géolocalisation",
            "Logiciels d'optimisation des tournées",
            "Outils de monitoring en temps réel"
        ]
    }

    # Affichage des sources
    st.subheader("Sources des Données")
    for categorie, details in sources_data.items():
        with st.expander(categorie):
            st.write(f"**Source:** {details['source']}")
            st.write(f"**Description:** {details['description']}")
            st.write(f"**Dernière mise à jour:** {details['dernière_mise_à_jour']}")
            st.write(f"**Lien:** [{details['lien']}]({details['lien']})")

    # Affichage de la documentation
    st.subheader("Documentation Technique")
    for categorie, items in documentation_data.items():
        with st.expander(categorie):
            for item in items:
                st.write(f"- {item}")

    show_methodology()

    st.subheader("Nature des données")
    st.info(
        "Ce projet est un **cas d'étude**. Les données démographiques et territoriales s'appuient sur les "
        "sources publiques ci-dessus (valeurs arrondies). Les données de pilotage (planning, budget, avancement, "
        "risques, résultats du pilote) sont **simulées** pour illustrer une démarche de gestion de projet et ne "
        "reflètent pas l'activité réelle de la Métropole Nice Côte d'Azur."
    )

    st.subheader("Méthodes de gestion de projet utilisées")
    st.markdown(
        "- **Charte projet** : objectifs, périmètre inclus / exclu, sponsor, budget\n"
        "- **WBS et diagramme de Gantt** avec dépendances et jalons\n"
        "- **Valeur acquise (EVM)** : PV, EV, AC, SPI, CPI, EAC\n"
        "- **Matrice RACI** avec contrôle d'unicité du « A »\n"
        "- **Registre des risques** : criticité probabilité × impact, stratégies de réponse, risque résiduel\n"
        "- **Grille pouvoir / intérêt** des parties prenantes (Mendelow)\n"
        "- **Gouvernance** : COPIL, comité projet, journal des décisions et plan d'actions"
    )


def show_methodology():
    st.subheader("Méthodologie de collecte des données")
    methodologie = {
        "Collecte des données": [
            "Recensement exhaustif des points de collecte",
            "Mesures quotidiennes des volumes collectés",
            "Enquêtes de satisfaction auprès des usagers",
            "Audits des circuits de collecte"
        ],
        "Traitement des données": [
            "Normalisation des données brutes",
            "Agrégation par quartier et par type de déchet",
            "Calcul des indicateurs de performance",
            "Validation croisée des résultats"
        ],
        "Mise à jour": [
            "Actualisation mensuelle des données de collecte",
            "Révision trimestrielle des indicateurs",
            "Mise à jour annuelle des données démographiques"
        ]
    }

    for categorie, items in methodologie.items():
        with st.expander(categorie):
            for item in items:
                st.write(f"- {item}")