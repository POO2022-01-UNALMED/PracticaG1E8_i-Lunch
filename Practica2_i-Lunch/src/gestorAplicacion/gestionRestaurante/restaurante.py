from gestorAplicacion.usuariosRestaurante.repartidor import Repartidor
from gestorAplicacion.usuariosRestaurante.mesero import Mesero

class Restaurante:
    
    # Atributos estaticos

    _restaurantes = []

    # Constructor

    def __init__(self, nombre = "", nit = 0, telefono = 0, direccion = "", email = "", abierto = False, capacidad = 0, balanceCuenta = 0):
        self._nombre = nombre
        self._nit = nit 
        self._telefono = telefono
        self._direccion = direccion
        self._email = email
        self._abierto = abierto
        self._capacidad = capacidad
        self._balanceCuenta = balanceCuenta

        self._empleados = []
        self._menu = []
        self._pedidos = []
        
        Restaurante._restaurantes.append(self)
   
    # Getters y Setters

    def getNombre(self):
        return self._nombre

    def setNombre(self, nombre):
        self._nombre = nombre
    
    def getNit(self):
        return self._nit

    def setNit(self, nit):
        self._nit = nit

    def getTelefono(self):
        return self._telefono

    def setTelefono(self, telefono):
        self._telefono = telefono

    def getDireccion(self):
        return self._direccion
    
    def setDireccion(self, direccion):
        self._direccion = direccion

    def getEmail(self):
        return self._email
    
    def setEmail(self, email):
        self._email = email
    
    def getAbierto(self):
        return self._abierto

    def setAbierto(self, abierto):
        self._abierto = abierto
    
    def getCapacidad(self):
        return self._capacidad
    
    def setCapacidad(self, capacidad):
        self._capacidad=capacidad
    
    def getEmpleados(self):
        return self._empleados
    
    def setEmpleados(self, empleados):
        self._empleados = empleados
    
    def getMenu(self):
        return self._menu
    
    def setMenu(self, menu):
        self._menu= menu

    def getPedidos(self):
        return self._pedidos
    
    def setPedidos(self, pedidos):
        self._pedidos = pedidos
    
    def getBalanceCuenta(self):
        return self._balanceCuenta

    def setBalanceCuenta(self, balanceCuenta):
        self._balanceCuenta = balanceCuenta  
    
    @classmethod
    def getRestaurantes(cls):
        return cls._restaurantes

    @classmethod
    def setRestaurantes(cls, restaurantes):
        cls._restaurantes = restaurantes

    # Metodos

    def verificarPersonal(self, pedido):
		# Comprobamos si existe un chef en el restaurante
        chef = False

        for empleado in self._empleados:
            if empleado.getCargo() == "Chef":
                chef = True
			
		# Identificar el tipo de pedido
        if pedido.getTipo() == "A domicilio": 
			# Rectificar el personal del restaurante y comprobar que haya el necesario para el tipo de pedido
            repartidor = False

            for empleado in self._empleados:
                if empleado.getCargo() == "Repartidor":
                    repartidor = True
			
            # Si si no hay alguno no se puede realizar
            if not chef and not repartidor:
                return False
		
        if pedido.getTipo() == "Para consumir en la tienda" or pedido.getTipo() == "Para llevar":
			# Rectificar el personal del restaurante y comprobar que haya el necesario para el tipo de pedido
            mesero = False
            
            for empleado in self._empleados:
                if (empleado.getCargo() == "mesero"):
                    mesero = True

			# Si si no hay alguno no se puede realizar
            if (not chef and not mesero):
                return False

		# Si todo es aceptable se realiza el pedido
        return True
    
    # Determina si el restaurante posee los productos solicitados en un pedido
    def verificarProductos(self, pedido):
        for demanda in pedido.getProductos():
            existe = False
            cantidad = False
            disponible = False
            
            for oferta in self._menu:
                if demanda.getNombre() == oferta.getNombre():
                    existe = True
                    disponible = oferta.getDisponibilidad()

                    if oferta.getCantidad() >= demanda.getCantidad():
                        cantidad = True
                        if not existe or not cantidad or not disponible:
                            return False
        
        return True

    def chequearPedido(self, pedido):
        if (self.verificarProductos(pedido) and self.verificarPersonal(pedido)):
            return True
        
        return False

    # Agregar un pedido al historial del restaurante
    def agregarPedido(self, pedido):
        if self._pedidos.count(pedido)==0:
            self._pedidos.append(pedido)

            return f"Pedido #{pedido.getCodigo()} anadido con exito al historial"
        else:
            return f"El pedido #{pedido.getCodigo()} ya se encuentra en el historial"
	
    # Funcionalidad estadisticas

    # Busqueda del repartidor con mas pedidos
    def  getRepartidorConMasPedidos(self):		
        # Repartidor vacio para que el metodo funcione
        topRepartidor = Repartidor(cedula = 0, nombre = "Nadie", disponibilidad = False, salario = 0, poseeVehiculo = False, placa = "", tipoVehiculo = "")
        
        # Loop para encontrar el repartidor con mas pedidos repartidos
        for repartidor in Repartidor.getRepartidores():
			# Comparamos cada repartidor en la lista de repartidores
            repartidos1 = repartidor.getCantidadPedidosEntregados()
            repartidos2 = topRepartidor.getCantidadPedidosEntregados()
            
            if repartidos1 > repartidos2:
                topRepartidor = repartidor
        
        return topRepartidor
	
    # Busqueda del mesero con mas propinas
    def getMeseroConMasPropinas(self):
		# Mesero vacio para que el metodo funcione
        topMeseroPropinas = Mesero(cedula = 0, nombre = "Nadie", disponibilidad = False, salario = 0)

		# Loop para encontrar al mesero con mas propinas
        for mesero in Mesero.getMeseros():
			#Comparamos todos los meseros en la lista de meseros
            propinas1 = topMeseroPropinas.totalPropinas()
            propinas2 = mesero.totalPropinas()
            
            if propinas2 > propinas1:
                topMeseroPropinas = mesero
	
        return topMeseroPropinas

    # Promedio de propinas que recibe un mesero
    def promedioPropinasMeseros(self):
        cantidad = 0
        propinas = 0

        for mesero in Mesero.getMeseros():
            cantidad += 1
            propinas += mesero.totalPropinas()
        
        return propinas / cantidad
	
    # Promedio de pedidos de los que se encarga un repartidor
    def promedioPedidosRepartidores(self):
        cantidad = 0
        pedidos = 0
        
        for repartidor in Repartidor.getRepartidores():
            cantidad += 1
            pedidos += repartidor.getCantidadPedidosEntregados()
        
        return pedidos / cantidad

	# Mostrar todas las estadisticas juntas.
    def estadisticasRestaurante(self):
        topMesero = self.getMeseroConMasPropinas()
        topRepartidor = self.getRepartidorConMasPedidos()

        return f"El mesero con mas propinas es: {topMesero.getNombre()} con ${topMesero.totalPropinas()} recibido en propinas.\n" \
               f"El repartidor con mas pedidos repartidos es: {topRepartidor.getNombre()} con {topRepartidor.getCantidadPedidosEntregados()} pedidos entregados.\n" \
               f"En promedio un mesero recibe ${round(self.promedioPropinasMeseros(),2)} en propinas en el restaurante.\n" \
               f"En promedio un repartidor ha entregado {round(self.promedioPedidosRepartidores(),2)} pedidos a clientes del restaurante."