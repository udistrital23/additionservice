from behave import given, when, then
from fastapi.testclient import TestClient

@given('el número A "{numero_a}" en base {base_a:d}')
def step_set_number_a(context, numero_a, base_a):
    context.numero_a = numero_a
    context.base_a = base_a

@given('el número B "{numero_b}" en base {base_b:d}')
def step_set_number_b(context, numero_b, base_b):
    context.numero_b = numero_b
    context.base_b = base_b

@given('la base de salida es {base_salida:d}')
def step_set_output_base(context, base_salida):
    context.base_salida = base_salida

@when('se realiza la suma')
def step_perform_addition(context):
    context.payload = {
        "numero_a": context.numero_a,
        "base_a": context.base_a,
        "numero_b": context.numero_b,
        "base_b": context.base_b,
        "base_salida": context.base_salida
    }
    context.response = context.client.post("/suma", json=context.payload)

@then('el resultado es "{resultado_esperado}" en base {base_esperada:d}')
def step_check_result(context, resultado_esperado, base_esperada):
    assert context.response.status_code == 200, f"Error: {context.response.text}"
    data = context.response.json()
    assert data["resultado"] == resultado_esperado, f"Esperaba {resultado_esperado}, obtuve {data['resultado']}"
    assert data["base"] == base_esperada, f"Esperaba base {base_esperada}, obtuve {data['base']}"