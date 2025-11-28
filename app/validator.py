from typing import Tuple


def _validar_enteros_no_negativos(a, b) -> None:
    """Valida que ambos valores sean enteros no negativos.

    Lanza ValueError con el mensaje requerido cuando la validación falla.
    """
    # Verificar tipos (aceptar valores que se puedan interpretar como int)
    if not isinstance(a, int) or not isinstance(b, int):
        raise ValueError("Ambos numeros deben ser enteros no negativos")

    # Verificar no negativos
    if a < 0 or b < 0:
        raise ValueError("Ambos numeros deben ser enteros no negativos")


def suma_bases(numero_a: int, numero_b: int) -> int:
    """Suma dos números en base 10 con validaciones.

    Raise:
        ValueError: Si alguno de los números no es un entero no negativo.

    Returns:
        int: Resultado de la suma en base 10.
    """
    _validar_enteros_no_negativos(numero_a, numero_b)
    return numero_a + numero_b


def sumar(a: int, b: int) -> int:
    """Función auxiliar simple que realiza la suma.

    Mantengo esta función para compatibilidad con tests que puedan
    importar una función `sumar`.
    """
    return suma_bases(a, b)
