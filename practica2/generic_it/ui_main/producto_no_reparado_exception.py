'''
@File    :   producto_no_reparado.py
@Time    :   2022/01/31
@Author  :   Erik Gonzalez
@Version :   1.0
@Desc    :   El error ocurre cuando se intenta cobrar el servicio pero el producto no ha sido reparado
'''

from .view_exception import ViewException

class ProductoNoReparadoException(ViewException):
    def __init__(self, message="El producto no ha sido reparado, porfavor revise el servicio prestado"):
        super().__init__(message)
