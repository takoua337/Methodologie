
class Panier:
    def __init__(self):
        self.articles = []
        self.code_utilise = False

    def ajouter(self, nom, prix, quantite):
        if quantite < 0:
            raise ValueError("Quantité négative")
        self.articles.append((nom, prix, quantite))

    def total(self):
        total = sum(prix * qte for _, prix, qte in self.articles)
        if total >= 100:
            total = total * 0.9
        return total

    def appliquer_code(self, code):
        if code == "BIENVENUE" and not self.code_utilise:
            self.code_utilise = True
