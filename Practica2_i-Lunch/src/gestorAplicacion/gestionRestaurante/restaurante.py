class Restaurante:

    # Atributos estaticos

    _restaurantes = []

    # Constructor

    def __init__(self):


        Restaurante._restaurantes.append(self)

    # Getters y Setters

    

    @classmethod
    def getRestaurantes(cls):
        return cls._restaurantes

    @classmethod
    def setRestaurantes(cls, restaurantes):
        cls._restaurantes = restaurantes

    # Metodos

    