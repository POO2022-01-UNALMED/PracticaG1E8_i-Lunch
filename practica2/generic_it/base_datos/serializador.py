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
 * Se utiliza para serializar todos los objetos creados durante la ejecucion
 * del proyecto
 * @author Erik Gonzalez
 * @author Felipe Miranda
 * @author Esteban Garcia
 * @author Emilio Porras
 */"""
class Serializador():
    
    def serializar(lista, className):
        def camino(className):
            string = os.path.join(pathlib.Path(__file__).parent.absolute(), "temp\\"+className+".txt")
            return string
        try:
            # Creo el archivo pickle para guardar los objetos
            picklefile = open(camino(className), 'wb')
            # pickle el objeto en el archivo
            pickle.dump(lista, picklefile)
            # cierro el archivo para guardar
            picklefile.close()
            
        except:
            print("paila tuqui tuqui muñeco")

    def serializarTodo():

        Serializador.serializar(Dependiente.getDependientes(), "Dependientes")
        Serializador.serializar(Tecnico.tecnicos, "Tecnicos")
        Serializador.serializar(CajaRegistradora.cajasRegistradoras, "CajasRegistradoras")
        Serializador.serializar(Cliente.getClientes(), "Clientes")
        Serializador.serializar(Componente.componentes, "Componentes")
        Serializador.serializar(Producto.productos, "Productos")
        Serializador.serializar(Servicio.getServicios(), "Servicios")
        Serializador.serializar(Bodega.getComponentes(), "Bodega")
        Serializador.serializar(Empleado.getEmpleados(), "Empleados")

