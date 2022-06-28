from excepciones.excepcionCampo import ExcepcionCampo

class ExcepcionLongitud(ExcepcionCampo):
    
    # Constructor

    def __init__(self, error):
        super().__init__(f"Texto del campo: \"{error[0]}\" demasiado corto, por favor usar {error[1]} caracteres")