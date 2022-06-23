from ..personal.empleado import Empleado
from ..tienda.servicio import Servicio
from ..tienda.bodega import Bodega

# @author: Emilio Porras
# @summary Esta clase busca representar el comportamiento de un empleado tipo tecnico
# Estructuras relevantes: servicios es una lista de servicios que se va modificando a medida que el tecnico toma o finaliza servicios

class Tecnico(Empleado):
    tecnicos = list()
    def __init__(self, nombre, cedula, servicios = None):
            super().__init__(nombre, cedula)
            self.tecnicos.append(self)
            
    # @param servicio
    # @summary El metodo verificarProblemas es un metodo auxiliar de la clase, el cual recibe un servicio y devuelve una lista con los componentes
    # averiados en el producto correspondiente a ese servicio
    
    def verificarProblemas(self, servicio):
        producto = servicio.getProducto()
        averiados = list()
        for componente in producto.getComponentes():
            if componente.isAveriado():
                averiados.append(componente)
        return averiados
    
    # @param componente
    # @summary El metodo buscarComponente es un metodo auxiliar de la clase, el cual recibe un componente y devuelve booleano dependiendo de si un componente
    # con el mismo nombre se encuentra en la Bodega o no.
    
    def buscarComponente(self, componente):
        return Bodega.sacarComponente(componente.getNombre())
    
    # @param servicio
    # @summary El metodo diagnosticar recibe como paremetro un servicio y modifica en este su atributo diagostico, brindando informacion 
    # sobre los problemas del producto correspondiente.
    
    def diagnosticar(self, servicio):
        servicio.setDiagnostico("Se encontraron problemas en los siguientes componentes del producto: "+ str([componente.__str__() for componente in self.verificarProblemas(servicio)]))
        
    # @param servicio
    # @summary El metodo reparar recibe como parametro un servicio. Luego, revisa si los componentes aveados estan disponibles en la bodega y, a 
    # aquellos que estan disponibles, los remueve de la lista de Bodega y los reemplaza en la lista de componentes del producto. Tambien, va sumando
    # el precio de los componentes utilizados en el atributo costo de servicio.
    
    def reparar(self, servicio):
        producto = servicio.getProducto()
        averiados = self.verificarProblemas(servicio)
        for componente in averiados:
            remplazo = self.buscarComponente(componente)
            if remplazo != None:
                componenteBodega = Bodega.sacarComponente(remplazo)
                producto.quitarComponente(componente)
                producto.agregarComponente(componenteBodega)
                servicio.setCosto(servicio.getCosto()+componenteBodega.getPrecio())
        servicio.setReparado(True)
        self.quitarServicio(servicio)
            
    # @param servicio
    # @summary El metodo asignarServicio recibe como parametro un servicio y lo agrega a la lista de servicios del tecnico en cuestion.
    
    def asignarServicio(self, servicio):
        self.getServicios().append(servicio)
        
    # @param servicio
    # summary El metodo quitarServicio recibe como parametro un servicio y lo remueve de la lista de servicios del tecnico en cuestion.
        
    def quitarServicio(self, servicio):
        self.getServicios().remove(servicio)
        
    # @param CaraRegistradora
    # @summary cobrarSalario utiliza el porcentaje que se le debe pagar a los tecnicos para calcular cuanto cobrar por su trabajo
    # y descontar de la caja registradora.
    
    def cobrarSalario(self, cajaRegistradora):
        porcentaje = 0.02
        self._cartera += cajaRegistradora.descontar(porcentaje)
        
    def __str__(self):
        return "Tecnico: " + self.getNombre()    