import pytest

def sumar(a: int, b: int) -> int:
    return a + b

def test_suma_valida():
    a = int("101", 2)   # 5
    b = int("12", 3)    # 5
    resultado = sumar(a, b)
    assert resultado == 10

