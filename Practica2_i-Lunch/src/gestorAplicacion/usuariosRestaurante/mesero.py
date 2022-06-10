from random import randint

from usuariosRestaurante.empleado import Empleado

from gestionRestaurante.estadoPedido import EstadoPedido
from gestionRestaurante.tipoPedido import TipoPedido

class Mesero(Empleado):

    # Constructor

    def __init__(self, cedula = 0, nombre = "", disponibilidad = False, salario = 0, restaurante = None):
        super().__init__(cedula, nombre, "Mesero", disponibilidad, salario, restaurante)
        self._pedidosAtendidos = []
        self._historialPropinas = []
    
    # Getters y Setters

    def getPedidosAtendidos(self):
        return self._pedidosAtendidos

    def setPedidosAtendidos(self, pedidosAtendidos):
        self._pedidosAtendidos = pedidosAtendidos

    def getHistorialPropinas(self):
        return self._historialPropinas

    def setHistorialPropinas(self, historialPropinas):
        self._historialPropinas = historialPropinas

    # Metodos

    def recibirPropina(self, propina):
        self._historialPropinas.append(propina)

    def agregarPedidoHistorial(self, pedido):
        self._pedidosAtendidos.append(pedido)
        self.recibirPropina(randint(1,10))

    def llevarPedido(self, pedido):
        self.agregarPedidoHistorial(pedido)
        
        if pedido.getEstado() == EstadoPedido.LISTO and pedido.getTipo() == TipoPedido.TIENDA:
            pedido.setEstado(EstadoPedido.DESPACHADO)

    def totalPropinas(self):
        total = 0

        for propina in self._historialPropinas:
            total += propina

        return total

    # Implementacion de la interfaz

    def informacion(self):
        info = f"El Mesero {self._nombre} con C.C. {self._cedula} trabaja en el restaurante {self._restaurante.getNombre()}. Tiene un salario de: ${self._salario}. "
        
        if self._disponibilidad:
            return info + "Está disponible actualmente."
        else:
            return info + "No está disponible actualmente."