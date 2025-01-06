import requests
import os
from PIL import Image
import io

class ImageGenerator:
    def __init__(self):
        self.api_key = os.getenv('OPENAI_API_KEY')  # Clé API DALL-E
        
    def generate_image(self, prompt, size="1024x1024"):
        """
        Génère une image via l'API DALL-E
        """
        if not self.api_key:
            return self._generate_placeholder(prompt)
            
        headers = {
            "Content-Type": "application/json",
            "Authorization": f"Bearer {self.api_key}"
        }
        
        data = {
            "prompt": prompt,
            "n": 1,
            "size": size
        }
        
        try:
            response = requests.post(
                "https://api.openai.com/v1/images/generations",
                headers=headers,
                json=data
            )
            if response.status_code == 200:
                return response.json()['data'][0]['url']
            else:
                return self._generate_placeholder(prompt)
        except Exception as e:
            print(f"Erreur de génération d'image: {e}")
            return self._generate_placeholder(prompt)
    
    def _generate_placeholder(self, prompt):
        """
        Génère une image placeholder si l'API n'est pas disponible
        """
        encoded_prompt = prompt.replace(" ", "+")[:100]
        return f"https://placehold.co/1024x1024?text={encoded_prompt}"