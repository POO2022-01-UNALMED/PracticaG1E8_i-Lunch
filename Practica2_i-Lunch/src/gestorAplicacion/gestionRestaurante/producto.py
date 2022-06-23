class Producto:

    # Atributos estaticos

    _productos = []

    # Constructor

    def __init__(self, nombre = "", descripcion = "", precio = 0, disponibilidad = False, restriccion = False, cantidad = 0):
        self._nombre = nombre
        self._descripcion = descripcion
        self._precio = precio
        self._restriccion = restriccion
        self._disponibilidad= disponibilidad
        self._cantidad = cantidad
        
        self._estado = False # Sin preparar aun

        Producto._productos.append(self)

    # Getters y Setters

    def getNombre(self):
        return self._nombre

    def setNombre(self, nombre):
        self._nombre = nombre

    def getDescripcion(self):
        return self._descripcion

    def setDescripcion(self, descripcion):
        self._descripcion = descripcion

    def getPrecio(self):
        return self._precio

    def setPrecio(self, precio):
        self._precio = precio

    def getDisponibilidad(self):
        return self._disponibilidad

    def setDisponibilidad(self, disponibilidad):
        self._disponibilidad = disponibilidad

    def getRestriccion(self):
        return self._restriccion

    def setRestriccion(self, restriccion):
        self._restriccion =  restriccion

    def getCantidad(self):
        return self._cantidad

    def setCantidad(self, cantidad):
        self._cantidad = cantidad

    def getEstado(self):
        return self._estado

    @classmethod
    def getProductos(cls):
        return cls._productos

    @classmethod
    def setProductos(cls, productos):
        cls._productos = productos

    # ToString

    def __str__(self):
        return f"Nombre: {self._nombre} \n" \
               f"Descripcion: {self._descripcion} \n" \
               f"Precio: ${self._precio}\n" \
               f"Disponibilidad: {self._disponibilidad} \n" \
               f"Restriccion de edad: {self._restriccion}\n" \
               f"Cantidad disponible: {self._cantidad}"
    