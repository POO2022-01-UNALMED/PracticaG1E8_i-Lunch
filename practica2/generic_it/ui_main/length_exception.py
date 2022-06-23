'''
@File    :   length_exception.py
@Time    :   2022/02/01
@Author  :   Erik Gonzalez
@Version :   1.0
@Desc    :  Exception principal de la que heredan todas
'''

from .field_exception import FieldException


class LengthException(FieldException):
    def __init__(self, message="La longitud de la cadena no es suficiente"):
        super().__init__(message)
