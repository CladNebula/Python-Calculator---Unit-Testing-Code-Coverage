"""
Casos de prueba unitaria para calculator.py
Corresponden a los casos CP-01, CP-02 y CP-03 del informe técnico.
"""

import pytest
import calculator


# CP-01 - Prueba funcional: suma de dos números positivos
def test_sumar_dos_positivos():
    resultado = calculator.sumar(15, 7)
    assert resultado == 22


# CP-02 - Prueba de manejo de excepciones: división por cero
def test_dividir_por_cero():
    with pytest.raises(ZeroDivisionError):
        calculator.dividir(10, 0)


# CP-03 - Prueba de validación de entradas: tipo de dato no numérico
def test_sumar_tipo_invalido():
    with pytest.raises(TypeError):
        calculator.sumar("diez", 5)


# --- Pruebas adicionales opcionales (para robustecer el trabajo) ---

def test_restar_numeros_negativos():
    resultado = calculator.restar(-10, -5)
    assert resultado == -5


def test_multiplicar_por_cero():
    resultado = calculator.multiplicar(100, 0)
    assert resultado == 0


def test_dividir_numeros_decimales():
    resultado = calculator.dividir(10, 4)
    assert resultado == 2.5
