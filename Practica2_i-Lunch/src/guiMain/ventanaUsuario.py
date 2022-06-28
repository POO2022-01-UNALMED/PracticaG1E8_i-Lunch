from random import randint
from tkinter import *
import tkinter
from random import choice, randint

from baseDatos.serializador import serializarTodo
from excepciones.errorAplicacion import ErrorAplicacion
from excepciones.excepcionExistente import ExcepcionExistente
from excepciones.excepcionLista import ExcepcionLista
from excepciones.excepcionNumerica import ExcepcionNumerica
from excepciones.excepcionVacio import ExcepcionVacio
from gestorAplicacion.gestionRestaurante.producto import Producto

from gestorAplicacion.gestionRestaurante.restaurante import Restaurante
from gestorAplicacion.gestionRestaurante.pedido import Pedido
from gestorAplicacion.datosAleatorios import nombresAleatorios,generarEmail, randDireccion

from gestorAplicacion.usuariosRestaurante.cliente import Cliente
from gestorAplicacion.usuariosRestaurante.administrador import Administrador
from gestorAplicacion.usuariosRestaurante.chef import Chef
from gestorAplicacion.usuariosRestaurante.empleado import Empleado

from guiMain.fieldFrame import FieldFrame
from guiMain.popUp import PopUp

class VentanaUsuario(Tk):
    framesEnPantalla = []

    def __init__(self, restaurante, administrador):
        super().__init__()

        # Configuracion de la ventana

        self.title('i-Lunch - Ventana de Usuario')
        self.option_add("*tearOff",  False)
        self.geometry("1400x720")
        self.resizable(False,False)

        # Creacion del menu

        self._barraMenu = Menu(self)
        archivo = Menu(self._barraMenu)
        archivo.add_command(label = "Aplicación", command = lambda: infoApp())
        archivo.add_command(label = "Salir y guardar", command = lambda: cerrarGuardar())
        self._barraMenu.add_cascade(label = "Archivo", menu = archivo)

        procesosYConsultas = Menu(self._barraMenu)

        infoRestaurante = Menu(self._barraMenu)
        infoRestaurante.add_command(label="Ver empleados", command=lambda: cambiarVista(frameVerEmpleados))
        infoRestaurante.add_command(label="Ver productos", command=lambda: cambiarVista(frameVerMenu))
        infoRestaurante.add_command(label="Ver historial de pedidos", command=lambda: cambiarVista(frameVerPedidos))
        infoRestaurante.add_command(label="Ver balance de cuenta", command=lambda: verBalanceDeCuenta())
        infoRestaurante.add_command(label="Ver estadísticas", command=lambda: verEstadisticas())
        procesosYConsultas.add_cascade(label="Información del restaurante", menu=infoRestaurante)

        gestionarMenu = Menu(self._barraMenu)
        gestionarMenu.add_command(label="Ver menú", command=lambda: cambiarVista(frameVerMenu))
        gestionarMenu.add_command(label="Crear producto", command=lambda: cambiarVista(frameCrearProducto))
        gestionarMenu.add_command(label="Eliminar producto", command=lambda: cambiarVista(frameEliminarProducto))
        gestionarMenu.add_command(label="Actualizar producto", command=lambda: cambiarVista(frameActualizarProducto))
        procesosYConsultas.add_cascade(label="Gestionar menú", menu=gestionarMenu)

        gestionarPersonal = Menu(self._barraMenu)
        gestionarPersonal.add_command(label="Ver personal", command=lambda: cambiarVista(frameVerPersonal))
        gestionarPersonal.add_command(label="Contratar empleado", command=lambda: cambiarVista(frameContratarEmpleado))
        gestionarPersonal.add_command(label="Despedir empleado", command=lambda: cambiarVista(frameDespedirEmpleado))
        procesosYConsultas.add_cascade(label="Gestionar personal", menu=gestionarPersonal)

        colaPedidos = Menu(self._barraMenu)
        colaPedidos.add_command(label="Ver cola de pedidos", command=lambda: cambiarVista(frameVerColaPedidos))
        colaPedidos.add_command(label="Gestionar pedidos en espera", command=lambda: cambiarVista(frameGestionarPedidos))
        procesosYConsultas.add_cascade(label="Cola de pedidos", menu=colaPedidos)

        procesosYConsultas.add_command(label="Pagar nómina", command=lambda: cambiarVista(framePagarNomina))

        procesosYConsultas.add_separator()

        procesosYConsultas.add_command(label="Simular pedido", command = lambda: simularPedido())

        gestionarClientela = Menu(self._barraMenu)
        gestionarClientela.add_command(label="Ver clientes", command=lambda: cambiarVista(frameVerClientes))
        gestionarClientela.add_command(label="Generar un cliente", command=lambda:generarCliente())
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

        # Verificar input vacio

        def verificarVacio(fieldFrame):
            for criterio in fieldFrame._criterios:
                if fieldFrame.getValue(criterio) == "":
                    raise ExcepcionVacio(criterio)

        # Verificar input numerico
        def verificarNumero(valor):
            if not valor.isnumeric():
                raise ExcepcionNumerica(valor)
        
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
            pedido = administrador.simularPedido(cliente)

            textoInfo = f"{pedido.__str__()}\n\n"
            
            simulado = Label(ventanaSimularPedido, text = textoInfo, justify = "left", font=("Verdana", 12))
            simulado.pack(fill=tkinter.Y, expand=True)

        # Procesos y consultas -> Ver cola de pedidos
        def refrescarColaPedidos():
            stringPedidos = ""
            for pedido in Pedido.getPedidos():
                if pedido.getEstado() == "Recibido":
                    stringPedidos += f"{pedido.__str__()}\n"

            if stringPedidos == "":
                stringPedidos += "No hay pedidos en cola"
            
            mostrarOutput(stringPedidos, outputVerColaPedidos)
        
        frameVerColaPedidos = Frame(self)
        nombreVerColaPedidos = Label(frameVerColaPedidos, text="Cola de pedidos", font=("Verdana", 16), fg = "#245efd")
        descVerColaPedidos = Label(frameVerColaPedidos, text="Recuerde que puede que inicialmente no se observe la totalidad de los pedidos. Puebe a mover rueda del mouse para ver más pedidos", font=("Verdana", 12))
        refrescarVerColaPedidos = Button(frameVerColaPedidos, text="Mostrar/Refescar", font = ("Verdana", 12), fg = "white", bg = "#245efd", command = refrescarColaPedidos)

        outputVerColaPedidos = Text(frameVerColaPedidos, height=100, font=("Verdana", 10))
        VentanaUsuario.framesEnPantalla.append(frameVerColaPedidos)
        
        nombreVerColaPedidos.pack()
        descVerColaPedidos.pack()
        refrescarVerColaPedidos.pack(pady=(10,10))

        VentanaUsuario.framesEnPantalla.append(frameVerColaPedidos)
        
        # Procesos y consultas -> Gestionar pedidos en cola
        def procesarPedido():
            try:
                verificarVacio(FFGestionarPedido)
                index = FFGestionarPedido.getValue("Código del pedido")
                verificarNumero(index)
                pedido = Pedido.getPedidos()[int(index)-1]
                if(pedido.getEstado()!="Recibido"):
                    return "Ingrese un codigo de pedido valido"         
                if administrador.procesarPedido(pedido):
                    administrador.actualizarEstadoPedido(pedido, True) # DE RECIBIDO A ACEPTADO
                    administrador.actualizarEstadoPedido(pedido, True) # DE ACEPTADO A EN PREPARACION
                    chef = Chef.getChefs()[randint(0, len(Chef.getChefs())-1)]
                    chef.prepararProducto(pedido)
                    for  chef_aux in Chef.getChefs():
                        if chef_aux.getCargoEnCocina()=="Chef en jefe":
                            chef = chef_aux       
                                
                    if chef.revisionPedido(pedido): # DE EN PREPARACION A LISTO 
                        administrador.actualizarEstadoPedido(pedido, True)
                        restaurante.setBalanceCuenta(restaurante.getBalanceCuenta() + pedido.getPrecioTotal())

                    return (f"Pedido {pedido.getCodigo()}\n"
                            f"Pedido aceptado. Iniciando preparacion\n"
                            f"Pedido preparado. Iniciando verificacion\n"
                            f"Pedido verificado por el chef en jefe. Iniciando envio\n"
                            f"Pedido despachado satisfactoriamente")
                else:
                    return "Ha habido un error, por favor intentelo nuevamente"
            except ErrorAplicacion as e:
                PopUp(str(e))

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
            try:
                verificarVacio(FFPagarNomina)
                index = FFPagarNomina.getValue("ID del empleado")

                if int(index) == -1:
                    resultadoPagoNomina = administrador.pagoNomina()
                    mostrarOutput(resultadoPagoNomina, outputPagarNomina)
                else:
                    verificarNumero(index)
                    resultadoPagoNomina = administrador.pagoNomina(int(index))
                    mostrarOutput(resultadoPagoNomina, outputPagarNomina)
            except ErrorAplicacion as e:
                PopUp(str(e))

        
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
        # Procesos y consultas -> Información del restaurante -> Ver productos
        def refrescarMenu():
            stringMenu = ""
            listaProductos = Producto.getProductos()
            for i in range(len(listaProductos)):
                stringMenu += f"ID: {i}\n" \
                              f"{listaProductos[i].__str__()}\n\n"
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
            try:
                verificarVacio(FFCrearProducto)
                nombre = FFCrearProducto.getValue("Nombre")
                descripcion = FFCrearProducto.getValue("Descripción")
                precio = FFCrearProducto.getValue("Precio")
                disponibilidad = FFCrearProducto.getValue("Disponibilidad")
                restriccion = FFCrearProducto.getValue("Restricción")
                cantidad = FFCrearProducto.getValue("Cantidad")

                verificarNumero(precio)
                verificarNumero(cantidad)

                if disponibilidad == "1":
                    disponibilidad = True
                else:
                    disponibilidad = False

                if restriccion == "1":
                    restriccion = True
                else:
                    restriccion = False
                
                resultadoCrearProducto = administrador.crearProducto(nombre, descripcion, int(precio), disponibilidad, restriccion, int(cantidad))
                mostrarOutput(resultadoCrearProducto, outputCrearProducto)
            except ErrorAplicacion as e:
                PopUp(str(e))

        
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
            try:
                verificarVacio(FFEliminarProducto)
                idProducto = FFEliminarProducto.getValue("ID Producto")
                verificarNumero(idProducto)
                resultadoEliminarProducto = administrador.eliminarProducto(int(idProducto))
                mostrarOutput(resultadoEliminarProducto, outputEliminarProducto)
            except ErrorAplicacion as e:
                PopUp(str(e))
        
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
        def buscarProductoBoton():
            try:
                verificarVacio(FFActualizarProductoBuscar)
                buscarProductoID()
            except ErrorAplicacion as e:
                PopUp(str(e))
        
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

                try:
                    verificarVacio(FFActualizarProducto)
                    verificarNumero(idProducto)
                    verificarNumero(FFActualizarProducto.getValue("Precio"))
                    verificarNumero(FFActualizarProducto.getValue("Cantidad"))

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
                except ErrorAplicacion as e:
                    PopUp(str(e))
            
            idProducto = FFActualizarProductoBuscar.getValue("ID Producto")
            verificarNumero(idProducto)

            if len(Producto.getProductos()) > int(idProducto) and int(idProducto) >= 0:
                producto = Producto.getProductos()[int(idProducto)]
                camposProducto = [producto.getNombre(), producto.getDescripcion(), producto.getPrecio(), producto.getDisponibilidad(), producto.getRestriccion(), producto.getCantidad()]
            else:
                raise ExcepcionLista([int(idProducto), len(Producto.getProductos())-1])

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
        FFActualizarProductoBuscar.crearBotones(buscarProductoBoton)

        outputActualizarProducto = Text(frameActualizarProducto, height=100, font=("Verdana", 10))
        VentanaUsuario.framesEnPantalla.append(outputActualizarProducto)

        nombreActualizarProducto.pack()
        descActualizarProducto.pack()
        FFActualizarProductoBuscar.pack()

        VentanaUsuario.framesEnPantalla.append(frameActualizarProducto)

        # Procesos y consultas -> Gestionar menú -> Ver personal
        def refrescarPersonal():
            stringPersonal = ""
            listaPersonal = Empleado.getEmpleados()
            for i in range(len(listaPersonal)):
                if not listaPersonal[i].getNombre() == "Nadie":
                    stringPersonal += f"ID: {i}\n" \
                                    f"{listaPersonal[i].informacion()}\n\n"

            if stringPersonal == "":
                stringPersonal += "No hay empleados contratados"

            mostrarOutput(stringPersonal, outputVerPersonal)

        frameVerPersonal = Frame(self)
        nombreVerPersonal = Label(frameVerPersonal, text="Personal del restaurante", font=("Verdana", 16), fg="#245efd")
        descVerPersonal = Label(frameVerPersonal,
                               text="Recuerde que puede que inicialmente no se observe la totalidad del personal. Pruebe a mover la rueda del mouse para ver más empleados",
                               font=("Verdana", 12))
        refrescarVerPersonal = Button(frameVerPersonal, text="Mostrar/Refescar", font=("Verdana", 12), fg="white",
                                     bg="#245efd", command=refrescarPersonal)

        outputVerPersonal = Text(frameVerPersonal, height=100, font=("Verdana", 10))
        VentanaUsuario.framesEnPantalla.append(frameVerPersonal)

        nombreVerPersonal.pack()
        descVerPersonal.pack()
        refrescarVerPersonal.pack(pady=(10, 10))

        VentanaUsuario.framesEnPantalla.append(frameVerPersonal)

        # Procesos y consultas -> Gestionar menú -> Contratar Empleado
        def botonContratarEmpleado():
            try:
                verificarVacio(FFContratarEmpleado)
                cedula = FFContratarEmpleado.getValue("Cédula")
                nombre = FFContratarEmpleado.getValue("Nombre")
                cargo = FFContratarEmpleado.getValue("Cargo")
                disponibilidad = FFContratarEmpleado.getValue("Disponibilidad")
                salario = FFContratarEmpleado.getValue("Salario")

                verificarNumero(cedula)
                verificarNumero(salario)

                if disponibilidad == "1":
                    disponibilidad = True
                else:
                    disponibilidad = False
                
                resultadoContratarEmpleado = administrador.contratarEmpleado(int(cedula), nombre, cargo, disponibilidad, int(salario), restaurante)
                mostrarOutput(resultadoContratarEmpleado, outputContratarEmpleado)
            except ErrorAplicacion as e:
                PopUp(str(e))
        
        frameContratarEmpleado = Frame(self)
        nombreContratarEmpleado = Label(frameContratarEmpleado, text="Contratar empleado", font=("Verdana", 16), fg = "#245efd")
        descContratarEmpleado = Label(frameContratarEmpleado, text="Por favor llene todos los campos. Recuerde que en el campo de \"Disponibilidad\" debe escribir \"0\" o \"1\" (Representando Falso y Verdadero respectivamente)", font=("Verdana", 12))
        FFContratarEmpleado = FieldFrame(frameContratarEmpleado, None, ["Cédula", "Nombre", "Cargo", "Disponibilidad", "Salario"], None, None, None)
        FFContratarEmpleado.crearBotones(botonContratarEmpleado)

        outputContratarEmpleado = Text(frameContratarEmpleado, height=100, font=("Verdana", 10))
        VentanaUsuario.framesEnPantalla.append(outputContratarEmpleado)

        nombreContratarEmpleado.pack()
        descContratarEmpleado.pack()
        FFContratarEmpleado.pack()

        VentanaUsuario.framesEnPantalla.append(frameContratarEmpleado)

        # Procesos y consultas -> Gestionar menú -> Despedir Empleado
        def botonDespedirEmpleado():
            try:
                verificarVacio(FFDespedirEmpleado)
                idEmpleado = FFDespedirEmpleado.getValue("ID Empleado")
                verificarNumero(idEmpleado)
                resultadoDespedirEmpleado = administrador.despedirEmpleado(int(idEmpleado))
                mostrarOutput(resultadoDespedirEmpleado, outputDespedirEmpleado)
            except ErrorAplicacion as e:
                PopUp(str(e))
        
        frameDespedirEmpleado = Frame(self)
        nombreDespedirEmpleado = Label(frameDespedirEmpleado, text="Despedir un empleado", font=("Verdana", 16), fg = "#245efd")
        descDespedirEmpleado = Label(frameDespedirEmpleado, text="Ingrese el ID del empleado a eliminar. Recuerde observar muy bien el ID en la pestaña \"Ver personal\".", font=("Verdana", 12))
        FFDespedirEmpleado = FieldFrame(frameDespedirEmpleado, None, ["ID Empleado"], None, None, None)
        FFDespedirEmpleado.crearBotones(botonDespedirEmpleado)

        outputDespedirEmpleado = Text(frameDespedirEmpleado, height=100, font=("Verdana", 10))
        VentanaUsuario.framesEnPantalla.append(outputDespedirEmpleado)

        nombreDespedirEmpleado.pack()
        descDespedirEmpleado.pack()
        FFDespedirEmpleado.pack()

        VentanaUsuario.framesEnPantalla.append(frameDespedirEmpleado)

        # Procesos y consultas -> Información del restaurante -> Ver empleados
        def refrescarEmpleados():
            stringEmpleados = ""
            listaPersonal = Empleado.getEmpleados()
            for i in range(len(listaPersonal)):
                if not listaPersonal[i].getNombre() == "Nadie":
                    stringEmpleados += f"ID: {i}\n" \
                                    f"{listaPersonal[i].informacion()}\n\n"

            if stringEmpleados == "":
                stringEmpleados += "No hay empleados contratados"

            mostrarOutput(stringEmpleados, outputVerEmpleados)

        frameVerEmpleados = Frame(self)
        nombreVerEmpleados = Label(frameVerEmpleados, text="Lista de empleados", font=("Verdana", 16), fg="#245efd")
        descVerEmpleados = Label(frameVerEmpleados,
                               text="Recuerde que puede que inicialmente no se observe la totalidad de los empleados. Puebe a mover rueda del mouse para ver más empleados",
                               font=("Verdana", 12))
        refrescarVerEmpleados = Button(frameVerEmpleados, text="Mostrar/Refescar", font=("Verdana", 12), fg="white",
                                     bg="#245efd", command=refrescarEmpleados)

        outputVerEmpleados = Text(frameVerEmpleados, height=100, font=("Verdana", 10))
        VentanaUsuario.framesEnPantalla.append(frameVerEmpleados)

        nombreVerEmpleados.pack()
        descVerEmpleados.pack()
        refrescarVerEmpleados.pack(pady=(10, 10))

        VentanaUsuario.framesEnPantalla.append(frameVerEmpleados)

        # Procesos y consultas -> Información del restaurante -> Ver historial de pedidos
        def refrescarHistorialPedidos():
            stringPedidos = ""
            listaPedidos = Pedido.getPedidos()
            for pedido in listaPedidos:
                stringPedidos += f"{pedido.__str__()}\n\n"

            if stringPedidos == "":
                stringPedidos += "No hay pedidos registrados"

            mostrarOutput(stringPedidos, outputVerPedidos)

        frameVerPedidos = Frame(self)
        nombreVerPedidos = Label(frameVerPedidos, text="Historial de pedidos", font=("Verdana", 16), fg="#245efd")
        descVerPedidos = Label(frameVerPedidos,
                               text="Recuerde que puede que inicialmente no se observe la totalidad de los pedidos. Puebe a mover rueda del mouse para ver más pedidos",
                               font=("Verdana", 12))
        refrescarVerPedidos = Button(frameVerPedidos, text="Mostrar/Refescar", font=("Verdana", 12), fg="white",
                                     bg="#245efd", command=refrescarHistorialPedidos)

        outputVerPedidos = Text(frameVerPedidos, height=100, font=("Verdana", 10))
        VentanaUsuario.framesEnPantalla.append(frameVerPedidos)

        nombreVerPedidos.pack()
        descVerPedidos.pack()
        refrescarVerPedidos.pack(pady=(10, 10))

        VentanaUsuario.framesEnPantalla.append(frameVerPedidos)

        # Procesos y consultas -> Gestionar clientela -> Ver clientes
        def refrescarClientes():
            stringClientes = ""
            listaClientes = Cliente.getClientes()
            for cliente in listaClientes:
                stringClientes += f"{cliente.informacion()}\n\n"

            if stringClientes == "Lista de clientes:\n\n":
                stringClientes += "No hay clientes registrados"

            mostrarOutput(stringClientes, outputVerClientes)

        frameVerClientes = Frame(self)
        nombreVerClientes = Label(frameVerClientes, text="Historial de pedidos", font=("Verdana", 16), fg="#245efd")
        descVerClientes = Label(frameVerClientes,
                               text="Recuerde que puede que inicialmente no se observe la totalidad de los clientes. Puebe a mover rueda del mouse para ver más clientes",
                               font=("Verdana", 12))
        refrescarVerClientes = Button(frameVerClientes, text="Mostrar/Refescar", font=("Verdana", 12), fg="white",
                                     bg="#245efd", command=refrescarClientes)

        outputVerClientes = Text(frameVerClientes, height=100, font=("Verdana", 10))
        VentanaUsuario.framesEnPantalla.append(frameVerClientes)

        nombreVerClientes.pack()
        descVerClientes.pack()
        refrescarVerClientes.pack(pady=(10, 10))

        VentanaUsuario.framesEnPantalla.append(frameVerClientes)

        # Procesos y consultas -> Gestionar clientela -> Generar un cliente
        def generarCliente():
            ventanaGenerarCliente = Tk()
            ventanaGenerarCliente.geometry("800x360")
            ventanaGenerarCliente.resizable(False, False)
            ventanaGenerarCliente.title("i-Lunch - Generar cliente nuevo")
            nombreCliente = choice(nombresAleatorios)

            cliente = Cliente(nombreCliente, generarEmail(nombreCliente),randint(1000000000, 9999999999), randDireccion(), randint(18, 65))
            textoInfo = f"Se ha generado el siguiente cliente:\n" \
                        f"{cliente.informacion()}"

            generado = Label(ventanaGenerarCliente, text=textoInfo, justify="left", font=("Verdana", 12))
            generado.pack(fill=tkinter.Y, expand=True)

        # Procesos y consultas -> Informacion del restaurante -> Ver estadisticas
        def verEstadisticas():
            ventanaverEstadisticas = Tk()
            ventanaverEstadisticas.geometry("800x360")
            ventanaverEstadisticas.resizable(False, False)
            ventanaverEstadisticas.title("i-Lunch - Ver Estadisticas")

            textoInfo = restaurante.estadisticasRestaurante()

            estadisticas = Label(ventanaverEstadisticas, text=textoInfo, justify="left", font=("Verdana", 12))
            estadisticas.pack(fill=tkinter.Y, expand=True)


        # Procesos y consultas -> Informacion del restaurante -> Ver balance de cuenta
        def verBalanceDeCuenta():
            ventanaVerBalanceDeCuenta = Tk()
            ventanaVerBalanceDeCuenta.geometry("640x360")
            ventanaVerBalanceDeCuenta.resizable(False, False)
            ventanaVerBalanceDeCuenta.title("i-Lunch - Ver balance de cuenta")
            textoInfo = f"El balance de cuenta actualmente es:\n" \
                        f"${restaurante.getBalanceCuenta()}"

            balance = Label(ventanaVerBalanceDeCuenta, text=textoInfo, justify="left", font=("Verdana", 12))
            balance.pack(fill=tkinter.Y, expand=True)