class Pedido:

    # Atributos estaticos

    _pedidos = []
    _totalPedidos = 0

    # Constructor

    def __init__(self, cliente = None, tipo = "", estado = "", mensaje = "", fechaHora = None, precioTotal = 0, restaurante = None):
        self._cliente = cliente
        self._tipo = tipo
        self._estado = estado
        self._mensaje = mensaje
        self._fechaHora = fechaHora
        self._precioTotal = precioTotal
        self._restaurante = restaurante
        
        self._codigo = Pedido._totalPedidos
        self._productos = []
        cliente.agregarPedidoHistorial(self)
        Pedido._pedidos.append(self)
        Pedido._totalPedidos += 1

    # Getters y Setters

    def getCliente(self):
        return self._cliente

    def setCliente(self, nuevoCliente):
        self._cliente = nuevoCliente

    def getCodigo(self):
        return self._codigo

    def setCodigo(self, codigo):
        self._codigo = codigo

    def getEstado(self):
        return self._estado

    def setEstado(self, estado):
        self._estado = estado

    def getTipo(self):
        return  self._tipo

    def setTipo(self, tipo):
        self._tipo = tipo

    def getMensaje(self):
        return self._mensaje

    def setMensaje(self, mensaje):
        self._mensaje = mensaje

    def getFechaHora(self):
        return self._fechaHora

    def setFechaHora(self, fechaHora):
        self._fechaHora = fechaHora

    def getPrecioTotal(self):
        return self._precioTotal

    def setPrecioTotal(self, precioTotal):
        self._precioTotal = precioTotal

    def getRestaurante(self):
        return self._restaurante

    def setRestaurante(self, restaurante):
        self._restaurante = restaurante

    def getProductos(self):
        return self._productos

    def setProductos(self, productos):
        self._productos = productos

    @classmethod
    def getPedidos(cls):
        return cls._pedidos

    @classmethod
    def setPedidos(cls, pedidos):
        cls._pedidos = pedidos

    @classmethod
    def getTotalPedidos(cls):
        return cls._totalPedidos

    @classmethod
    def setTotalPedidos(cls, totalPedidos):
        cls._totalPedidos = totalPedidos

    # Metodos
    
    def calcularPrecioTotal(self):
        sum = 0
        for i in self._productos:
            sum += i.getPrecio()
            
        return sum

    # ToString

    def __str__(self):
        return f"Pedido {self._codigo} hecho por el cliente {self._cliente}\n" \
               f"Fecha y hora: {self._fechaHora}\n" \
               f"Estado: {self._estado}\n" \
               f"Mensaje: {self._mensaje}\n" \
               f"Tipo: {self._tipo}\n" \
               f"Precio total: ${self._precioTotal}"