class Producto:

    # Atributos estaticos

    _productos = []

    # Constructor

    def __init__(self):


        Producto._productos.append(self)

    # Getters y Setters

    

    @classmethod
    def getProductos(cls):
        return cls._productos

    @classmethod
    def setProductos(cls, productos):
        cls._productos = productos

    # Metodos

    