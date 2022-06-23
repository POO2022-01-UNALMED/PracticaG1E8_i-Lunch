from random import randint
from tkinter import *
import tkinter

from baseDatos.serializador import serializarTodo
from gestorAplicacion.usuariosRestaurante.cliente import Cliente
from gestorAplicacion.usuariosRestaurante.administrador import Administrador

class VentanaUsuario(Tk):
    def __init__(self):
        super().__init__()

        # Configuracion de la ventana

        self.title('i-Lunch - Ventana de Usuario')
        self.option_add("*tearOff",  False)
        self.geometry("1280x720")
        self.resizable(False,False)

        # Creacion del menu

        self._barraMenu = Menu(self)
        archivo = Menu(self._barraMenu)
        archivo.add_command(label = "Aplicación", command = lambda: self.infoApp())
        archivo.add_command(label = "Salir y guardar", command = lambda: self.cerrarGuardar())
        self._barraMenu.add_cascade(label = "Archivo", menu = archivo)

        procesosYConsultas = Menu(self._barraMenu)
        procesosYConsultas.add_command(label="Información del restaurante", command=lambda:print("IDK"))
        procesosYConsultas.add_command(label="Gestionar menú", command=lambda: print("IDK"))
        procesosYConsultas.add_command(label="Gestionar personal", command=lambda: print("IDK"))
        procesosYConsultas.add_command(label="Cola de pedidos", command=lambda: print("IDK"))
        procesosYConsultas.add_separator()
        procesosYConsultas.add_command(label="Simular pedido", command = lambda: self.simularPedido())
        procesosYConsultas.add_command(label="Gestionar clientela", command=lambda: print("IDK"))
        self._barraMenu.add_cascade(label="Procesos y consultas", menu= procesosYConsultas)

        ayuda = Menu(self._barraMenu)
        ayuda.add_command(label="Acerca de", command = lambda: self.infoDevs())
        self._barraMenu.add_cascade(label="Ayuda", menu = ayuda)

        self.config(menu = self._barraMenu)

        # ! Continuar

    # Archivo -> Aplicación

    def infoApp(self):
        ventanaInfo = Tk()
        ventanaInfo.geometry("640x360")
        ventanaInfo.resizable(False,False)
        ventanaInfo.title("i-Lunch - Aplicación")

        textoInfo = f"i-Lunch es una aplicación de gestión de restaurantes.\n" \
                    f"El administrador del restaurante que contrate la aplicación\n" \
                    f"tendrá acceso a un software en el cual podrá llevar el control\n"\
                    f"de todos los aspectos de su restaurante como:\n" \
                    f"• La información básica del restaurante.\n" \
                    f"• Su oferta de productos.\n" \
                    f"• Sus empleados.\n" \
                    f"• Los pedidos realizados al restaurante.\n" \
                    f"• El balance de cuenta y la nómina de los empleados.\n" \
                    f"• Su clientela."
        info = Label(ventanaInfo, text = textoInfo, justify = "left", font=("Verdana", 12))
        info.pack(fill=tkinter.Y, expand=True)

    # Archivo -> Salir y guardar

    def cerrarGuardar(self):
        from guiMain.ventanaInicio import VentanaInicio
        serializarTodo()
        self.destroy()
        ventanaInicio = VentanaInicio()
    
    # Ayuda -> Acerca de

    def infoDevs(self):
        ventanaDevs = Tk()
        ventanaDevs.geometry("640x360")
        ventanaDevs.resizable(False,False)
        ventanaDevs.title("i-Lunch - Acerca de")

        textoInfo = f"Desarrolladores:\n" \
                    f"• Emmanuel López Rodríguez\n" \
                    f"• Jerónimo Gómez Restrepo\n" \
                    f"• Andrés Felipe Aparicio Mestre\n" \
                    f"• David Alejandro López Zapata"
        devs = Label(ventanaDevs, text = textoInfo, justify = "left", font=("Verdana", 12))
        devs.pack(fill=tkinter.Y, expand=True)

        # FUNCIONALIDADES

        #Simular pedido
    def simularPedido(self):
        cliente =  Cliente.getClientes()[(randint(0, len(Cliente.getClientes()) - 1))]
        pedido = Administrador.getAdministradores()[0].simularPedido(cliente)     
        ventanaDevs = Tk()
        ventanaDevs.geometry("640x360")
        ventanaDevs.resizable(False,False)
        ventanaDevs.title("i-Lunch - Simular pedido")

        textoInfo = f"Pedido Recibio\n" \
                    f"Información del pedido:\n" \
                    f"• Cliente: " \
                    f"{cliente.getNombre()}\n"\
                    f"• Codigo pedido: " \
                    f"{pedido.getCodigo()}"
        devs = Label(ventanaDevs, text = textoInfo, justify = "left", font=("Verdana", 12))
        devs.pack(fill=tkinter.Y, expand=True)
		

