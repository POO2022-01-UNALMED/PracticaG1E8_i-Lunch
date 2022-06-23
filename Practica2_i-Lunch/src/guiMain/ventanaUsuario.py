from random import randint
from tkinter import *
import tkinter

from baseDatos.serializador import serializarTodo

from gestorAplicacion.gestionRestaurante.restaurante import Restaurante
from gestorAplicacion.usuariosRestaurante.cliente import Cliente
from gestorAplicacion.usuariosRestaurante.administrador import Administrador
from gestorAplicacion.usuariosRestaurante.empleado import Empleado
from gestorAplicacion.gestionRestaurante.pedido import Pedido

from guiMain.fieldFrame import FieldFrame

class VentanaUsuario(Tk):
    framesEnPantalla = []

    def __init__(self):
        super().__init__()

        # Referencias al admin y restaurante que serán útiles más adelante

        restaurante = Restaurante.getRestaurantes()[0]
        administrador = Administrador.getAdministradores()[0]

        # Configuracion de la ventana

        self.title('i-Lunch - Ventana de Usuario')
        self.option_add("*tearOff",  False)
        self.geometry("1280x720")
        self.resizable(False,False)

        # Creacion del menu

        self._barraMenu = Menu(self)
        archivo = Menu(self._barraMenu)
        archivo.add_command(label = "Aplicación", command = lambda: infoApp())
        archivo.add_command(label = "Salir y guardar", command = lambda: cerrarGuardar())
        self._barraMenu.add_cascade(label = "Archivo", menu = archivo)

        procesosYConsultas = Menu(self._barraMenu)
        procesosYConsultas.add_command(label="Información del restaurante", command=lambda:print("IDK"))
        procesosYConsultas.add_command(label="Gestionar menú", command=lambda: print("IDK"))
        procesosYConsultas.add_command(label="Gestionar personal", command=lambda: print("IDK"))
        procesosYConsultas.add_command(label="Cola de pedidos", command=lambda: print("IDK"))
        procesosYConsultas.add_command(label="Gestionar pedidos en cola", command=lambda: cambiarVista(frameGestionarPedidos))
        procesosYConsultas.add_command(label="Pagar nómina", command=lambda: cambiarVista(framePagarNomina))
        procesosYConsultas.add_separator()
        procesosYConsultas.add_command(label="Simular pedido", command = lambda: simularPedido())
        procesosYConsultas.add_command(label="Gestionar clientela", command=lambda: print("IDK"))
        self._barraMenu.add_cascade(label="Procesos y consultas", menu= procesosYConsultas)

        ayuda = Menu(self._barraMenu)
        ayuda.add_command(label="Acerca de", command = lambda: infoDevs())
        self._barraMenu.add_cascade(label="Ayuda", menu = ayuda)

        self.config(menu = self._barraMenu)

        # Funciones útiles en la manipulación de Frames
        
        # Cambiar vista del frame
        def cambiarVista(frameUtilizado):
            for frame in VentanaUsuario.framesEnPantalla:
                frame.pack_forget()
            frameUtilizado.pack(fill=BOTH,expand=True, pady = (10,10))

        # Mostrar un output
        def mostrarOutput(string, text):
            text.delete("1.0", "end")
            text.insert(INSERT, string)
            text.pack(fill=X, expand=True, padx=(10,10))
        
        # Funcionalidades
        
        # Archivo -> Aplicación
        def infoApp():
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
        def cerrarGuardar():
            from guiMain.ventanaInicio import VentanaInicio
            serializarTodo()
            self.destroy()
            ventanaInicio = VentanaInicio()
        
        # Ayuda -> Acerca de
        def infoDevs():
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

        # Procesos y consultas -> Simular pedido
        def simularPedido():
            ventanaSimularPedido = Tk()
            ventanaSimularPedido.geometry("640x360")
            ventanaSimularPedido.resizable(False,False)
            ventanaSimularPedido.title("i-Lunch - Simular pedido")

            cliente =  Cliente.getClientes()[(randint(0, len(Cliente.getClientes()) - 1))]
            pedido = Administrador.getAdministradores()[0].simularPedido(cliente)     

            textoInfo = f"Pedido Recibio\n" \
                        f"Información del pedido:\n" \
                        f"• Cliente: " \
                        f"{cliente.getNombre()}\n"\
                        f"• Codigo pedido: " \
                        f"{pedido.getCodigo()}"
            
            simulado = Label(ventanaSimularPedido, text = textoInfo, justify = "left", font=("Verdana", 12))
            simulado.pack(fill=tkinter.Y, expand=True)
        
        # Procesos y consultas -> Gestionar pedidos en cola
        def finalizarPedido(): 
            index = FFGestionarPedido.getValue("Código del pedido")
            pedido = Pedido.getPedidos()[int(index)-1]                
            if Empleado.procesarPedido(pedido):
                return (f"{pedido.getCodigo()}\n"
                        f"Pedido aceptado")

        def aceptarPedido():           
            mostrarOutput(finalizarPedido(), outputGestionarPedido)

        frameGestionarPedidos = Frame(self)
        nombreGestionarPedido = Label(frameGestionarPedidos, text="Gestionar pedidos en espera", font=("Verdana", 16))
        descGestionarPedido = Label(frameGestionarPedidos, text="Ingrese el ID del pedido", font=("Verdana", 12))
        FFGestionarPedido = FieldFrame(frameGestionarPedidos, None, ["Código del pedido"], None, None, [True])
        FFGestionarPedido.crearBotones(aceptarPedido)

        outputGestionarPedido = Text(frameGestionarPedidos, height=6, font=("Verdana", 10))
        VentanaUsuario.framesEnPantalla.append(outputGestionarPedido)

        nombreGestionarPedido.pack()
        descGestionarPedido.pack()
        FFGestionarPedido.pack()

        VentanaUsuario.framesEnPantalla.append(frameGestionarPedidos)

        # Procesos y consultas -> Pagar nómina
        def efectuarPagoNomina():
            index = FFPagarNomina.getValue("ID del empleado")

            if int(index) == -1:
                resultadoPagoNomina = administrador.pagoNomina()
                mostrarOutput(resultadoPagoNomina, outputPagarNomina)
            else:
                resultadoPagoNomina = administrador.pagoNomina(int(index))
                mostrarOutput(resultadoPagoNomina, outputPagarNomina)
        
        framePagarNomina = Frame(self)
        nombrePagarNomina = Label(framePagarNomina, text="Pagar la nómina de los empleados", font=("Verdana", 16))
        descPagarNomina = Label(framePagarNomina, text="Ingrese el ID del empleado o ingrese el valor -1 para pagar a todos los empleados", font=("Verdana", 12))
        FFPagarNomina = FieldFrame(framePagarNomina, None, ["ID del empleado"], None, None, None)
        FFPagarNomina.crearBotones(efectuarPagoNomina)

        outputPagarNomina = Text(framePagarNomina, height=6, font=("Verdana", 10))
        VentanaUsuario.framesEnPantalla.append(outputPagarNomina)

        nombrePagarNomina.pack()
        descPagarNomina.pack()
        FFPagarNomina.pack()

        VentanaUsuario.framesEnPantalla.append(framePagarNomina)