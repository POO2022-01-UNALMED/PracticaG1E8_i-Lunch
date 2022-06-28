from excepciones.excepcionCampo import ExcepcionCampo

class ExcepcionVacio(ExcepcionCampo):
    
    # Constructor

    def __init__(self, error):
        super().__init__(f"Por favor rellenar el campo de informacion: \"{error}\"")