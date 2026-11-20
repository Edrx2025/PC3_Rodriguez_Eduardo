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