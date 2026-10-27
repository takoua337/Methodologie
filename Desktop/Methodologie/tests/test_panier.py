import pytest
from src.panier import Panier

def test_panier_vide_vaut_zero():
    assert Panier().total() == 0

def test_total_simple():
    p = Panier()
    p.ajouter("stylo", 2.0, 3)
    p.ajouter("cahier", 4.5, 2)
    assert p.total() == 15.0

def test_pas_de_remise_a_100_pile():
    p = Panier()
    p.ajouter("x", 100.0, 1)
    assert p.total() == 100.0

def test_remise_au_dessus_de_100():
    p = Panier()
    p.ajouter("x", 120.0, 1)
    assert p.total() == 108.0

def test_quantite_negative_refusee():
    with pytest.raises(ValueError):
        Panier().ajouter("x", 10.0, -1)

def test_quantite_nulle_refusee():
    with pytest.raises(ValueError):
        Panier().ajouter("x", 10.0, 0)

def test_code_promo_valide():
    p = Panier()
    p.ajouter("x", 20.0, 1)
    p.appliquer_code("BIENVENUE")
    assert p.total() == 15.0

def test_code_promo_une_seule_fois():
    p = Panier()
    p.ajouter("x", 20.0, 1)
    p.appliquer_code("BIENVENUE")
    with pytest.raises(ValueError):
        p.appliquer_code("BIENVENUE")

def test_code_promo_invalide():
    with pytest.raises(ValueError):
        Panier().appliquer_code("FAUX")

def test_total_jamais_negatif():
    p = Panier()
    p.ajouter("x", 2.0, 1)
    p.appliquer_code("BIENVENUE")
    assert p.total() == 0.0

def test_remise_et_code_cumules():
    p = Panier()
    p.ajouter("x", 200.0, 1)
    p.appliquer_code("BIENVENUE")
    assert p.total() == 175.0