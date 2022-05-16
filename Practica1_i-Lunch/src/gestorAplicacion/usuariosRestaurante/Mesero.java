/*CLASE CREADA POR JERONIMO GOMEZ RESTREPO
  Clase que hereda de EMPLEADO y que tiene como finalidad tomar los pedidos(crear?), llevar un pedido a su etapa final "Entregado"
  y dar a conocer el precio total del pedido.
  Por ahora no se agregan nuevos atributos. 
  */

package gestorAplicacion.usuariosRestaurante;
import java.io.Serializable;
import java.util.ArrayList;

import javax.print.event.PrintJobAttributeEvent;

import gestorAplicacion.gestionRestaurante.*;

public class Mesero extends Empleado implements Serializable{
	
	// Serialización
	private static final long serialVersionUID = 1L;
	private static ArrayList<Mesero> meseros;
	static {
		meseros = new ArrayList<Mesero>();
	}
	
	// Aca se almacenan todos los pedidos atentidos por el mesero en cuestion
	
	private ArrayList<Pedido> pedidosAtendidos = new ArrayList<Pedido>();
	private ArrayList<Float> historialPropinas = new ArrayList<Float>();
	
	/*Constructor de la clase Mesero*/
	public Mesero(int cedula, String nombre, String cargo, boolean disponibilidad, int salario, Restaurante restaurante/*, boolean pagado*/) {
		this.setCedula(cedula);
		this.setNombre(nombre);
		this.setCargo(cargo);
		this.setDisponibilidad(disponibilidad);
		this.setSalario(salario);
		this.setRestaurante(restaurante);
		/*this.setPagado = pagado;*/
		meseros.add(this);
	}
	
	/*Sobrecarga del constructor para valores predeterminados*/
	public Mesero() {
		this(0, "NN","NA", false, 0, null/*, false*/);
	}
	
	// Getters y Setters
	public static ArrayList<Mesero> getMeseros() {
		return meseros;
	}

	
	/* Metodo para cambiar el estado de un pedido(atributo "estadoPedido") a su estado final "Entregado". Recibe como parametro un pedido 
	  y tiene como finalidad modificar el atributo "estadoPedido", por ultima vez y de manera unica. Se debe revisar que el estado anterior
	  del pedido sea "Listo para ser despachado" y que sea para consumir en el lugar. */
	 
	 public void llevarPedido(Pedido pedido) {
		 pedidosAtendidos.add(pedido); // Se agrega el pedido a la lista de pedidos
		 if(pedido.getEstado().equals("Listo") && pedido.getTipo().equals("Para Consumir en el lugar")) { /*<<<<<--------- Falta aplicar el ENUM*/
				pedido.setEstado("Despachado"); 		/*<<<<<--------- Falta aplicar el ENUM*/
			}
	}
	 
	//metodo para agregar una propina al historial de propinas
	 
	 public void recibirPropina(float propina) {
		 historialPropinas.add(propina);
	 }
	 
	 //Metodo que calcula el total de las propinas recibidas por un mesero.
	 public int totalPropinas() {
		 int propinaAdder = 0;
		 for (float propina: historialPropinas) {
			 propinaAdder += propina;
		 }
		 return propinaAdder;
	 }
	 
	//// GETTERS AND SETTERS \\\\
	public ArrayList<Pedido> getPedidosAtendidos() {
		return pedidosAtendidos;
	}

	public void setPedidosAtendidos(ArrayList<Pedido> pedidosAtendidos) {
		this.pedidosAtendidos = pedidosAtendidos;
	}

	public static void setMeseros(ArrayList<Mesero> meseros) {
		Mesero.meseros = meseros;
	}

	public ArrayList<Float> getHistorialPropinas() {
		return historialPropinas;
	}

	public void setHistorialPropinas(ArrayList<Float> historialPropinas) {
		this.historialPropinas = historialPropinas;
	}
}

