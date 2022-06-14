from asyncio.windows_events import NULL
from operator import truediv

class Restaurante:

    

    # Atributos estaticos

    _restaurantes = []

    # Constructor

    def __init__(self, nombre="", nit=0, telefono=0, direccion = "", correo = "", abierto=False,
			capacidad = 0, empleados = NULL, menu = NULL,pedidos = NULL, balanceCuenta=0):
        self.__nombre = nombre
        self.__nit = nit 
        self.__telefono = telefono
        self.__direccion = direccion
        self.__correo = correo
        self.__abierto = abierto
        self.__capacidad = capacidad
        self.__empleados = empleados
        self.__menu = menu
        self.__pedidos = pedidos
        self.__balanceCuenta = balanceCuenta
        Restaurante._restaurantes.append(self)
   

    # Getters y Setters
    def getNombre(self):
        return self.__nombre

    def setNombre(self, nombre):
        self.__nombre=nombre
    
    def getNit(self):
        return self.__nit

    def setNit(self, nit):
        self.__nit=nit

    def getTelefono(self):
        return self.__telefono

    def setTelefono(self, telefono):
        self.__telefono=telefono

    def getDireccion(self):
        return self.__direccion
    
    def setDireccion(self, direccion):
        self.__direccion = direccion

    def getCorreo(self):
        return self.__correo
    
    def setCorreo(self, correo):
        self.__correo = correo
    
    def getAbierto(self):
        return self.__abierto

    def setAbierto(self, abierto):
        self.__abierto = abierto
    
    def getCapacidad(self):
        return self.__capacidad
    
    def setCapacidad(self, capacidad):
        self.__capacidad=capacidad
    
    def getEmpleados(self):
        return self.__empleados
    
    def setEmpleados(self, empleados):
        self.__empleados = empleados
    
    def getMenu(self):
        return self.__menu
    
    def setMenu(self, menu):
        self.__menu= menu

    def getPedidos(self):
        return self.__pedidos
    
    def setPedidos(self, pedidos):
        self.__pedidos = pedidos
    
    def getBalanceCuenta(self):
        return self.__balanceCuenta

    def setBalanceCuenta(self, balanceCuenta):
        self.__balanceCuenta = balanceCuenta  
    
    @classmethod
    def getRestaurantes(cls):
        return cls._restaurantes

    @classmethod
    def setRestaurantes(cls, restaurantes):
        cls._restaurantes = restaurantes

    # Metodos

    def verificarPersonal(self, pedido):
		#Comprobamos si existe un chef en el restaurante
        chef = False
        for empleado in self.__empleados:
            if (empleado.getCargo() == "Chef"):
                chef = True
			

		# Identificar el tipo de pedido
		
        if(pedido.getTipo() == "A domicilio"): 
			#Rectificar el personal del restaurante y comprobar que haya el necesario para el tipo de pedido
            repartidor = False
            for empleado in self.__empleados:
                if (empleado.getCargo() == "Repartidor"):
                    repartidor = True
			#Si si no hay alguno no se puede realizar
            if (not chef and not repartidor):
                return False
			
			#Si todo es aceptable se realiza el pedido
		
        if(pedido.getTipo() =="Para consumir en la tienda" or pedido.getTipo() =="Para llevar"):
			#Rectificar el personal del restaurante y comprobar que haya el necesario para el tipo de pedido
            mesero = False
            for empleado in self.__empleados:
                if (empleado.getCargo() == "mesero"):
                    mesero = True

			#Si si no hay alguno no se puede realizar
            if (not chef and not mesero):
                return False
			#Si todo es aceptable se realiza el pedido

		#Si todo es aceptable se realiza el pedido
        return True
    
    # Metodo que determina si el restaurante posee los productos solicitados en un pedido
    def verificarProductos(self, pedido):
        for demanda in pedido.getProductos():
            existe = False
            cantidad = False
            disponible = False
            for oferta in self.__menu:
                if (demanda.getNombre() == oferta.getNombre()):
                    existe = True
                    disponible = oferta.getDisponiblidad()
                    if (oferta.getCantidad() >= demanda.getCantidad()):
                        cantidad = True
                        if(not existe or not cantidad or not disponible):
                            return False
        return True
	
    # ESTADISTICAS
    def  getRepartidorConMasPedidos(self):
		#Repartidor vacio para que el metodo funcione
        topRepartidor
		#Loop para encontrar el repartidor con mas pedidos repartidos
        for repartidor in repartidor.getRepartidores():
			#Comparamos cada repartidor en la lista de repartidores
            repartidos1 = repartidor.getCantidadPedidosEntregados()
            repartidos2 = topRepartidor.getCantidadPedidosEntregados()
            if (repartidos1 > repartidos2):
                topRepartidor = repartidor
        return topRepartidor
	
    def getMeseroConMasPropinas(self):
		#Mesero vacio para que el metodo funcione
        topMeseroPropinas
		#Loop para encontrar al mesero con mas propinas
        for mesero in mesero.getMeseros():
			#Comparamos todos los meseros en la lista de meseros
            Propinas1 = topMeseroPropinas.totalPropinas()
            Propinas2 = mesero.totalPropinas()
            if (Propinas2 > Propinas1):
                topMeseroPropinas = mesero
	
        return topMeseroPropinas

    def promedioPropinasMeseros(self):
        cantidad = 0
        propinas = 0		
        for mesero in mesero.getMeseros():
            cantidad += 1
            propinas += mesero.totalPropinas()
        return propinas / cantidad
	
    def promedioPedidosRepartidores(self):
        cantidad = 0
        pedidos = 0
        for repartidor in repartidor.getRepartidores():
            cantidad += 1
            pedidos += repartidor.getCantidadPedidosEntregados()
        return pedidos / cantidad

	#Este es el metodo para mostrar todas las estadisticas que querramos implementar juntas.
    def estadisticasRestaurante(self):
        topMesero = self.getMeseroConMasPropinas()
        topRepartidor = self.getRepartidorConMasPedidos()
        return "El mesero con mas propinas es: " + topMesero.getNombre() + " con $" + topMesero.totalPropinas() + " Recibido en propinas." + "\n" + "El repartidor con mas pedidos repartidos es: " + topRepartidor.getNombre() + " con " + topRepartidor.getCantidadPedidosEntregados() + " Pedidos entregados." + "\n" + "En promedio un mesero recibe $" + self.promedioPropinasMeseros() + " en propinas en el restaurante." + "\n" + "En promedio un mesero ha entregado " + self.promedioPedidosRepartidores() + " pedidos a clientes del restaurante."


	#Metodo chequear pedido

    def chequearPedido(self, pedido):
        if (self.verificarProductos(pedido) and self.verificarPersonal(pedido)):
            return True
        return False

	#Agregar un pedido al historial
    def agregarPedido(self, pedido):
        if(not self.__pedidos.contains(pedido)):
            self.__pedidos.add(pedido)
            return "Pedido anadido con exito"
        else:
            return "ERROR: El pedido ya se encuentra anadido"