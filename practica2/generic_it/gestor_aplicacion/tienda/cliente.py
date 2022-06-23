'''
@File    :   cliente.py
@Time    :   2022/01/26
@Author  :   Erik Gonzalez
@Version :   1.0
@Desc    :   El cliente tiene tres funcionalidades. solicitar una reparacion,
             pagar es servicio que se se presto y recibir su producto.
             El cliente muchas veces puede pa
'''


class Cliente():
    clientes = []

    def __init__(
            self,
            nombre,
            cedula,
            productos,
            dependiente,
            cartera,
            direccion=None
    ):
        if direccion is not None:
            self._direccion = direccion
        self._nombre = nombre
        self._cedula = cedula
        self._productos = productos
        self._dependiente = dependiente
        self._cartera = cartera
        self._recibos = []
        Cliente.clientes.append(self)

    def solicitarReparacion(self, producto):
        self._dependiente.atenderCliente(self, producto)
        self._productos.append(producto)

    def pagarServicio(self, servicio, cobro):
        if(not servicio.isPagado() and self._cartera >= cobro):
            self._cartera -= cobro

    def recibirProducto(self, producto):
        self._productos.append(producto)

    def getNombre(self):
        return self._nombre

    def setNombre(self, nombre):
        self._nombre = nombre

    def getCedula(self):
        return self._cedula

    def getProductos(self):
        return self._productos

    def setProductos(self, productos):
        self._productos = productos

    def getDependiente(self):
        return self._dependiente

    def setDepediente(self, dependiente):
        self._dependiente = dependiente

    def recibirRecibo(self, recibo):
        self._recibos.append(recibo)

    def getRecibos(self):
        return self._recibos

    @classmethod
    def getClientes(cls):
        return cls.clientes

    @classmethod
    def setClientes(cls, clientes):
        cls.clientes = clientes

    def getCartera(self):
        return self._cartera

    def __str__(self):
        return "Nombre: " + str(self._nombre) + " CC: " + str(self._cedula) + " Cartera: " + str(self._cartera)# + " Direccion: " + str(self._direccion)
