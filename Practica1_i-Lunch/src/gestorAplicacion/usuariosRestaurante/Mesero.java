/*CLASE CREADA POR JERONIMO GOMEZ RESTREPO
  Clase que hereda de EMPLEADO y que tiene como finalidad tomar los pedidos(crear?), llevar un pedido a su etapa final "Entregado"
  y dar a conocer el precio total del pedido.
  Por ahora no se agregan nuevos atributos. 
  */

package gestorAplicacion.usuariosRestaurante;
import java.io.Serializable;
import java.util.ArrayList;

import gestorAplicacion.gestionRestaurante.*;


public class Mesero extends Empleado implements Serializable{
	
	private static final long serialVersionUID = 1L;
	private static ArrayList<Mesero> meseros;
	static {
		meseros = new ArrayList<Mesero>();
	}
	
	/*Como CHEF hereda de EMPLEADO, utiliza sus atributo*/
	
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
	
	
	public static ArrayList<Mesero> getMeseros() {
		return meseros;
	}

	
	/* Metodo para cambiar el estado de un pedido(atributo "estadoPedido") a su estado final "Entregado". Recibe como parametro un pedido 
	  y tiene como finalidad modificar el atributo "estadoPedido", por ultima vez y de manera unica. Se debe revisar que el estado anterior
	  del pedido sea "Listo para ser despachado" y que sea para consumir en el lugar. */
	 
	 public void llevarPedido(Pedido pedido) {
		 if(pedido.getEstado().equals("Listo") && pedido.getTipo().equals("Para Consumir en el lugar")) { /*<<<<<--------- Falta aplicar el ENUM*/
				pedido.setEstado("Despachado"); 		/*<<<<<--------- Falta aplicar el ENUM*/
			}
	}
	

	
}

