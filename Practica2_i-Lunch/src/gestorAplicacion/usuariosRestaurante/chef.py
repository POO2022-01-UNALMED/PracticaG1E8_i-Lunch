from gestorAplicacion.usuariosRestaurante.empleado import Empleado

class Chef(Empleado):

    # Atributos estaticos

    _chefs = []

    # Constructor

    def __init__(self):
        super().__init__()



        Chef._chefs.append(self)

    # Getters y Setters



    @classmethod
    def getChefs(cls):
        return cls._chefs

    @classmethod
    def setChefs(cls, chefs):
        cls._chefs = chefs

    # Metodos



    # Implementacion de la interfaz

    def informacion(self):
        pass