from gestorAplicacion.usuariosRestaurante.usuario import Usuario

class Cliente(Usuario):

    # Atributos estaticos

    _clientes = []

    # Constructor

    def __init__(self):
        super().__init__()


        
        Cliente._clientes.append(self)

    # Getters y Setters

    

    @classmethod
    def getClientes(cls):
        return cls._clientes

    @classmethod
    def setClientes(cls, clientes):
        cls._clientes = clientes

    # Metodos



    # Implementacion de la interfaz

    def informacion(self):
        pass