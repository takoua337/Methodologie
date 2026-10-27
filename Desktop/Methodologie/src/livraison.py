
def frais_livraison(poids, montant):
    if poids < 0:
        raise ValueError("Le poids ne peut pas être négatif")

    tarifs = [
        (1, 4.99),
        (5, 7.99),
        (float("inf"), 12.99),
    ]

    for limite, tarif in tarifs:
        if poids <= limite:
            return tarif
