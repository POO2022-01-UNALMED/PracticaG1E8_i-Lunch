package gestorAplicacion.usuariosRestaurante;

import java.io.Serializable;
import java.util.ArrayList;

import gestorAplicacion.gestionRestaurante.*;

/* Esta es la clase principal de la aplicación, ya que el administrador
 * es quien tiene acceso a la aplicación y desde su cuenta se manejan
 * todas las funcionalidades. Esta clase hereda de Empleado */

public class Administrador extends Empleado implements Serializable, Usuario {
	/* Como Administrador hereda de Empleado, se utilizarán los atributos de este.
	 * Solo se implementa el atributo extra IMPUESTOS ya que se usará en una de sus funcionalidades */
	private static final float IMPUESTOS = 1.19f; // 19% de impuestos
	
	// Atributos utilizados para la serialización
	private static final long serialVersionUID = 1L; // Se requiere del atributo serialVersionUID por usar la interface Serializable.
	private static ArrayList<Administrador> administradores;
	static {
		administradores = new ArrayList<Administrador>();
	}
	
	// Constructor de la clase Administrador. No se recibe el atributo "cargo" debido a que este siempre será "Administrador"
	public Administrador(int cedula, String nombre, boolean disponibilidad, int salario, Restaurante restaurante) {
		super(cedula, nombre, "Administrador", disponibilidad, salario, restaurante);
		administradores.add(this);
	}
	
	// Sobrecarga del constructor. No toma parámetros y llama al constructor usando valores predeterminados.
	public Administrador() {
		this(0, "NN", false, 0, null);
	}

	// Método utilizado para la serialización/deserielización
	public static ArrayList<Administrador> getAdministradores(){
		return administradores;
	}
	
	// Getter de IMPUESTOS (No se implementa Setter debido a que es una constante
	public static float getImpuestos() {
		return Administrador.IMPUESTOS;
	}
	
	/* Este método recibe como parámetro un objeto Empleado, comprueba que no esté ya
	 * contratado en el restaurante y si no lo está lo agrega a la lista de empleados
	 * del restaurante. También cambia el atributo Resturante del Empleado. */
	public void contratarEmpleado(Empleado empleado) {
		ArrayList<Empleado> listaEmpleados = this.restaurante.getEmpleados();
		listaEmpleados.add(empleado);
		this.restaurante.setEmpleados(listaEmpleados);
	}
	
	/* Este método recibe como parámetro un objeto Empleado, comprueba que este esté ya
	 * contratado en el restaurante y si lo está lo agrega a la lista de empleados
	 * del restaurante. También cambia el atributo Resturante del Empleado. */
	public void despedirEmpleado(Empleado empleado) {
		ArrayList<Empleado> listaEmpleados = this.restaurante.getEmpleados();
		listaEmpleados.remove(empleado);
		this.restaurante.setEmpleados(listaEmpleados);
	}
	
	/* Este método recibe como parámetros:
	 * - Un String con el nombre del producto
	 * - Un String con la descripción del producto
	 * - Un int con el precio del procucto
	 * - Un bool que es true si el producto solo puede ser vendido a mayores de edad
	 * - Un bool que indica la disponibilidad actual del producto
	 * Luego, se crea un objeto de tipo Producto con estos atributos y se agrega a la lista
	 * de productos del restaurante. Antes de agregarlo se comprueba que no haya un producto
	 * con un nombre exactamente igual y si esto no se cumple, se agrega. */
	public String crearProducto(String nombre, String descripcion, int precio, boolean disponibilidad, boolean restriccion, int cantidad) {
		Producto productoNuevo = new Producto(nombre, descripcion, precio, disponibilidad, restriccion, cantidad);
		
		ArrayList<Producto> listaMenu = this.restaurante.getMenu();
		if(!listaMenu.contains(productoNuevo)) {
			listaMenu.add(productoNuevo);
			this.restaurante.setMenu(listaMenu);
			return "Producto " + nombre + "creado con éxito";
		} else {
			return "ERROR: El producto ya se encuentra creado";
		}
	}
	
	/* Método útil para cambiar el nombre de un Producto pasado por parámetro.
	 * Antes de cambiar el atributo se debe de comprobar que el producto esté 
	 * en la lista de productos del restaurante. */
	public String actualizarNombreProducto(Producto producto, String nombre) {
		ArrayList<Producto> listaMenu = this.restaurante.getMenu();
		if(listaMenu.contains(producto)) {
			int indiceProducto = listaMenu.indexOf(producto);
			Producto productoActualizado = listaMenu.get(indiceProducto);
			productoActualizado.setNombre(nombre);
			listaMenu.set(indiceProducto, productoActualizado);
			this.restaurante.setMenu(listaMenu);
			return "Producto " + producto.getNombre() + " actualizado con éxito";
		} else {
			return "ERROR: El producto que intentas actualizar no existe";
		}
	}
	
	/* Método útil para cambiar la descripción de un Producto pasado por parámetro.
	 * Antes de cambiar el atributo se debe de comprobar que el producto esté 
	 * en la lista de productos del restaurante. */
	public String actualizarDescripcionProducto(Producto producto, String descripcion) {
		ArrayList<Producto> listaMenu = this.restaurante.getMenu();
		if(listaMenu.contains(producto)) {
			int indiceProducto = listaMenu.indexOf(producto);
			Producto productoActualizado = listaMenu.get(indiceProducto);
			productoActualizado.setDescripcion(descripcion);
			listaMenu.set(indiceProducto, productoActualizado);
			this.restaurante.setMenu(listaMenu);
			return "Producto " + producto.getNombre() + " actualizado con éxito";
		} else {
			return "ERROR: El producto que intentas actualizar no existe";
		}
	}
	
	/* Método útil para cambiar el precio de un Producto pasado por parámetro.
	 * Antes de cambiar el atributo se debe de comprobar que el producto esté 
	 * en la lista de productos del restaurante. */
	public String actualizarPrecioProducto(Producto producto, int precio) {
		ArrayList<Producto> listaMenu = this.restaurante.getMenu();
		if(listaMenu.contains(producto)) {
			int indiceProducto = listaMenu.indexOf(producto);
			Producto productoActualizado = listaMenu.get(indiceProducto);
			productoActualizado.setPrecio(precio);
			listaMenu.set(indiceProducto, productoActualizado);
			this.restaurante.setMenu(listaMenu);
			return "Producto " + producto.getNombre() + " actualizado con éxito";
		} else {
			return "ERROR: El producto que intentas actualizar no existe";
		}
	}
	
	/* Método útil para cambiar el estado de la restricción de un Producto pasado por parámetro.
	 * Antes de cambiar el atributo se debe de comprobar que el producto esté 
	 * en la lista de productos del restaurante. */
	public String actualizarRestriccionProducto(Producto producto, boolean restriccion) {
		ArrayList<Producto> listaMenu = this.restaurante.getMenu();
		if(listaMenu.contains(producto)) {
			int indiceProducto = listaMenu.indexOf(producto);
			Producto productoActualizado = listaMenu.get(indiceProducto);
			productoActualizado.setRestriccion(restriccion);
			listaMenu.set(indiceProducto, productoActualizado);
			this.restaurante.setMenu(listaMenu);
			return "Producto " + producto.getNombre() + " actualizado con éxito";
		} else {
			return "ERROR: El producto que intentas actualizar no existe";
		}
	}
	
	/* Método útil para cambiar la disponibilidad actual de un Producto pasado por parámetro.
	 * Antes de cambiar el atributo se debe de comprobar que el producto esté 
	 * en la lista de productos del restaurante. */
	public String actualizarDisponibilidadProducto(Producto producto, boolean disponibilidad) {
		ArrayList<Producto> listaMenu = this.restaurante.getMenu();
		if(listaMenu.contains(producto)) {
			int indiceProducto = listaMenu.indexOf(producto);
			Producto productoActualizado = listaMenu.get(indiceProducto);
			productoActualizado.setDisponiblidad(disponibilidad);
			listaMenu.set(indiceProducto, productoActualizado);
			this.restaurante.setMenu(listaMenu);
			return "Producto " + producto.getNombre() + " actualizado con éxito";
		} else {
			return "ERROR: El producto que intentas actualizar no existe";
		}
	}
	
	/* Método útil para cambiar la cantidad actual de un Producto pasado por parámetro.
	 * Antes de cambiar el atributo se debe de comprobar que el producto esté 
	 * en la lista de productos del restaurante. */
	public String actualizarCantidadProducto(Producto producto, int cantidad) {
		ArrayList<Producto> listaMenu = this.restaurante.getMenu();
		if(listaMenu.contains(producto)) {
			int indiceProducto = listaMenu.indexOf(producto);
			Producto productoActualizado = listaMenu.get(indiceProducto);
			productoActualizado.setCantidad(cantidad);
			listaMenu.set(indiceProducto, productoActualizado);
			this.restaurante.setMenu(listaMenu);
			return "Producto " + producto.getNombre() + " actualizado con éxito";
		} else {
			return "ERROR: El producto que intentas actualizar no existe";
		}
	}
	
	/* Método que sirve para eliminar un Producto de la lista de productos del restaurante.
	 * Antes de eliminar el producto se debe de verificar que el producto se encuentre
	 * en la lista de productos del restaurante. */
	public String eliminarProducto(Producto producto) {
		ArrayList<Producto> listaMenu = this.restaurante.getMenu();
		if(listaMenu.contains(producto)) {
			listaMenu.remove(producto);
			this.restaurante.setMenu(listaMenu);
			return "Producto " + producto.getNombre() + " eliminado con éxito";
		} else {
			return "ERROR: El producto que intentas eliminar no existe";
		}
	}
	
	/* Método que realiza el pago de la nómina a todos los empleados del restaurante incluyendo
	 * al Administrador mismo. Antes de hacer efectivo el pago se debe de comprobar que en el balance
	 * de cuenta del restaurtante existan fondos sufucientes para pagar a los empleados */
	public String pagoNomina() {
		ArrayList<Empleado> listaEmpleados = this.restaurante.getEmpleados();
		float totalSalarios = 0;
		
		for(Empleado empleado: listaEmpleados) {
			totalSalarios += (empleado.getSalario()*Administrador.getImpuestos()); // Salario más un impuesto
		}
		
		if(totalSalarios <= this.restaurante.getBalanceCuenta()) {
			float nuevoBalance = this.restaurante.getBalanceCuenta() - totalSalarios;
			this.restaurante.setBalanceCuenta(nuevoBalance);
			return "Nómina de todos los empleados pagada con éxito. El nuevo balance de cuenta es: $" + restaurante.getBalanceCuenta();
		} else {
			return "ERROR: No se posee el suficiente dinero para pagar la nómina de todos los empleados";
		}
	}
	
	/* Método que realiza el pago de la nómina a un solo los empleado del restaurante.
	 * Antes de hacer efectivo el pago se debe de comprobar que en el balance de cuenta
	 * del restaurtante existan fondos sufucientes para pagar al empleado en cuestión */
	public String pagoNomina(Empleado empleado) {
		if((empleado.getSalario()*Administrador.getImpuestos()) <= this.restaurante.getBalanceCuenta()) { // Salario más un impuesto
			float nuevoBalance = this.restaurante.getBalanceCuenta() - (empleado.getSalario()*Administrador.getImpuestos());
			this.restaurante.setBalanceCuenta(nuevoBalance);
			return "Nómina de todos los empleados pagada con éxito. El nuevo balance de cuenta es: $" + restaurante.getBalanceCuenta();
		} else {
			return "ERROR: No se posee el suficiente dinero para pagar la nómina de todos los empleados";
		}
	}
	
	/* Método que sirve para simular un pedido al restaurante. Este recibe como parámetros un Cliente
	 * con quien se asociará el pedido simulado y un objeto Pedido que contiene toda la información
	 * del pedido simulado. */
	public void simularPedido(Cliente cliente, Pedido pedido) {
		// Esta funcionalidad es algo más complicada
	}
	
	// Implementación de la interfaz Usuario
	public String informacion() {
		if(this.getDisponibilidad()) {
			return "El Administrador del restaurante + " + this.restaurante.getNombre() + " es " + this.nombre + " con C.C. " + this.cedula + ".\n"
					+ "Tiene un salario de: $" + this.salario+ "\n"
					+ "Está disponible actualmente.";
		} else {
			return "El Administrador del restaurante + " + this.restaurante.getNombre() + " es " + this.nombre + " con C.C. " + this.cedula + ".\n"
					+ "Tiene un salario de: $" + this.salario+ "\n"
					+ "No está disponible actualmente.";
		}
	}
}
