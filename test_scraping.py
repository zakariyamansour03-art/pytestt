import requests
from bs4 import BeautifulSoup

# 1. Télécharger la page HTML [cite: 83]
url = "http://books.toscrape.com"
reponse = requests.get(url)

# 2. Vérifier que la requête a réussi [cite: 83]
if reponse.status_code != 200:
    print("Impossible de charger la page.")
else:
    # 3. Analyser le HTML avec BeautifulSoup [cite: 83]
    soupe = BeautifulSoup(reponse.text, "html.parser")

    # 4. Trouver tous les articles (livres) de la page [cite: 83]
    # Ga3 l-ktob f l-site 3ndhom class="product_pod" [cite: 79]
    livres = soupe.find_all("article", class_="product_pod")

    print(f"Nombre de livres trouvés : {len(livres)}")
    print("-" * 50)

    # 5. Extraire le titre et le prix de chaque livre [cite: 83]
    for i, livre in enumerate(livres, 1):
        # Le titre est dans h3 -> a (attribut title) [cite: 80]
        titre = livre.h3.a["title"]
        # Le prix est dans la balise p avec class price_color [cite: 81]
        prix  = livre.find("p", class_="price_color").text
        print(f"{i:2}. {titre[:45]:<45} | {prix}")