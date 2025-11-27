from typing import Tuple


def validar_base(base: int) -> bool:
    """La base debe estar entre 2 y 10 (inclusive)."""
    return 2 <= base <= 10


def validar_numero(numero: str, base: int) -> bool:
    """Valida que `numero` sólo contenga dígitos y que cada dígito sea < base.

    También valida que la base sea válida.
    """
    if not validar_base(base):
        return False
    if not numero.isdigit():
        return False
    return all(int(d) < base for d in numero)


def convert_base(numero: str, base_origen: int, base_destino: int) -> str:
    """Convierte `numero` (string) desde `base_origen` a `base_destino`.

    Bases entre 2 y 10.
    """
    # Convertir a entero
    value = 0
    for d in numero:
        value = value * base_origen + int(d)

    # Convertir a base_destino
    if value == 0:
        return "0"
    digits = []
    while value > 0:
        digits.append(str(value % base_destino))
        value //= base_destino
    return "".join(reversed(digits))


def suma_bases(numero_a: str, base_a: int, numero_b: str, base_b: int, base_salida: int) -> str:
    """Suma dos números en diferentes bases y retorna el resultado en base_salida.
    
    Args:
        numero_a: Primer número como string
        base_a: Base del primer número
        numero_b: Segundo número como string
        base_b: Base del segundo número
        base_salida: Base en la que se desea el resultado
    
    Returns:
        El resultado de la suma como string en base_salida
    """
    # Validar que los números sean válidos en sus bases
    if not validar_numero(numero_a, base_a):
        raise ValueError(f"Número {numero_a} inválido en base {base_a}")
    if not validar_numero(numero_b, base_b):
        raise ValueError(f"Número {numero_b} inválido en base {base_b}")
    if not validar_base(base_salida):
        raise ValueError(f"Base de salida {base_salida} no válida")
    
    # Convertir ambos números a decimal
    value_a = 0
    for d in numero_a:
        value_a = value_a * base_a + int(d)
    
    value_b = 0
    for d in numero_b:
        value_b = value_b * base_b + int(d)
    
    # Realizar la suma en decimal
    suma = value_a + value_b
    
    # Convertir el resultado a base_salida
    if suma == 0:
        return "0"
    digits = []
    while suma > 0:
        digits.append(str(suma % base_salida))
        suma //= base_salida
    return "".join(reversed(digits))
