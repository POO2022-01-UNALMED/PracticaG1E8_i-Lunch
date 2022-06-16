from random import randint, choice

from gestorAplicacion.datosAleatorios import nombresAleatorios, randbool, randPlaca, tiposVehiculos, cargosEnCocina, especialidadesChefs, productosAleatorios, generarEmail, randDireccion

from gestorAplicacion.gestionRestaurante.restaurante import Restaurante
from gestorAplicacion.gestionRestaurante.producto import Producto

from gestorAplicacion.usuariosRestaurante.administrador import Administrador
from gestorAplicacion.usuariosRestaurante.chef import Chef
from gestorAplicacion.usuariosRestaurante.cliente import Cliente
from gestorAplicacion.usuariosRestaurante.mesero import Mesero
from gestorAplicacion.usuariosRestaurante.repartidor import Repartidor

# Si es la primera vez que se usa la aplicacion. Genera los datos necesarios para usar la app

def inicializar():
    if len(Administrador.getAdministradores()) == 0:
        restaurante = Restaurante("Teso's Food", randint(1000000000, 9999999999), randint(1000000000, 9999999999), "M9 Segundo piso", "poo@fuiciosos.com", True, randint(5, 20), randint(25000, 250000))
        administrador = Administrador(randint(1000000000, 9999999999), "Pepito Perez", True, randint(1000, 5000), restaurante)
        
        # Generar de 3 a 5 empleados random de cada tipo
        empleados = [administrador]

        for i in range(randint(3, 5)): # Repartidores
            empleados.append(Repartidor(randint(1000000000, 9999999999), choice(nombresAleatorios), True, randint(500, 2500), restaurante, randbool(), randPlaca(), choice(tiposVehiculos)))

        for i in range(randint(3, 5)): # Meseros
            empleados.append(Mesero(randint(1000000000, 9999999999), choice(nombresAleatorios), True, randint(500, 2500), restaurante))

        # Chef en jefe predeterminado
        empleados.append(Chef(randint(1000000000, 9999999999), choice(nombresAleatorios), True, randint(500, 2500), restaurante, "Chef en jefe", choice(especialidadesChefs)))

        for i in range(randint(2, 4)): # Chefs
            empleados.append(Chef(randint(1000000000, 9999999999), choice(nombresAleatorios), True, randint(500, 2500), restaurante, choice(cargosEnCocina), choice(especialidadesChefs)))

        restaurante.setEmpleados(empleados)

        # Generar de 5 a 10 productos random
        menu = []

        for i in range(5, 10):
            menu.append(Producto(choice(productosAleatorios), "Lorem ipsum dolor sit amet, consectetur adipiscing elit. Pellentesque feugiat.", randint(5, 30), True, randbool(), randint(25, 100)))

        restaurante.setMenu(menu)
        
        # Generar de 5 a 15 clientes random
        for i in range(randint(5, 15)):
            nombre = choice(nombresAleatorios)
            Cliente(nombre, generarEmail(nombre), randint(1000000000, 9999999999), randDireccion(), randint(18, 65))