// CLASE CREADA POR: Emmanuel López Rodríguez

package gestorAplicacion.usuariosRestaurante;

import java.io.Serializable;
import java.util.ArrayList;

import gestorAplicacion.gestionRestaurante.*;

/* Esta es la clase principal de la aplicación, ya que el administrador
 * es quien tiene acceso a la aplicación y desde su cuenta se manejan
 * todas las funcionalidades. Esta clase hereda de Empleado
 */

public class Administrador extends Empleado implements Serializable{
	// Como Administrador hereda de Empleado, se utilizarán los atributos de este. No es necesario implementar atributos nuevos
	
	// Atributos utilizados para la serialización
	private static final long serialVersionUID = 1L; // Se requiere del atributo serialVersionUID por usar la interface Serializable.
	private static ArrayList<Administrador> administradores;
	static {
		administradores = new ArrayList<Administrador>();
	}
	
	// Constructor de la clase Administrador. No se recibe el atributo "cargo" debido a que este siempre será "Administrador"
	public Administrador(int cedula, String nombre, boolean disponibilidad, int salario, Restaurante restaurante) {
		/*
		this.setCedula(cedula);
		this.setNombre(nombre);
		this.setCargo("Administrador");
		this.setDisponibilidad(disponibilidad);
		this.setSalario(salario);
		this.setRestaurante(restaurante);
		*/
	}
	
	// Sobrecarga del constructor. No toma parámetros y llama al constructor usando valores predeterminados.
	public Administrador() {
		this(0, "NN", false, 0, null);
	}
	
	// Método utilizado para la serialización/deserielización
	public static ArrayList<Administrador> getAdministradores(){
		return administradores;
	}
	
	/* Este método recibe como parámetro un objeto Empleado, comprueba que no esté ya
	 * contratado en el restaurante y si no lo está lo agrega a la lista de empleados
	 * del restaurante. También cambia el atributo Resturante del Empleado.
	 */
	public void contratarEmpleado(Empleado empleado) {
		
	}
	
	/* Este método recibe como parámetro un objeto Empleado, comprueba que este esté ya
	 * contratado en el restaurante y si lo está lo agrega a la lista de empleados
	 * del restaurante. También cambia el atributo Resturante del Empleado.
	 */
	public void despedirEmpleado(Empleado empleado) {
		
	}
	
	/* Este método recibe como parámetros:
	 * - Un String con el nombre del producto
	 * - Un String con la descripción del producto
	 * - Un int con el precio del procucto
	 * - Un bool que es true si el producto solo puede ser vendido a mayores de edad
	 * - Un bool que indica la disponibilidad actual del producto
	 * Luego, se crea un objeto de tipo Producto con estos atributos y se agrega a la lista
	 * de productos del restaurante. Antes de agregarlo se comprueba que no haya un producto
	 * con un nombre exactamente igual y si esto no se cumple, se agrega.
	 */
	public void crearProducto(String nombre, String descripcion, int precio, boolean restriccion, boolean disponibilidad) {
		
	}
	
	/* Método útil para cambiar el nombre de un Producto pasado por parámetro.
	 * Antes de cambiar el atributo se debe de comprobar que el producto esté 
	 * en la lista de productos del restaurante.
	 */
	public void actualizarNombreProducto(Producto producto, String nombre) {
		
	}
	
	/* Método útil para cambiar la descripción de un Producto pasado por parámetro.
	 * Antes de cambiar el atributo se debe de comprobar que el producto esté 
	 * en la lista de productos del restaurante.
	 */
	public void actualizarDescripcionProducto(Producto producto, String descripcion) {
		
	}
	
	/* Método útil para cambiar el precio de un Producto pasado por parámetro.
	 * Antes de cambiar el atributo se debe de comprobar que el producto esté 
	 * en la lista de productos del restaurante.
	 */
	public void actualizarPrecioProducto(Producto producto, int precio) {
		
	}
	
	/* Método útil para cambiar el estado de la restricción de un Producto pasado por parámetro.
	 * Antes de cambiar el atributo se debe de comprobar que el producto esté 
	 * en la lista de productos del restaurante.
	 */
	public void actualizarRestriccionProducto(Producto producto, boolean restriccion) {
		
	}
	
	/* Método útil para cambiar la disponibilidad actual de un Producto pasado por parámetro.
	 * Antes de cambiar el atributo se debe de comprobar que el producto esté 
	 * en la lista de productos del restaurante.
	 */
	public void actualizarDisponibilidadProducto(Producto producto, boolean disponibilidad) {
		
	}
	
	/* Método que sirve para eliminar un Producto de la lista de productos del restaurante.
	 * Antes de eliminar el producto se debe de verificar que el producto se encuentre
	 * en la lista de productos del restaurante.
	 */
	public void eliminarProducto(Producto producto) {
		
	}
	
	/* Método que realiza el pago de la nómina a todos los empleados del restaurante incluyendo
	 * al Administrador mismo. Antes de hacer efectivo el pago se debe de comprobar que en el balance
	 * de cuenta del restaurtante existan fondos sufucientes para pagar a los empleados
	 */
	public void autorizarPagoNomina() {
		
	}
	
	/* Método que sirve para simular un pedido al restaurante. Este recibe como parámetros un Cliente
	 * con quien se asociará el pedido simulado y un objeto Pedido que contiene toda la información
	 * del pedido simulado.
	 */
	public void simularPedido(Cliente cliente, Pedido pedido) {
		
	}
}
