'''
@File    :   error_aplicacion.py
@Time    :   2022/01/31
@Author  :   Erik Gonzalez
@Version :   1.0
@Desc    :  Exception principal de la que heredan todas
'''

class ErrorAplicacion(Exception):
    def __init__(self, extra_message="", message="Manejo de errores de la Aplicación: "):
        c_type = type(self)
        self.message = message + " " + extra_message
        super().__init__(self.message)
