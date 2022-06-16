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

def deserializar(lista, className):
        def camino(className):
            return os.path.join(pathlib.Path(__file__).parent.absolute(), f"temp\{className}.txt")

        # Leo el archivo
        try:
            picklefile = open(camino(className), 'rb')

        except:
            picklefile = open(camino(className), 'x')
            picklefile = open(camino(className), 'rb')

        # Unpickle los datos
        if os.path.getsize(camino(className)) > 0:
            lista = pickle.load(picklefile)
        
        # Cierro el archivo
        picklefile.close()

        return lista
    
def deserializarTodo():
    Empleado._empleados = deserializar(Empleado._empleados, "empleados")
    Administrador._administradores =  deserializar(Administrador._administradores, "administradores")
    Repartidor._repartidores = deserializar(Repartidor._repartidores, "repartidores")
    Mesero._meseros = deserializar(Mesero._meseros, "meseros")
    Chef._chefs = deserializar(Chef._chefs, "chefs")
    Cliente._clientes = deserializar(Cliente._clientes, "clientes")
    Restaurante._restaurantes = deserializar(Restaurante._restaurantes, "restaurantes")
    Producto._productos = deserializar(Producto._productos, "productos")
    Pedido._pedidos = deserializar(Pedido._pedidos, "pedidos")