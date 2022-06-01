package uiMain;

import java.util.ArrayList;
import java.util.InputMismatchException;
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

	// Metodo de "Presiona enter para continuar
	static void pressEnter() {
		System.out.println("\nPresiona Enter para continuar...");
		readString();
	}

	// Usado en el inicio de la app
	private static void pressEnter(boolean ingreso) {
		if (ingreso) {
			System.out.println("\nPresiona Enter para ingresar...");
			readString();
		}
	}

	// Administrador que maneja la app
	static Administrador admin;
	static Restaurante restaurante;

	// Metodo main
	public static void main(String[] args) {
		// Deserializa todos los objetos.
		Deserializador.deserializarTodo();

		// Mensaje de bienvenida
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
						+ "                                     @@@@@@@@@                                                      \r\n");

		// Generar los datos iniciales
		inicializar();

		// Administrador que maneja la app
		admin = Administrador.getAdministradores().get(0);
		restaurante = admin.getRestaurante();

		System.out.println(
				"----------------------------------------------------------------------------------------------------\n");

		System.out.println("\"" + admin.getNombre() + "\" Bienvenido de nuevo a i-Lunch");
		System.out.println("Restaurante: \"" + restaurante.getNombre() + "\"");
		pressEnter(true);

		String opcion = "0";

		do {
			System.out.println(
					"----------------------------------------------------------------------------------------------------");
			System.out.println("\nEscribe el numero asociado a la funcion que quieres realizar\n");

			System.out.println("Gestion del restaurante:\n");

			System.out.println(" 1. Ver informacion del Restaurante");
			System.out.println(" 2. Gestionar Menu");
			System.out.println(" 3. Gestionar Personal");
			System.out.println(" 4. Cola de pedidos");
			System.out.println(" 5. Pagar nomina\n");

			System.out.println("Funciones extra del sistema:\n");

			System.out.println(" 6. Simular Pedido");
			System.out.println(" 7. Gestionar Clientela");
			System.out.println(" 8. Guardar y Salir\n");

			System.out.println("Elija una opcion: ");

			try {
				opcion = readString();
			} catch (Exception e) {
				opcion = "0";
			}

			switch (opcion) {

			case "1": // David
				// Muestra la info basica del restaurante
				/*
				 * 1. empleados 2. productos 3. historial pedidos 4. balance de cuenta 5.
				 * estadisticas (Funcionalidad) 6. Volver al menu principal
				 */
				DaviMenu1();
				break;

			case "2":
				submenu2();
				break;

			case "3":
				submenu3();
				break;

			case "4":
				ArrayList<Pedido> listapedidos = Pedido.getPedidos();
				ArrayList<Integer> codPedidos = new ArrayList<Integer>();
				
				for (Pedido pedido : listapedidos) {
					if (pedido.getEstado().equals(estadoPedido.Enviado.toString())) {
						codPedidos.add(pedido.getCodigo());
					}
				}
				if (codPedidos.size() == 0) {
					System.out.println(
							"\n----------------------------------------------------------------------------------------------------\n");
					System.out.println("No hay pedidos en espera en este momento");
					pressEnter();
				} else {
					submenu4(codPedidos);
				}
				break;

			case "5":
				submenu5();
				break;

			case "6":
				// Mensaje de control
				Cliente cliente = Cliente.getClientes()
						.get(DatosAleatorios.randInt(0, Cliente.getClientes().size() - 1));
				Pedido pedido = admin.simularPedido(cliente);

				System.out.println(
						"\n----------------------------------------------------------------------------------------------------\n");
				System.out.println("Pedido recibido");
				System.out.println("Cliente: " + cliente.getNombre());
				System.out.println("Codigo pedido: " + pedido.getCodigo());
				pressEnter();

				// Cliente, codigo pedido
				break;

			case "7":
				// David
				// 1. Ver clientes
				// 2. Crear cliente
				// 2.1 Manual
				// 2.2 Automatico
				DaviMenu2();
				break;

			case "8": // Jero
				System.out.println(
						"\n----------------------------------------------------------------------------------------------------\n");
				System.out.println("Gracias por haber usado nuestra aplicacion! Vuelva pronto =)\n");
				Serializador.serializarTodo();
				break;

			default:
				System.out.println("\nLa opcion ingresada no es valida. Por favor intentelo nuevamente"); // Mensaje de
																											// control
																											// para
																											// inputs
																											// invalidos.
				pressEnter();
				break;
			}

		} while (!opcion.equals("8"));

	}

	// Registro si es la primera vez que se usa la app. Pregunta datos del admin y
	// restaurante y genera otros datos aleatroios
	public static void inicializar() {
		Restaurante restaurante = null;
		ArrayList<Empleado> empleados = new ArrayList<Empleado>();
		ArrayList<Producto> menu = new ArrayList<Producto>();
		ArrayList<Pedido> pedidos = new ArrayList<Pedido>();
		if (Administrador.getAdministradores().isEmpty()) {
			// Registro admin y restaurante
			System.out.println(
					"----------------------------------------------------------------------------------------------------\n");

			System.out.println("Bienvenido a i-Lunch, por favor ingrese su nombre: ");
			String nombreAdmin = readString();
			System.out.println("Ingrese su cedula: ");
			String ccAdminSt = readString();
			int ccAdmin;
			try {
				ccAdmin = Integer.parseInt(ccAdminSt);
			} catch (Exception e) {
				ccAdmin = 0;
			}

			System.out.println("Por favor, ingresa los datos del restaurante que quieres registrar: ");
			System.out.println("Nombre: ");
			String nombreRestaurante = readString();
			System.out.println("Email: ");
			String emailRestaurante = readString();
			System.out.println("Direccion: ");
			String direccionRestaurante = readString();

			System.out.println("\nRegistro completado con exito!\n");

			restaurante = new Restaurante(nombreRestaurante, DatosAleatorios.randInt(100000, 999999),
					DatosAleatorios.randInt(100000, 999999), direccionRestaurante, emailRestaurante, true,
					DatosAleatorios.randInt(1, 20), empleados, menu, pedidos, DatosAleatorios.randInt(1000, 10000));
			new Administrador(ccAdmin, nombreAdmin, true, DatosAleatorios.randInt(500, 2000), restaurante);

			// Generar de 1 a 3 empleados random de cada tipo
			int numEmpleados = DatosAleatorios.randInt(1, 3);

			for (int i = 0; i < numEmpleados * 3; i++) {
				if (i < 3) {
					empleados.add(new Repartidor(DatosAleatorios.randInt(100000, 999999),
							DatosAleatorios.randString(DatosAleatorios.nombresAleatorios), DatosAleatorios.randBool(),
							DatosAleatorios.randInt(400, 1200), restaurante, DatosAleatorios.randBool(),
							"ABC-" + DatosAleatorios.randInt(100, 999),
							DatosAleatorios.randString(DatosAleatorios.tiposVehiculos)));
				} else if (i < 6) {
					empleados.add(new Mesero(DatosAleatorios.randInt(100000, 999999),
							DatosAleatorios.randString(DatosAleatorios.nombresAleatorios), DatosAleatorios.randBool(),
							DatosAleatorios.randInt(400, 1200), restaurante));
				} else {
					empleados.add(new Chef(DatosAleatorios.randInt(100000, 999999),
							DatosAleatorios.randString(DatosAleatorios.nombresAleatorios), DatosAleatorios.randBool(),
							DatosAleatorios.randInt(400, 1200), restaurante,
							DatosAleatorios.randString(DatosAleatorios.cargosEnCocina),
							DatosAleatorios.randString(DatosAleatorios.especialidadesChefs)));
				}
			}

			// Generar de 1 a 10 productos random
			int numProductos = DatosAleatorios.randInt(1, 10);

			for (int i = 0; i < numProductos; i++) {
				menu.add(new Producto(DatosAleatorios.randString(DatosAleatorios.productosAleatorios),
						"Lorem ipsum dolor sit amet, consectetur adipiscing elit. Duis nec ultrices dui, ut ultricies leo.",
						DatosAleatorios.randInt(2, 30), DatosAleatorios.randBool(), DatosAleatorios.randBool(),
						DatosAleatorios.randInt(10, 50)));
			}

			restaurante.setEmpleados(empleados);
			restaurante.setMenu(menu);

			// Generar de 1 a 10 clientes random
			int numClientes = DatosAleatorios.randInt(1, 10);

			for (int i = 0; i < numClientes; i++) {
				new Cliente(DatosAleatorios.randInt(100000, 999999),
						DatosAleatorios.randString(DatosAleatorios.nombresAleatorios),
						"Calle " + DatosAleatorios.randInt(10, 99) + " #" + DatosAleatorios.randInt(10, 99) + "-"
								+ DatosAleatorios.randInt(10, 99),
						DatosAleatorios.randInt(18, 99), null, new ArrayList<Pedido>(), "cliente" + i + "@gmail.com");
			}
		}
	}

	// Submenu de la opcion "2. Gestionar Menu"
	static void submenu2() {
		String opcion;
		do {
			System.out.println(
					"\n----------------------------------------------------------------------------------------------------");
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
				if (dispSt.equals("1")) {
					disponibilidad = true;
				} else {
					disponibilidad = false;
				}

				System.out.println("¿Tiene restriccion de edad? (1: True): ");
				String restSt = readString();
				boolean restriccion;
				if (restSt.equals("1")) {
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

				System.out.println(
						admin.crearProducto(nombre, descripcion, precio, disponibilidad, restriccion, cantidad));
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
				System.out.println("\nLa opcion ingresada no es valida. Por favor intentelo nuevamente"); // Mensaje de
																											// control
																											// para
																											// inputs
																											// invalidos.
				pressEnter();
				break;
			}
		} while (!opcion.equals("5"));
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

		if (id >= restaurante.getMenu().size()) {
			System.out.println("El ID ingresado no es valido. Por favor intentelo nuevamente");
			pressEnter();
			return;
		}

		String opcion;
		do {
			System.out.println(
					"¿Que atributo del producto " + restaurante.getMenu().get(id).getNombre() + " quieres editar?\n");

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
				System.out.println("¿El tiene restriccion de edad? (1: True): ");
				String restSt = readString();
				boolean restriccion;
				if (restSt.equals("1")) {
					restriccion = true;
				} else {
					restriccion = false;
				}

				System.out.println(admin.actualizarRestriccionProducto(id, restriccion));
				pressEnter();
				return;
			case "5":
				// Disponibilidad
				System.out.println("¿El producto sigue disponible? (1: True): ");
				String dispSt = readString();
				boolean disponibilidad;
				if (dispSt.equals("1")) {
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
				System.out.println("\nLa opcion ingresada no es valida. Por favor intentelo nuevamente"); // Mensaje de
																											// control
																											// para
																											// inputs
																											// invalidos.
				pressEnter();
				break;
			}
		} while (!opcion.equals("7"));
	}

	static void submenu3() {
		String opcion;
		do {
			System.out.println(
					"\n----------------------------------------------------------------------------------------------------");
			System.out.println("Gestionar Personal\n");

			System.out.println(" 1. Ver personal");
			System.out.println(" 2. Contratar empleado");
			System.out.println(" 3. Despedir empleado");
			System.out.println(" 4. Volver al menu principal\n");

			opcion = readString();

			switch (opcion) {
			case "1":
				// Ver personal
				System.out.println("\nPersonal del restaurante");

				for (int i = 0; i < restaurante.getEmpleados().size(); i++) {
					Empleado empleado = restaurante.getEmpleados().get(i);
					System.out.println("\nID: " + i);
					System.out.println(empleado.informacion());
				}

				pressEnter();
				break;

			case "2":
				// Contratar empleado
				System.out.println("Contratar empleado\n");

				System.out.println("Ingrese la cedula del empleado: "); // <--- Se pueden crear empleados con cedulas
																		// repetidas.
				String cedSt = readString();
				int cedula;
				try {
					cedula = Integer.parseInt(cedSt);
				} catch (Exception e) {
					cedula = 0;
				}

				System.out.println("Ingrese el nombre del empleado: ");
				String nombre = readString();

				System.out.println("Ingrese el cargo del empleado (Chef, Repartidor, Mesero u otros): ");
				String cargo = readString();

				System.out.println("Esta disponible inmediatamente? (1: True): ");
				String dispSt = readString();
				boolean disponibilidad;
				if (dispSt.equals("1")) {
					disponibilidad = true;
				} else {
					disponibilidad = false;
				}

				System.out.println("Ingrese el salario del empleado: ");
				String salarioSt = readString();
				int salario;
				try {
					salario = Integer.parseInt(salarioSt);
				} catch (Exception e) {
					salario = 0;
				}

				System.out
						.println(admin.contratarEmpleado(cedula, nombre, cargo, disponibilidad, salario, restaurante));

				Empleado empleadoNuevo = restaurante.getEmpleados().get(restaurante.getEmpleados().size() - 1);

				System.out.println(empleadoNuevo.informacion());

				pressEnter();
				break;

			case "3":
				// Despedir empleado
				System.out.println("Despedir empleado\n");

				System.out.println("Ingrese el ID del empleado a despedir: ");
				String cedStr = readString();

				System.out.println(admin.despedirEmpleado(cedStr));
				pressEnter();
				break;

			case "4":
				break;
			default:
				System.out.println("\nLa opcion ingresada no es valida. Por favor intentelo nuevamente"); // Mensaje de
																											// control
																											// para
																											// inputs
																											// invalidos.
				pressEnter();
				break;
			}
		} while (!opcion.equals("4"));
	}

	// Submenu de la opcion "4. Cola de pedidos"

	static void submenu4(ArrayList<Integer> codPedidos) {
		boolean continuar = true;
		do {
			codPedidos = listarPedidosEnEspera();
			
			if(codPedidos.size()==0) {
				System.out.println("No hay mas pedidos en cola");
				pressEnter();
				return;
			}
			System.out.println("Ingrese el codigo de un pedido");
			System.out.println("Ingrese 0 para volver al menu principal");
			
			int codigo = 0;
			boolean valido = false;
			do {
				try {
					String entrada = readString();
					codigo = Integer.parseInt(entrada);
					
					if(entrada.equals("0")) {
						return;
					}
					
					if (codPedidos.contains(codigo)) {
						valido = true;
					} else {
						System.out.print("Ingrese un codigo de pedido valido: ");
					}
				} catch (InputMismatchException e) {
					System.out.print("Ingrese un codigo de pedido valido: ");
					sc.next();
				}
			} while (!valido);

			valido = false;
			String opcion;
			
			Pedido pedido = null;
			for (Pedido pedido_aux : restaurante.getPedidos()) {
				if (pedido_aux.getCodigo() == codigo) {
					pedido = pedido_aux;
				}
			}

			do {
				System.out.println("Que desea hacer con este pedido?\n");

				System.out.println(" 1. Aceptar");
				System.out.println(" 2. Rechazar");

				opcion = sc.nextLine();
			
			if(pedido != null) {
				switch (opcion) {
				case "1": {
					if (admin.procesarPedido(pedido)) {
						
						
						System.out.println("Pedido aceptado. Iniciando preparacion");
						System.out.println("Pedido despachado");
						admin.actualizarEstadoPedido(pedido, true);
						valido = true;
						break;
					} else {
						System.out.println("Lo sentimos el pedido no puede ser aceptado por restricciones del restaurante");
						admin.actualizarEstadoPedido(pedido, false);
						valido = true;
						break;
					}
				}
				case "2": {
					System.out.println("Pedido rechazado");
					admin.actualizarEstadoPedido(pedido, false);
					valido = true;
					break;
				}
				default:
					System.out.println("Opcion no valida\n");
					break;
				}

			}
			}
			while (!valido);

			valido = false;

			do {
				System.out.println("Desea continuar con la gestion de pedidos?\n");

				System.out.println(" 1. Si, continuar");
				System.out.println(" 2. No, volver al menu principal");

				opcion = readString();

				switch (opcion) {
				case "1": {
					valido = true;
					break;
				}
				case "2": {
					valido = true;
					continuar = false;
					break;
				}
				default:
					System.out.println("Opcion no valida\n");
				}
			} while (!valido);
		} while (continuar);

	}

	static ArrayList<Integer> listarPedidosEnEspera() {
		ArrayList<Pedido> listapedidos = Pedido.getPedidos();
		ArrayList<Integer> codPedidos = new ArrayList<Integer>();
		System.out.println("Codigo pedido - " + "Estado pedido");

		for (Pedido pedido : listapedidos) {
			if (pedido.getEstado().equals(estadoPedido.Enviado.toString())) {
				System.out.println(pedido.getCodigo() + " - " + pedido.getEstado());
				codPedidos.add(pedido.getCodigo());
			}
		}
		System.out.println("\n");
		return codPedidos;
	}

	// Submenu de la opcion "5. Pagar nomina"
	static void submenu5() {

		String opcion;
		do {
			System.out.println(
					"\n----------------------------------------------------------------------------------------------------");
			System.out.println("Pagar nomina\n");

			System.out.println("Balance de cuenta: $" + restaurante.getBalanceCuenta() + "\n");

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
				System.out.println("\nLa opcion ingresada no es valida. Por favor intentelo nuevamente"); // Mensaje de
																											// control
																											// para
																											// inputs
																											// invalidos.
				pressEnter();
				break;
			}
		} while (!opcion.equals("3"));
	}

	static void DaviMenu1() {

		String opcion;
		do {
			System.out.println(
					"\n----------------------------------------------------------------------------------------------------");
			System.out.println("Informacion Basica del restaurante\n");

			System.out.println(" 1. Empleados.");
			System.out.println(" 2. Productos.");
			System.out.println(" 3. Historial pedidos.");
			System.out.println(" 4. Balance de cuenta.");
			System.out.println(" 5. Estadisticas.");
			System.out.println(" 6. Volver al menu principal\n");

			opcion = readString();

			switch (opcion) {
			case "1":
				DaviSubmenuEmpleado();
				break;
			case "2":
				DaviSubmenuProductos();
				break;
			case "3":
				DaviSubmenuHistorialPedidos();
				break;
			case "4":
				DaviSubmenuBalanceDeCuenta();
				break;
			case "5":
				DaviSubmenuEstadisticas();
				break;

			case "6":
				break;

			default:
				System.out.println("\nLa opcion ingresada no es valida. Por favor intentelo nuevamente"); // Mensaje de
																											// control
																											// para
																											// inputs
																											// invalidos.
				pressEnter();
				break;
			}
		} while (!opcion.equals("6"));
	}

	static void DaviSubmenuEmpleado() {
		int opcionempleado;
		ArrayList<Empleado> listaempleados = restaurante.getEmpleados();
		opcionempleado = -727;
		do {
			System.out.println(
					"\n----------------------------------------------------------------------------------------------------");
			System.out.println("Informacion sobre empleados");

			System.out.println("Seleccione al empleado sobre el que desea consultar \n");

			for (int i = 0; i < listaempleados.size(); ++i) {
				System.out.println(" " + (i + 1) + ". " + listaempleados.get(i).getNombre());
			}
			System.out.println("\n 0. Regresar al menu principal.");
			try {
				opcionempleado = Integer.parseInt(Consola.readString());
			} catch (Exception e) {
				System.out.println("\nPor favor introduzca un numero valido");
				pressEnter();
			}
			if ((opcionempleado - 1 >= listaempleados.size()) || (opcionempleado < 0)) {
				System.out.println("Por favor introduzca un numero valido");
				pressEnter();
				continue;

			}
			if (opcionempleado == 0) {
				continue;
			}
			if (opcionempleado != -727) {
				System.out.println(listaempleados.get(opcionempleado - 1).informacion());
				pressEnter();
				opcionempleado = -727;
			}
		} while (!(opcionempleado == 0));

	}

	static void DaviSubmenuProductos() {
		int opcionproducto;
		ArrayList<Producto> listaproductos = Producto.getProductos();
		opcionproducto = -727;
		do {
			System.out.println(
					"\n----------------------------------------------------------------------------------------------------");
			System.out.println("Informacion sobre productos");

			System.out.println("Seleccione el producto sobre el que desea consultar\n");

			for (int i = 0; i < listaproductos.size(); ++i) {
				System.out.println(" " + (i + 1) + ". " + listaproductos.get(i).getNombre());
			}
			System.out.println("\n 0. Regresar al menu principal.");
			try {
				opcionproducto = Integer.parseInt(Consola.readString());
			} catch (Exception e) {
				System.out.println("\nPor favor introduzca un numero valido");
				pressEnter();
			}

			if ((opcionproducto - 1 >= listaproductos.size()) || (opcionproducto < 0)) {
				System.out.println("Por favor introduzca un numero valido");
				pressEnter();
				continue;

			}
			if (opcionproducto == 0) {
				continue;
			}
			if (opcionproducto != -727) {
				System.out.println(listaproductos.get(opcionproducto - 1));
				pressEnter();
				opcionproducto = -727;
			}
		} while (!(opcionproducto == 0));

	}

	static void DaviSubmenuHistorialPedidos() {
		int opcionpedidos;
		ArrayList<Pedido> listapedidos = Pedido.getPedidos();
		opcionpedidos = -727;
		do {
			System.out.println(
					"\n----------------------------------------------------------------------------------------------------");
			System.out.println("Informacion sobre pedidos realizados");
			System.out.println("Total de pedidos recibidos: " + Pedido.getTotalPedidos());

			System.out.println("Seleccione el pedido sobre el que desea consultar\n");

			for (int i = 0; i < listapedidos.size(); ++i) {
				System.out.println(" " + (i + 1) + ". Pedido " + listapedidos.get(i).getCodigo());
			}
			
			System.out.println("\n 0. Regresar al menu principal.");
			try {
				opcionpedidos = Integer.parseInt(Consola.readString());
			} catch (Exception e) {
				System.out.println("\nPor favor introduzca un numero valido");
				pressEnter();
			}

			if ((opcionpedidos - 1 >= listapedidos.size()) || (opcionpedidos < 0)) {
				System.out.println("Por favor introduzca un numero valido");
				pressEnter();
				continue;

			}
			if (opcionpedidos == 0) {
				continue;
			}
			if (opcionpedidos != -727) {
				System.out.println(
						"\n----------------------------------------------------------------------------------------------------");
				System.out.println(listapedidos.get(opcionpedidos - 1));
				pressEnter();
				opcionpedidos = -727;
			}
		} while (!(opcionpedidos == 0));

	}

	static void DaviSubmenuEstadisticas() {

		String opcion;
		do {
			System.out.println(
					"\n----------------------------------------------------------------------------------------------------");
			System.out.println("Estadisticas\n");
			System.out.println(restaurante.estadisticasRestaurante());
			System.out.println("\n 0. Regresar al menu principal.");

			opcion = readString();

			switch (opcion) {
			case "0":
				break;

			default:
				System.out.println("\nLa opcion ingresada no es valida. Por favor intentelo nuevamente"); // Mensaje de
																											// control
																											// para
																											// inputs
																											// invalidos.
				pressEnter();
				break;
			}
		} while (!opcion.equals("0"));
	}

	static void DaviSubmenuBalanceDeCuenta() {

		String opcion;
		do {
			System.out.println(
					"\n----------------------------------------------------------------------------------------------------");
			System.out.println("Balance de cuenta\n");
			System.out.println("$" + restaurante.getBalanceCuenta());
			System.out.println("\n 0. Regresar al menu principal.");

			opcion = readString();

			switch (opcion) {
			case "0":
				break;

			default:
				System.out.println("\nLa opcion ingresada no es valida. Por favor intentelo nuevamente"); // Mensaje de
																											// control
																											// para
																											// inputs
																											// invalidos.
				pressEnter();
				break;
			}
		} while (!opcion.equals("0"));
	}

	static void DaviMenu2() {

		String opcion;
		do {
			System.out.println(
					"\n----------------------------------------------------------------------------------------------------");
			System.out.println("Informacion Basica sobre clientes \n");
			System.out.println(" 1. Ver clientes.");
			System.out.println(" 2. Crear cliente.");
			System.out.println(" 3. Regresar al menu principal.");
			opcion = readString();

			switch (opcion) {
			case "1":
				DaviSubmenuVerClientes();
				break;

			case "2":
				DaviSubmenuCrearCliente();
				break;

			case "3":
				break;

			default:
				System.out.println("\nLa opcion ingresada no es valida. Por favor intentelo nuevamente"); // Mensaje de
																											// control
																											// para
																											// inputs
																											// invalidos.
				pressEnter();
				break;
			}
		} while (!opcion.equals("3"));
	}

	static void DaviSubmenuVerClientes() {
		int opcionClientes;
		ArrayList<Cliente> listaclientes = Cliente.getClientes();
		opcionClientes = -727;
		do {
			System.out.println(
					"\n----------------------------------------------------------------------------------------------------");
			System.out.println("Informacion sobre los clientes\n");

			System.out.println("Seleccione el cliente sobre el que desea consultar\n");

			for (int i = 0; i < listaclientes.size(); ++i) {
				System.out.println(" " + (i + 1) + ". " + listaclientes.get(i).getNombre());
			}

			System.out.println("\n 0. Regresar al menu principal.");

			try {
				opcionClientes = Integer.parseInt(Consola.readString());
			} catch (Exception e) {
				System.out.println("Por favor introduzca un numero valido");
				pressEnter();
			}
			if ((opcionClientes - 1 >= listaclientes.size()) || (opcionClientes < 0)) {
				System.out.println("Por favor introduzca un numero valido");
				pressEnter();
				continue;

			}
			if (opcionClientes == 0) {
				continue;
			}
			if (opcionClientes != -727) {
				System.out.println(listaclientes.get(opcionClientes - 1).informacion());
				pressEnter();
				opcionClientes = -727;
			}
		} while (!(opcionClientes == 0));

	}

	static void DaviSubmenuCrearCliente() {

		String opcion;
		do {
			System.out.println(
					"\n----------------------------------------------------------------------------------------------------");
			System.out.println("Crear clientes \n");
			System.out.println(" 1. Crear Manualmente.");
			System.out.println(" 2. Crear Automaticamente.");
			System.out.println(" 3. Regresar al menu principal.");
			opcion = readString();

			switch (opcion) {

			case "1":
				DaviSubSubMenuCrearClienteManual();
				break;

			case "2":
				DaviSubmenuGenerarClienteRandom();
				break;

			case "3":
				break;

			default:
				System.out.println("\nLa opcion ingresada no es valida. Por favor intentelo nuevamente"); // Mensaje de
																											// control
																											// para
																											// inputs
																											// invalidos.
				pressEnter();
				break;
			}
		} while (!opcion.equals("3"));
	}

	static void DaviSubSubMenuCrearClienteManual() {
		String nombreCliente;
		String edadClienteString;
		String numeroCliente;
		int numeroClienteInt = 0;
		int edadClienteInt = 0;
		String direccionCliente;
		String correoElectronicoClienteString;
		boolean verdad = false;
		System.out.println("Por favor ingrese el nombre del cliente que desea registrar");
		nombreCliente = readString();
		System.out.println("Por favor ingrese la edad del cliente que desea registrar");
		do {
			edadClienteString = readString();
			try {
				edadClienteInt = Integer.parseInt(edadClienteString);
				verdad = true;
			} catch (Exception e) {
				System.out.println("Por favor ingrese un numero.");
			}

			if (edadClienteInt < 0 || edadClienteInt > 125) {
				System.out.println("Por favor ingrese una edad valida.");
				verdad = false;
			}
		} while (!verdad);

		System.out.println("Por favor ingrese el correo electronico del cliente que desea registrar");

		correoElectronicoClienteString = readString();

		System.out.println("Por favor ingrese el numero del cliente que desea registrar");
		verdad = false;
		do {
			numeroCliente = readString();
			try {
				numeroClienteInt = Integer.parseInt(numeroCliente);
				verdad = true;
			} catch (Exception e) {
				System.out.println("Por favor ingrese un numero.");
			}
		} while (!verdad);
		System.out.println("Por favor ingrese la direccion del cliente que desea registrar");
		direccionCliente = readString();
		new Cliente(numeroClienteInt, nombreCliente, direccionCliente, edadClienteInt, null, new ArrayList<Pedido>(),
				correoElectronicoClienteString);

		System.out.println("Se ha creado el cliente con nombre: " + nombreCliente + "\n" + "con una edad de: "
				+ edadClienteInt + " anhos" + "\n" + "el cual tiene el numero telfonico: " + numeroCliente + "\n"
				+ "con el correo electronico: " + correoElectronicoClienteString + "\n"
				+ "el cual tiene por direccion: " + direccionCliente);
		pressEnter();
	}

	static void DaviSubmenuGenerarClienteRandom() {
		Cliente clienteSummonCliente = new Cliente(DatosAleatorios.randInt(100000, 999999),
				DatosAleatorios.randString(DatosAleatorios.nombresAleatorios),
				"Calle " + DatosAleatorios.randInt(10, 99) + " #" + DatosAleatorios.randInt(10, 99) + "-"
						+ DatosAleatorios.randInt(10, 99),
				DatosAleatorios.randInt(18, 99), null, new ArrayList<Pedido>(),
				"cliente" + DatosAleatorios.randInt(150, 999999) + "@gmail.com");

		System.out.println("Se ha creado el cliente con nombre: " + clienteSummonCliente.getNombre() + "\n"
				+ "con una edad de: " + clienteSummonCliente.getEdad() + " anhos" + "\n"
				+ "el cual tiene el numero telfonico: " + clienteSummonCliente.getTelefono() + "\n"
				+ "con el correo electronico: " + clienteSummonCliente.getCorreoElectronico() + "\n"
				+ "el cual tiene por direccion: " + clienteSummonCliente.getDireccion());
		pressEnter();
	}

}
