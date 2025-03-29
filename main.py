import requests
from bs4 import BeautifulSoup

url = 'https://chrysler.fr/les-50-modeles-emblematiques-des-voitures-des-annees-2000/'  # Remplace par une URL réelle

response = requests.get(url)
soup = BeautifulSoup(response.content, 'html.parser')

# Trouve tous les titres d'articles
titres = soup.find_all('h2')

for i, titre in enumerate(titres, 1):
    print(f"{i}. {titre.get_text()}")

print("✅ Extraction terminée !")
