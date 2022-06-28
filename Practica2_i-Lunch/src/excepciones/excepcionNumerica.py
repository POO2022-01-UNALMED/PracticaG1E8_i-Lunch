from excepciones.excepcionDatos import ExcepcionDatos

class ExcepcionNumerica(ExcepcionDatos):
    
    # Constructor

    def __init__(self, error):
        super().__init__(f"Se debe de usar un dato de tipo numerico y usaste un dato de tipo \"{type(error).__name__}\"")