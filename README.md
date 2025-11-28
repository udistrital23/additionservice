# Addition Service

Servicio de suma de números enteros no negativos en base 10 con validaciones y pruebas.

## Características

- Suma de dos números enteros no negativos
- Validación de entrada (solo enteros no negativos)
- API REST con FastAPI
- Pruebas unitarias con pytest
- Pruebas de comportamiento (BDD) con behave

## Requisitos

- Python 3.8+
- pip

## Instalación

1. Clonar el repositorio:
```bash
git clone <repository-url>
cd additionservice
```

2. Crear un entorno virtual:
```bash
python3 -m venv .venv
source .venv/bin/activate  # En macOS/Linux
# o en Windows:
# .venv\Scripts\activate
```

3. Instalar dependencias:
```bash
pip install -r requirements.txt
```

## Cómo probar la API

### 1. Iniciar el servidor

```bash
uvicorn app.main:app --reload --host 0.0.0.0 --port 8000
```

El servidor estará disponible en `http://localhost:8000`

### 2. Acceder a la documentación interactiva

- **Swagger UI**: http://localhost:8000/docs
- **ReDoc**: http://localhost:8000/redoc

### 3. Probar con curl

**Caso exitoso** (suma de números positivos):
```bash
curl -X POST "http://localhost:8000/suma" \
  -H "Content-Type: application/json" \
  -d '{"numero_a": 15, "numero_b": 25}'
```

Respuesta esperada:
```json
{"resultado": 40}
```

**Caso con error** (número negativo):
```bash
curl -X POST "http://localhost:8000/suma" \
  -H "Content-Type: application/json" \
  -d '{"numero_a": -5, "numero_b": 10}'
```

Respuesta esperada (HTTP 400):
```json
{"detail": "Ambos numeros deben ser enteros no negativos"}
```

### 4. Probar con Python requests

```python
import requests

# Caso exitoso
response = requests.post(
    "http://localhost:8000/suma",
    json={"numero_a": 15, "numero_b": 25}
)
print(response.json())  # {"resultado": 40}

# Caso con error
response = requests.post(
    "http://localhost:8000/suma",
    json={"numero_a": -5, "numero_b": 10}
)
print(response.status_code)  # 400
print(response.json())  # {"detail": "Ambos numeros deben ser enteros no negativos"}
```

## Ejecutar pruebas

### Pruebas unitarias (pytest)

```bash
pytest -v
```

O para un resumen simple:
```bash
pytest -q
```

### Pruebas de comportamiento (BDD con behave)

```bash
behave
```

O con más detalles:
```bash
behave -v
```

## Estructura del proyecto

```
additionservice/
├── app/
│   ├── __init__.py
│   ├── main.py           # Aplicación FastAPI y endpoint /suma
│   └── validator.py      # Lógica de suma y validaciones
├── features/
│   ├── environment.py    # Configuración de behave
│   ├── validacion.feature # Escenarios de prueba BDD
│   └── steps/
│       └── steps.py      # Definiciones de pasos behave
├── tests/
│   ├── __init__.py
│   └── test_validator.py # Pruebas unitarias
├── Dockerfile
├── Makefile
├── README.md
└── requirements.txt
```

## Validaciones

La API valida que:
- Ambos números sean enteros
- Ambos números sean no negativos (>= 0)

Si alguna validación falla, retorna HTTP 400 con el mensaje:
```
"Ambos numeros deben ser enteros no negativos"
```

## Licencia

MIT
