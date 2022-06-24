
# ! ACTUALIZAR METODOS DE ACTUALIZACION PARA LOS NUMEROS Y BOOLEANOS
# ! ACTUALIZAR METODOS DE ACTUALIZACION PARA LOS NUMEROS Y BOOLEANOS
# ! ACTUALIZAR METODOS DE ACTUALIZACION PARA LOS NUMEROS Y BOOLEANOS
# ! ACTUALIZAR METODOS DE ACTUALIZACION PARA LOS NUMEROS Y BOOLEANOS
# ! ACTUALIZAR METODOS DE ACTUALIZACION PARA LOS NUMEROS Y BOOLEANOS
# ! ACTUALIZAR METODOS DE ACTUALIZACION PARA LOS NUMEROS Y BOOLEANOS
# ! ACTUALIZAR METODOS DE ACTUALIZACION PARA LOS NUMEROS Y BOOLEANOS
# ! ACTUALIZAR METODOS DE ACTUALIZACION PARA LOS NUMEROS Y BOOLEANOS
# ! ACTUALIZAR METODOS DE ACTUALIZACION PARA LOS NUMEROS Y BOOLEANOS
# ! ACTUALIZAR METODOS DE ACTUALIZACION PARA LOS NUMEROS Y BOOLEANOS
# ! ACTUALIZAR METODOS DE ACTUALIZACION PARA LOS NUMEROS Y BOOLEANOS
# ! ACTUALIZAR METODOS DE ACTUALIZACION PARA LOS NUMEROS Y BOOLEANOS
# ! ACTUALIZAR METODOS DE ACTUALIZACION PARA LOS NUMEROS Y BOOLEANOS
# ! ACTUALIZAR METODOS DE ACTUALIZACION PARA LOS NUMEROS Y BOOLEANOS
# ! ACTUALIZAR METODOS DE ACTUALIZACION PARA LOS NUMEROS Y BOOLEANOS
# ! ACTUALIZAR METODOS DE ACTUALIZACION PARA LOS NUMEROS Y BOOLEANOS

from datetime import date
from random import choice, randint

from gestorAplicacion.datosAleatorios import randbool, tiposVehiculos, cargosEnCocina, especialidadesChefs, randPlaca

from gestorAplicacion.usuariosRestaurante.empleado import Empleado
from gestorAplicacion.usuariosRestaurante.repartidor import Repartidor
from gestorAplicacion.usuariosRestaurante.mesero import Mesero
from gestorAplicacion.usuariosRestaurante.chef import Chef

from gestorAplicacion.gestionRestaurante.producto import Producto
from gestorAplicacion.gestionRestaurante.pedido import Pedido
from gestorAplicacion.gestionRestaurante.estadoPedido import EstadoPedido
from gestorAplicacion.gestionRestaurante.tipoPedido import TipoPedido

from excepciones.excepcionLista import ExcepcionLista

class Administrador(Empleado):

    # Atributos estaticos

    _administradores = []
    _IMPUESTOS = 1.19 # Constante

    # Constructor

    def __init__(self, cedula = 0, nombre = "", disponibilidad = False, salario = 0, restaurante = None):
        super().__init__(cedula, nombre, "Administrador", disponibilidad, salario, restaurante)

        Administrador._administradores.append(self)

    # Getters y Setters

    @classmethod
    def getAdministradores(cls):
        return cls._administradores

    @classmethod
    def setAdministradores(cls, administradores):
        cls._administradores = administradores

    @classmethod
    def getImpuestos(cls):
        return cls._IMPUESTOS

    @classmethod
    def setImpuestos(cls, impuestos):
        cls._IMPUESTOS = impuestos

    # Metodos

    # Crear un nuevo empleado (O alguno de sus subtipos) y añadirlo a los empleados del restaurante
    def contratarEmpleado(self, cedula, nombre, cargo, disponibilidad, salario, restaurante):
        empleadoNuevo = None

        # Verificar cargo del empleado
        if cargo == "Mesero":
            empleadoNuevo = Mesero(cedula, nombre, disponibilidad, salario, restaurante)
        elif cargo == "Repartidor":
            poseeVehiculo = randbool()
            placa = randPlaca()
            tipoVehiculo = choice(tiposVehiculos)
            empleadoNuevo = Repartidor(cedula, nombre, disponibilidad, salario, restaurante, poseeVehiculo, placa, tipoVehiculo)
        elif cargo == "Chef":
            cargoEnCocina = choice(cargosEnCocina)
            especialidad = choice(especialidadesChefs)
            empleadoNuevo = Chef(cedula, nombre, disponibilidad, salario, restaurante, cargoEnCocina, especialidad)
        else:
            empleadoNuevo = Empleado(cedula, nombre, disponibilidad, salario, restaurante)

        # Añadir a la lista de empleados
        listaEmpleados = self._restaurante.getEmpleados()
        listaEmpleados.append(empleadoNuevo)
        self._restaurante.setEmpleados(listaEmpleados)

        # Mensaje de confirmacion
        return f"Empleado {nombre} creado con exito"

    # Sacar empleado de la lista del restaurente, primero verificar si existe
    def despedirEmpleado(self, idEmpleado):
        listaEmpleados = self._restaurante.getEmpleados()

        # Verificar si el numero dado pertenece a la lista
        if len(listaEmpleados) > idEmpleado and idEmpleado >= 0:
            nombre = listaEmpleados[idEmpleado].getNombre()
            del listaEmpleados[idEmpleado]
            self._restaurante.setEmpleados(listaEmpleados)

            return f"El empleado {nombre} ha sido despedido"
        else:
            raise ExcepcionLista([idEmpleado, len(listaEmpleados)-1])

    # Crear nuevo producto y añadirlo al menu del restaurante
    def crearProducto(self, nombre, descripcion, precio, disponibilidad, restriccion, cantidad):
        productoNuevo = Producto(nombre, descripcion, precio, disponibilidad, restriccion, cantidad)
        
        # Verificar primero si ya existe un producto que se llame asi
        listaMenu = self._restaurante.getMenu()
        listaNombresMenu = []
        
        for producto in listaMenu:
            listaNombresMenu.append(producto.getNombre())

        # Si no existe, añadirlo a la lista
        if not nombre in listaNombresMenu:
            listaMenu.append(productoNuevo)
            self._restaurante.setMenu(listaMenu)

            return f"Producto {nombre} creado con exito"
        else:
            return f"El producto que intentas crear ya existe"

    # Actualizar el nombre de un producto, primero verificar si existe
    def actualizarNombreProducto(self, idProducto, nombre):
        # Verificar si hay ya un producto que se llame asi
        listaMenu = self._restaurante.getMenu()
        listaNombresMenu = []

        for producto in listaMenu:
            listaNombresMenu.append(producto.getNombre())
        
        # Verificar que existe el ID especificado
        if len(listaMenu) > idProducto and idProducto >= 0:
            productoActualizado = listaMenu[idProducto]

            # Si no hay producto con el mismo nombre, actualizarlo
            if not nombre in listaNombresMenu:
                productoActualizado.setNombre(nombre)
                listaMenu[idProducto] = productoActualizado
                self._restaurante.setMenu(listaMenu)

                return f"Producto {productoActualizado.getNombre()} actualizado con exito"
            else:
                return f"Ya exista un producto con este nombre. Intentalo de nuevo con otro nombre"
        else:
            raise ExcepcionLista([idProducto, len(listaMenu)-1])

    # Actualizar la descripcion de un producto, primero verificar si existe
    def actualizarDescripcionProducto(self, idProducto, descripcion):
        listaMenu = self._restaurante.getMenu()

        if len(listaMenu) > idProducto and idProducto >= 0:
            productoActualizado = listaMenu[idProducto]
            productoActualizado.setDescripcion(descripcion)
            listaMenu[idProducto] = productoActualizado
            self._restaurante.setMenu(listaMenu)

            return f"Producto {productoActualizado.getNombre()} actualizado con exito"
        else:
            raise ExcepcionLista([idProducto, len(listaMenu)-1])

    # Actualizar el precio de un producto, primero verificar si existe
    def actualizarPrecioProducto(self, idProducto, precio):
        listaMenu = self._restaurante.getMenu()

        if len(listaMenu) > idProducto and idProducto >= 0:
            productoActualizado = listaMenu[idProducto]
            productoActualizado.setPrecio(precio)
            listaMenu[idProducto] = productoActualizado
            self._restaurante.setMenu(listaMenu)

            return f"Producto {productoActualizado.getNombre()} actualizado con exito"
        else:
            raise ExcepcionLista([idProducto, len(listaMenu)-1])

    # Actualizar la restriccion de edad de un producto, primero verificar si existe
    def actualizarRestriccionProducto(self, idProducto, restriccion):
        listaMenu = self._restaurante.getMenu()

        if len(listaMenu) > idProducto and idProducto >= 0:
            productoActualizado = listaMenu[idProducto]
            productoActualizado.setRestriccion(restriccion)
            listaMenu[idProducto] = productoActualizado
            self._restaurante.setMenu(listaMenu)

            return f"Producto {productoActualizado.getNombre()} actualizado con exito"
        else:
            raise ExcepcionLista([idProducto, len(listaMenu)-1])

    # Actualizar la disponibilidad de un producto, primero verificar si existe
    def actualizarDisponibilidadProducto(self, idProducto, disponibilidad):
        listaMenu = self._restaurante.getMenu()

        if len(listaMenu) > idProducto and idProducto >= 0:
            productoActualizado = listaMenu[idProducto]
            productoActualizado.setDisponibilidad(disponibilidad)
            listaMenu[idProducto] = productoActualizado
            self._restaurante.setMenu(listaMenu)

            return f"Producto {productoActualizado.getNombre()} actualizado con exito"
        else:
            raise ExcepcionLista([idProducto, len(listaMenu)-1])

    # Actualizar la cantidad disponible de un producto, primero verificar si existe
    def actualizarCantidadProducto(self, idProducto, cantidad):
        listaMenu = self._restaurante.getMenu()

        if len(listaMenu) > idProducto and idProducto >= 0:
            productoActualizado = listaMenu[idProducto]
            productoActualizado.setCantidad(cantidad)
            listaMenu[idProducto] = productoActualizado
            self._restaurante.setMenu(listaMenu)

            return f"Producto {productoActualizado.getNombre()} actualizado con exito"
        else:
            raise ExcepcionLista([idProducto, len(listaMenu)-1])

    # Eliminar un producto del menu, primero verificar si existe
    def eliminarProducto(self, idProducto):
        listaMenu = self._restaurante.getMenu()
        
        if len(listaMenu) > idProducto and idProducto >= 0:
            producto = listaMenu[idProducto].getNombre()
            del listaMenu[idProducto]
            self._restaurante.setMenu(listaMenu)

            return f"El producto {producto} ha sido eliminado"
        else:
            raise ExcepcionLista([idProducto, len(listaMenu)-1])

    # Funcionalidad de pago de nomina
    
    def pagoNomina(self, idEmpleado = None):
        listaEmpleados = self._restaurante.getEmpleados()

        # Verificar si se especifico un empleado, si no, se le paga a todos
        if idEmpleado is None:
            total = 0

            # Conseguir el total de los salarios
            for empleado in listaEmpleados:
                total += empleado.getSalario() * Administrador.getImpuestos() # Considerar el 19% de impuestos

            # Verificar si se posee el dinero suficiente para pagar
            if total <= self._restaurante.getBalanceCuenta():
                nuevoBalance = self._restaurante.getBalanceCuenta() - total
                self._restaurante.setBalanceCuenta(nuevoBalance)

                return f"Nomina de todos los empleados pagada con exito. El nuevo balance de cuenta es: ${self._restaurante.getBalanceCuenta()}"
            else:
                return f"No se posee el suficiente dinero para pagar la nomina de todos los empleados (${total})"
        
        # Pagar a un empleado en especifico
        else:
            empleado = self._restaurante.getEmpleados()[idEmpleado]
            salario = empleado.getSalario() * Administrador.getImpuestos()

            # Verificar si existe el empleado
            if  not (len(listaEmpleados) > idEmpleado and idEmpleado >= 0):
                raise ExcepcionLista([idEmpleado, len(listaEmpleados)-1])

            # Verificar si se posee el dinero suficiente para pagar
            if salario <= self._restaurante.getBalanceCuenta():
                nuevoBalance = self._restaurante.getBalanceCuenta() - salario
                self._restaurante.setBalanceCuenta(nuevoBalance)

                return f"Nomina del empleado {empleado.getNombre()} pagada con exito. El nuevo balance de cuenta es: ${self._restaurante.getBalanceCuenta()}"
            else:
                return f"No se posee el suficiente dinero para pagar la nomina del empleado (${salario})"

    # Funcionalidad simular pedido

    def simularPedido(self, cliente):
        # Crear el nuevo pedido
        pedido = Pedido(cliente)
        pedido.setRestaurante(self._restaurante)
        pedido.setCodigo(Pedido.getTotalPedidos())
        pedido.setFechaHora(date.today().strftime("%b-%d-%Y"));

        # Escoger aleatoriamente el tipo del pedido
        tipoRandom = randint(0,2)

        if tipoRandom == 0:
            tipo = TipoPedido.LLEVAR.value
        elif tipoRandom == 1:
            tipo = TipoPedido.TIENDA.value
        elif tipoRandom == 2:
            tipo = TipoPedido.DOMICILIO.value

        pedido.setTipo(tipo)
        
        # Asignar un mesero aleatorio
        listaMeseros = Mesero.getMeseros()
        meseroElegido = listaMeseros[randint(0, len(listaMeseros)-1)]
        meseroElegido.agregarPedidoHistorial(pedido, randint(1, 10))

        # Escoger aleatoriamente una cantidad de productos del restaurante (Minimo 1)
        cantidadProductos = randint(1, len(self._restaurante.getMenu())-1)
        productos = []

        for i in range(cantidadProductos):
            # Escoger el producto de la lista
            productoRandom = randint(0, len(self._restaurante.getMenu())-1)
            producto = self._restaurante.getMenu()[productoRandom]

            # Verificar si el producto ya esta en la lista del pedido
            if producto not in productos:
                # Escoger cantidad a pedir del producto y agregarlo al pedido
                cantidadXProducto = randint(1, 5)
                producto.setCantidad(cantidadXProducto)
                productos.append(producto)
            else:
                i -= 1

        pedido.setProductos(productos)

        # Calcular el precio total
        precioTotal = 0

        for producto in productos:
            precioTotal += producto.getCantidad() * producto.getPrecio()

        pedido.setPrecioTotal(precioTotal)

        # Poner el producto en estado recibido y agregarlo a la lista del restaurante
        pedido.setEstado(EstadoPedido.RECIBIDO.value);
        self._restaurante.agregarPedido(pedido);
        return pedido

    # Implementacion de la interfaz

    def informacion(self):
        info = f"El Administrador {self._nombre} del restaurente {self._restaurante.getNombre()} es {self._nombre} con C.C. {self._cedula}.\n" \
               f"Tiene un salario de: ${self._salario}.\n"
        
        if self._disponibilidad:
            return info + "Esta disponible actualmente."
        else:
            return info + "No esta disponible actualmente."