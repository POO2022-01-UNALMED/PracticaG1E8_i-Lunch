from gestorAplicacion.usuariosRestaurante.empleado import Empleado

class Repartidor(Empleado):

    # Atributos estaticos

    _repartidores = []

    # Constructor

    def __init__(self):
        super().__init__()



        Repartidor._repartidores.append(self)

    # Getters y Setters

    

    @classmethod
    def getRepartidores(cls):
        return cls._repartidores

    @classmethod
    def setRepartidores(cls, repartidores):
        cls._repartidores = repartidores

    # Metodos



    # Implementacion de la interfaz

    def informacion(self):
        pass