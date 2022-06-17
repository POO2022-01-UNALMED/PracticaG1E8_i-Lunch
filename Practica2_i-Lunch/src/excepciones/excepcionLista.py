from excepciones.excepcionDatos import ExcepcionDatos

class ExcepcionLista(ExcepcionDatos):
    
    # Constructor

    def __init__(self, error):
        super().__init__(f"Numero indicado ({error[0]}) fuera del rango permitido (0, {error[1]})")