import pytest

def sumar(a: int, b: int) -> int:
    return a + b

def test_suma_valida():
    a = int(101) 
    b = int(12) 
    resultado = sumar(a, b)
    assert resultado == 113

