from usuariosRestaurante.usuario import Usuario

class Empleado(Usuario):
     
    # Constructor

    def __init__(self, cedula = 0, nombre = "", cargo = "", disponibilidad = False, salario = 0, restaurante = None):
        self._cedula = cedula
        self._nombre = nombre
        self._cargo = cargo
        self._disponibilidad = disponibilidad
        self._salario = salario
        self._restaurante = restaurante

    # Getters y Setters
    
    def getCedula(self):
        return self._cedula

    def setCedula(self, cedula): 
        self._cedula = cedula

    def getNombre(self): 
        return self._nombre

    def setNombre(self, nombre):
        self._nombre = nombre

    def getCargo(self): 
        return self._cargo

    def setCargo(self, cargo):
        self._cargo = cargo

    def getSalario(self): 
        return self._salario

    def getDisponibilidad(self): 
        return self._disponibilidad

    def setDisponibilidad(self, disponibilidad):
        self._disponibilidad = disponibilidad

    def setSalario(self, salario):
        self._salario = salario


    def getRestaurante(self):
        return self._restaurante


    def setRestaurante(self, restaurante):
        self._restaurante = restaurante

    # Metodos

    def procesarPedido(self, pedido):
        if self._restaurante.verificarPedido(pedido) and self._restaurante.verificarProductos(pedido):
            return True
        else:
            return False

    def actualizarEstadoPedido(self, pedido, aceptado):
        if not aceptado:
            pedido.setEstado(EstadoPedido.RECHAZADO)
            return False
        
        if pedido.getEstado() == "Recibido":
            pedido.setEstado(EstadoPedido.ACEPTADO);
        elif pedido.getEstado() == "Aceptado":
            pedido.setEstado(EstadoPedido.EN_PREPARACION);
        elif pedido.getEstado() == "EnPreparacion":
            pedido.setEstado(EstadoPedido.LISTO);
        elif pedido.getEstado() == "Listo":
            pedido.setEstado(EstadoPedido.DESPACHADO);

        return True

    # Implementacion de la interfaz

    def informacion(self):
        info = f"El Empleado {self._nombre} con C.C. {self._cedula} trabaja en el restaurante {self._restaurante.getNombre()}. Tiene un salario de: ${self._salario} y desempeña el cargo de {self._salario}. "
        
        if self._disponibilidad:
            return info + "Está disponible actualmente."
        else:
            return info + "No está disponible actualmente."