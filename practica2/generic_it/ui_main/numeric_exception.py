'''
@File    :   numeric_exception.py
@Time    :   2022/01/31
@Author  :   Erik Gonzalez
@Version :   1.0
@Desc    :   Error cuando se ingresan letras en vez de numeros
'''

from .field_exception import  FieldException

class NumericException(FieldException):
    def __init__(self, message="Esta usando valores no numericos"):
        super().__init__(message)
