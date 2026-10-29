import pytest
from src.livraison import frais_livraison


def test_poids_negatif_refuse():
    with pytest.raises(ValueError):
        frais_livraison(poids=-1, montant=20)


def test_livraison_poids_jusqua_1_kg():
    assert frais_livraison(poids=1, montant=20) == 4.99


def test_livraison_poids_jusqua_5_kg():
    assert frais_livraison(poids=5, montant=20) == 7.99


def test_livraison_poids_superieur_5_kg():
    assert frais_livraison(poids=6, montant=20) == 12.99