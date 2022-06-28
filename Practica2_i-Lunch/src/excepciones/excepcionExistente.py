from excepciones.excepcionCampo import ExcepcionCampo

class ExcepcionExistente(ExcepcionCampo):
    
    # Constructor

    def __init__(self, error):
        super().__init__(f"Un objeto con el mismo nombre ya existe: \"{error}\"")