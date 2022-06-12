from excepciones.errorAplicacion import ErrorAplicacion

class ErrorReferencia(ErrorAplicacion):
    
    # Constructor

    def __init__(self, error):
        super().__init__("No se encuentra la referencia: " + error)