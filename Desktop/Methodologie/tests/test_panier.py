import pytest
from src.panier import Panier

def test_panier_vide_vaut_zero():
    assert Panier().total() == 0

def test_total_simple():
    p = Panier()
    p.ajouter("stylo", 2.0, 3)
    p.ajouter("cahier", 4.5, 2)
    assert p.total() == 15.0