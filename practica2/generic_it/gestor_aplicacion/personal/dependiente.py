import random
from ..personal.empleado import Empleado
from ..tienda.servicio import Servicio
from ..personal.tecnico import Tecnico
"""/**
 * 
 * @author Esteban Garcia
 * @summary Busca representar el comportamiento de un empleado dependiente,
 *          quien esta a cargo de atender a los clientes y asignar servicios. Es
 *          mediante el cual se efectuan los pagos y pasan los productos
 *          solicitados para reparar y se devuelven a sus clientes.
 *
 */"""

class Dependiente(Empleado):

    dependientes = []
    _MARGEN_GANANCIA = 1.5

    def __init__(self, nombre, cedula, caja, servicios = None):
        if servicios == None:
            super().__init__(nombre,cedula)
            self._cajaRegistradora = caja
            Dependiente.dependientes.append(self)
        else:
            super().__init__(nombre,cedula)
            self._cajaRegistradora = caja
            Empleado.servicios = servicios
            Dependiente.dependientes.append(self)


    def getCajaRegistradora(self):
        return self._cajaRegistradora
    
    def setCajaRegistradora(self, caja):
        self._cajaRegistradora = caja
    
    def __str__(self):
        return "Dependiente: " + super().getNombre()
    
    @classmethod
    def getDependientes(cls):
        return cls.dependientes
    
    @classmethod
    def setDependientes(cls, dependientes):
        cls.dependientes = dependientes
    
    @classmethod
    def getMargenGanancia(cls):
        return cls._MARGEN_GANANCIA

    def quitarServicio(self, servicio):
        self.getServicios().remove(servicio)

    def asignarServicio(self, servicio):
        self.getServicios().append(servicio)

    def finalizarServicio(self,servicio):
        self.notificarCliente(servicio)
        self.entregarProducto(servicio)

    def generarServicio(self, tecnico, producto, cliente):
        servicio = Servicio(tecnico, producto, cliente, self)
        tecnico.asignarServicio(servicio)
        self.asignarServicio(servicio)

    def atenderCliente(self, cliente, producto):
        if len(cliente.getRecibos()) == 0:
            rand = random.randint(0, len(Tecnico.tecnicos)-1)
            tecnico = Tecnico.tecnicos[rand]
            self.generarServicio(tecnico, producto, cliente)
    
    def registrarPago(self, servicio):
        self._cajaRegistradora.registrarVenta(servicio.getCosto() * Dependiente._MARGEN_GANANCIA, servicio)
        self.quitarServicio(servicio)
    
    def notificarCliente(self, servicio):
        cliente = servicio.getCliente()
        recibo = """Factura # {} \nCliente: {} con cedula {} \nCostoTotal: {} \nRecibir el producto: {}""".format(str(servicio.getIdentificador()), str(cliente.getNombre()), str(cliente.getCedula()), str(servicio.getCosto() * Dependiente._MARGEN_GANANCIA), servicio.getProducto().getNombre())
        cliente.recibirRecibo(recibo)
    
    def entregarProducto(self, servicio):
        servicio.getCliente().recibirProducto(servicio.getProducto())
    
    def cobrarServicio(self, servicio):
        cobro = servicio.getCosto() * Dependiente._MARGEN_GANANCIA
        servicio.getCliente().pagarServicio(servicio, cobro)
        if not servicio.isPagado():
            self._cajaRegistradora.registrarVenta(cobro, servicio)
            servicio.setPagado(True)
    
    def cobrarSalario(self, caja):
        porcentaje = 0.01
        self._cartera += caja.descontar(porcentaje)
    
    def liquidar(self):
        caja = self._cajaRegistradora

        liquidaciones = []
        contador = 0

        for empleado in Empleado.getEmpleados():
            carterainicial = empleado.getCartera()

            empleado.cobrarSalario(caja)

            carteraAhora = empleado.getCartera()
            liquidado = carteraAhora - carterainicial

            contador += liquidado
            liquidaciones.append("El {} ha recibido {} por su trabajo.".format(empleado.__str__(), str(round(liquidado))))
        
        caja.setTotalIngresos(caja.getTotalIngresos() - contador)
        return liquidaciones



