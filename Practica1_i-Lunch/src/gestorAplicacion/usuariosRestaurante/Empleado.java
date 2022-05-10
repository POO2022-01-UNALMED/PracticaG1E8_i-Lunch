/*CLASE CREADA POR JERONIMO GOMEZ RESTREPO 
 
 *Clase padre de las clases ADMINISTRADOR, REPARTIDOR, CHEF y MESERO. Aqui se definen los atributos cedula,
 *nombre, cargo, disponinilidad, salario, restaurante y ****pagado****. Ademas de sus respectivos metodos get y set.*/

package gestorAplicacion.usuariosRestaurante;

import gestorAplicacion.gestionRestaurante.*;
import java.io.Serializable;
import java.util.ArrayList;

public class Empleado implements Serializable { /*
						 * Por ahora puse todos protected, si no recuerdo mal por sugerencia del profe.
						 * Sujeto a revision
						 */
	protected int cedula;
	protected String nombre;
	protected String cargo;
	protected boolean disponibilidad;
	protected int salario;
	protected Restaurante restaurante;

	/*protected boolean pagado=false; <--- Que tal este atributo pagado? Refiriendose a su salario.  */
	
	// Atributos utilizados para la serialización
		private static final long serialVersionUID = 1L; // Se requiere del atributo serialVersionUID por usar la interface Serializable.
		private static ArrayList<Empleado> empleados;
		static {
			empleados = new ArrayList<Empleado>();
		}
	
	/*Constructor de la clase empleado*/								/*Tengo duda con este atributo restaurante, explicarme porfa que es.*/
	public Empleado(int cedula, String nombre, String cargo, boolean disponibilidad, int salario, Restaurante restaurante/*, boolean pagado*/) {

		this.cedula = cedula;
		this.nombre = nombre;
		this.cargo = cargo;
		this.disponibilidad = disponibilidad;
		this.salario = salario;
		this.restaurante = restaurante;
		/* this.pagado = pagado; */
	}

	/* Sobrecarga del constructor para valores predeterminados */
	public Empleado() {
		this(0, "NN", "NA", false, 0, null/* , false */);
	}

	/* Metodos GET y SET para los atributos */

	public int getCedula() {
		return this.cedula;
	}

	public void setCedula(int cedula) {
		this.cedula = cedula;
	}

	public String getNombre() {
		return this.nombre;
	}

	public void setNombre(String nombre) {
		this.nombre = nombre;
	}

	public String getCargo() {
		return this.cargo;
	}

	public void setCargo(String cargo) {
		this.cargo = cargo;
	}

	public int getSalario() {
		return this.salario;
	}

	public boolean getDisponibilidad() {
		return this.disponibilidad;
	}

	public void setDisponibilidad(boolean disponibilidad) {
		this.disponibilidad = disponibilidad;
	}

	public void setSalario(int salario) {
		this.salario = salario;
	}

	public Restaurante getRestaurante(Restaurante restaurante) {
		return this.restaurante;
	}

	public void setRestaurante(Restaurante restaurante) {
		this.restaurante = restaurante;
	}
	
	public static ArrayList<Empleado> getEmpleados() {
		return empleados;
	}

	public Restaurante getRestaurante() {
		return restaurante;
	}

	/*
	 * SET Y GET del atributo pagado
	 * 
	 * public boolean isPagado() { return pagado; }
	 * 
	 * public void setPagado(boolean estado) { pagado=estado;}
	 */

	/*
	 * Metodo para cambiar el estado de un pedido(atributo "estadoPedido") a su fase
	 * inicial "En preparacion". Recibe como parametro un pedido y tiene como
	 * finalidad modificar el atributo "estadoPedido", la primera vez y de manera
	 * unica.
	 */
	public boolean procesarPedido(Pedido pedido) {
		if (restaurante.verificarPersonal(pedido) && restaurante.verificarProductos(pedido)) {
			return true;
		}
		return false;
	}

	/*
	 * Metodo para cambiar el estado de un pedido(atributo "estadoPedido") en sus
	 * distintas etapas, de manera secuencial. Una vez termine la etapa actual, se
	 * puede continuar con la siguiente fase. Recibe como parametro un pedido y
	 * tiene como finalidad modificar el atributo "estadoPedido".
	 */
	public boolean actualizarEstadoPedido(Pedido pedido, boolean rechazo) {
		if (rechazo) {
			pedido.setEstado(estadoPedido.Rechazado.name());
			return false;
		}
		switch (pedido.getEstado()) {
		case "Enviado":
			pedido.setEstado(estadoPedido.Aceptado.name());
		case "Aceptado":
			pedido.setEstado(estadoPedido.EnPreparacion.name());
		case "EnPreparacion":
			pedido.setEstado(estadoPedido.Listo.name());
		case "Listo":
			pedido.setEstado(estadoPedido.Despachado.name());
		}
		return true;

	}
}
