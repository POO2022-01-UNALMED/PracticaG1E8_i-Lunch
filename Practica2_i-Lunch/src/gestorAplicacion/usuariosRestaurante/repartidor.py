from gestorAplicacion.gestionRestaurante.estadoPedido import EstadoPedido
from gestorAplicacion.gestionRestaurante.tipoPedido import TipoPedido
from gestorAplicacion.usuariosRestaurante.empleado import Empleado

class Repartidor(Empleado):

    # Atributos estaticos

    _repartidores = []

    # Aca se guardan todos pedidos entregados por el repartidor en cuestion.
    _pedidosEntregados = []

    # Constructor

    def __init__(self, cedula = 0, nombre = "", disponibilidad = False, salario = 0, restaurante = None, poseeVehiculo = False, placa = " ", tipoVehiculo = " "):
        self._poseeVehiculo = poseeVehiculo
        self._placa = placa
        self._tipoVehiculo = tipoVehiculo
        super().__init__(cedula, nombre, "Mesero", disponibilidad, salario, restaurante)



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

    def repartirPedido(self, pedido):
        Repartidor._pedidosEntregados.append(pedido)
        if pedido.getEstado() == EstadoPedido.LISTO.value and pedido.getTipo() == TipoPedido.DOMICILIO.value:
            pedido.setEstado(EstadoPedido.DESPACHADO)

        

    # Implementacion de la interfaz

    def informacion(self):
        info = f"El Repartidor {self._nombre} con C.C. {self._cedula} trabaja en el restaurante {self._restaurante.getNombre()}. Tiene un salario de: ${self._salario}. "
        
        if self._poseeVehiculo:
            return info + f"Posee un vehiculo de tipo {self._tipoVehiculo}, con placa {self._placa}."
        else:
            info + "No tiene vehiculo."

        if self._disponibilidad:
            return info + "Está disponible actualmente."
        else:
            return info + "No está disponible actualmente."