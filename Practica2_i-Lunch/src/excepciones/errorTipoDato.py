from src.excepciones.errorAplicacion import ErrorAplicacion

class ErrorTipoDato(ErrorAplicacion):
    
    # Constructor

    def __init__(self, error):
        super().__init__("Tipo de dato incorrecto: " + error)