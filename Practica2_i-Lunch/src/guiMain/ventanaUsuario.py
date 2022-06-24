from random import randint
from tkinter import *
import tkinter

from baseDatos.serializador import serializarTodo

from gestorAplicacion.gestionRestaurante.restaurante import Restaurante
from gestorAplicacion.usuariosRestaurante.cliente import Cliente
from gestorAplicacion.usuariosRestaurante.administrador import Administrador
from gestorAplicacion.usuariosRestaurante.empleado import Empleado
from gestorAplicacion.gestionRestaurante.pedido import Pedido
from gestorAplicacion.usuariosRestaurante.chef import Chef

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

        infoRestaurante = Menu(self._barraMenu)
        infoRestaurante.add_command(label="Ver empleados", command=lambda: print("IDK"))
        infoRestaurante.add_command(label="Ver productos", command=lambda: print("IDK"))
        infoRestaurante.add_command(label="Ver historial de pedidos", command=lambda: print("IDK"))
        infoRestaurante.add_command(label="Ver balance de cuenta", command=lambda: print("IDK"))
        infoRestaurante.add_command(label="Ver estadísticas", command=lambda: print("IDK"))
        procesosYConsultas.add_cascade(label="Información del restaurante", menu=infoRestaurante)

        gestionarMenu = Menu(self._barraMenu)
        gestionarMenu.add_command(label="Ver menú", command=lambda: cambiarVista(frameVerMenu))
        gestionarMenu.add_command(label="Crear producto", command=lambda: cambiarVista(frameCrearProducto))
        gestionarMenu.add_command(label="Eliminar producto", command=lambda: cambiarVista(frameEliminarProducto))
        gestionarMenu.add_command(label="Actualizar producto", command=lambda: cambiarVista(frameActualizarProducto))
        procesosYConsultas.add_cascade(label="Gestionar menú", menu=gestionarMenu)

        gestionarPersonal = Menu(self._barraMenu)
        gestionarPersonal.add_command(label="Ver personal", command=lambda: print("IDK"))
        gestionarPersonal.add_command(label="Contratar empleado", command=lambda: print("IDK"))
        gestionarPersonal.add_command(label="Despedir empleado", command=lambda: print("IDK"))
        procesosYConsultas.add_cascade(label="Gestionar personal", menu=gestionarPersonal)

        colaPedidos = Menu(self._barraMenu)
        colaPedidos.add_command(label="Ver cola de pedidos", command=lambda: cambiarVista(frameVerPedidos))
        colaPedidos.add_command(label="Gestionar pedidos en espera", command=lambda: cambiarVista(frameGestionarPedidos))
        procesosYConsultas.add_cascade(label="Cola de pedidos", menu=colaPedidos)

        procesosYConsultas.add_command(label="Pagar nómina", command=lambda: cambiarVista(framePagarNomina))

        procesosYConsultas.add_separator()

        procesosYConsultas.add_command(label="Simular pedido", command = lambda: simularPedido())

        gestionarClientela = Menu(self._barraMenu)
        gestionarClientela.add_command(label="Ver clientes", command=lambda: print("IDK"))
        gestionarClientela.add_command(label="Generar un cliente", command=lambda: print("IDK"))
        procesosYConsultas.add_cascade(label="Gestionar clientela", menu=gestionarClientela)

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

        # Procesos y consultas -> Ver cola de pedidos

        def refrescarCola():
            stringPedidos = "Pedidos en espera:\n"
            for pedido in Pedido.getPedidos():
                    stringPedidos += f"Código: {pedido.getCodigo()} - Cliente: {pedido.getCliente().getNombre()} - Estado: {pedido.getEstado()}\n"
            if stringPedidos == "Pedidos en espera:\n":
                stringPedidos += "No hay pedidos en cola"
            
            mostrarOutput(stringPedidos, outputVerPedidos)
        
        frameVerPedidos = Frame(self)
        nombreVerPedidos = Label(frameVerPedidos, text="Cola de pedidos", font=("Verdana", 16), fg = "#245efd")
        descVerPedidos = Label(frameVerPedidos, text="Recuerde que puede que inicialmente no se observe la totalidad de los pedidos. Puebe a mover rueda del mouse para ver más pedidos", font=("Verdana", 12))
        refrescarVerPedidos = Button(frameVerPedidos, text="Mostrar/Refescar", font = ("Verdana", 12), fg = "white", bg = "#245efd", command = refrescarCola)

        outputVerPedidos = Text(frameVerPedidos, height=100, font=("Verdana", 10))
        VentanaUsuario.framesEnPantalla.append(frameVerPedidos)
        
        nombreVerPedidos.pack()
        descVerPedidos.pack()
        refrescarVerPedidos.pack(pady=(10,10))

        VentanaUsuario.framesEnPantalla.append(frameVerPedidos)
        
        # Procesos y consultas -> Gestionar pedidos en cola
        def procesarPedido(): 
            index = FFGestionarPedido.getValue("Código del pedido")
            pedido = Pedido.getPedidos()[int(index)-1]
            if(pedido.getEstado()!="Recibido"):
                return "Ingrese un codigo de pedido valido"         
            if administrador.procesarPedido(pedido):
                administrador.actualizarEstadoPedido(pedido, True) #DE RECIBIDO A ACEPTADO
                administrador.actualizarEstadoPedido(pedido, True) #DE ACEPTADO A EN PREPARACION
                chef = Chef.getChefs()[randint(0, len(Chef.getChefs())-1)]
                chef.prepararProducto(pedido)
                for  chef_aux in Chef.getChefs():
                    if chef_aux.getCargoEnCocina()=="Chef en jefe":
                        chef = chef_aux
								
							
                if chef.revisionPedido(pedido): # DE EN PREPARACION A LISTO 
                    administrador.actualizarEstadoPedido(pedido, True)
                    restaurante.setBalanceCuenta(restaurante.getBalanceCuenta() + pedido.getPrecioTotal())

                return (f"{pedido.getCodigo()}\n"
                        f"Pedido aceptado. Iniciando preparacion\n"
                        f"Pedido preparado. Iniciando verificacion\n"
                        f"Pedido verificado por el chef en jefe. Iniciando envio\n"
                        f"Pedido despachado satisfactoriamente")
            else:
                return "Ha habido un error, por favor intentelo nuevamente"

        def aceptarPedido():           
            mostrarOutput(procesarPedido(), outputGestionarPedido)

        frameGestionarPedidos = Frame(self)
        nombreGestionarPedido = Label(frameGestionarPedidos, text="Gestionar pedidos en espera", font=("Verdana", 16), fg = "#245efd")
        descGestionarPedido = Label(frameGestionarPedidos, text="Ingrese el ID del pedido", font=("Verdana", 12))
        FFGestionarPedido = FieldFrame(frameGestionarPedidos, None, ["Código del pedido"], None, None, [True])
        FFGestionarPedido.crearBotones(aceptarPedido)

        outputGestionarPedido = Text(frameGestionarPedidos, height=100, font=("Verdana", 10))
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
        nombrePagarNomina = Label(framePagarNomina, text="Pagar la nómina de los empleados", font=("Verdana", 16), fg = "#245efd")
        descPagarNomina = Label(framePagarNomina, text="Ingrese el ID del empleado o ingrese el valor -1 para pagar a todos los empleados", font=("Verdana", 12))
        FFPagarNomina = FieldFrame(framePagarNomina, None, ["ID del empleado"], None, None, None)
        FFPagarNomina.crearBotones(efectuarPagoNomina)

        outputPagarNomina = Text(framePagarNomina, height=100, font=("Verdana", 10))
        VentanaUsuario.framesEnPantalla.append(outputPagarNomina)

        nombrePagarNomina.pack()
        descPagarNomina.pack()
        FFPagarNomina.pack()

        VentanaUsuario.framesEnPantalla.append(framePagarNomina)

        # Procesos y consultas -> Gestionar menú -> Ver menú
        def refrescarMenu():
            stringMenu = ""
            for i in range(len(restaurante.getMenu())):
                stringMenu += f"ID: {i}\n" \
                            f"{restaurante.getMenu()[i].__str__()}\n\n"
            if stringMenu == "":
                stringMenu += "No hay productos creados"
            
            mostrarOutput(stringMenu, outputVerMenu)
        
        frameVerMenu = Frame(self)
        nombreVerMenu = Label(frameVerMenu, text="Menú del restaurante", font=("Verdana", 16), fg = "#245efd")
        descVerMenu = Label(frameVerMenu, text="Recuerde que puede que inicialmente no se observe la totalidad del menú. Puebe a mover rueda del mouse para ver más productos", font=("Verdana", 12))
        refrescarVerMenu = Button(frameVerMenu, text="Mostrar/Refescar", font = ("Verdana", 12), fg = "white", bg = "#245efd", command = refrescarMenu)

        outputVerMenu = Text(frameVerMenu, height=100, font=("Verdana", 10))
        VentanaUsuario.framesEnPantalla.append(frameVerMenu)
        
        nombreVerMenu.pack()
        descVerMenu.pack()
        refrescarVerMenu.pack(pady=(10,10))

        VentanaUsuario.framesEnPantalla.append(frameVerMenu)

        # Procesos y consultas -> Gestionar menú -> Crear producto
        def botonCrearProducto():
            nombre = FFCrearProducto.getValue("Nombre")
            descripcion = FFCrearProducto.getValue("Descripción")
            precio = FFCrearProducto.getValue("Precio")
            disponibilidad = FFCrearProducto.getValue("Disponibilidad")
            restriccion = FFCrearProducto.getValue("Restricción")
            cantidad = FFCrearProducto.getValue("Cantidad")

            if disponibilidad == "1":
                disponibilidad = True
            else:
                disponibilidad = False

            if restriccion == "1":
                restriccion = True
            else:
                restriccion = False
            
            resultadoCrearProducto = administrador.crearProducto(nombre, descripcion, precio, disponibilidad, restriccion, cantidad)
            mostrarOutput(resultadoCrearProducto, outputCrearProducto)
        
        frameCrearProducto = Frame(self)
        nombreCrearProducto = Label(frameCrearProducto, text="Crear un producto", font=("Verdana", 16), fg = "#245efd")
        descCrearProducto = Label(frameCrearProducto, text="Por favor llene todos los campos. Recuerde que en los campos de \"Disponibilidad\" y \n\"Restricción de edad\" debe escribir \"0\" o \"1\" (Representando Falso y Verdadero respectivamente)", font=("Verdana", 12))
        FFCrearProducto = FieldFrame(frameCrearProducto, None, ["Nombre", "Descripción", "Precio", "Disponibilidad", "Restricción", "Cantidad"], None, None, None)
        FFCrearProducto.crearBotones(botonCrearProducto)

        outputCrearProducto = Text(frameCrearProducto, height=100, font=("Verdana", 10))
        VentanaUsuario.framesEnPantalla.append(outputCrearProducto)

        nombreCrearProducto.pack()
        descCrearProducto.pack()
        FFCrearProducto.pack()

        VentanaUsuario.framesEnPantalla.append(frameCrearProducto)

        # Procesos y consultas -> Gestionar menú -> Eliminar producto
        def botonEliminarProducto():
            idProducto = FFEliminarProducto.getValue("ID Producto")
            resultadoEliminarProducto = administrador.eliminarProducto(int(idProducto))
            mostrarOutput(resultadoEliminarProducto, outputEliminarProducto)
        
        frameEliminarProducto = Frame(self)
        nombreEliminarProducto = Label(frameEliminarProducto, text="Eliminar un producto", font=("Verdana", 16), fg = "#245efd")
        descEliminarProducto = Label(frameEliminarProducto, text="Ingrese el ID del producto a eliminar. Recuerde observar muy bien el ID en la pestaña \"Ver menú\", ya que este ID puede variar", font=("Verdana", 12))
        FFEliminarProducto = FieldFrame(frameEliminarProducto, None, ["ID Producto"], None, None, None)
        FFEliminarProducto.crearBotones(botonEliminarProducto)

        outputEliminarProducto = Text(frameEliminarProducto, height=100, font=("Verdana", 10))
        VentanaUsuario.framesEnPantalla.append(outputEliminarProducto)

        nombreEliminarProducto.pack()
        descEliminarProducto.pack()
        FFEliminarProducto.pack()

        VentanaUsuario.framesEnPantalla.append(frameEliminarProducto)

        # Procesos y consultas -> Gestionar menú -> Actualizar producto
        def buscarProductoID():
            # Volver a la búsqueda
            def volverBuscarProductoID():
                FFActualizarProductoBuscar.pack()
                descActualizarProducto2.pack_forget()
                FFActualizarProducto.pack_forget()
                botonActualizarProductoVolver.pack_forget()
                outputActualizarProducto.pack_forget()

            def botonActualizarProducto():
                idProducto = FFActualizarProductoBuscar.getValue("ID Producto")

                stringResultadosActualizarProducto = ""

                disponibilidad = FFActualizarProducto.getValue("Disponibilidad")
                restriccion = FFActualizarProducto.getValue("Restricción")

                if disponibilidad == "1":
                    disponibilidad = True
                else:
                    disponibilidad = False

                if restriccion == "1":
                    restriccion = True
                else:
                    restriccion = False

                stringResultadosActualizarProducto += "Nombre del " + administrador.actualizarNombreProducto(int(idProducto), FFActualizarProducto.getValue("Nombre")) + "\n"
                stringResultadosActualizarProducto += "Descripción del " + administrador.actualizarDescripcionProducto(int(idProducto), FFActualizarProducto.getValue("Descripción")) + "\n"
                stringResultadosActualizarProducto += "Precio del " + administrador.actualizarPrecioProducto(int(idProducto), FFActualizarProducto.getValue("Precio")) + "\n"
                stringResultadosActualizarProducto += "Disponibilidad del " + administrador.actualizarDisponibilidadProducto(int(idProducto), disponibilidad) + "\n"
                stringResultadosActualizarProducto += "Restricción de edad del " + administrador.actualizarRestriccionProducto(int(idProducto), restriccion) + "\n"
                stringResultadosActualizarProducto += "Cantidad disponible del " + administrador.actualizarCantidadProducto(int(idProducto), FFActualizarProducto.getValue("Cantidad"))

                mostrarOutput(stringResultadosActualizarProducto, outputActualizarProducto)
            
            idProducto = FFActualizarProductoBuscar.getValue("ID Producto")
            producto = restaurante.getMenu()[int(idProducto)]
            camposProducto = [producto.getNombre(), producto.getDescripcion(), producto.getPrecio(), producto.getDisponibilidad(), producto.getRestriccion(), producto.getCantidad()]

            descActualizarProducto2 = Label(frameActualizarProducto, text="Por favor llene todos los campos. Recuerde que en los campos de \"Disponibilidad\" y\n\"Restricción de edad\" debe escribir \"0\" o \"1\" (Representando Falso y Verdadero respectivamente)", font=("Verdana", 12))
            FFActualizarProducto = FieldFrame(frameActualizarProducto, None, ["Nombre", "Descripción", "Precio", "Disponibilidad", "Restricción", "Cantidad"], None, camposProducto, None)
            FFActualizarProducto.crearBotones(botonActualizarProducto)
            botonActualizarProductoVolver = Button(frameActualizarProducto, text="Volver a buscar ID", font = ("Verdana", 12), fg = "white", bg = "#245efd", command = volverBuscarProductoID)

            # Mostrar campos para actualizar y quitar formulario de busquedas
            descActualizarProducto2.pack()
            FFActualizarProducto.pack()
            FFActualizarProductoBuscar.pack_forget()
            botonActualizarProductoVolver.pack()
        
        frameActualizarProducto = Frame(self)
        nombreActualizarProducto = Label(frameActualizarProducto, text="Actualizar un producto", font=("Verdana", 16), fg = "#245efd")
        descActualizarProducto = Label(frameActualizarProducto, text="Ingrese el ID del producto a actualizar. Recuerde observar muy bien el ID en la pestaña \"Ver menú\", ya que este ID puede variar", font=("Verdana", 12))

        FFActualizarProductoBuscar = FieldFrame(frameActualizarProducto, None, ["ID Producto"], None, None, None)
        FFActualizarProductoBuscar.crearBotones(buscarProductoID)

        outputActualizarProducto = Text(frameActualizarProducto, height=100, font=("Verdana", 10))
        VentanaUsuario.framesEnPantalla.append(outputActualizarProducto)

        nombreActualizarProducto.pack()
        descActualizarProducto.pack()
        FFActualizarProductoBuscar.pack()

        VentanaUsuario.framesEnPantalla.append(frameActualizarProducto)