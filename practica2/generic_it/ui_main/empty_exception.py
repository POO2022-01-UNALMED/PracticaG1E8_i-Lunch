'''
@File    :   empty_exception.py
@Time    :   2022/01/31
@Author  :   Erik Gonzalez
@Version :   1.0
@Desc    :   Error cuando esta vacio el campo
'''

from .field_exception import FieldException


class EmptyException(FieldException):
    def __init__(self, message="Campo vacio"):
        super().__init__(message)
