class Panier:
    def __init__(self):
        self.articles = []
        self.code_utilise = False

    def ajouter(self, nom, prix, quantite):
        if quantite <= 0:
            raise ValueError("La quantité doit être positive")
        if prix < 0:
            raise ValueError("Le prix ne peut pas être négatif")

        self.articles.append((nom, prix, quantite))

    def total(self):
        total = sum(prix * qte for _, prix, qte in self.articles)

        if total > 100:
            total *= 0.9

        return max(0.0, total)

    def appliquer_code(self, code):
        if code != "BIENVENUE":
            raise ValueError("Code promo invalide")

        if self.code_utilise:
            raise ValueError("Code promo déjà utilisé")

        self.code_utilise = True

    