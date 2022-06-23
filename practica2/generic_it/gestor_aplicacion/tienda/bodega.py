'''
@File    :   bodega.py
@Time    :   2022/01/26
@Author  :   Erik Gonzalez
@Version :   1.0
@Desc    :   La bodega se encarga de almacenar los componentes de los cuales
dispone la empresa, que puede usar el tecnico para remplazar piezas.
'''

class Bodega:
    _componentes = []

    @classmethod
    def agregarComponente(cls, componente):
        cls._componentes.append(componente)

    @classmethod
    def sacarComponente(cls, nombre):
        if type(nombre) is str:
            for componente in cls._componentes:
                if componente.getNombre() == nombre:
                    return componente
            return None
        else:
            cls._componentes.remove(nombre)
            return nombre

    @classmethod
    def getComponentes(cls):
        return cls._componentes

    @classmethod
    def setComponentes(cls, componentes):
        cls._componentes = componentes
