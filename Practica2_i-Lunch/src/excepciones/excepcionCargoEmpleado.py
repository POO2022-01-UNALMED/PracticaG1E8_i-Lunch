from excepciones.excepcionCampo import ExcepcionCampo

class ExcepcionCargoEmpleado(ExcepcionCampo):
    
    # Constructor

    def __init__(self, error):
        super().__init__(f"Tipo de empleado no válido: \"{error}\". Por favor utilizar \"Chef\", \"Mesero\" o \"Repartidor\"")