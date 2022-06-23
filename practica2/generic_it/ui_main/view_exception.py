'''
@File    :   view_exception.py
@Time    :   2022/01/31
@Author  :   Erik Gonzalez
@Version :   1.0
@Desc    : Exception padre para las excepciones que ocurren dentro de la vista
'''

from .error_aplicacion import ErrorAplicacion

class ViewException(ErrorAplicacion):
    def __init__(self, message):
        super().__init__(extra_message=message)
