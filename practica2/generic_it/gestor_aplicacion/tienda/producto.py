# @author: Emilio Porras
# @summary Esta clase busca representar el comportamiento de un producto traido a la tienda por un cliente, el cual espera sea reparado.
# Estructuras relevantes: componentes corresponde a la lista de todos los componentes que conforman el producto, pueden estar averiados o no.

class Producto:
    productos = list()
    def __init__(self, nombre, componentes):
        self._nombre = nombre
        self._componentes = componentes
        self.productos.append(self)
    
    # @param componente
    # @summary El metodo agregarComponente recibe como parametro un componente y lo agrega a la lista de componentes del producto.
	
    def agregarComponente(self, componente):
        self._componentes.append(componente)
        
    # @param componente
    # @summary El metodo quitarComponente recibe como parametro un componente y lo quita de la lista de componentes del producto.
   
    def quitarComponente(self, componente):
        self._componentes.remove(componente)
        
    def getComponentes(self):
        return self._componentes
    
    def __str__(self):
        return self._nombre

    def getNombre(self):
        return self._nombre
    
    def setNombre(self, nombre):
        self._nombre = nombre
        