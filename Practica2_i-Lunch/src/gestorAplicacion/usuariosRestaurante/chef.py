from gestorAplicacion.gestionRestaurante.estadoPedido import EstadoPedido

from gestorAplicacion.usuariosRestaurante.empleado import Empleado

class Chef(Empleado):

    # Atributos estaticos

    _chefs = []

    # Constructor

    def __init__(self, cedula = 0, nombre = "", disponibilidad = False, salario = 0, restaurante = None, cargoEnCocina = "", especialidad = ""):
        super().__init__(cedula, nombre, "Chef", disponibilidad, salario, restaurante)

        self._cargoEnCocina = cargoEnCocina
        self._especialidad = especialidad

        Empleado._empleados.append(self)
        Chef._chefs.append(self)

    # Getters y Setters

    def getCargoEnCocina(self):
        return self._cargoEnCocina

    def setCargoEnCocina(self, cargoEnCocina):
        self._cargoEnCocina = cargoEnCocina
    
    def getEspecialidad(self):
        return self._especialidad

    def setEspecialidad(self, especialidad):
        self._especialidad = especialidad
    
    @classmethod
    def getChefs(cls):
        return cls._chefs

    @classmethod
    def setChefs(cls, chefs):
        cls._chefs = chefs

    # Metodos

    # Simulacion de la preparacion completa de un pedido por parte de un chef
    def prepararProducto(self, pedido):
        for i in range(0, len(pedido.getProductos())):
            pedido.getProductos()[i].setEstado(True)
    
    # Funcionalidad revisar pedido antes de ser despachado

    def revisionPedido(self,pedido):
        # Solo puede revisar un Chef en jefe
        if self._cargoEnCocina == "Chef en jefe":
            cuenta = 0

            # Verificar si cada producto esta preparado
            for i in range(0, len(pedido.getProductos())):
                if pedido.getProductos()[i].getEstado() == True:
                    cuenta += 1
            
            # Solo poner el pedido como listo si todos los productos fueron preparados
            if cuenta == len(pedido.getProductos()):
                pedido.setEstado(EstadoPedido.LISTO.value)
    
    # Implementacion de la interfaz

    def informacion(self):
        info = f"El Chef {self._nombre} con C.C. {self._cedula} trabaja en el restaurante {self._restaurante.getNombre()}.\n" \
               f"Tiene un salario de: ${self._salario}.\n" \
               f"Tiene el cargo {self._cargo} en la cocina y esta especializado en {self.especialidad}.\n"
        
        if self._disponibilidad:
            return info + "Esta disponible actualmente."
        else:
            return info + "No esta disponible actualmente."