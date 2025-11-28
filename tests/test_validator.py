
===================  SUMA  =======================

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


===================  MULTIPLICACION  =======================

import pytest

def multiplicar(a: int, b: int) -> int:
    return a * b

def test_multiplicacion_exitosa_pequenos():
    assert multiplicar(3, 4) == 12

def test_multiplicacion_exitosa_grandes():
    assert multiplicar(50, 20) == 1000

@pytest.mark.parametrize("factor1, factor2", [
    (-5, 10),     # Factor1 negativo
    (10, -5),     # Factor2 negativo
    (-10, -5),    # Ambos negativos
])
def test_numeros_negativos(factor1, factor2):
    with pytest.raises(Exception) as excinfo:
        multiplicar(factor1, factor2)
    assert str(excinfo.value) == "Ambos numeros deben ser enteros positivos"

@pytest.mark.parametrize("factor1, factor2", [
    (4, 3.5),     # Factor2 es flotante
    (3.5, 4),     # Factor1 es flotante
    (4.1, 5.2)    # Ambos son flotantes
])
def test_numeros_no_enteros(factor1, factor2):
    with pytest.raises(Exception) as excinfo:
        multiplicar(factor1, factor2)
    assert str(excinfo.value) == "Ambos numeros deben ser enteros positivos"


===================  DIVISION  =======================

import pytest

def dividir(a: int, b: int) -> int:
    return a // b

def test_division_exitosa_enteros():
    assert dividir(10, 5) == 2

def test_division_por_cero():
    with pytest.raises(Exception) as excinfo:
        dividir(10, 0)
    assert str(excinfo.value) == "No se puede dividir por cero"

@pytest.mark.parametrize("dividendo, divisor", [
    (-10, 5),    # Dividendo negativo
    (10, -5),    # Divisor negativo
    (-10, -5)    # Ambos negativos
])
def test_numeros_negativos(dividendo, divisor):
    with pytest.raises(Exception) as excinfo:
        dividir(dividendo, divisor)
    assert str(excinfo.value) == "Los numeros deben ser positivos"


===================  RESTA  =======================

import pytest

def restar(a: int, b: int) -> int:
    return a - b

def test_division_exitosa_enteros():
    assert restar(10, 3) == 7
    
@pytest.mark.parametrize("minuendo, sustraendo, esperado", [
    (10, 5, 5),     # Positivo - Positivo = Positivo
    (5, 5, 0),      # Igual - Igual = Cero
    (10, 0, 10),    # Cero en sustraendo
    (0, 0, 0),      # Cero - Cero
    (200, 150, 50)  # Grandes positivos
])
def test_resta_exitosa_resultado_no_negativo(minuendo, sustraendo, esperado):
    assert restar(minuendo, sustraendo) == esperado

def test_resta_resultado_negativo():
    with pytest.raises(Exception) as excinfo:
        restar(5, 10) # 5 < 10, resultado sería -5
    assert str(excinfo.value) == "El resultado de la resta no puede ser negativo"

@pytest.mark.parametrize("minuendo, sustraendo", [
    (-5, 10),     # Minuendo negativo
    (10, -5),     # Sustraendo negativo
    (10, 3.5),    # Sustraendo flotante
    (3.5, 5),     # Minuendo flotante
    (10, "a")     # Sustraendo no numérico
])
def test_numeros_de_entrada_no_validos(minuendo, sustraendo):
    with pytest.raises(Exception) as excinfo:
        restar(minuendo, sustraendo)
    assert str(excinfo.value) == "Ambos numeros deben ser enteros no negativos"


===================  BASE CONVERTER  =======================

import pytest
from app.validator import validar_base, validar_numero

def convertir_a_base_10(numero_str: str, base_origen: int) -> int:
    return int(numero_str, base_origen)


def test_base_valida():
    assert validar_base(8) is True


def test_base_fuera_de_rango():
    assert validar_base(1) is False
    assert validar_base(11) is False


def test_numero_valido_para_base():
    assert validar_numero("1207", 8) is True


def test_numero_invalido_para_base():
    assert validar_numero("1982", 8) is False

@pytest.mark.parametrize("numero_str, base, esperado", [
    ("1011", 2, 11),
    ("37", 8, 31),
    ("10", 8, 8),
    ("77", 8, 63),
    ("123", 10, 123),
    ("99", 10, 99),
    ("1", 2, 1),
    ("1", 10, 1)
])
def test_conversion_exitosa(numero_str, base, esperado):
    assert convertir_a_base_10(numero_str, base) == esperado

@pytest.mark.parametrize("numero_str, base, error_msg", [
    ("-101", 2, "El numero debe ser un entero no negativo"), # Negativo
    ("10.1", 2, "El numero debe ser un entero no negativo"),  # Flotante
    ("abc", 8, "El numero debe ser un entero no negativo")   # No numérico
])
def test_numero_invalido(numero_str, base, error_msg):
    with pytest.raises(Exception) as excinfo:
        convertir_a_base_10(numero_str, base)
    assert str(excinfo.value) == error_msg

@pytest.mark.parametrize("base", [
    1,   # Base menor a 2
    11,  # Base mayor a 10
    0,
    -2
])
def test_base_invalida(base):
    with pytest.raises(Exception) as excinfo:
        validar_base(base)
    assert str(excinfo.value) == "La base debe ser un entero entre 2 y 10"

@pytest.mark.parametrize("numero_str, base", [
    ("201", 2),  # Dígito 2 no válido en base 2
    ("80", 8),   # Dígito 8 no válido en base 8
    ("1A", 10),  # Carácter no numérico
    ("19", 9)    # Dígito 9 no válido en base 9
])
def test_digito_invalido_para_la_base(numero_str, base):
    with pytest.raises(Exception) as excinfo:
        validar_numero(numero_str, base)
    assert str(excinfo.value) == f"El numero contiene digitos invalidos para la base {base}"

===================  FORMATTER  =======================

import pytest
from app.validator import validar_base

def convertir_de_base_10(numero_base_10: int, base_destino: int) -> str:
    if not isinstance(base_destino, int) or not (2 <= base_destino <= 10):
        raise ValueError("La base de destino debe ser un entero entre 2 y 10")

    # Caso especial para el cero
    if numero_base_10 == 0:
        return "0"

    resultado = ""
    n = numero_base_10
    
    while n > 0:
        residuo = n % base_destino
        resultado = str(residuo) + resultado  # Agrega el residuo al inicio
        n = n // base_destino                 # Usa división entera
        
    return resultado


@pytest.mark.parametrize("numero_base_10, base_destino, esperado", [
    (13, 2, "1101"),
    (0, 2, "0"),
    (1, 2, "1"),
    (16, 2, "10000"),
    (31, 8, "37"),
    (63, 8, "77"),
    (64, 8, "100"),
    (15, 5, "30"),
    (24, 5, "44"),
    (99, 10, "99"),
    (5, 10, "5"),
])
def test_conversion_exitosa(numero_base_10, base_destino, esperado):
    assert convertir_de_base_10(numero_base_10, base_destino) == esperado

@pytest.mark.parametrize("base_destino", [
    1,   # Base menor a 2
    11,  # Base mayor a 10
    0,
    -2
])
def test_base_invalida(base_destino):
    with pytest.raises(Exception) as excinfo:
        validar_base(base)
    assert str(excinfo.value) == "La base debe ser un entero entre 2 y 10"

