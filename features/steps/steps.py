from behave import given, when, then
from fastapi.testclient import TestClient

@given('el número A "{numero_a}"')
def step_set_number_a(context, numero_a):
    context.numero_a = numero_a

@given('el número B "{numero_b}"')
def step_set_number_b(context, numero_b):
    context.numero_b = numero_b

@when('se realiza la suma')
def step_perform_addition(context):
    context.payload = {
        "numero_a": context.numero_a,
        "numero_b": context.numero_b
    }
    context.response = context.client.post("/suma", json=context.payload)

@then('el resultado es "{resultado_esperado}"')
def step_check_result(context, resultado_esperado):
    assert context.response.status_code == 200, f"Error: {context.response.text}"
    data = context.response.json()
    assert data["resultado"] == resultado_esperado, f"Esperaba {resultado_esperado}, obtuve {data['resultado']}"
