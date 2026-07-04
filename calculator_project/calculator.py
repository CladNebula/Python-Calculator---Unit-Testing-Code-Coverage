"""
Módulo de calculadora simple.
Basado en el repositorio de referencia:
https://github.com/balram-vis/Python-Calculator---Unit-Testing-Code-Coverage
"""

import logging

logging.basicConfig(level=logging.INFO, format="%(asctime)s - %(levelname)s - %(message)s")


def sumar(a, b):
    """Suma dos números."""
    logging.info(f"Ejecutando sumar({a}, {b})")
    return a + b


def restar(a, b):
    """Resta dos números."""
    logging.info(f"Ejecutando restar({a}, {b})")
    return a - b


def multiplicar(a, b):
    """Multiplica dos números."""
    logging.info(f"Ejecutando multiplicar({a}, {b})")
    return a * b


def dividir(a, b):
    """Divide dos números. Lanza ZeroDivisionError si b es 0."""
    logging.info(f"Ejecutando dividir({a}, {b})")
    if b == 0:
        logging.error("Intento de división por cero")
        raise ZeroDivisionError("No es posible dividir por cero")
    return a / b


if __name__ == "__main__":
    # Ejemplo de uso manual (útil para tomar capturas de pantalla)
    print("Suma:", sumar(15, 7))
    print("Resta:", restar(15, 7))
    print("Multiplicación:", multiplicar(15, 7))
    print("División:", dividir(15, 7))
