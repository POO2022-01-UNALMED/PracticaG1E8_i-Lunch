from src.gestorAplicacion.usuariosRestaurante.usuario import Usuario
from src.gestorAplicacion.usuariosRestaurante.empleado import Empleado
from src.gestorAplicacion.usuariosRestaurante.administrador import Administrador
from src.gestorAplicacion.usuariosRestaurante.repartidor import Repartidor
from src.gestorAplicacion.usuariosRestaurante.mesero import Mesero
from src.gestorAplicacion.usuariosRestaurante.chef import Chef
from src.gestorAplicacion.usuariosRestaurante.cliente import Cliente

from src.gestorAplicacion.gestionRestaurante.restaurante import Restaurante
from src.gestorAplicacion.gestionRestaurante.producto import Producto
from src.gestorAplicacion.gestionRestaurante.pedido import Pedido
from src.gestorAplicacion.gestionRestaurante.estadoPedido import EstadoPedido
from src.gestorAplicacion.gestionRestaurante.tipoPedido import TipoPedido

class Empleado(Usuario):

    # Atributos estaticos

    _empleados = []

    # Constructor

    def __init__(self, cedula = 0, nombre = "", cargo = "", disponibilidad = False, salario = 0, restaurante = None):
        self._cedula = cedula
        self._nombre = nombre
        self._cargo = cargo
        self._disponibilidad = disponibilidad
        self._salario = salario
        self._restaurante = restaurante

        Empleado._empleados.append(self)

    # Getters y Setters
    
    def getCedula(self):
        return self._cedula

    def setCedula(self, cedula): 
        self._cedula = cedula

    def getNombre(self): 
        return self._nombre

    def setNombre(self, nombre):
        self._nombre = nombre

    def getCargo(self): 
        return self._cargo

    def setCargo(self, cargo):
        self._cargo = cargo

    def getSalario(self): 
        return self._salario

    def getDisponibilidad(self): 
        return self._disponibilidad

    def setDisponibilidad(self, disponibilidad):
        self._disponibilidad = disponibilidad

    def setSalario(self, salario):
        self._salario = salario


    def getRestaurante(self):
        return self._restaurante


    def setRestaurante(self, restaurante):
        self._restaurante = restaurante

    @classmethod
    def getEmpleados(cls):
        return cls._empleados

    @classmethod
    def setEmpleados(cls, empleados):
        cls._empleados = empleados

    # Metodos

    def procesarPedido(self, pedido):
        if self._restaurante.verificarPedido(pedido) and self._restaurante.verificarProductos(pedido):
            return True
        else:
            return False

    def actualizarEstadoPedido(self, pedido, aceptado):
        if not aceptado:
            pedido.setEstado(EstadoPedido.RECHAZADO.value)
            return False
        
        if pedido.getEstado() == "Recibido":
            pedido.setEstado(EstadoPedido.ACEPTADO.value);
        elif pedido.getEstado() == "Aceptado":
            pedido.setEstado(EstadoPedido.PREPARACION.value);
        elif pedido.getEstado() == "EnPreparacion":
            pedido.setEstado(EstadoPedido.LISTO.value);
        elif pedido.getEstado() == "Listo":
            pedido.setEstado(EstadoPedido.DESPACHADO.value);

        return True

    # Implementacion de la interfaz

    def informacion(self):
        info = f"El Empleado {self._nombre} con C.C. {self._cedula} trabaja en el restaurante {self._restaurante.getNombre()}. Tiene un salario de: ${self._salario} y desempeña el cargo de {self._salario}. "
        
        if self._disponibilidad:
            return info + "Está disponible actualmente."
        else:
            return info + "No está disponible actualmente."