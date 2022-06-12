from src.gestorAplicacion.usuariosRestaurante.usuario import Usuario
from src.gestorAplicacion.usuariosRestaurante.empleado import Empleado
from src.gestorAplicacion.usuariosRestaurante.administrador import Administrador
from src.gestorAplicacion.usuariosRestaurante.repartidor import Repartidor
from src.gestorAplicacion.usuariosRestaurante.mesero import Mesero
from src.gestorAplicacion.usuariosRestaurante.chef import Chef

from src.gestorAplicacion.gestionRestaurante.restaurante import Restaurante
from src.gestorAplicacion.gestionRestaurante.producto import Producto
from src.gestorAplicacion.gestionRestaurante.pedido import Pedido
from src.gestorAplicacion.gestionRestaurante.estadoPedido import EstadoPedido
from src.gestorAplicacion.gestionRestaurante.tipoPedido import TipoPedido

class Cliente(Usuario):

    # Atributos estaticos

    _clientes = []

    # Constructor

    def __init__(self):
        super().__init__()


        
        Cliente._clientes.append(self)

    # Getters y Setters

    

    @classmethod
    def getClientes(cls):
        return cls._clientes

    @classmethod
    def setClientes(cls, clientes):
        cls._clientes = clientes

    # Metodos



    # Implementacion de la interfaz

    def informacion(self):
        pass