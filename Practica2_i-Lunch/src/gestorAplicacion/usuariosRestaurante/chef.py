from re import T
from sympy import true
from gestorAplicacion.gestionRestaurante.estadoPedido import EstadoPedido
from gestorAplicacion.gestionRestaurante.pedido import Pedido
from gestorAplicacion.usuariosRestaurante.empleado import Empleado

class Chef(Empleado):

    # Atributos estaticos

    _chefs = []

    # Constructor

    def __init__(self, cedula = 0, nombre = "", disponibilidad = False, salario = 0, restaurante = None, cargoEnCocina = " ", especialidad = " "):
        self._cargoEnCocina = cargoEnCocina
        self._especialidad = especialidad
        super().__init__(cedula, nombre, "Mesero", disponibilidad, salario, restaurante)
        

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

    def prepararProducto(self, pedido):
        for i in range(0, len(pedido.getProductos)):
            pedido.getProductos.get(i).setEstado(True)
    
    def revisionPedido(self,pedido):
        if self._cargoEnCocina == "Chef en jefe":
            cuenta = 0
            for i in range(0, len(pedido.getProductos)):
                if pedido.getProductos.get(i).getEstado() == True:
                    cuenta += 1
            
            if cuenta == len(pedido.getProductos()):
                pedido.setEstado(EstadoPedido.LISTO.value)




    # Implementacion de la interfaz

    def informacion(self):
        info = f"El Chef {self._nombre} con C.C. {self._cedula} trabaja en el restaurante {self._restaurante.getNombre()}. Tiene un salario de: ${self._salario}, tiene el cargo {self._cargo} en la cocina y esta especializado en {self.especialidad}."
        
        if self._disponibilidad:
            return info + "Está disponible actualmente."
        else:
            return info + "No está disponible actualmente."