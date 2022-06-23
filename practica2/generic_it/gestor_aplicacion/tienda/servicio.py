# from ..tienda.cliente import Cliente
# from ..tienda.producto import Producto
# from ..personal.dependiente import Dependiente
# from ..personal.tecnico import Tecnico
from queue import Empty
"""
 * 
 * @author Felipe Miranda
 * @summary Servicio deberia contener toda la informacion que relaciona a un cliente y su producto a reparar 
 * con los empleados (el dependiente que le atendio y el tecnico encargado de la reparacion) del sistema. 
 *
 """

class Servicio:
    servicios = list()
    def __init__(self, _tecnico, _producto, _cliente, _dependiente):
        self._tecnico = _tecnico
        self._producto = _producto
        self._cliente = _cliente
        self._dependiente = _dependiente
        self._reparado = False
        self._costo = 0
        self._diagnostico = None
        self._pagado = False
        if self.servicios is Empty:
            self.identificador = 0
        else:
            self.identificador = len(self.servicios)
        self.servicios.append(self)

    def setPagado(self, _pagado):
        self._pagado = _pagado

    def getProducto(self):
        return self._producto

    def getDependiente(self):
        return self._dependiente

    def anadirCosto(self, precio):
        self.costo+=precio

    def getCosto(self):
        return self._costo

    def getDiagnostico(self):
        return self._diagnostico

    def isPagado(self):
        return self._pagado

    def setCosto(self, costo):
        self._costo=costo

    def getIdentificador(self):
        return self.identificador

    def getCliente(self):
        return self._cliente

    def setCliente(self, cliente):
        self._cliente = cliente

    def setDiagnostico(self, diagnostico):
        self._diagnostico = diagnostico
        
    @classmethod
    def getServicios(cls):
        return cls.servicios

    @classmethod
    def setServicios(cls, servicios):
        cls.servicios = servicios

    def getTecnico(self):
        return self._tecnico

    def isReparado(self):
        return self._reparado

    def setReparado(self, reparado):
        self._reparado = reparado

    def __str__(self):
        return "Identificador del servicio: " + str(self.identificador) + "\nCliente: " + str(self._cliente) + "\nProducto asociado: " + str(self._producto)+ "\nReparado: " + str(self._reparado) + "\nPagado: " + str(self._pagado) + "\n"