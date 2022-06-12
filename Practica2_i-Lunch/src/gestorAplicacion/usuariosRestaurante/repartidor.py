from src.gestorAplicacion.usuariosRestaurante.usuario import Usuario
from src.gestorAplicacion.usuariosRestaurante.empleado import Empleado
from src.gestorAplicacion.usuariosRestaurante.administrador import Administrador
from src.gestorAplicacion.usuariosRestaurante.mesero import Mesero
from src.gestorAplicacion.usuariosRestaurante.chef import Chef
from src.gestorAplicacion.usuariosRestaurante.cliente import Cliente

from src.gestorAplicacion.gestionRestaurante.restaurante import Restaurante
from src.gestorAplicacion.gestionRestaurante.producto import Producto
from src.gestorAplicacion.gestionRestaurante.pedido import Pedido
from src.gestorAplicacion.gestionRestaurante.estadoPedido import EstadoPedido
from src.gestorAplicacion.gestionRestaurante.tipoPedido import TipoPedido

class Repartidor(Empleado):

    # Atributos estaticos

    _repartidores = []

    # Constructor

    def __init__(self):
        super().__init__()



        Repartidor._repartidores.append(self)

    # Getters y Setters

    

    @classmethod
    def getRepartidores(cls):
        return cls._repartidores

    @classmethod
    def setRepartidores(cls, repartidores):
        cls._repartidores = repartidores

    # Metodos



    # Implementacion de la interfaz

    def informacion(self):
        pass