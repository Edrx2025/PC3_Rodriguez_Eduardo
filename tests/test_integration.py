from fastapi.testclient import TestClient
from app.main import app

client = TestClient(app)
def test_sumar_integracion():
  response = client.get("/sumar/?a=5&b=3")

  #Observamos si el status del codigo es 200
  assert response.status_code == 200

  # Chequeamos que el JSON devuelto es el correcto
  assert response.json() == {"a": 5, "b": 3, "Suma": 8}

def test_promedio_lista_valida():
  response = client.post("/promedio/", json={"valores": [10.0, 20.0, 30.0]})
  assert response.status_code == 200
  assert response.json() == {"Promedio": 20.0}


def test_promedio_lista_vacia():
  response = client.post("/promedio/", json={"valores": []})
  assert response.status_code == 200
  assert response.json() == {
      "HTTPException(status_code": 400,
      "detail": "Lista vacía",
  }

def test_convivencia_endpoints_integracion():
  # 1. Verificando el nuevo endpoint GET /health
  res_health = client.get("/health")
  assert res_health.status_code == 200
  assert res_health.json() == {"status": "ok"}

  # 2. Verificando el endpoint GET /sumar/
  res_sumar = client.get("/sumar/?a=10&b=5")
  assert res_sumar.status_code == 200
  assert res_sumar.json() == {"a": 10, "b": 5, "Suma": 15}

  # 3. Verficiando el endpoint POST /promedio/ (caso válido)
  res_promedio = client.post("/promedio/", json={"valores": [4.0, 6.0, 8.0]})
  assert res_promedio.status_code == 200
  assert res_promedio.json() == {"Promedio": 6.0}

