class CampaignTemplates:
    @staticmethod
    def get_seasonal_templates():
        return {
            "Été": {
                "Plages Propres": {
                    "title": "Nice Plages Propres 2024",
                    "content": """
                    🏖️ Un été responsable à Nice !
                    
                    ♻️ Nouveaux points de collecte sur toutes les plages
                    🗑️ Poubelles de tri tous les 50m
                    📱 Localisez le point le plus proche sur l'app
                    
                    Ensemble, préservons notre littoral !
                    #NicePlagesPropres #NiceDurable
                    """,
                    "channels": ["Instagram", "Facebook", "Application"],
                    "frequency": "Quotidienne",
                    "duration": "Juin-Septembre"
                },
                "Tourisme Responsable": {
                    "title": "Welcome to Eco-Friendly Nice",
                    "content": """
                    🌍 Welcome to Nice!
                    
                    Help us keep our city clean:
                    ✅ Use recycling bins
                    ✅ Download our app
                    ✅ Join local initiatives
                    
                    Available in 🇫🇷 🇬🇧 🇮🇹
                    #VisitNice #GreenTourism
                    """,
                    "channels": ["Hotels", "Tourist Office", "Social Media"],
                    "frequency": "Continue",
                    "duration": "Mai-Octobre"
                }
            },
            "Événements": {
                "Carnaval": {
                    "title": "Carnaval Éco-Responsable",
                    "content": {...},
                },
                "Festivals": {...}
            }
        }

    @staticmethod
    def get_emergency_templates():
        return {
            "Perturbation Service": {
                "title": "Information Collecte",
                "content": """
                ⚠️ Information importante
                
                En raison de [CAUSE], la collecte est temporairement modifiée dans votre quartier.
                
                📅 Date : [DATE]
                📍 Zone : [QUARTIER]
                ♻️ Solution temporaire : [ALTERNATIVE]
                
                Merci de votre compréhension.
                """,
                "channels": ["SMS", "App", "Social Media"],
                "priority": "Haute"
            }
        }

    @staticmethod
    def get_educational_templates():
        return {
            "Guide du Tri": {
                "title": "Guide Pratique du Tri à Nice",
                "sections": [
                    {
                        "title": "Les Bases du Tri",
                        "content": "..."
                    },
                    {
                        "title": "Points de Collecte",
                        "content": "..."
                    }
                ]
            }
        }