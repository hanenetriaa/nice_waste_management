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

    # Contact et support
    st.subheader("Contact et Support")
    st.write("""
    Pour toute question ou demande d'information supplémentaire :
    - Email: support.dechets@nicecotedazur.org
    - Téléphone: +33 4 XX XX XX XX
    - Adresse: XX Avenue XXXX, Nice
    """)

    # Mentions légales
    st.subheader("Mentions Légales")
    st.write("""
    Les données présentées dans cette application sont soumises aux droits d'auteur 
    et de propriété intellectuelle de la Métropole Nice Côte d'Azur. 
    Leur utilisation est autorisée dans le cadre de ce projet conformément aux 
    licences open data en vigueur.
    """)

def show_methodology():
    st.subheader("Méthodologie de Collecte des Données")
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