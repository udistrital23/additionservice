from behave import given, when, then


@given('los numeros enteros {numero_a:d} y {numero_b:d}')
def step_set_numbers(context, numero_a, numero_b):
    context.numero_a = numero_a
    context.numero_b = numero_b


@when('realizo la suma')
def step_perform_addition(context):
    payload = {"numero_a": context.numero_a, "numero_b": context.numero_b}
    context.response = context.client.post("/suma", json=payload)


@when('intento realizar la suma')
def step_attempt_addition(context):
    payload = {"numero_a": context.numero_a, "numero_b": context.numero_b}
    context.response = context.client.post("/suma", json=payload)


@then('el resultado debe ser {resultado_esperado:d}')
def step_check_result(context, resultado_esperado):
    assert context.response.status_code == 200, f"Error: {context.response.text}"
    data = context.response.json()
    assert data.get("resultado") == resultado_esperado, f"Esperaba {resultado_esperado}, obtuve {data.get('resultado')}"


@then('se lanza una excepcion de "{mensaje}"')
def step_check_exception_message(context, mensaje):
    # FastAPI devuelve 400 con {'detail': '...'} cuando se lanza HTTPException
    assert context.response.status_code == 400, f"Se esperaba 400, obtuvo {context.response.status_code}"
    data = context.response.json()
    assert data.get("detail") == mensaje, f"Esperaba mensaje '{mensaje}', obtuvo '{data.get('detail')}'"
