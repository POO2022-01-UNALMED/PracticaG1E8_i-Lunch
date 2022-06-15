from gestorAplicacion.usuariosRestaurante.usuario import Usuario

class Cliente(Usuario):

    # Atributos estaticos

    _clientes = []

    # Constructor

    def __init__(self, nombre = "", email = "", telefono = 0, direccion = "", edad = 0):
        self._nombre = nombre
        self._email = email
        self._telefono = telefono
        self._direccion = direccion
        self._edad = edad

        self._historialPedidos = []

        Cliente._clientes.append(self)

    # Getters y Setters

    def getNombre(self):
        return self._nombre

    def setNombre(self, nombre):
        self._nombre = nombre

    def getEmail(self):
        return self._email

    def setEmail(self, email):
        self._email = email
    
    def getTelefono(self):
        return self._telefono

    def setTelefono(self, telefono):
        self._telefono = telefono

    def getDireccion(self):
        return self._direccion

    def setDireccion(self, direccion):
        self._direccion = direccion

    def getEdad(self):
        return self._edad

    def setEdad(self, edad):
        self._edad  = edad

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

    def agregarPedidoHistorial(self,  pedido):
        self._historialPedidos.append(pedido)
    
    # Implementacion de la interfaz

    def informacion(self):
        return f"El cliente {self._nombre} tiene email {self._correoElectronico} y telefono {self._telefono}.\n" \
               f"Tiene {self._edad} años.\n" \
               f"Vive en la direccion {self._direccion}.\n" \
               f"Ha hecho {len(self._historialPedidos)} pedidos en la aplicacion."