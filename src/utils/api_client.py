import requests
import os
from PIL import Image
import io

class APIClient:
    def __init__(self):
        self.dalle_api_key = os.getenv('DALLE_API_KEY')
        self.openai_api_key = os.getenv('OPENAI_API_KEY')

    def generate_image(self, prompt):
        """
        Génère une image avec DALL-E
        """
        if not self.dalle_api_key:
            return "https://placehold.co/600x400?text=Image+Placeholder"

        try:
            response = requests.post(
                "https://api.openai.com/v1/images/generations",
                headers={"Authorization": f"Bearer {self.dalle_api_key}"},
                json={
                    "prompt": prompt,
                    "n": 1,
                    "size": "1024x1024"
                }
            )
            return response.json()['data'][0]['url']
        except Exception as e:
            print(f"Erreur lors de la génération d'image: {e}")
            return "https://placehold.co/600x400?text=Error+Generating+Image"

    def generate_content(self, prompt):
        """
        Génère du contenu avec GPT
        """
        if not self.openai_api_key:
            return "Contenu exemple (API key non configurée)"

        try:
            response = requests.post(
                "https://api.openai.com/v1/completions",
                headers={"Authorization": f"Bearer {self.openai_api_key}"},
                json={
                    "model": "text-davinci-003",
                    "prompt": prompt,
                    "max_tokens": 150
                }
            )
            return response.json()['choices'][0]['text']
        except Exception as e:
            print(f"Erreur lors de la génération de contenu: {e}")
            return "Erreur lors de la génération du contenu"