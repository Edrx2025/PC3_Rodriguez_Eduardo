from fastapi import FastAPI
from pydantic import BaseModel

app = FastAPI()

##Entidad para almacenar la lista de numeros
class Numeros(BaseModel):
    valores: list[float]


##---Parte A2 del examen:---

##Creandp la función sumar
def sumar(a:int,b:int):
    return a+b

##Realizar suma al utilizar get
@app.get("/sumar/")
def endpoint_sumar(a:int, b:int):
    result= sumar(a,b)
    return {"a":a,"b":b,"Suma":result}

##Obteniendo el promedio al utilizar post
@app.post("/promedio/")
def endpoint_promedio(datos: Numeros):
    if len(datos.valores)==0:
        return {"HTTPException(status_code":400, "detail":"Lista vacía"}
    else:
        result=sum(datos.valores) / len(datos.valores)
        return {"Promedio":result}

@app.get("/health")
def endpoint_health():
  return {"status": "ok"}

        