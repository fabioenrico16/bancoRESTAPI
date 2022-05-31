from pydantic import BaseModel

class Cuenta(BaseModel):
    cedula: str
    cuenta: int
    telefono: str
    factura: str
    monto: int
    moneda: str
