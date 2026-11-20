from fastapi import FastAPI
from pydantic import BaseModel

app = FastAPI()

#DICCIOANRIO
items_db: dict[int,dict]={}
next_id=1

#Entidad que se usa para contener el registro
class Item(BaseModel):
    name: str
    price: float
    is_offer: bool = False

##Entidad para almacenar la lista de numeros
class Numeros(BaseModel):
    valores: list[float]
    
#Guardar un item nuevo
@app.post("/items/",status_code=201)
def create_item(item: Item):
    global next_id
    item_id = next_id
    items_db[item_id]=item.model_dump()
    next_id+=1
    return {"item_id": item_id, **items_db[item_id]}
    
##Consultar todos los items guardados
@app.get("/items/")
def read_item():
    return items_db

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
        