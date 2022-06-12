class ErrorAplicacion(Exception):
    
    # Constructor

    def __init__(self, error):
        super().__init__("Manejo de errores de la aplicacion: " + error)