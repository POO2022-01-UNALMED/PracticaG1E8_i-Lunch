from src.gestorAplicacion.usuariosRestaurante.usuario import Usuario
from src.gestorAplicacion.usuariosRestaurante.empleado import Empleado
from src.gestorAplicacion.usuariosRestaurante.administrador import Administrador
from src.gestorAplicacion.usuariosRestaurante.repartidor import Repartidor
from src.gestorAplicacion.usuariosRestaurante.mesero import Mesero
from src.gestorAplicacion.usuariosRestaurante.cliente import Cliente

from src.gestorAplicacion.gestionRestaurante.restaurante import Restaurante
from src.gestorAplicacion.gestionRestaurante.producto import Producto
from src.gestorAplicacion.gestionRestaurante.pedido import Pedido
from src.gestorAplicacion.gestionRestaurante.estadoPedido import EstadoPedido
from src.gestorAplicacion.gestionRestaurante.tipoPedido import TipoPedido

class Chef(Empleado):

    # Atributos estaticos

    _chefs = []

    # Constructor

    def __init__(self):
        super().__init__()



        Chef._chefs.append(self)

    # Getters y Setters



    @classmethod
    def getChefs(cls):
        return cls._chefs

    @classmethod
    def setChefs(cls, chefs):
        cls._chefs = chefs

    # Metodos



    # Implementacion de la interfaz

    def informacion(self):
        pass