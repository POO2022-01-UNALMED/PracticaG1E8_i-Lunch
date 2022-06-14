from gestorAplicacion.usuariosRestaurante.usuario import Usuario

class Cliente(Usuario):

    # Atributos estaticos

    _clientes = []

    # Constructor

    def __init__(self,telefono = None, nombre = None, direccion = None, edad = None, pedidoActivo = None, correoElectronico = None):
        super().__init__()
        self._telefono = telefono
        self._nombre = nombre
        self._direccion = direccion
        self._edad = edad
        self._correoElectronico = correoElectronico
        self._pedidoActivo = pedidoActivo
        self._historialPedidos = []

        
        Cliente._clientes.append(self)

    # Getters y Setters
    def getTelefono(self):
        return self._telefono
    def setTelefono(self,telefono):
        self._telefono = telefono
    def getNombre(self):
        return self._nombre
    def setNombre(self, nombre):
        self._nombre = nombre
    def getDireccion(self):
        return self._direccion
    def setDireccion(self,direccion):
        self._direccion = direccion
    def getEdad(self):
        return self._edad
    def setEdad(self, edad):
        self._edad  = edad
    def getCorreoElectronico(self):
        return self._correoElectronico
    def setCorreoElectronico(self, correo):
        self._correoElectronico = correo
    def getHistorialPedidos(self):
        return self._historialPedidos
    def setHistorialPedidos(self, historial):
        self._historialPedidos = historial

    @classmethod
    def getClientes(cls):
        return cls._clientes

    @classmethod
    def setClientes(cls, clientes):
        cls._clientes = clientes

    # Metodos



    # Implementacion de la interfaz

    def informacion(self):
        return f'El cliente {self._nombre} con email {self._correoElectronico} y telefono {self._telefono}' \
               f'vive en la direccion {self._direccion} y tiene {self._edad} años.\n Ha hecho {len(self._historialPedidos)}' \
               f' pedidos en la aplicacion'

    def agregarPedidoHistorial(self,  pedido):
        self._historialPedidos.append(pedido)