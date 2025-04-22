import pytest
from src.utils import calculer_moyenne, convertir_temperature

# === Tests pour calculer_moyenne ===

def test_calculer_moyenne_valeurs_positives():
    assert calculer_moyenne([2, 4, 6]) == 4

def test_calculer_moyenne_avec_floats():
    assert calculer_moyenne([1.5, 2.5, 3.5]) == pytest.approx(2.5)

def test_calculer_moyenne_mixte():
    assert calculer_moyenne([1, 2.5, 3]) == pytest.approx(2.1666667)

def test_calculer_moyenne_vide():
    assert calculer_moyenne([]) is None

def test_calculer_moyenne_erreur_type():
    with pytest.raises(TypeError):
        calculer_moyenne([1, 'a', 3])

# === Tests pour convertir_temperature ===

def test_convertir_temperature_C_vers_F():
    assert convertir_temperature(0, 'C', 'F') == 32

def test_convertir_temperature_F_vers_C():
    assert convertir_temperature(32, 'F', 'C') == 0

def test_convertir_temperature_C_vers_K():
    assert convertir_temperature(100, 'C', 'K') == pytest.approx(373.15)

def test_convertir_temperature_K_vers_C():
    assert convertir_temperature(273.15, 'K', 'C') == pytest.approx(0)

def test_convertir_temperature_F_vers_K():
    assert convertir_temperature(32, 'F', 'K') == pytest.approx(273.15)

def test_convertir_temperature_K_vers_F():
    assert convertir_temperature(273.15, 'K', 'F') == pytest.approx(32)

def test_convertir_temperature_meme_unite():
    assert convertir_temperature(25, 'C', 'C') == 25

def test_convertir_temperature_unite_invalide():
    with pytest.raises(ValueError):
        convertir_temperature(100, 'X', 'C')
    
    with pytest.raises(ValueError):
        convertir_temperature(100, 'C', 'Z')
