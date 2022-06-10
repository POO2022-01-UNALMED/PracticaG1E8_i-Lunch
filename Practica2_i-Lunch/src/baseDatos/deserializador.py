import pathlib
import pickle
import os

from src.gestorAplicacion.usuariosRestaurante.usuario import Usuario
from src.gestorAplicacion.usuariosRestaurante.empleado import Empleado
from src.gestorAplicacion.usuariosRestaurante.administrador import Administrador
from src.gestorAplicacion.usuariosRestaurante.repartidor import Repartidor
from src.gestorAplicacion.usuariosRestaurante.mesero import Mesero
from src.gestorAplicacion.usuariosRestaurante.chef import Chef
from src.gestorAplicacion.usuariosRestaurante.cliente import Cliente

from src.gestorAplicacion.gestionRestaurante.restaurante import Restaurante
from src.gestorAplicacion.gestionRestaurante.producto import Producto
from src.gestorAplicacion.gestionRestaurante.pedido import Pedido
from src.gestorAplicacion.gestionRestaurante.estadoPedido import EstadoPedido
from src.gestorAplicacion.gestionRestaurante.tipoPedido import TipoPedido

def deserializar():
    deserializarEmpleados()
    deserializarAdministradores()
    deserializarRepartidores()
    deserializarMeseros()
    deserializarChefs()
    deserializarClientes()
    deserializarRestaurantes()
    deserializarProductos()
    deserializarPedidos()

def deserializarEmpleados():
    ficheroEmpleados = open(os.path.join(pathlib.Path(__file__).parent.absolute(), "temp\\empleados"),"rb") 
    Empleado.setEmpleados(pickle.load(ficheroEmpleados))
    ficheroEmpleados.close()

def deserializarAdministradores():
    ficheroAdministradores = open(os.path.join(pathlib.Path(__file__).parent.absolute(), "temp\\administradores"),"rb") 
    Administrador.setAdministradores(pickle.load(ficheroAdministradores))
    ficheroAdministradores.close()

def deserializarRepartidores():
    ficheroRepartidores = open(os.path.join(pathlib.Path(__file__).parent.absolute(), "temp\\repartidores"),"rb") 
    Repartidor.setRepartidores(pickle.load(ficheroRepartidores))
    ficheroRepartidores.close()

def deserializarMeseros():
    ficheroMeseros = open(os.path.join(pathlib.Path(__file__).parent.absolute(), "temp\\meseros"),"rb") 
    Mesero.setMeseros(pickle.load(ficheroMeseros))
    ficheroMeseros.close()

def deserializarChefs():
    ficheroChefs = open(os.path.join(pathlib.Path(__file__).parent.absolute(), "temp\\chefs"),"rb") 
    Chef.setChefs(pickle.load(ficheroChefs))
    ficheroChefs.close()

def deserializarClientes():
    ficheroClientes = open(os.path.join(pathlib.Path(__file__).parent.absolute(), "temp\\clientes"),"rb") 
    Cliente.setClientes(pickle.load(ficheroClientes))
    ficheroClientes.close()

def deserializarRestaurantes():
    ficheroRestaurantes = open(os.path.join(pathlib.Path(__file__).parent.absolute(), "temp\\restaurantes"),"rb") 
    Restaurante.setRestaurantes(pickle.load(ficheroRestaurantes))
    ficheroRestaurantes.close()

def deserializarProductos():
    ficheroProductos = open(os.path.join(pathlib.Path(__file__).parent.absolute(), "temp\\productos"),"rb") 
    Producto.setProductos(pickle.load(ficheroProductos))
    ficheroProductos.close()

def deserializarPedidos():
    ficheroPedidos = open(os.path.join(pathlib.Path(__file__).parent.absolute(), "temp\\pedidos"),"rb") 
    Pedido.setPedidos(pickle.load(ficheroPedidos))
    ficheroPedidos.close()