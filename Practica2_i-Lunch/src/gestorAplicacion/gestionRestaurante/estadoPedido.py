from enum import Enum

class EstadoPedido(Enum):
    RECIBIDO = "Recibido"
    ACEPTADO = "Aceptado"
    PREPARACION = "En preparacion"
    LISTO = "Listo"
    DESPACHADO = "Despachado"
    RECHAZADO = "Rechazado"