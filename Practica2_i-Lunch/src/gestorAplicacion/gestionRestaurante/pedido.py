class Pedido:

    # Atributos estaticos

    _pedidos = []

    # Constructor

    def __init__(self):


        Pedido._pedidos.append(self)

    # Getters y Setters

    

    @classmethod
    def getPedidos(cls):
        return cls._pedidos

    @classmethod
    def setPedidos(cls, pedidos):
        cls._pedidos = pedidos

    # Metodos
    
