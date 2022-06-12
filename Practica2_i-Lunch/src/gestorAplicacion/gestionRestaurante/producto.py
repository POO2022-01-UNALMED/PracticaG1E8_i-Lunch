from src.gestorAplicacion.usuariosRestaurante.usuario import Usuario
from src.gestorAplicacion.usuariosRestaurante.empleado import Empleado
from src.gestorAplicacion.usuariosRestaurante.administrador import Administrador
from src.gestorAplicacion.usuariosRestaurante.repartidor import Repartidor
from src.gestorAplicacion.usuariosRestaurante.mesero import Mesero
from src.gestorAplicacion.usuariosRestaurante.chef import Chef
from src.gestorAplicacion.usuariosRestaurante.cliente import Cliente

from src.gestorAplicacion.gestionRestaurante.restaurante import Restaurante
from src.gestorAplicacion.gestionRestaurante.pedido import Pedido
from src.gestorAplicacion.gestionRestaurante.estadoPedido import EstadoPedido
from src.gestorAplicacion.gestionRestaurante.tipoPedido import TipoPedido

class Producto:

    # Atributos estaticos

    _productos = []

    # Constructor

    def __init__(self):


        Producto._productos.append(self)

    # Getters y Setters

    

    @classmethod
    def getProductos(cls):
        return cls._productos

    @classmethod
    def setProductos(cls, productos):
        cls._productos = productos

    # Metodos

    