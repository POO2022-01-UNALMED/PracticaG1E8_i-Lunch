import pathlib
import pickle
import os

from gestorAplicacion.usuariosRestaurante.empleado import Empleado
from gestorAplicacion.usuariosRestaurante.administrador import Administrador
from gestorAplicacion.usuariosRestaurante.repartidor import Repartidor
from gestorAplicacion.usuariosRestaurante.mesero import Mesero
from gestorAplicacion.usuariosRestaurante.chef import Chef
from gestorAplicacion.usuariosRestaurante.cliente import Cliente

from gestorAplicacion.gestionRestaurante.restaurante import Restaurante
from gestorAplicacion.gestionRestaurante.producto import Producto
from gestorAplicacion.gestionRestaurante.pedido import Pedido

def serializar(lista, className):
    def camino(className):
        return os.path.join(pathlib.Path(__file__).parent.absolute(), f"temp\{className}.txt")

    try:
        # Creo el archivo pickle para guardar los objetos
        picklefile = open(camino(className), 'wb')

        # Pickle el objeto en el archivo
        pickle.dump(lista, picklefile)

        # Cierro el archivo para guardar
        picklefile.close()
        
    except:
        print("Error de serializacion")

def serializarTodo():
    serializar(Empleado.getEmpleados(), "ampleados")
    serializar(Administrador.getAdministradores(), "administradores")
    serializar(Repartidor.getRepartidores(), "repartidores")
    serializar(Mesero.getMeseros(), "meseros")
    serializar(Chef.getChefs(), "chefs")
    serializar(Cliente.getClientes(), "clientes")
    serializar(Restaurante.getRestaurantes(), "restaurantes")
    serializar(Producto.getProductos(), "productos")
    serializar(Pedido.getPedidos(), "pedidos")