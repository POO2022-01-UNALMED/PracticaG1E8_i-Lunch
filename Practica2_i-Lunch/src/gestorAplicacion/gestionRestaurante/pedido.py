from src.gestorAplicacion.usuariosRestaurante.usuario import Usuario
from src.gestorAplicacion.usuariosRestaurante.empleado import Empleado
from src.gestorAplicacion.usuariosRestaurante.administrador import Administrador
from src.gestorAplicacion.usuariosRestaurante.repartidor import Repartidor
from src.gestorAplicacion.usuariosRestaurante.mesero import Mesero
from src.gestorAplicacion.usuariosRestaurante.chef import Chef
from src.gestorAplicacion.usuariosRestaurante.cliente import Cliente

from src.gestorAplicacion.gestionRestaurante.restaurante import Restaurante
from src.gestorAplicacion.gestionRestaurante.producto import Producto
from src.gestorAplicacion.gestionRestaurante.estadoPedido import EstadoPedido
from src.gestorAplicacion.gestionRestaurante.tipoPedido import TipoPedido

class Pedido:

    # Atributos estaticos

    _pedidos = []

    # Constructor

    def __init__(self):


        Pedido._pedidos.append(self)

    # Getters y Setters

    

    @classmethod
    def getPedidos(cls):
        return cls._pedidos

    @classmethod
    def setPedidos(cls, pedidos):
        cls._pedidos = pedidos

    # Metodos
    
