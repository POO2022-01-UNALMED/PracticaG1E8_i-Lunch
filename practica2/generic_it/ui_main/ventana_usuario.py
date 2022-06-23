from gestor_aplicacion.personal.empleado import Empleado
from gestor_aplicacion.tienda.cliente import Cliente
from gestor_aplicacion.personal.tecnico import Tecnico
from gestor_aplicacion.personal.dependiente import Dependiente
from gestor_aplicacion.tienda.servicio import Servicio
from gestor_aplicacion.tienda.componente import Componente
from gestor_aplicacion.tienda.precio_componente import PrecioComponente
from gestor_aplicacion.tienda.bodega import Bodega
from gestor_aplicacion.tienda.producto import Producto
from gestor_aplicacion.tienda.caja_registradora import CajaRegistradora
from ui_main.field_frame import FieldFrame
from ui_main.inicio import Inicio
from base_datos.serializador import Serializador
from ctypes import resize
from tkinter import *
from numpy import diag
from random import choice, random, randint
from .producto_no_reparado_exception import ProductoNoReparadoException
from .servicio_pagado_exception import ServicioPagadoException
from .error_aplicacion import ErrorAplicacion
from .exception_pop_up import ExceptionPopUp
from .cliente_incorrecto_exception import ClientIncorrectoException
""""
  Ventana principal, donde se crea todo el UI principal y se enlazan
  las diferentes funciones y archivos para crear funcionalidades con 
  interfaz grafica. 
 * @author Erik Gonzalez
 * @author Felipe Miranda
 * @author Esteban Garcia
 * @author Emilio Porras
 */"""

if len(Dependiente.dependientes) == 0:
    dependiente = Dependiente("Esteban", 102943784, CajaRegistradora())

if len(Tecnico.tecnicos) == 0:
    tecnico = Tecnico("Emilio", 12312391)
    tecnico2 = Tecnico("Sebastian", 496875)

        

def outPut(string, text):
    text.delete("1.0", "end")
    text.insert(INSERT, string)
    text.pack(fill=X, expand=True)




def iniciar_ventana_usuario():
    #Ventana principal
    window = Tk()
    window.geometry("680x420")
    window.title("Generic IT")
    window.option_add("*tearOff",  FALSE)


    #Métodos sin argumentos para poder ejecutarlos-------------------------------------


    framesAMatar = []

    def matarloTodo(frameUtilizado):

        for frame in framesAMatar:
            frame.pack_forget()
        frameUtilizado.pack(fill=BOTH,expand=True)


    def evtClienteManual():
        matarloTodo(clienteManual)

    #Output de Generar cliente  
    outputGenerarCliente = Text(window, height=3)
    framesAMatar.append(outputGenerarCliente)    
    def evtGenerarCliente():
        cliente = generarCliente()
        outPut("Se genero el cliente ID: "+str(Cliente.clientes.index(cliente))+" "+cliente.__str__() ,outputGenerarCliente)
        matarloTodo(outputGenerarCliente)

    def evtSolicitarServicio():
        matarloTodo(solicitarServicio)
    
    def evtDiagnosticarProducto():
        matarloTodo(diagnosticarProducto)
    
    def evtRepararProducto():
        matarloTodo(repararProducto)
    
    def evtFinalizarServicio():
        matarloTodo(finalizarServicio)
    
    def evtCobrarServicio():
        matarloTodo(cobrarServicio)

    #Output de Liquidar el periodo  
    outputLiquidarPeriodo = Text(window, height=6)
    framesAMatar.append(outputLiquidarPeriodo)   
    def evtLiquidarPeriodo():
        dependiente = Dependiente.getDependientes()[0]
        stringqueseprintiara = "En la caja registradora hay " + str(round(dependiente.getCajaRegistradora().getTotalIngresos(),2)) + " antes de liquidar.\n"
        for liquidacion in dependiente.liquidar():
            stringqueseprintiara += "\n" + liquidacion

        stringqueseprintiara += "\n\nEn la caja registradora quedan " + str(round(dependiente.getCajaRegistradora().getTotalIngresos(),2))
        
        outPut(stringqueseprintiara, outputLiquidarPeriodo)
        matarloTodo(outputLiquidarPeriodo)
    
    #Output de mostrar clientes
    outPutMostrarClientes = Text(window, height=len(Cliente.clientes))
    framesAMatar.append(outPutMostrarClientes)
    #Evento para mostrar clientes
    def evtMostrarClientes():
        stri = ""
        for i in range(len(Cliente.clientes)):
            stri+="ID cliente: " + str(i) + " " + Cliente.clientes[i].__str__() + "\n"
        if stri == "":
            stri = "Aun no hay ningun cliente. :("
        outPut(stri, outPutMostrarClientes)
        matarloTodo(outPutMostrarClientes)
    
    #Output de mostrar servicios
    outPutMostrarServicios = Text(window, height=len(Servicio.servicios))
    framesAMatar.append(outPutMostrarServicios)
    #Evento para mostrar servicios
    def evtMostrarServicios():
        stri = ""
        for i in range(len(Servicio.servicios)):
            stri+= Servicio.servicios[i].__str__() + "\n"
        if stri == "":
            stri = "Aun no se ha generado ningun servicio. :("
        outPut(stri, outPutMostrarServicios)
        matarloTodo(outPutMostrarServicios)

    #Abre la pestana de dialogo con los nombres de los integrantes del equipo
    def open_popup():
        top= Toplevel(window)
        top.grid_rowconfigure(0, weight=1)
        top.geometry("450x250")
        top.resizable(False,False)
        top.title("Ayuda")
        Label(top, text= "AUTORES\nEmilio Porras Mejia\nEsteban Garcia Carmona\nErik Alexander Gonzalez Cardona\nFelipe Miranda Arboleda", font=('Times 18 bold')).pack(fill=BOTH, expand=True)

    #Abre la pestana de dialogo con la informacion del programa y su funcionalidad. 
    def aplicacion_popup():
        top= Toplevel(window)
        top.geometry("580x320")
        top.resizable(False,False)
        top.title("Aplicación")
        Label(top, text= textonimo , font=('Times 12')).pack(fill=BOTH, expand=True)
    textonimo = "Generic IT es una compañía tecnológica.\nSe busca crear un programa que emule las interacciones de Generic IT,\npara mejorar la organización de la empresa y proveer un mejor servicio.\nSe tendrá en cuenta toda la cadena de servicio, desde que llega el\ncliente con un producto a reparar, su paso por las manos del ténico,\nlas partes que tendrán que ser cambiadas, hasta finalizar con la\ndevolución del producto y el pago del servicio."




    #----------------------------------------------------------------------------------
    def salir():
        Serializador.serializarTodo()
        from ui_main.ventana_inicio.inicio import VentanaInicio
        framesAMatar = []
        window.destroy()
        ventana = VentanaInicio()
        ventana.mainloop()
        
    def evento():
        pass

    frame_a = Frame()#master = window
    
    frame_a.pack()
    #Barra menu superior
    menubar = Menu()

    menuarchivo = Menu(window)
    menuprocesos = Menu(window)
    menuayuda = Menu(window)
    

    menubar.add_cascade(menu = menuarchivo,
                        label='Archivo',
                        command = evento)
    menubar.add_cascade(menu = menuprocesos,
                        label = 'Procesos y Consultas',
                        command = evento)
    menubar.add_cascade(menu = menuayuda,
                        label='Ayuda',
                        command = evento)

    #submenu de procesos y consultas
    submenu = Menu(window)
    submenu.add_command(label = "Crear cliente manualmente", command = evtClienteManual)
    submenu.add_command(label = "Generar cliente", command = evtGenerarCliente)
    submenu.add_command(label = "Solicitar servicio", command = evtSolicitarServicio)
    submenu.add_command(label = "Diagnosticar producto", command = evtDiagnosticarProducto)

    menuarchivo.add_command(label = "Aplicacion", command = aplicacion_popup)
    menuarchivo.add_command(label = "Guardar y salir", command = salir)

    menuprocesos.add_cascade(label = "Menu diagnosticar un producto", menu = submenu)

    menuprocesos.add_command(label = "Reparar un producto", command = evtRepararProducto)
    menuprocesos.add_command(label = "Finalizar un servicio", command = evtFinalizarServicio)
    menuprocesos.add_command(label = "Cobrar un servicio", command = evtCobrarServicio)
    menuprocesos.add_command(label = "Liquidar el periodo", command = evtLiquidarPeriodo)
    menuprocesos.add_command(label = "Mostrar clientes", command = evtMostrarClientes)
    menuprocesos.add_command(label = "Mostrar servicios", command = evtMostrarServicios)

    menuayuda.add_command(label = "Acerca de", command = open_popup)

    window['menu'] = menubar


    #Frame de creacion manual del cliente ------------------------------------------------------------
    window.resizable(True,True)

    clienteManual = Frame(window, bd=10)
    nombre = Label(clienteManual, text="Crear cliente manualmente", bd= 10)



    #Interfaz de inicio----------------------------------------------------------------
    interfazInicio = Inicio(window)

    framesAMatar.append(interfazInicio)
    #----------------------------------------------------------------------------------


    

    descripcion = Label(clienteManual, text="Diligenciar la siguiente información para el correcto ingreso del cliente al sistema: ", bd= 10)

    #VALOR DE ID = len(Cliente.clientes)
    crearCliente = FieldFrame(clienteManual, "Datos cliente",["ID","Nombre", "Cedula", "Cartera"], "Valor", [len(Cliente.clientes), None, None, None], ["ID"],[1, 0, 1, 1])
    crearCliente.grid_columnconfigure(0, weight=1)
    crearCliente.grid_columnconfigure(1, weight=1)
    crearCliente.grid_rowconfigure(0, weight=1)
    crearCliente.grid_rowconfigure(1, weight=1)
    crearCliente.grid_rowconfigure(2, weight=1)
    crearCliente.grid_rowconfigure(3, weight=1)
    crearCliente.grid_rowconfigure(4, weight=1)
    crearCliente.grid_rowconfigure(5, weight=1)
    
    output = Text(clienteManual, height=3)
    framesAMatar.append(output)

    def creacionCliente():
        try:
            crearCliente.aceptarCheck()
            producto = generarProductoAleatorio()
            productos = [producto]
            #Creacion del cliente manual, actualizacion de las entries y ID cliente
            if float(crearCliente.getValue("Cartera")) > 500000:
                cliente = Cliente(crearCliente.getValue("Nombre"), crearCliente.getValue("Cedula"), productos, Dependiente.getDependientes()[0], float(crearCliente.getValue("Cartera")))
                valores = crearCliente.getValores()
                #Actualizar id del cliente en el FieldFrame
                crearCliente.setValores([int(valores[0]) + 1] + [valores[i] for i in range(1, len(valores))])
                #Resetear entries del FieldFrame
                crearCliente.setEntries(list())
                #Refrescar el FieldFrame
                crearCliente.actualizacion()
                outPut("Se ha generado manualmente el cliente con ID: " + str(len(Cliente.clientes)-1) + " " + cliente.__str__(), output)

            else: 
                outPut("No se ha generado el cliente, muy poco dinero!", output)
        except ErrorAplicacion as e:
            ExceptionPopUp(str(e))
        
    #Creacion de los botones para aceptar y borrar de creacion manual de cliente
    crearCliente.crearBotones(creacionCliente)   #     Aceptar             Borrar

    nombre.pack()
    #texto.pack()
    interfazInicio.pack()
    descripcion.pack()
    crearCliente.pack(fill=BOTH,expand=True)
    framesAMatar.append(clienteManual)
    
    #--------------------------------------------------------------------------------
     
    
    
    #Frame de Solicitar servicio-----------------------------------------------------
    solicitarServicio = Frame(window)
    nombreSolicitarServicio = Label(solicitarServicio, text="Solicitar servicio", bd=10)
    dcrSolicitarServicio = Label(solicitarServicio, text="Ingrese el ID del cliente para solicitar la reparacion de su producto", bd=10)
    FFsolicitarServicio = FieldFrame(solicitarServicio, None, ["ID cliente"], None, [None], [],[1])
    outputsolicitarServicio = Text(solicitarServicio, height=3)
    framesAMatar.append(outputsolicitarServicio)


    def aceptarSolicitarServicio():
        try:
            FFsolicitarServicio.aceptarCheck()
            outPut(funSolicitarServicio(FFsolicitarServicio.getValue("ID cliente")), outputsolicitarServicio) 
        except ErrorAplicacion as e:
            ExceptionPopUp(str(e))

    FFsolicitarServicio.crearBotones(aceptarSolicitarServicio)


    nombreSolicitarServicio.pack()
    dcrSolicitarServicio.pack()
    FFsolicitarServicio.pack()
    framesAMatar.append(solicitarServicio)
    #-------------------------------------------------------------------------------
    #@summary Diagnostica el servicio seleccionado por el administrador.
    #Frame de Diagnosticar producto-----------------------------------------------------
    diagnosticarProducto = Frame(window)
    nombreDiagnosticarProducto = Label(diagnosticarProducto, text="Diagnosticar un producto", bd=10)
    dcrDiagnosticarProducto = Label(diagnosticarProducto, text = "Ingrese el ID del servicio a diagnosticar", bd=10)
    FFdiagnosticarProducto = FieldFrame(diagnosticarProducto, None, ["ID Servicio"], None, [None], [],[1])
    outputDiagnosticarProducto = Text(diagnosticarProducto, height=7)
    framesAMatar.append(outputDiagnosticarProducto)

    def aceptarDiagnosticarProducto():
        try:
            FFdiagnosticarProducto.aceptarCheck()
        
            outPut(diagnosticarUnProducto(), outputDiagnosticarProducto)
        except ErrorAplicacion as e:
            ExceptionPopUp(str(e))

    FFdiagnosticarProducto.crearBotones(aceptarDiagnosticarProducto)


    nombreDiagnosticarProducto.pack()
    dcrDiagnosticarProducto.pack()
    FFdiagnosticarProducto.pack()
    framesAMatar.append(diagnosticarProducto)
    #-------------------------------------------------------------------------------

    


    #Frame de Reparar un producto-----------------------------------------------------
    repararProducto = Frame(window)
    nombreRepararProducto = Label(repararProducto, text="Reparar un producto", bd=10)
    dcrRepararProducto = Label(repararProducto, text="Ingrese el ID del servicio a reparar", bd=10)
    FFrepararProducto = FieldFrame(repararProducto, None, ["ID Servicio"], None, [None], [],[1])
    outputRepararProducto = Text(repararProducto, height=3)
    framesAMatar.append(outputRepararProducto)

    def aceptarRepararProducto():
        try:
            FFrepararProducto.aceptarCheck()
            outPut(reparar(), outputRepararProducto)
        except ErrorAplicacion as e:
            ExceptionPopUp(str(e))

    FFrepararProducto.crearBotones(aceptarRepararProducto)


    nombreRepararProducto.pack()
    dcrRepararProducto.pack()
    FFrepararProducto.pack()
    framesAMatar.append(repararProducto)
    #-------------------------------------------------------------------------------





    #Frame de Finalizar un servicio-----------------------------------------------------
    finalizarServicio = Frame(window)
    nombreFinalizarServicio = Label(finalizarServicio, text="Finalizar un servicio", bd=10)
    dcrFinalizarServicio = Label(finalizarServicio, text="Ingrese el ID del servicio a finalizar", bd=10)
    FFfinalizarServicio = FieldFrame(finalizarServicio, None, ["ID Servicio"], None, [None], [],[1])
    outputFinalizarServicio = Text(finalizarServicio, height=6)
    framesAMatar.append(outputFinalizarServicio)


    def aceptarFinalizarServicio():
        try:
            FFfinalizarServicio.aceptarCheck()
            outPut(finalizar(), outputFinalizarServicio)
        except ErrorAplicacion as e:
            ExceptionPopUp(str(e))


    FFfinalizarServicio.crearBotones(aceptarFinalizarServicio)


    nombreFinalizarServicio.pack()
    dcrFinalizarServicio.pack()
    FFfinalizarServicio.pack()
    framesAMatar.append(finalizarServicio)
    #-------------------------------------------------------------------------------





    #Frame de Cobrar un servicio-----------------------------------------------------
    cobrarServicio = Frame(window)
    nombreCobrarServicio = Label(cobrarServicio, text="Cobrar un servicio", bd=10)
    dcrCobrarServicio = Label(cobrarServicio, text="Ingrese el ID del servicio a cobrar", bd=10)
    FFcobrarServicio = FieldFrame(cobrarServicio, None, ["ID Servicio"], None, [None], [],[1])
    outputCobrarServicio = Text(cobrarServicio, height=3)
    framesAMatar.append(outputCobrarServicio)


    def aceptarCobrarServicio():
        try:
            FFcobrarServicio.aceptarCheck()
            #FUNCIONALIDAD DE COBRAR SERVICIO
            outPut(cobrar(), outputCobrarServicio)
        except ErrorAplicacion as e:
            ExceptionPopUp(str(e))


    FFcobrarServicio.crearBotones(aceptarCobrarServicio)


    nombreCobrarServicio.pack()
    dcrCobrarServicio.pack()
    FFcobrarServicio.pack()
    framesAMatar.append(cobrarServicio)
    #-------------------------------------------------------------------------------

    #FUNCIONALIDADES---------------------------------------------------------------------------------------

    def generarProductoAleatorio():
        rand = random()
        nombreProductos = [ "Laptop Legion 5", "Hp zbook 1", "Hp Omen 15", "Asus TUF Gaming", "HP XPS",
                    "Macbook pro", "Lenovo Thinkpad", "Hp pavilion", "Notebook Gigabyte", "MSI Strike" ]
        componentes = [ Componente("Memoria 4g Kinsgton", True),
                        Componente("Disco duro SSD 256gb", True),
                        Componente("Bateria laptop lenovo supercharger", True),
                        Componente("Procesador AMD", True),
                        Componente("Display 15 pulgadas", True),
                        Componente("Memoria 8g Kinsgton", True),
                        Componente("Disco duro HDD 512gb", True),
                        Componente("Bateria laptop lenovo", True),
                        Componente("Procesador Intel", True),
                        Componente("Display 17 pulgadas", True)]
        
        productoComponentes = list()
        productoComponentes.append(choice(componentes))
        productoComponentes.append(choice(componentes))

        return Producto(choice(nombreProductos), productoComponentes)
        

    def generarCliente():
        nombres = ["Esteban", "Emilio", "Felipe", "Erik", "Alexander", "Jaime", "Alejandro", "Emiliana", "Dua lipa", "Erika", "Michael", "Juliana"]
        componentes = [Componente("Memoria 4g Kingston", False, PrecioComponente.RAM_4GB.value),
        Componente("Disco duro SSD 256gb", False, PrecioComponente.DISCO_DURO_SSD_256GB.value),
        Componente("Bateria laptop lenovo supercharger", False, PrecioComponente.BATERIA_LAPTOP_SUPERCHARGER.value),
        Componente("Procesador AMD", False, PrecioComponente.PROCESADOR_AMD.value),
        Componente("Display 15 pulgadas", False, PrecioComponente.DISPLAY_LAPTOP_15In.value),
        Componente("Memoria 8g Kingston", False, PrecioComponente.RAM_8GB.value),
        Componente("Disco duro HDD 512gb", False, PrecioComponente.DISCO_DURO_HDD_512GB.value),
        Componente("Bateria laptop lenovo", False, PrecioComponente.BATERIA_LAPTOP.value),
        Componente("Procesador Intel", False, PrecioComponente.PROCESADOR_INTEL.value),
        Componente("Display 17 pulgadas", False, PrecioComponente.DISPLAY_LAPTOP_17In.value)]
        dependiente = Dependiente.dependientes[0]
        producto = generarProductoAleatorio()
        productos = [producto]
        cartera = int(450000+1000000*random())
        cliente = Cliente(choice(nombres), randint(100000000, 9999999999), productos, dependiente, cartera)

        valores = crearCliente.getValores()
        #Actualizar id del cliente en el FieldFrame
        crearCliente.setValores([int(valores[0]) + 1] + [valores[i] for i in range(1, len(valores))])
        #Resetear entries del FieldFrame
        crearCliente.setEntries(list())
        #Refrescar el FieldFrame
        crearCliente.actualizacion()

        for componente in componentes:
            Bodega.agregarComponente(componente)
        return cliente

    def funSolicitarServicio(index):
        try:
            cliente = Cliente.getClientes()[int(index)]
        except:
            raise ClientIncorrectoException("El id del cliente no es correcto")
        if len(cliente.getRecibos()) == 0:
            producto = cliente.getProductos()[0]
            cliente.solicitarReparacion(producto)
            return "El cliente fue atendido exitosamente por " + cliente.getDependiente().getNombre() + " y se ha generado el servicio con: " + producto.__str__() + ".\nYa puede consultar en los servicios para iniciar su diagnostico."
        else:
            return "El cliente " + cliente.getNombre() + " ya habia sido atendido\n"

    def diagnosticarUnProducto():
        try:
            servicio = Servicio.getServicios()[int(FFdiagnosticarProducto.getValue("ID Servicio"))] 
        except:
            raise ClientIncorrectoException("El id del servicio no es correcto")
        if not servicio.isReparado():
            servicio.getTecnico().diagnosticar(servicio)
            # Devuelve el diagnostico hecho por el tecnico.
            stringDiagnostico = servicio.getDiagnostico()
            stringDiagnostico += "\nYa puede volver al menu principal para solicitar reparacion\n"
        else:
            stringDiagnostico = "Este producto ya habia sido reparado\n"
        return stringDiagnostico

    def reparar():
        try:
            servicio = Servicio.getServicios()[int(FFrepararProducto.getValue("ID Servicio"))]
        except:
            raise ClientIncorrectoException("El id del servicio no es correcto")

        if not servicio.isReparado():
            if servicio.getDiagnostico != None:
                servicio.getTecnico().reparar(servicio)
                return "El servicio de " + servicio.getCliente().getNombre() + " fue arreglado por "+ servicio.getTecnico().__str__() + " y tuvo un costo para la empresa de " + str(servicio.getCosto())
            else:
                return "No se ha diagnosticado el producto del cliente "+ servicio.getCliente().__str__()
        else: 
            return "Ya se ha reparado el producto!"

    def finalizar():
        try: 
            index = FFfinalizarServicio.getValue("ID Servicio")
            servicio = Servicio.getServicios()[int(index)]
        except:
            raise ClientIncorrectoException("El id del servicio no es correcto")

        if servicio.isReparado():
            dependiente = servicio.getDependiente()
            dependiente.finalizarServicio(servicio)
            return servicio.getCliente().getRecibos()[0] + "\nEl servicio ya esta listo para ser cobrado."
        else:
            raise ProductoNoReparadoException("El servicio no ha sido reparado aun y no se puede finalizar.")

    def cobrar():
        try:
            servicio = Servicio.getServicios()[int(FFcobrarServicio.getValue("ID Servicio"))]
            dependiente = Dependiente.getDependientes()[0]
        except:
            raise ClientIncorrectoException("El id del servicio no es correcto")

        if not servicio.isPagado():
            if servicio.isReparado():
                dependiente.cobrarServicio(servicio)
                sancocho = "Se cobra el servicio por un total de "+ str(servicio.getCosto() * Dependiente.getMargenGanancia())
                sancocho += "\nEn la caja registradora ahora hay "+ str(dependiente.getCajaRegistradora().getTotalIngresos()) + " pesos."
                return sancocho
            else:
                raise ProductoNoReparadoException("Aun no se ha reparado el producto, Que esperas?")
        else:
            raise ServicioPagadoException("Ya se ha cobrado el servicio! Se lamenta la molestia.")
    #------------------------------------------------------------------------------------------------------
    window.mainloop()




