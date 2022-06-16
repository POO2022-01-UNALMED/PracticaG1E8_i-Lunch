from gestorAplicacion.gestionRestaurante.estadoPedido import EstadoPedido
from gestorAplicacion.gestionRestaurante.tipoPedido import TipoPedido

from gestorAplicacion.usuariosRestaurante.empleado import Empleado

class Repartidor(Empleado):

    # Atributos estaticos

    _repartidores = []

    # Constructor

    def __init__(self, cedula = 0, nombre = "", disponibilidad = False, salario = 0, restaurante = None, poseeVehiculo = False, placa = "", tipoVehiculo = ""):
        super().__init__(cedula, nombre, "Repartidor", disponibilidad, salario, restaurante)

        self._poseeVehiculo = poseeVehiculo

        # Solo agregar informacion del vehiculo si se posee uno
        if poseeVehiculo:
            self._placa = placa
            self._tipoVehiculo = tipoVehiculo
        else:
            self._placa = None
            self._tipoVehiculo = None

        self._pedidosEntregados = []

        Repartidor._repartidores.append(self)

    # Getters y Setters

    def getPoseeVehiculo(self):
        return self._poseeVehiculo

    def setPoseeVehiculo(self, poseeVehiculo):
        self._poseeVehiculo = poseeVehiculo

    def getPlaca(self):
        return self._placa

    def setPlaca(self, placa):
        self._placa = placa

    def getTipoVehiculo(self):
        return self._tipoVehiculo

    def setTipoVehiculo(self, tipoVehiculo):
        self._tipoVehiculo = tipoVehiculo
    
    def getPedidosEntregados(self):
        return self._pedidosEntregados
    
    def setPedidosEntregados(self, pedidosEntregados):
        self._pedidosEntregados = pedidosEntregados

    @classmethod
    def getRepartidores(cls):
        return cls._repartidores

    @classmethod
    def setRepartidores(cls, repartidores):
        cls._repartidores = repartidores

    # Metodos

    # Simulacion de llevar un pedido a domicilio a un cliente
    def repartirPedido(self, pedido):
        self._pedidosEntregados.append(pedido)

        # Solo se puede hacer si el pedido es de tipo domicilio y ya esta listo. Cambiar el estado del pedido
        if pedido.getEstado() == EstadoPedido.LISTO.value and pedido.getTipo() == TipoPedido.DOMICILIO.value:
            pedido.setEstado(EstadoPedido.DESPACHADO)
    
    # Implementacion de la interfaz

    def informacion(self):
        info = f"El Repartidor {self._nombre} con C.C. {self._cedula} trabaja en el restaurante {self._restaurante.getNombre()}.\n" \
               f"Tiene un salario de: ${self._salario}.\n"
        
        if self._poseeVehiculo:
            info += f"Posee un vehiculo de tipo {self._tipoVehiculo}, con placa {self._placa}.\n"
        else:
            info += "No tiene vehiculo.\n"

        if self._disponibilidad:
            return info + "Esta disponible actualmente."
        else:
            return info + "No esta disponible actualmente."