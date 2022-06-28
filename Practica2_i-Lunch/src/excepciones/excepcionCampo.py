from excepciones.errorAplicacion import ErrorAplicacion

class ExcepcionCampo(ErrorAplicacion):
    
    # Constructor

    def __init__(self, error):
        super().__init__(f"Error en el campo:\n{error}")