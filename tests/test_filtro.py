import sys
import os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..', 'src')))

from filtro import procesar_numeros

def test_procesar_numeros_normal():
    resultado = procesar_numeros([1, 2, 3, 4])
    assert resultado == {
        'pares': [2, 4],
        'suma_pares': 6,
        'impares': [1, 3],
        'suma_impares': 4
    }

def test_lista_vacia():
    resultado = procesar_numeros([])
    assert resultado == {
        'pares': [],
        'suma_pares': 0,
        'impares': [],
        'suma_impares': 0
    }

def test_solo_pares():
    resultado = procesar_numeros([2, 4, 6])
    assert resultado == {
        'pares': [2, 4, 6],
        'suma_pares': 12,
        'impares': [],
        'suma_impares': 0
    }

def test_numeros_negativos():
    resultado = procesar_numeros([-1, -2, -3, -4])
    assert resultado == {
        'pares': [-2, -4],
        'suma_pares': -6,
        'impares': [-1, -3],
        'suma_impares': -4
    }
