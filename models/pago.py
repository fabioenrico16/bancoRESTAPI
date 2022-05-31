from pydantic import BaseModel

class Pago(BaseModel):
    cedula: str
    cuenta: int
    telefono: str
    factura: str
    monto: int
    moneda: str
