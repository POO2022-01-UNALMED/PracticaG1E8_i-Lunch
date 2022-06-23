'''
@File    :   client_incorrecto_exception.py
@Time    :   2022/01/31
@Author  :   Erik Gonzalez
@Version :   1.0
@Desc    :   El error ocurre cuando se intenta cobrar el servicio pero el producto no ha sido reparado
'''

from .view_exception import ViewException

class ClientIncorrectoException(ViewException):
    def __init__(self, message="Esta usado un id del cliente incorrecto"):
        super().__init__(message)
