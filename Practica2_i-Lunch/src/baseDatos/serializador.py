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

def serializar():
    serializarEmpleados()
    serializarAdministradores()
    serializarRepartidores()
    serializarMeseros()
    serializarChefs()
    serializarClientes()
    serializarRestaurantes()
    serializarProductos()
    serializarPedidos()

def serializarEmpleados():
    ficheroEmpleados = open(os.path.join(pathlib.Path(__file__).parent.absolute(), "temp\\empleados.txt"),"wb") 
    pickle.dump(Empleado.getEmpleados(), ficheroEmpleados)
    ficheroEmpleados.close()

def serializarAdministradores():
    ficheroAdministradores = open(os.path.join(pathlib.Path(__file__).parent.absolute(), "temp\\administradores.txt"),"wb") 
    pickle.dump(Administrador.getAdministradores(), ficheroAdministradores)
    ficheroAdministradores.close()

def serializarRepartidores():
    ficheroRepartidores = open(os.path.join(pathlib.Path(__file__).parent.absolute(), "temp\\repartidores.txt"),"wb") 
    pickle.dump(Repartidor.getRepartidores(), ficheroRepartidores)
    ficheroRepartidores.close()

def serializarMeseros():
    ficheroMeseros = open(os.path.join(pathlib.Path(__file__).parent.absolute(), "temp\\meseros.txt"),"wb") 
    pickle.dump(Mesero.getMeseros(), ficheroMeseros)
    ficheroMeseros.close()

def serializarChefs():
    ficheroChefs = open(os.path.join(pathlib.Path(__file__).parent.absolute(), "temp\\chefs.txt"),"wb") 
    pickle.dump(Chef.getChefs(), ficheroChefs)
    ficheroChefs.close()

def serializarClientes():
    ficheroClientes = open(os.path.join(pathlib.Path(__file__).parent.absolute(), "temp\\clientes.txt"),"wb") 
    pickle.dump(Cliente.getClientes(), ficheroClientes)
    ficheroClientes.close()

def serializarRestaurantes():
    ficheroRestaurantes = open(os.path.join(pathlib.Path(__file__).parent.absolute(), "temp\\restaurantes.txt"),"wb") 
    pickle.dump(Restaurante.getRestaurantes(), ficheroRestaurantes)
    ficheroRestaurantes.close()

def serializarProductos():
    ficheroProductos = open(os.path.join(pathlib.Path(__file__).parent.absolute(), "temp\\productos.txt"),"wb") 
    pickle.dump(Producto.getProductos(), ficheroProductos)
    ficheroProductos.close()

def serializarPedidos():
    ficheroPedidos = open(os.path.join(pathlib.Path(__file__).parent.absolute(), "temp\\pedidos.txt"),"wb") 
    pickle.dump(Pedido.getPedidos(), ficheroPedidos)
    ficheroPedidos.close()