from enum import Enum

class TipoPedido(Enum):
    LLEVAR = "Para llevar"
    TIENDA = "Para consumir en la tienda"
    DOMICILIO = "A domicilio"