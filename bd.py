from typing import Union
from models.cliente import Cliente
from models.cuenta import Cuenta
from models.pago import Pago


class Repositorio:

    clienteTabla : dict[int, Cliente] = {}
    pagoTabla : dict[int, Pago] = {}
    id = 0
    id_pagos = 0
    @classmethod
    def insertarCliente(cls, cliente:Cliente):
        listaClientes = cls.clienteTabla.values()
        for clientes in listaClientes:
            if cliente.nro_cuenta == clientes.nro_cuenta and cliente.cedula == clientes.cedula:
                print("Error 500 El cliente ya existe")           
        else:     
         cls.id =  cls.id +1 
         cliente.id = cls.id 
         cls.clienteTabla[cls.id] = cliente

    @classmethod
    def recuperar_clientes(cls):
        return cls.clienteTabla.values()

    @classmethod
    def recuperar_cliente(cls, id:int):
        return cls.clienteTabla[id]
    
    @classmethod
    def modificar_cliente(cls, id:int,clienteModificado:Cliente):
        cls.clienteTabla[id] = clienteModificado
        
        return cls.clienteTabla[id] + "El cliente ha sido modificado"
    
    @classmethod
    def eliminar_cliente(cls, id:int):
        cls.clienteTabla.pop(id)
        return "Cliente ha sido Eliminado"
    
    @classmethod
    def insertarPago(cls, pago:Pago):
        pagoResgistrados = cls.pagoTabla.values()
        for pagos in pagoResgistrados:
            if pago.nro_cuenta == pagos.nro_cuenta and pago.cedula == pagos.cedula:
                 if pagos.factura != "":
                    cls.id_pagos =  cls.id_pagos +1 
                    pago.id = cls.id 
                    cls.pagoTabla[cls.id_pagos] = pago
            else:
             print("Código 400 Bad Request")
            
             
    @classmethod
    def modificar_pago(cls, id:int,pagoModificado:Pago):
        cls.pagoTabla[id] = pagoModificado
        
        return cls.pagoTabla[id] + "modificado"
    
    @classmethod
    def eliminar_pago(cls, id:int):
        cls.pagoTabla.pop(id)
        return "Pago Eliminado"
       

    @classmethod
    def recuperar_pagos(cls):
        return cls.pagoTabla.values()

    @classmethod
    def recuperar_pago(cls, id:int):
        return cls.pagoTabla[id]



