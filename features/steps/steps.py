
===================  SUMA  ======================================

from behave import given, when, then
from fastapi.testclient import TestClient

@given('el número A "{numero_a:d}"')
def step_set_number_a(context, numero_a):
    context.numero_a = numero_a

@given('el número B "{numero_b:d}"')
def step_set_number_b(context, numero_b):
    context.numero_b = numero_b

@when('se realiza la suma')
def step_perform_addition(context):
    context.payload = {
        "numero_a": context.numero_a,
        "numero_b": context.numero_b
    }
    context.response = context.client.post("/suma", json=context.payload)

@then('el resultado es "{resultado_esperado:d}"')
def step_check_result(context, resultado_esperado):
    assert context.response.status_code == 200, f"Error: {context.response.text}"
    data = context.response.json()


    assert data["resultado"] == resultado_esperado, f"Esperaba {resultado_esperado}, obtuve {data['resultado']}"


===================  MULTIPLICACION  ======================================

from behave import given, when, then
from fastapi.testclient import TestClient

@given('el número A "{numero_a:d}"')
def step_set_number_a(context, numero_a):
    context.numero_a = numero_a

@given('el número B "{numero_b:d}"')
def step_set_number_b(context, numero_b):
    context.numero_b = numero_b

@when('se realiza la multiplicacion')
def step_perform_multiplication(context):
    context.payload = {
        "numero_a": context.numero_a,
        "numero_b": context.numero_b
    }
    context.response = context.client.post("/multiplicacion", json=context.payload)

@then('el resultado es "{resultado_esperado:d}"')
def step_check_result(context, resultado_esperado):
    assert context.response.status_code == 200, f"Error: {context.response.text}"
    data = context.response.json()
    assert data["resultado"] == resultado_esperado, f"Esperaba {resultado_esperado}, obtuve {data['resultado']}"


====================  DIVISION  ======================================

from behave import given, when, then
from fastapi.testclient import TestClient
import math

@given('el número A "{numero_a:d}"')
def step_set_number_a(context, numero_a):
    context.numero_a = numero_a

@given('el número B "{numero_b:d}"')
def step_set_number_b(context, numero_b):
    context.numero_b = numero_b

@when('se realiza la division')
def step_perform_division(context):
    context.payload = {
        "numero_a": context.numero_a,
        "numero_b": context.numero_b
    }
    # context.client debe estar inicializado en environment.py
    context.response = context.client.post("/division", json=context.payload)

# --- Validación con TRUNCADO (desechar decimales) ---
@then('el resultado entero (truncado) es "{resultado_esperado:d}"')
def step_check_result_truncated(context, resultado_esperado):
    assert context.response is not None, "No hay respuesta del cliente."
    assert context.response.status_code == 200, f"Error HTTP: {context.response.text}"
    try:
        data = context.response.json()
    except Exception as e:
        raise AssertionError(f"Respuesta no es JSON válido: {e}. Cuerpo: {context.response.text}")

    assert "resultado" in data, f"Falta el campo 'resultado' en la respuesta: {data}"
    valor = data["resultado"]

    try:
        valor_float = float(valor)
    except Exception:
        raise AssertionError(f"'resultado' no es numérico: {valor}")

    # Truncado: desecha la parte decimal (hacia cero)
    valor_truncado = math.trunc(valor_float)

    assert valor_truncado == resultado_esperado, (
        f"Esperaba {resultado_esperado} (truncado), obtuve {valor_truncado} a partir de {valor_float}"
    )

# --- Error por división entre cero ---
@then('falla por division entre cero con estado "{status_code:d}"')
def step_check_division_by_zero_error(context, status_code):
    assert context.response is not None, "No hay respuesta del cliente."
    assert context.response.status_code == status_code, (
        f"Código HTTP distinto al esperado ({status_code}): {context.response.status_code}. "
        f"Cuerpo: {context.response.text}"
    )
    try:
        data = context.response.json()
    except Exception as e:
        raise AssertionError(f"Respuesta no es JSON válido: {e}. Cuerpo: {context.response.text}")

    assert "error" in data, f"Falta clave 'error' en respuesta de error: {data}"
    error_val = str(data["error"]).lower()
    assert "division" in error_val and "cero" in error_val, (
        f"El mensaje no indica división por cero: {data}"
    )


====================  RESTA  ======================================

from behave import given, when, then
from fastapi.testclient import TestClient

@given('el número A "{numero_a:d}"')
def step_set_number_a(context, numero_a):
    context.numero_a = numero_a

@given('el número B "{numero_b:d}"')
def step_set_number_b(context, numero_b):
    context.numero_b = numero_b

@when('se realiza la resta')
def step_perform_subtraction(context):
    context.payload = {
        "numero_a": context.numero_a,
        "numero_b": context.numero_b
    }
    # Nota: context.client debe inicializarse en environment.py
    context.response = context.client.post("/resta", json=context.payload)

@then('el resultado es "{resultado_esperado:d}"')
def step_check_result(context, resultado_esperado):
    # Validación HTTP
    assert context.response is not None, "No hay respuesta del cliente."
    assert context.response.status_code == 200, f"Error HTTP: {context.response.status_code}. Cuerpo: {context.response.text}"

    # Parseo robusto de JSON
    try:
        data = context.response.json()
    except Exception as e:
        raise AssertionError(f"Respuesta no es JSON válido: {e}. Cuerpo: {context.response.text}")

    # Contrato
    assert "resultado" in data, f"Falta el campo 'resultado' en la respuesta: {data}"
    resultado = data["resultado"]

    # Tipo y dominio: la regla de negocio exige resultado >= 0
    assert isinstance(resultado, int), f"'resultado' debe ser entero, recibido: {type(resultado)} ({resultado})"
    assert resultado >= 0, f"El resultado no puede ser negativo según la regla: {resultado}"

    # Chequeo contra lo esperado
    assert resultado == resultado_esperado, f"Esperaba {resultado_esperado}, obtuve {resultado}"

    # (Opcional) Consistencia con los operandos recibidos, si el servicio los ecoa:
    # assert data.get("numero_a") == context.numero_a
    # assert data.get("numero_b") == context.numero_b

@then('falla porque A es menor que B con estado "{status_code:d}"')
def step_check_subtraction_negative_error(context, status_code):
    assert context.response is not None, "No hay respuesta del cliente."
    assert context.response.status_code == status_code, (
        f"Código HTTP distinto al esperado ({status_code}): {context.response.status_code}. "
        f"Cuerpo: {context.response.text}"
    )

    # Cuerpo de error legible
    try:
        data = context.response.json()
    except Exception as e:
        raise AssertionError(f"Respuesta de error no es JSON válido: {e}. Cuerpo: {context.response.text}")

    # Ejemplo: {"error": "resta_negativa_no_permitida", "detalle": "numero_a debe ser >= numero_b"}
    assert "error" in data, f"Falta clave 'error' en respuesta de error: {data}"
    error_text = str(data["error"]).lower()
    # Verificación semántica 
    assert ("resta" in error_text or "subtracción" in error_text or "subtraction" in error_text) and (
            "negativ" in error_text or "menor" in error_text or "invalid" in error_text
        ), f"El mensaje no refleja que A < B viola la regla: {data}"

  
====================  BASE CONVERTER  ======================================

# QUEDA IGUAL PORQUE NO SUPE CÓMO AGREGARLE QUE VALIDARA QUE EL NÚMERO A CONVERTIR NO SEA NEGATIVO NI FLOTANTE




====================  FORMATTER  ======================================

from behave import given, then
from fastapi.testclient import TestClient

# --- Steps para Escenarios de BASE DE RESPUESTA ---

@given('que la base es {base:d}')
def step_set_base(context, base):
    context.payload = {"base": base}

@then('la base es aceptada')
def step_base_accepted(context):
    response = context.client.post("/converter", json=context.payload)
    assert response.status_code == 200, f"Esperaba 200, obtuve {response.status_code}: {response.text}"
    assert response.json()["status"] == "Base aceptada"

@then('la base es rechazada')
def step_base_rejected(context):
    response = context.client.post("/converter", json=context.payload)
    # Esperamos un error 400 (Bad Request)
    assert response.status_code == 400, f"Esperaba 400, obtuve {response.status_code}"

# =========================================================
# Helpers comunes
# =========================================================

def _parse_json(response):
    try:
        return response.json()
    except Exception as e:
        raise AssertionError(f"Respuesta no es JSON válido: {e}. Cuerpo: {response.text}")

# =========================================================
#  Casos negativos: flotante, base < 2, base > 10
# =========================================================

@given('el numero en base 10 es {numero}')
def step_set_numero_decimal(context, numero):
    context.numero_decimal = numero

@when('intento realizar la conversion a la base {base_destino:d}')
def step_intento_conversion(context, base_destino):
    payload = {
        "numero_decimal": context.numero_decimal,
        "base_destino": base_destino
    }
    context.response = context.client.post("/formatter", json=payload)

@then('se lanza una excepcion de "{mensaje_error}"')
def step_valida_mensaje_excepcion(context, mensaje_error):
    assert context.response is not None, "No hay respuesta del cliente."
    assert context.response.status_code == 400, (
        f"Esperaba 400, obtuve {context.response.status_code}. Cuerpo: {context.response.text}"
    )
    data = _parse_json(context.response)
    assert "error" in data, f"Se esperaba 'error' en la respuesta: {data}"
    assert data["error"] == mensaje_error, (
        f'Mensaje de error inesperado. Esperaba "{mensaje_error}", obtuve "{data["error"]}"'
    )

