import pytest

def sumar(a: int, b: int) -> int:
    return a + b

def test_suma_valida():
    a = 101 
    b = 12 
    resultado = sumar(a, b)
    assert resultado == 113

@pytest.mark.parametrize("a, b, esperado", [
    (10, 12, 22),  
    (5, 5, 10),   
    (0, 7, 7), 
])
def test_suma_con_parametros(a, b, esperado):
    # La función 'sumar' se asume que está definida/importada
    resultado = sumar(a, b)
    assert resultado == esperado