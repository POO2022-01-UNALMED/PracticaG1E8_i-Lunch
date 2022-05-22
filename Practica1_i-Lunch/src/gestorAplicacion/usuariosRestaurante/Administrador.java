package gestorAplicacion.usuariosRestaurante;

import java.io.Serializable;
import java.time.LocalDateTime;
import java.util.ArrayList;

import gestorAplicacion.gestionRestaurante.*;

/* Esta es la clase principal de la aplicación, ya que el administrador
 * es quien tiene acceso a la aplicación y desde su cuenta se manejan
 * todas las funcionalidades. Esta clase hereda de Empleado */

public class Administrador extends Empleado implements Serializable, Usuario {
	/*
	 * Como Administrador hereda de Empleado, se utilizarán los atributos de este.
	 * Solo se implementa el atributo extra IMPUESTOS ya que se usará en una de sus
	 * funcionalidades
	 */
	private static final float IMPUESTOS = 1.19f; // 19% de impuestos

	// Atributos utilizados para la serialización
	private static final long serialVersionUID = 1L; // Se requiere del atributo serialVersionUID por usar la interface
														// Serializable.
	private static ArrayList<Administrador> administradores;
	static {
		administradores = new ArrayList<Administrador>();
	}

	// Constructor de la clase Administrador. No se recibe el atributo "cargo"
	// debido a que este siempre será "Administrador"
	public Administrador(int cedula, String nombre, boolean disponibilidad, int salario, Restaurante restaurante) {
		super(cedula, nombre, "Administrador", disponibilidad, salario, restaurante);
		
		ArrayList<Empleado> empleados = this.restaurante.getEmpleados();
		empleados.add(this);
		this.restaurante.setEmpleados(empleados);
		
		administradores.add(this);
	}

	// Sobrecarga del constructor. No toma parámetros y llama al constructor usando
	// valores predeterminados.
	public Administrador() {
		this(0, "NN", false, 0, null);
	}

	// Método utilizado para la serialización/deserielización
	public static ArrayList<Administrador> getAdministradores() {
		return administradores;
	}

	// Getter de IMPUESTOS (No se implementa Setter debido a que es una constante
	public static float getImpuestos() {
		return Administrador.IMPUESTOS;
	}

	/*
	 * Este método recibe como parámetro un objeto Empleado, comprueba que no
	 * esté ya contratado en el restaurante y si no lo está lo agrega a la lista
	 * de empleados del restaurante. También cambia el atributo Resturante del
	 * Empleado.
	 */
	public void contratarEmpleado(Empleado empleado) {
		ArrayList<Empleado> listaEmpleados = this.restaurante.getEmpleados();
		listaEmpleados.add(empleado);
		this.restaurante.setEmpleados(listaEmpleados);
	}

	/*
	 * Este método recibe como parámetro un objeto Empleado, comprueba que este
	 * esté ya contratado en el restaurante y si lo está lo agrega a la lista de
	 * empleados del restaurante. También cambia el atributo Resturante del
	 * Empleado.
	 */
	public void despedirEmpleado(Empleado empleado) {
		ArrayList<Empleado> listaEmpleados = this.restaurante.getEmpleados();
		listaEmpleados.remove(empleado);
		this.restaurante.setEmpleados(listaEmpleados);
	}

	/*
	 * Este método recibe como parámetros: - Un String con el nombre del producto
	 * - Un String con la descripción del producto - Un int con el precio del
	 * procucto - Un bool que es true si el producto solo puede ser vendido a
	 * mayores de edad - Un bool que indica la disponibilidad actual del producto
	 * Luego, se crea un objeto de tipo Producto con estos atributos y se agrega a
	 * la lista de productos del restaurante. Antes de agregarlo se comprueba que no
	 * haya un producto con un nombre exactamente igual y si esto no se cumple, se
	 * agrega.
	 */
	public String crearProducto(String nombre, String descripcion, int precio, boolean disponibilidad,
			boolean restriccion, int cantidad) {
		Producto productoNuevo = new Producto(nombre, descripcion, precio, disponibilidad, restriccion, cantidad);

		ArrayList<Producto> listaMenu = this.restaurante.getMenu();
		if (!listaMenu.contains(productoNuevo)) {
			listaMenu.add(productoNuevo);
			this.restaurante.setMenu(listaMenu);
			return "Producto " + nombre + " creado con éxito";
		} else {
			return "ERROR: El producto ya se encuentra creado";
		}
	}

	/*
	 * Método útil para cambiar el nombre de un Producto pasado por parámetro.
	 * Antes de cambiar el atributo se debe de comprobar que el producto esté en la
	 * lista de productos del restaurante.
	 */
	public String actualizarNombreProducto(int producto, String nombre) {
		ArrayList<Producto> listaMenu = this.restaurante.getMenu();
		try {
			Producto productoActualizado = listaMenu.get(producto);
			productoActualizado.setNombre(nombre);
			listaMenu.set(producto, productoActualizado);
			this.restaurante.setMenu(listaMenu);
			return "Producto " + productoActualizado.getNombre() + " actualizado con éxito";
		} catch (Exception e) {
			return "ERROR: El producto que intentas actualizar no existe";
		}
	}

	/*
	 * Método útil para cambiar la descripción de un Producto pasado por
	 * parámetro. Antes de cambiar el atributo se debe de comprobar que el producto
	 * esté en la lista de productos del restaurante.
	 */
	public String actualizarDescripcionProducto(int producto, String descripcion) {
		ArrayList<Producto> listaMenu = this.restaurante.getMenu();
		try {
			Producto productoActualizado = listaMenu.get(producto);
			productoActualizado.setDescripcion(descripcion);
			listaMenu.set(producto, productoActualizado);
			this.restaurante.setMenu(listaMenu);
			return "Producto " + productoActualizado.getNombre() + " actualizado con éxito";
		} catch (Exception e) {
			return "ERROR: El producto que intentas actualizar no existe";
		}
	}

	/*
	 * Método útil para cambiar el precio de un Producto pasado por parámetro.
	 * Antes de cambiar el atributo se debe de comprobar que el producto esté en la
	 * lista de productos del restaurante.
	 */
	public String actualizarPrecioProducto(int producto, int precio) {
		ArrayList<Producto> listaMenu = this.restaurante.getMenu();
		try {
			Producto productoActualizado = listaMenu.get(producto);
			productoActualizado.setPrecio(precio);
			listaMenu.set(producto, productoActualizado);
			this.restaurante.setMenu(listaMenu);
			return "Producto " + productoActualizado.getNombre() + " actualizado con éxito";
		} catch(Exception e) {
			return "ERROR: El producto que intentas actualizar no existe";
		}
	}

	/*
	 * Método útil para cambiar el estado de la restricción de un Producto pasado
	 * por parámetro. Antes de cambiar el atributo se debe de comprobar que el
	 * producto esté en la lista de productos del restaurante.
	 */
	public String actualizarRestriccionProducto(int producto, boolean restriccion) {
		ArrayList<Producto> listaMenu = this.restaurante.getMenu();
		try {
			Producto productoActualizado = listaMenu.get(producto);
			productoActualizado.setRestriccion(restriccion);
			listaMenu.set(producto, productoActualizado);
			this.restaurante.setMenu(listaMenu);
			return "Producto " + productoActualizado.getNombre() + " actualizado con éxito";
		} catch(Exception e) {
			return "ERROR: El producto que intentas actualizar no existe";
		}
	}

	/*
	 * Método útil para cambiar la disponibilidad actual de un Producto pasado por
	 * parámetro. Antes de cambiar el atributo se debe de comprobar que el producto
	 * esté en la lista de productos del restaurante.
	 */
	public String actualizarDisponibilidadProducto(int producto, boolean disponibilidad) {
		ArrayList<Producto> listaMenu = this.restaurante.getMenu();
		try {
			Producto productoActualizado = listaMenu.get(producto);
			productoActualizado.setDisponiblidad(disponibilidad);
			listaMenu.set(producto, productoActualizado);
			this.restaurante.setMenu(listaMenu);
			return "Producto " + productoActualizado.getNombre() + " actualizado con éxito";
		} catch(Exception e) {
			return "ERROR: El producto que intentas actualizar no existe";
		}
	}

	/*
	 * Método útil para cambiar la cantidad actual de un Producto pasado por
	 * parámetro. Antes de cambiar el atributo se debe de comprobar que el producto
	 * esté en la lista de productos del restaurante.
	 */
	public String actualizarCantidadProducto(int producto, int cantidad) {
		ArrayList<Producto> listaMenu = this.restaurante.getMenu();
		try {
			Producto productoActualizado = listaMenu.get(producto);
			productoActualizado.setCantidad(cantidad);
			listaMenu.set(producto, productoActualizado);
			this.restaurante.setMenu(listaMenu);
			return "Producto " + productoActualizado.getNombre() + " actualizado con éxito";
		} catch(Exception e) {
			return "ERROR: El producto que intentas actualizar no existe";
		}
	}

	/*
	 * Método que sirve para eliminar un Producto de la lista de productos del
	 * restaurante. Antes de eliminar el producto se debe de verificar que el
	 * producto se encuentre en la lista de productos del restaurante.
	 */
	public String eliminarProducto(String producto) {
		ArrayList<Producto> listaMenu = this.restaurante.getMenu();
		int productoID;
		try {
			productoID = Integer.parseInt(producto);
			String nombreProd = listaMenu.get(productoID).getNombre();
			listaMenu.remove(productoID);
			this.restaurante.setMenu(listaMenu);
			return "Producto \"" + nombreProd + "\" eliminado con éxito";
		} catch(Exception e) {
			return "ERROR: El producto que intentas eliminar no existe";
		}
	}

	/*
	 * Método que realiza el pago de la nómina a todos los empleados del
	 * restaurante incluyendo al Administrador mismo. Antes de hacer efectivo el
	 * pago se debe de comprobar que en el balance de cuenta del restaurtante
	 * existan fondos sufucientes para pagar a los empleados
	 */
	public String pagoNomina() {
		ArrayList<Empleado> listaEmpleados = this.restaurante.getEmpleados();
		float totalSalarios = 0;

		for (Empleado empleado : listaEmpleados) {
			totalSalarios += (empleado.getSalario() * Administrador.getImpuestos()); // Salario más un impuesto
		}

		if (totalSalarios <= this.restaurante.getBalanceCuenta()) {
			float nuevoBalance = this.restaurante.getBalanceCuenta() - totalSalarios;
			this.restaurante.setBalanceCuenta(nuevoBalance);
			return "Nomina de todos los empleados pagada con éxito. El nuevo balance de cuenta es: $"
					+ restaurante.getBalanceCuenta();
		} else {
			return "ERROR: No se posee el suficiente dinero para pagar la nomina de todos los empleados ($" + totalSalarios + ")";
		}
	}

	/*
	 * Método que realiza el pago de la nómina a un solo los empleado del
	 * restaurante. Antes de hacer efectivo el pago se debe de comprobar que en el
	 * balance de cuenta del restaurtante existan fondos sufucientes para pagar al
	 * empleado en cuestión
	 */
	public String pagoNomina(int empleadoID) {
		Empleado empleado = this.restaurante.getEmpleados().get(empleadoID);
		
		if ((empleado.getSalario() * Administrador.getImpuestos()) <= this.restaurante.getBalanceCuenta()) { 
			// Salario mas un impuesto
			float nuevoBalance = this.restaurante.getBalanceCuenta() - (empleado.getSalario() * Administrador.getImpuestos());
			this.restaurante.setBalanceCuenta(nuevoBalance);
			return "Nómina del empleado " + empleado.getNombre() + " pagada con éxito.\n" +
				   "El nuevo balance de cuenta es: $" + restaurante.getBalanceCuenta();
		} else {
			return "ERROR: No se posee el suficiente dinero para pagar la nómina del empleado ($" + (empleado.getSalario() * Administrador.getImpuestos()) +")";
		}
	}

	/*
	 * Método que sirve para simular un pedido al restaurante. Este recibe como
	 * parámetros un Cliente con quien se asociará el pedido simulado.
	 */
	public Pedido simularPedido(Cliente cliente) {
		Pedido pedido = new Pedido();
		int idTipo = (int) (Math.random()*2);
		String tipo = "";

		// Se asigna el cliente
		pedido.setCliente(cliente);
		// Se asigna el restaurante
		pedido.setRestaurante(restaurante);
		// Se le asigna un codigo
		pedido.setCodigo(Pedido.getTotalPedidos());
		// Se guarda fecha y hora
		pedido.setFechaHora(LocalDateTime.now());
		// Se le asigna un tipo 
		switch (idTipo) {
		case 0: {
			tipo = TipoPedido.Llevar.toString();
		}
		case 1: {
			tipo = TipoPedido.EnTienda.toString();
		}
		case 2: {
			tipo = TipoPedido.Domicilio.toString();
		}
		}
		pedido.setTipo(tipo);
		
		
	// Se asgina la lista de productos
		// Se define la canidad de productos a ordenar con base en la cantidad de productos disponible en el restaurante.
		// De 1 a la cantidad disponible en el restaurante.
		int cantidadProductos = (int) ((Math.random()*(restaurante.getMenu().size()-1))+1);
		ArrayList<Producto> productos = new ArrayList<Producto>();
		//En un ciclo que se repite el numero de productos a solicitar se seleccionan los productos del menu del restaurante.
		for(int i=0; i<cantidadProductos;i++){
			// Generamos un numero aleatorio para seleccionar un producto al azar de entre el menu del restaurante.
			int idProducto = (int) (Math.random() * restaurante.getMenu().size());
			Producto producto = restaurante.getMenu().get(idProducto);
			// Si el producto ya hace parte del pedido no se agrega
			if(!productos.contains(producto)) {
				// Se genera una cantidad aleatoria del producto seleccionado para ser agregado al pedido.
				int cantidadXProducto = (int) ((Math.random()*(5-1))+1);
				producto.setCantidad(cantidadXProducto);
				productos.add(producto);
			}else {
				//Si no se selecciona un producto se repite el ciclo.
				i--;
			}
		}
		pedido.setProductos(productos);
		
		 //Se calcula el precio total 
		int total = 0;
		for(Producto producto:pedido.getProductos()) {
			total += producto.getCantidad() * producto.getPrecio();
		}
		pedido.setPrecioTotal(total);
		//Se pone en estado de Enviado
		pedido.setEstado(estadoPedido.Enviado.toString());
		//Se agregan los mensajes del usuario
		//Se retorna el pedido completo
		restaurante.agregarPedido(pedido);
		return pedido;

	}

	// Implementación de la interfaz Usuario
	public String informacion() {
		if (this.getDisponibilidad()) {
			return "El Administrador del restaurante + " + this.restaurante.getNombre() + " es " + this.nombre
					+ " con C.C. " + this.cedula + ".\n" + "Tiene un salario de: $" + this.salario + "\n"
					+ "Está disponible actualmente.";
		} else {
			return "El Administrador del restaurante + " + this.restaurante.getNombre() + " es " + this.nombre
					+ " con C.C. " + this.cedula + ".\n" + "Tiene un salario de: $" + this.salario + "\n"
					+ "No está disponible actualmente.";
		}
	}
}
