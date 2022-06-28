from excepciones.errorAplicacion import ErrorAplicacion

class ExcepcionDatos(ErrorAplicacion):
    
    # Constructor

    def __init__(self, error):
        super().__init__(f"Error en los datos:\n{error}")