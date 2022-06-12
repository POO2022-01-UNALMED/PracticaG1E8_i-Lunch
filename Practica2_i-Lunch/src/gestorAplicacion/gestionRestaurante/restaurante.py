from src.gestorAplicacion.usuariosRestaurante.usuario import Usuario
from src.gestorAplicacion.usuariosRestaurante.empleado import Empleado
from src.gestorAplicacion.usuariosRestaurante.administrador import Administrador
from src.gestorAplicacion.usuariosRestaurante.repartidor import Repartidor
from src.gestorAplicacion.usuariosRestaurante.mesero import Mesero
from src.gestorAplicacion.usuariosRestaurante.chef import Chef
from src.gestorAplicacion.usuariosRestaurante.cliente import Cliente

from src.gestorAplicacion.gestionRestaurante.producto import Producto
from src.gestorAplicacion.gestionRestaurante.pedido import Pedido
from src.gestorAplicacion.gestionRestaurante.estadoPedido import EstadoPedido
from src.gestorAplicacion.gestionRestaurante.tipoPedido import TipoPedido

class Restaurante:

    # Atributos estaticos

    _restaurantes = []

    # Constructor

    def __init__(self):


        Restaurante._restaurantes.append(self)

    # Getters y Setters

    

    @classmethod
    def getRestaurantes(cls):
        return cls._restaurantes

    @classmethod
    def setRestaurantes(cls, restaurantes):
        cls._restaurantes = restaurantes

    # Metodos

    