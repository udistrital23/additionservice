from fastapi.testclient import TestClient
from app.main import app

def before_all(context):
    # Creamos el cliente de pruebas y lo guardamos en el contexto global
    context.client = TestClient(app)

