from datetime import date
from random import choice, randint
from string import ascii_uppercase

from gestorAplicacion.datosAleatorios import randbool, tiposVehiculos, cargosEnCocina, especialidadesChefs

from gestorAplicacion.usuariosRestaurante.empleado import Empleado
from gestorAplicacion.usuariosRestaurante.repartidor import Repartidor
from gestorAplicacion.usuariosRestaurante.mesero import Mesero
from gestorAplicacion.usuariosRestaurante.chef import Chef

from gestorAplicacion.gestionRestaurante.producto import Producto
from gestorAplicacion.gestionRestaurante.pedido import Pedido
from gestorAplicacion.gestionRestaurante.estadoPedido import EstadoPedido
from gestorAplicacion.gestionRestaurante.tipoPedido import TipoPedido

class Administrador(Empleado):

    # Atributos estaticos

    _administradores = []
    _IMPUESTOS = 1.19 # Constante

    # Constructor

    def __init__(self, cedula = 0, nombre = "", disponibilidad = False, salario = 0, restaurante = None):
        super().__init__(cedula, nombre, "Administrador", disponibilidad, salario, restaurante)
        
        listaEmpleados = self._restaurante.getEmpleados()
        listaEmpleados.append(self)
        self._restaurante.setEmpleados(listaEmpleados)

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

    def contratarEmpleado(self, cedula, nombre, cargo, disponibilidad, salario, restaurante):
        empleadoNuevo = None

        if cargo == "Mesero":
            empleadoNuevo = Mesero(cedula, nombre, disponibilidad, salario, restaurante)
        elif cargo == "Repartidor":
            poseeVehiculo = randbool()
            placa = f"{choice(ascii_uppercase)}{choice(ascii_uppercase)}{choice(ascii_uppercase)}-{randint(100, 999)}"
            tipoVehiculo = choice(tiposVehiculos)
            empleadoNuevo = Repartidor(cedula, nombre, disponibilidad, salario, restaurante, poseeVehiculo, placa, tipoVehiculo)
        elif cargo == "Chef":
            cargoEnCocina = choice(cargosEnCocina)
            especialidad = choice(especialidadesChefs)
            empleadoNuevo = Chef(cedula, nombre, disponibilidad, salario, restaurante, cargoEnCocina, especialidad)
        else:
            empleadoNuevo = Empleado(cedula, nombre, disponibilidad, salario, restaurante)

        listaEmpleados = self._restaurante.getEmpleados()
        listaEmpleados.append(empleadoNuevo)
        self._restaurante.setEmpleados(listaEmpleados)

        return f"Empleado {nombre} creado con exito"

    def despedirEmpleado(self, idEmpleado):
        listaEmpleados = self._restaurante.getEmpleados()
        nombre = listaEmpleados[idEmpleado].getNombre()

        if len(listaEmpleados) > idEmpleado:
            listaEmpleados.remove(idEmpleado)
            self._restaurante.setEmpleados(listaEmpleados)
            return f"El empleado {nombre} ha sido despedido"
        else:
            return "El empleado que intentas despedir no trabaja en el restaurante"

    def crearProducto(self, nombre, descripcion, precio, disponibilidad, restriccion, cantidad):
        productoNuevo = Producto(nombre, descripcion, precio, disponibilidad, restriccion, cantidad)
        
        listaMenu = self._restaurante.getMenu()
        listaNombresMenu = []
        
        for producto in listaMenu:
            listaNombresMenu.append(producto.getNombre())

        if not nombre in listaNombresMenu:
            listaMenu.append(productoNuevo)
            self._restaurante.setMenu(listaMenu)
            return f"Producto {nombre} creado con exito"
        else:
            return f"El producto que intentas crear ya existe"

    def actualizarNombreProducto(self, idProducto, nombre):
        listaMenu = self._restaurante.getMenu()
        listaNombresMenu = []

        for producto in listaMenu:
            listaNombresMenu.append(producto.getNombre())
        
        if len(listaMenu) > idProducto:
            productoActualizado = listaMenu[idProducto]

            if not nombre in listaNombresMenu:
                productoActualizado.setNombre(nombre)
                listaMenu[idProducto] = productoActualizado
                self._restaurante.setMenu(listaMenu)
                return f"Producto {productoActualizado.getNombre()} actualizado con exito"
            else:
                return f"Ya exista un producto con este nombre. Intentalo de nuevo con otro nombre"
        else:
            return f"El producto que intentas actualizar no existe"

    def actualizarDescripcionProducto(self, idProducto, descripcion):
        listaMenu = self._restaurante.getMenu()

        if len(listaMenu) > idProducto:
            productoActualizado = listaMenu[idProducto]
            productoActualizado.setDescripcion(descripcion)
            listaMenu[idProducto] = productoActualizado
            self._restaurante.setMenu(listaMenu)
            return f"Producto {productoActualizado.getNombre()} actualizado con exito"
        else:
            return f"El producto que intentas actualizar no existe"

    def actualizarPrecioProducto(self, idProducto, precio):
        listaMenu = self._restaurante.getMenu()

        if len(listaMenu) > idProducto:
            productoActualizado = listaMenu[idProducto]
            productoActualizado.setPrecio(precio)
            listaMenu[idProducto] = productoActualizado
            self._restaurante.setMenu(listaMenu)
            return f"Producto {productoActualizado.getNombre()} actualizado con exito"
        else:
            return f"El producto que intentas actualizar no existe"

    def actualizarRestriccionProducto(self, idProducto, restriccion):
        listaMenu = self._restaurante.getMenu()

        if len(listaMenu) > idProducto:
            productoActualizado = listaMenu[idProducto]
            productoActualizado.setRestriccion(restriccion)
            listaMenu[idProducto] = productoActualizado
            self._restaurante.setMenu(listaMenu)
            return f"Producto {productoActualizado.getNombre()} actualizado con exito"
        else:
            return f"El producto que intentas actualizar no existe"

    def actualizarDisponibilidadProducto(self, idProducto, disponibilidad):
        listaMenu = self._restaurante.getMenu()

        if len(listaMenu) > idProducto:
            productoActualizado = listaMenu[idProducto]
            productoActualizado.setDisponiblidad(disponibilidad)
            listaMenu[idProducto] = productoActualizado
            self._restaurante.setMenu(listaMenu)
            return f"Producto {productoActualizado.getNombre()} actualizado con exito"
        else:
            return f"El producto que intentas actualizar no existe"

    def actualizarCantidadProducto(self, idProducto, cantidad):
        listaMenu = self._restaurante.getMenu()

        if len(listaMenu) > idProducto:
            productoActualizado = listaMenu[idProducto]
            productoActualizado.setCantidad(cantidad)
            listaMenu[idProducto] = productoActualizado
            self._restaurante.setMenu(listaMenu)
            return f"Producto {productoActualizado.getNombre()} actualizado con exito"
        else:
            return f"El producto que intentas actualizar no existe"

    def eliminarProducto(self, idProducto):
        listaMenu = self._restaurante.getMenu()
        producto = listaMenu[idProducto].getNombre()
        
        if len(listaMenu) > idProducto:
            listaMenu.remove(idProducto)
            self._restaurante.setMenu(listaMenu)
            return f"El producto {producto} ha sido eliminado"
        else:
            return f"El producto que intentas eliminar no existe"

    def pagoNomina(self, idEmpleado = None):
        if idEmpleado is None:
            listaEmpleados = self._restaurante.getEmpleados()
            total = 0

            for empleado in listaEmpleados:
                total += empleado.getSalario() * Administrador.getImpuestos()

            if total <= self._restaurante.getBalanceCuenta():
                nuevoBalance = self._restaurante.getBalanceCuenta() - total
                self._restaurante.setBalanceCuenta(nuevoBalance)
                return f"Nomina de todos los empleados pagada con exito. El nuevo balance de cuenta es: ${self._restaurante.getBalanceCuenta()}"
            else:
                return f"No se posee el suficiente dinero para pagar la nomina de todos los empleados (${total})"
        else:
            empleado = self._restaurante.getEmpleados()[idEmpleado]
            salario = empleado.getSalario() * Administrador.getImpuestos()

            if salario <= self._restaurante.getBalanceCuenta():
                nuevoBalance = self._restaurante.getBalanceCuenta() - salario
                self._restaurante.setBalanceCuenta(nuevoBalance)
                return f"Nomina del empleado {empleado.getNombre()} pagada con exito. El nuevo balance de cuenta es: ${self._restaurante.getBalanceCuenta()}"
            else:
                return f"No se posee el suficiente dinero para pagar la nomina del empleado (${salario})"

    def simularPedido(self, cliente):
        pedido = Pedido(cliente)
        pedido.setRestaurante(self._restaurante)
        pedido.setCodigo(Pedido.getTotalPedidos())
        pedido.setFechaHora(date.today().strftime("%b-%d-%Y"));

        tipoRandom = randint(0,2)

        if tipoRandom == 0:
            tipo = TipoPedido.LLEVAR.value
        elif tipoRandom == 1:
            tipo = TipoPedido.TIENDA.value
        elif tipoRandom == 2:
            tipo = TipoPedido.DOMICILIO.value

        pedido.setTipo(tipo)
        
        listaMeseros = Mesero.getMeseros()
        meseroElegido = listaMeseros[randint(0, len(listaMeseros)-1)]
        meseroElegido.agregarPedidoHistorial(pedido)

        cantidadProductos = randint(1, len(self._restaurante.getMenu())-1)
        productos = []

        for i in range(cantidadProductos):
            productoRandom = randint(0, len(self._restaurante.getMenu())-1)
            producto = self._restaurante.getMenu()[productoRandom]

            if producto not in productos:
                cantidadXProducto = randint(1, 5)
                producto.setCantidad(cantidadXProducto)
                productos.append(producto)
            else:
                i -= 1

        pedido.setProductos(productos)

        precioTotal = 0

        for producto in productos:
            precioTotal += producto.getCantidad() * producto.getPrecio()

        pedido.setPrecioTotal(precioTotal)

        pedido.setEstado(EstadoPedido.RECIBIDO.value);
        self._restaurante.agregarPedido(pedido);
        return pedido

    # Implementacion de la interfaz

    def informacion(self):
        info = f"El Administrador {self._nombre} del restaurente {self._restaurante.getNombre()} es {self._nombre} con C.C. {self._cedula}. Tiene un salario de: ${self._salario}. "
        
        if self._disponibilidad:
            return info + "Está disponible actualmente."
        else:
            return info + "No está disponible actualmente."