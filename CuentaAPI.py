from typing import Union

from fastapi import FastAPI
from pydantic import BaseModel
from models.cliente import Cliente
from models.cuenta import Cuenta
from bd import Repositorio
import json
from fastapi.encoders import jsonable_encoder

from models.pago import Pago

app = FastAPI()


#Recursos
# 1 - Cliente
# 2 - Pago 


@app.post("/clientes")
def registar_cliente(cliente: Cliente):
    Repositorio.insertarCliente(cliente)
    return cliente

@app.get("/clientes")
def recuperar_clientes():
    registros: dict[int, Cliente]= Repositorio.recuperar_clientes()
    listObjetos =  list(registros) #lista DE objetos CLIENTES 
    listaJson = jsonable_encoder(listObjetos) #convertimos lista de objetos a json

    return listaJson

@app.get("/clientes/{id}")
def recuperar_cliente(id:int):
    cliente: Cliente= Repositorio.recuperar_cliente(id)
    return cliente

@app.put("/clientes/{id}")
def modificar_cliente(id:int,cliente:Cliente):
    clienteDevuelto: Cliente= Repositorio.modificar_cliente(id)
    return clienteDevuelto

@app.delete("/clientes/{id}")
def eliminar_cliente(id:int):
    clienteBorrado: Cliente= Repositorio.eliminar_cliente(id)
    return clienteBorrado

@app.post("/pagos")
def registra_pagos(pago: Pago):
    Repositorio.insertarPago(pago)
    return pago

@app.get("/pagos")
def recuperar_pagos():
    registros: dict[int, Pago]= Repositorio.recuperar_pagos()
    listObjetos =  list(registros) #lista DE objetos pagos
    listaJson = jsonable_encoder(listObjetos) #convertimos lista de objetos a json

    return listaJson

@app.put("/pagos/{id}")
def modificar_pago(id:int,pago:Pago):
    pagoModificado: Pago = Repositorio.modificar_pago(id)
    return pagoModificado

@app.delete("/pagos/{id}")
def eliminar_pago(id:int):
    pago: Pago= Repositorio.eliminar_pago(id)
    return Pago

@app.get("/pagos/{id}")
def recuperar_pago(id:int):
    pago: Pago= Repositorio.recuperar_pago(id)
    return pago