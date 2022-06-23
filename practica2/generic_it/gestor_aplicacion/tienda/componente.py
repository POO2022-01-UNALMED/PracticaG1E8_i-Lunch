"""
 * 
 * @author Felipe Miranda
 * @summary Componente son las posibles partes que requiere un producto para ser reparado. Se almacenan en bodega. 
 * tienen averiado (si el producto esta bueno o no), precio (de aca se calcularan las ganancias), y nombre. 
 """
class Componente:
    componentes = list()
    def __init__ (self, _nombre, _averiado, _precio = 0):
            self._nombre = _nombre
            self._averiado = _averiado
            self._precio = _precio
            Componente.componentes.append(self)

    def setNombre(self, nombre):
        self._nombre = nombre

    def getNombre(self):
        return self._nombre

    def isAveriado(self):
        return self._averiado

    def getPrecio(self):
        return self._precio

    def setPrecio(self, precio):
        self.precio = precio

    def __str__(self):
        return self._nombre

    
