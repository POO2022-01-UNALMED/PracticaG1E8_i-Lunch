package uiMain;

import java.util.ArrayList;
import java.util.Scanner;

import baseDatos.*;
import gestorAplicacion.gestionRestaurante.*;
import gestorAplicacion.usuariosRestaurante.*;

public class Consola {
	static Scanner sc = new Scanner(System.in);

	// Leer int	
	static int readInt() {
		return sc.nextInt();
	}

	// Leer string
	static String readString() {
		return sc.nextLine();
	}

	// Leer double	
	static double readDouble() {
		return sc.nextDouble();
	}
	
	// Metodo util para sacar ints randoms
	static int randInt(int min, int max) {
		return min + (int)(Math.random() * ((max - min) + 1));
	}
	
	// Metodo util para sacar bools randoms
	static boolean randBool() {
		int rand = randInt(0, 1);
		if(rand == 0) {
			return true;
		} else {
			return false;
		}
	}
	
	// Metodo util para sacar strings randoms de una lista
	static String randString(String[] lista) {
		return lista[randInt(0, lista.length-1)];
	}
	
	// Metodo de "Presiona enter para continuar
	static void pressEnter() {
		System.out.println("\nPresiona Enter para continuar...");
		readString();
	}
	
	// Usado en el inicio de la app
	private static void pressEnter(boolean ingreso) {
		if(ingreso) {
			System.out.println("\nPresiona Enter para ingresar...");
			readString();
		}
	}

	// Administrador que maneja la app
	static Administrador admin;
	static Restaurante restaurante;
	
	// Metodo main
	public static void main(String[] args) {
		//Deserializa todos los objetos.
		Deserializador.deserializarTodo();
		
		//Mensaje de bienvenida
		System.out.println(
				  "                                ,                                                                   \r\n"
				+ "                        @@@@@@@@@@#                                                                 \r\n"
				+ "                    @@@@@  @@@@@@@                                                                  \r\n"
				+ "                  @@@@    (@@@@@@,                                                                  \r\n"
				+ "    /@@@@       ,@@@@     @@@@@@@                                                       @@@@@       \r\n"
				+ "    @@@@@(      @@@@@    &@@@@@@                                                       @@@@@,       \r\n"
				+ "                 @@@@    @@@@@@@                                                       @@@@@        \r\n"
				+ "   @@@@@                @@@@@@@    @@@@@,   @@@@@*    @@@@@@@@@@@@@       @@@@@&@@@   @@@@@@@@@@@@@ \r\n"
				+ "  &@@@@&                @@@@@@@    @@@@@    @@@@@    @@@@@@   @@@@@     @@@@@   %@@  *@@@@@/  @@@@@@\r\n"
				+ "  @@@@@                @@@@@@@    @@@@@.   @@@@@.   ,@@@@@    @@@@@    @@@@@         @@@@@    @@@@@ \r\n"
				+ " @@@@@#   @@@@@@@@@    @@@@@@@   ,@@@@@   .@@@@@    @@@@@    @@@@@    @@@@@         %@@@@@    @@@@@ \r\n"
				+ " @@@@@                @@@@@@@    @@@@@    @@@@@    %@@@@@    @@@@@   #@@@@@         @@@@@    @@@@@  \r\n"
				+ "%@@@@@                @@@@@@&    @@@@@   @@@@@@   @@@@@@    @@@@@#  ,@@@@@@      @@@@@@@@    @@@@@  \r\n"
				+ " @@@@@@@             @@@@@@@     @@@@@@@@ #@@@@@@@&@@@@@     @@@@@@@@ ,@@@@@@@@@@  @@@@@     @@@@@@@\r\n"
				+ "                    *@@@@@@@@,                                                                      \r\n"
				+ "                          @@@@@@@@*                                                                 \r\n"
				+ "                              @@@@@@@@@@                                                            \r\n"
				+ "                                 @@@@@@@@@@@@@@.                                                    \r\n"
				+ "                                     @@@@@@@@@                                                      \r\n"
		);
		
		// Generar los datos iniciales
		inicializar();
		
		// Administrador que maneja la app
		admin = Administrador.getAdministradores().get(0);
		restaurante = admin.getRestaurante();
		
		System.out.println("----------------------------------------------------------------------------------------------------\n");
		
		System.out.println("Bienvenido de nuevo a i-Lunch " + admin.getNombre());
		System.out.println("Restaurante: \"" + restaurante.getNombre() + "\"");
		pressEnter(true);
		
		String opcion = "0";
		
		do {
			System.out.println("----------------------------------------------------------------------------------------------------");
			System.out.println("\nEscribe el numero asociado a la funcion que quieres realizar\n");
			
			System.out.println("Gestion del restaurante:\n");
			
			System.out.println(" 1. Ver informacion del Restaurante"); 
			System.out.println(" 2. Gestionar Menu");
			System.out.println(" 3. Gestionar Pesonal");
			System.out.println(" 4. Cola de pedidos");
			System.out.println(" 5. Pagar nomina\n");
			
			System.out.println("Funciones extra del sistema:\n");
			
			System.out.println(" 6. Simular Pedido");
			System.out.println(" 7. Gestionar Clientela");
			System.out.println(" 8. Guardar y Salir\n");

			System.out.println("Elija una opcion: ");
			
			try {
				opcion =  readString();
			} catch (Exception e) {
				opcion = "0";
			}
			
			switch (opcion) {

			case "1": // David
				// Muestra la info basica del restaurante
				/* 1. empleados
				 * 2. productos
				 * 3. historial pedidos
				 * 4. balance de cuenta
				 * 5. estadisticas (Funcionalidad)
				 * 6. Volver al menu principal*/
				break;
				
			case "2":
				submenu2();
				break;
				
			case "3": //Jero
				/* 1. Ver personal
				 * 2. Contratar empleado
				 * 2.1 Manual
				 * 2.2 Automatico
				 * 3. Despedir empleado 
				 * 4. Volver al menu principal*/
				break;
				
			case "4": // Apa
				// Se muestran todos los pedidos en espera
				/* 1. Aceptar
				 * 2. Rechazar */
				break;
				
			case "5": 
				submenu5();
				break;
			
			case "6": // Apa
				// Mensaje de control
				// Cliente, codigo pedido
				break;	
				
			case "7": // Jero
				// 1. Ver clientes
				// 2. Crear cliente
				// 2.1 Manual
				// 2.2 Automatico
				break;	
			
			case "8": // David
				//Serializador
				break;
				
			default:
				System.out.println("\nLa opcion ingresada no es valida. Por favor intentelo nuevamente"); //Mensaje de control para inputs invalidos.
				pressEnter();
				break;
			}
			
		} while (!opcion.equals("8"));

	}
	
	// Registro si es la primera vez que se usa la app. Pregunta datos del admin y restaurante y genera otros datos aleatroios
	public static void inicializar() {
		Restaurante restaurante = null;
		ArrayList<Empleado> empleados = new ArrayList<Empleado>();
		ArrayList<Producto> menu = new ArrayList<Producto>();
		ArrayList<Pedido> pedidos = new ArrayList<Pedido>();
		
		// Nombres aleatorios para empleados
		String[] nombresAleatorios = {"Yasemin Phillips",
		                              "Lavinia Banks",
		                              "Kodi Paine",
		                              "Phebe Beaumont",
		                              "Amba Bowman",
		                              "Mila-Rose Bartlett",
		                              "Alejandro Ventura",
		                              "Zavier Burns",
		                              "Rivka Cantu",
		                              "Anastasia Mckeown"};
		
		// Nombres aleatorios para productos
		String[] productosAleatorios = {"Pizza",
									    "Hamburguesa",
									    "Bandeja Paisa",
									    "Sushi",
									    "Empanadas",
									    "Pollo frito",
									    "Spaghetti",
									    "Paella",
									    "Tacos"};
		
		// Tipos de cargos en la cocina
		String[] cargosEnCocina = {"Chef en jefe",
								   "Chef ejecutivo",
								   "Chef de cocina",
								   "Chef repostero",
								   "Lavaplatos"};
		
		// Tipos de especialidades de chefs
		String[] especialidadesChefs = {"Saucier",
										"Poissonnier",
										"Rotisseur",
										"Grillardin",
										"Friturier",
										"Entremetier",
										"Tournant",
										"Garde Manger",
										"Boucher",
										"Patissier"};
		
		// Tipos de vehiculos
		String[] tiposVehiculos = {"Automovil",
								   "Motoicicleta",
								   "Bicicleta",
								   "Cuatrimoto",
								   "Monopatin",
								   "Helicoptero",
								   "Dirigible",
								   "Globo aerostatico",
								   "Tanque de guerra",
								   "Excavadora industrial",
								   "Tractor"};
		
		if (Administrador.getAdministradores().isEmpty()) {
			// Registro admin y restaurante
			System.out.println("----------------------------------------------------------------------------------------------------\n");
			
			System.out.println("Bienvenido a i-Lunch, por favor ingrese su nombre: ");
			String nombreAdmin = readString();
			
			System.out.println("Por favor, ingresa los datos del restaurante que quieres registrar: ");
			System.out.println("Nombre: ");
			String nombreRestaurante = readString();
			System.out.println("Email: ");
			String emailRestaurante = readString();
			System.out.println("Direccion: ");
			String direccionRestaurante = readString();
			
			System.out.println("\n¡Registro completado con exito!\n");
			
			restaurante = new Restaurante(nombreRestaurante, randInt(100000, 999999), randInt(100000, 999999), direccionRestaurante, emailRestaurante, true, randInt(1, 20),  empleados,  menu,  pedidos, randInt(1000, 10000));
			new Administrador(0 , nombreAdmin, true, randInt(500, 2000), restaurante);
			
			// Generar de 1 a 3 empleados random de cada tipo
			int numEmpleados = randInt(1, 3);
			
			for(int i=0;i<numEmpleados*3; i++) {
				if(i<3) {
					empleados.add(new Repartidor(i+1, randString(nombresAleatorios), randBool(), randInt(400, 1200), restaurante, randBool(), "ABC-"+randInt(100,999) , randString(tiposVehiculos)));
				} else if(i<6) {
					empleados.add(new Mesero(i+1, randString(nombresAleatorios), randBool(), randInt(400, 1200), restaurante));
				} else {
					empleados.add(new Chef(i+1, randString(nombresAleatorios), randBool(), randInt(400, 1200), restaurante, randString(cargosEnCocina), randString(especialidadesChefs)));
				}
			}
			
			// Generar de 1 a 10 productos random
			int numProductos = randInt(1, 10);
			
			for(int i=0; i<numProductos; i++) {
				menu.add(new Producto(randString(productosAleatorios), "Lorem ipsum dolor sit amet, consectetur adipiscing elit. Duis nec ultrices dui, ut ultricies leo.", randInt(2, 30), randBool(), randBool(), randInt(1, 50)));
			}
			
			restaurante.setEmpleados(empleados);
			restaurante.setMenu(menu);
		}
	}
	
	// Submenu de la opcion "2. Gestionar Menu"
	static void submenu2() {
		String opcion;
		do {
			System.out.println("\n----------------------------------------------------------------------------------------------------");
			System.out.println("Gestionar Menu\n");
			
			System.out.println(" 1. Ver menu"); 
			System.out.println(" 2. Crear producto");
			System.out.println(" 3. Eliminar producto");
			System.out.println(" 4. Actualizar producto");
			System.out.println(" 5. Volver al menu principal\n");

			opcion = readString();

			switch (opcion) {
			case "1":
				// Ver menu
				System.out.println("\nMenu del restaurante:");
				
				for (int i = 0; i < restaurante.getMenu().size(); i++) {
					Producto producto = restaurante.getMenu().get(i);
					System.out.println("\nID: " + i);
					System.out.println(producto.toString());
				}
				pressEnter();
				break;
			case "2":		
				// Crear producto
				System.out.println("Crear producto\n");
				
				System.out.println("Ingrese el nombre del producto: ");
				String nombre = readString();
				
				System.out.println("Ingrese la descripcion del producto: ");
				String descripcion = readString();
				
				System.out.println("Ingrese el precio del producto: ");
				String precioSt = readString();
				int precio;
				try {
					precio = Integer.parseInt(precioSt);
				} catch (Exception e) {
					precio = 0;
				}
				
				System.out.println("¿Esta disponible? (1: True): ");
				String dispSt = readString();
				boolean disponibilidad;
				if(dispSt.equals("1")) {
					disponibilidad = true;
				} else {
					disponibilidad = false;
				}
				
				System.out.println("¿Tiene restriccion de edad? (1: True): ");
				String restSt = readString();
				boolean restriccion;
				if(restSt.equals("1")) {
					restriccion = true;
				} else {
					restriccion = false;
				}
				
				System.out.println("Ingrese la cantidad disponible actualmente: ");
				String cantSt = readString();
				int cantidad;
				try {
					cantidad = Integer.parseInt(cantSt);
				} catch (Exception e) {
					cantidad = 0;
				}
				
				System.out.println(admin.crearProducto(nombre, descripcion, precio, disponibilidad, restriccion, cantidad));
				pressEnter();
				break;
			case "3":
				// Eliminar producto
				System.out.println("Eliminar producto\n");
				
				System.out.println("Ingrese el ID del producto a eliminar: ");
				String idSt = readString();
				
				System.out.println(admin.eliminarProducto(idSt));
				pressEnter();
				break;
			case "4":
				// Actualizar producto
				submenu2_4();
				break;
			case "5":
				break;
			default:
				System.out.println("\nLa opcion ingresada no es valida. Por favor intentelo nuevamente"); //Mensaje de control para inputs invalidos.
				pressEnter();
				break;
			}
		} while(!opcion.equals("5"));
	}
	
	// Submenu de la opcion "4. Gestionar Menu" del submenu "2. Gestionar Menu"
	static void submenu2_4() {
		System.out.println("Actualizar producto\n");
		
		System.out.println("Ingrese el ID del producto a actualizar: ");
		String idSt = readString();
		int id;
		try {
			id = Integer.parseInt(idSt);
		} catch (Exception e) {
			System.out.println("El ID ingresado no es valido. Por favor intentelo nuevamente");
			pressEnter();
			return;
		}
		
		if(id >= restaurante.getMenu().size()) {
			System.out.println("El ID ingresado no es valido. Por favor intentelo nuevamente");
			pressEnter();
			return;
		}
		
		String opcion;
		do {
			System.out.println("¿Que atributo del producto " + restaurante.getMenu().get(id).getNombre() + " quieres editar?\n");
			
			System.out.println(" 1. Nombre"); 
			System.out.println(" 2. Descripcion");
			System.out.println(" 3. Precio");
			System.out.println(" 4. Restriccion");
			System.out.println(" 5. Disponibilidad");
			System.out.println(" 6. Cantidad");
			System.out.println(" 7. Volver a \"Gestionar Menu\"\n");
			
			opcion = readString();

			switch (opcion) {
			case "1":
				// Nombre
				System.out.println("Ingrese el nuevo nombre del producto: ");
				String nombre = readString();
				
				System.out.println(admin.actualizarNombreProducto(id, nombre));
				pressEnter();
				return;
			case "2":		
				// Descripcion
				System.out.println("Ingrese la nueva descripcion del producto: ");
				String descripcion = readString();
				
				System.out.println(admin.actualizarDescripcionProducto(id, descripcion));
				pressEnter();
				return;
			case "3":
				// Precio
				System.out.println("Ingrese el nuevo precio del producto: ");
				String precioSt = readString();
				int precio;
				try {
					precio = Integer.parseInt(precioSt);
				} catch (Exception e) {
					precio = 0;
				}
				
				System.out.println(admin.actualizarPrecioProducto(id, precio));
				pressEnter();
				return;
			case "4":
				// Restriccion
				System.out.println("¿El tiene restriccion de edad?: ");
				String restSt = readString();
				boolean restriccion;
				if(restSt.equals("1")) {
					restriccion = true;
				} else {
					restriccion = false;
				}
				
				System.out.println(admin.actualizarRestriccionProducto(id, restriccion));
				pressEnter();
				return;
			case "5":
				// Disponibilidad
				System.out.println("¿El producto sigue disponible?: ");
				String dispSt = readString();
				boolean disponibilidad;
				if(dispSt.equals("1")) {
					disponibilidad = true;
				} else {
					disponibilidad = false;
				}
				
				System.out.println(admin.actualizarDisponibilidadProducto(id, disponibilidad));
				pressEnter();
				return;
			case "6":
				// Cantidad
				System.out.println("Ingrese la nueva cantidad disponible del producto: ");
				String cantSt = readString();
				int cantidad;
				try {
					cantidad = Integer.parseInt(cantSt);
				} catch (Exception e) {
					cantidad = 0;
				}
				
				System.out.println(admin.actualizarCantidadProducto(id, cantidad));
				pressEnter();
				return;
			case "7":
				break;
			default:
				System.out.println("\nLa opcion ingresada no es valida. Por favor intentelo nuevamente"); //Mensaje de control para inputs invalidos.
				pressEnter();
				break;
			}
		} while(!opcion.equals("7"));
	}
	
	// Submenu de la opcion "5. Pagar nomina"
	static void submenu5() {
	
		String opcion;
		do {
			System.out.println("\n----------------------------------------------------------------------------------------------------");
			System.out.println("Pagar nomina\n");
			
			System.out.println("Balance de cuenta: $" + restaurante.getBalanceCuenta() +"\n");
			
			System.out.println(" 1. Pagar a un empleado en especifico"); 
			System.out.println(" 2. Pagar a todos los empleados");
			System.out.println(" 3. Volver al menu principal\n");

			opcion = readString();

			switch (opcion) {
			case "1":
				// Pagar a un empleado en especifico
				System.out.println("Ingrese el ID del empleado: ");
				String idSt = readString();
				int id;
				try {
					id = Integer.parseInt(idSt);
				} catch (Exception e) {
					id = 0;
				}
				
				System.out.println(admin.pagoNomina(id));
				pressEnter();
				break;
			case "2":		
				// Pagar a todos los empleados
				System.out.println(admin.pagoNomina());
				pressEnter();
				break;
			case "3":
				break;
			default:
				System.out.println("\nLa opcion ingresada no es valida. Por favor intentelo nuevamente"); //Mensaje de control para inputs invalidos.
				pressEnter();
				break;
			}
		} while(!opcion.equals("3"));
	}
}

