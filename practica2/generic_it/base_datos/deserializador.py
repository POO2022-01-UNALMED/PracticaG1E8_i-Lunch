import pickle
from gestor_aplicacion.personal.empleado import Empleado
from gestor_aplicacion.tienda.cliente import Cliente
from gestor_aplicacion.personal.tecnico import Tecnico
from gestor_aplicacion.personal.dependiente import Dependiente
from gestor_aplicacion.tienda.servicio import Servicio
from gestor_aplicacion.tienda.componente import Componente
from gestor_aplicacion.tienda.bodega import Bodega
from gestor_aplicacion.tienda.producto import Producto
from gestor_aplicacion.tienda.caja_registradora import CajaRegistradora
import pathlib
import os
""""
/**
 * Clase para deserializar los objetos que se crearon en ejecucion
 * @author Erik Gonzalez
 * @author Felipe Miranda
 * @author Esteban Garcia
 * @author Emilio Porras 
 */"""


class Deserializador():
    
    def deserializar(lista, className):
        def camino(className):
            string = os.path.join(pathlib.Path(__file__).parent.absolute(), "temp\\"+className+".txt")
            return string
        # Leo el archivo
        try:
            picklefile = open(camino(className), 'rb')
        except:
            picklefile = open(camino(className), 'x')
            picklefile = open(camino(className), 'rb')
        # unpickle los datos
        if os.path.getsize(camino(className)) > 0:
            lista = pickle.load(picklefile)
        
        # Cierro el archivo
        picklefile.close()
        return lista
        # Cierro el archivo
    
    def deserializarTodo():
        Dependiente.dependientes = Deserializador.deserializar(Dependiente.dependientes, "Dependientes")
        Tecnico.tecnicos =  Deserializador.deserializar(Tecnico.tecnicos, "Tecnicos")
        CajaRegistradora.cajasRegistradoras = Deserializador.deserializar(CajaRegistradora.cajasRegistradoras, "CajasRegistradoras")
        Cliente.clientes = Deserializador.deserializar(Cliente.clientes, "Clientes")
        Componente.componentes = Deserializador.deserializar(Componente.componentes, "Componentes")
        Producto.productos = Deserializador.deserializar(Producto.productos, "Productos")
        Servicio.servicios = Deserializador.deserializar(Servicio.servicios, "Servicios")
        Bodega._componentes = Deserializador.deserializar(Bodega._componentes, "Componentes")
        Empleado._empleados = Deserializador.deserializar(Empleado._empleados, "Empleados")
        
    