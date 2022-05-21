package uiMain;

import java.io.IOException;
import java.util.ArrayList;
import java.util.Scanner;

import baseDatos.*;
import gestorAplicacion.gestionRestaurante.*;
import gestorAplicacion.usuariosRestaurante.*;

public class Consola {

	static Scanner sc = new Scanner(System.in);
	
	//Se crean metodos para utilizar el Scanner de Java.
	static int readInt() {
		return sc.nextInt();
	}

	static String readString() {
		return sc.nextLine();
	}

	static double readDouble() {
		return sc.nextDouble();
	}
	
	// Administrador que maneja la app
	static Administrador admin;
	static Restaurante restaurante;

	// Metodo main
	public static void main(String[] args) {
		//Deserializa todos los objetos.
		Deserializador.deserializarTodo();
		
		// Datos predeterminados
		inicializar();
		
		// Administrador que maneja la app
		admin = Administrador.getAdministradores().get(0);
		restaurante = admin.getRestaurante();
		
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
		
		System.out.println("----------------------------------------------------------------------------------------------------\n");
		System.out.println("Bienvenido a i-Lunch: " + admin.getNombre());
		System.out.println("Restaurante: " + restaurante.getNombre() + "\n");
		
		String opcion = "0";
		
		do {
			System.out.println("----------------------------------------------------------------------------------------------------");
			System.out.println("Escribe el numero asociado a la funcion que quieres realizar\n");
			
			System.out.println("Funciones principales del sistema\n");
			
			System.out.println(" 1. Ver informacion del Restaurante"); 
			System.out.println(" 2. Gestionar Menu");
			System.out.println(" 3. Gestionar Pesonal");
			System.out.println(" 4. Cola de pedidos");
			System.out.println(" 5. Pagar nomina\n");
			
			System.out.println("Funciones extra del sistema\n");
			
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
				
			case "5": // Emma
				/* 1. Pagar a un empleado
				 * 2. Pagar a todos los empleados*/
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
				break;
			}
			
		} while (!opcion.equals("8"));

	}
	
	// Genera datos predeterminados si no existe ninguno
	// Se puede hacer que se pidan los datos. Pero es algo extra
	
	public static void inicializar() {
		Restaurante restaurante = null;
		ArrayList<Empleado> empleados = new ArrayList<Empleado>();
		ArrayList<Producto> menu = new ArrayList<Producto>();
		ArrayList<Pedido> pedidos = new ArrayList<Pedido>();
		
		if (Administrador.getAdministradores().isEmpty())
			empleados.add(new Empleado(2, "Leo Messi", "Chef", true, 1000, restaurante));
			empleados.add(new Empleado(3, "CR7", "Repartidor", false, 1000, restaurante));
			
			menu.add(new Producto("Hamburguesa", "Mejor que la Cangreburger y a un menor precio", 5, true, false, 25));
			menu.add(new Producto("Pizza sin pinha", "Como debe de ser", 7, true, false, 10));
			menu.add(new Producto("Sushi", "Su chicharron", 3, false, false, 50));
			
			restaurante = new Restaurante("El Mejor Restaurante de la Facultad", 987654, 300, "En la mejor mesa de la Facultad", "lamejormesa@gmail.com", true, 4,  empleados,  menu,  pedidos, 0);
			new Administrador(1 , "Fulanito de Tal", true, 0, restaurante);
	}
	
	// Submenu de la opcion "2. Gestionar Menu"
	static void submenu2() {
		String opcion;
		do {
			System.out.println("\n--------------------------------------------------");
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
				
				break;
			case "3":
				// Eliminar producto
				System.out.println("Eliminar producto\n");
				
				System.out.println("Ingrese el ID del producto a eliminar: ");
				String idSt = readString();
				
				System.out.println(admin.eliminarProducto(idSt));
				break;
			case "4":
				// Actualizar producto
				submenu2_4();
				break;
			case "5":
				break;
			default:
				System.out.println("\nLa opcion ingresada no es valida. Por favor intentelo nuevamente"); //Mensaje de control para inputs invalidos.
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
			return;
		}
		
		if(id >= restaurante.getMenu().size()) {
			System.out.println("El ID ingresado no es valido. Por favor intentelo nuevamente");
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
			System.out.println(" 7. Volver al menu principal\n");
			
			opcion = readString();

			switch (opcion) {
			case "1":
				// Nombre
				System.out.println("Ingrese el nuevo nombre del producto: ");
				String nombre = readString();
				
				System.out.println(admin.actualizarNombreProducto(id, nombre));
				return;
			case "2":		
				// Descripcion
				System.out.println("Ingrese la nueva descripcion del producto: ");
				String descripcion = readString();
				
				System.out.println(admin.actualizarDescripcionProducto(id, descripcion));
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
				return;
			case "7":
				break;
			default:
				System.out.println("\nLa opcion ingresada no es valida. Por favor intentelo nuevamente"); //Mensaje de control para inputs invalidos.
				break;
			}
		} while(!opcion.equals("7"));
	}
}

