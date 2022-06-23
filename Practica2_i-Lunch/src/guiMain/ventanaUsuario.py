import imp
from random import randint
import this
from tkinter import *
import tkinter

from baseDatos.serializador import serializarTodo
from gestorAplicacion.usuariosRestaurante.cliente import Cliente
from gestorAplicacion.usuariosRestaurante.administrador import Administrador
from gestorAplicacion.usuariosRestaurante.empleado import Empleado
from gestorAplicacion.gestionRestaurante.pedido import Pedido
from guiMain.fieldFrame import FieldFrame

class VentanaUsuario(Tk):
    framesAMatar=[]
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
        procesosYConsultas.add_command(label="Cola de pedidos", command=lambda: self.colaPedidos())
        procesosYConsultas.add_command(label="Gestionar pedidos en cola", command=lambda: self.gestionarPedidos())
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


    # Cambiar vista del frame

    def cambiarVista(frameUtilizado):
        for frame in VentanaUsuario.framesAMatar:
            frame.pack_forget()
        frameUtilizado.pack(fill=BOTH,expand=True)

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
    
    #Gestionar pedidos en cola
    def outPut(string, text):
        text.delete("1.0", "end")
        text.insert(INSERT, string)
        text.pack(fill=X, expand=True)

    def gestionarPedidos(self):

        def finalizar(): 
            index = FFGestionarPedido.getValue("Codigo del pedido")
            pedido = Pedido.getPedidos()[int(index)-1]                
            if Empleado.procesarPedido(pedido):
                return (f"{pedido.getCodigo()}\n"
                        f"Pedido aceptado")

        def aceptarPedido():           
            VentanaUsuario.outPut(finalizar(), outputGestionarPedido)

        gestionarPedido = Frame(self)
        nombreGestionarPedido = Label(gestionarPedido, text="Gestionar pedidos en espera", bd=10)
        dcrGestionarPedido = Label(gestionarPedido, text="Ingrese el ID del pedidos", bd=10)
        FFGestionarPedido = FieldFrame(gestionarPedido, None, ["Codigo del pedido"], None, None, [True])
        outputGestionarPedido = Text(gestionarPedido, height=6)
        VentanaUsuario.framesAMatar.append(outputGestionarPedido)
        FFGestionarPedido.crearBotones(aceptarPedido)
        gestionarPedido.pack()
        nombreGestionarPedido.pack()
        dcrGestionarPedido.pack()
        FFGestionarPedido.pack()
        VentanaUsuario.framesAMatar.append(gestionarPedido)

        
    
        
        





