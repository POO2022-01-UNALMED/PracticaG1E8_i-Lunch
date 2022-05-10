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
	}
	
	/*Sobrecarga del constructor para valores predeterminados*/
	public Mesero() {
		this(0, "NN","NA", false, 0, null/*, false*/);
	}
	
	/*Metodo que permite ingresar al sistema la orden del cliente y asi crear el objeto de tipo pedido.?? dudas con la creacion del objeto pedido
	  Seria como el paso previo a utilizar el metodo aceptarPedido?*/
	
	public static ArrayList<Mesero> getMeseros() {
		return meseros;
	}

	public void tomarPedido(Pedido pedido) { /*<-- Puede ser que tomar pedido no sea tan util y que mejor sea crearPedido directamente*/
		
	}
	
	
	/* Metodo para cambiar el estado de un pedido(atributo "estadoPedido") a su estado final "Entregado". Recibe como parametro un pedido 
	  y tiene como finalidad modificar el atributo "estadoPedido", por ultima vez y de manera unica. Se debe revisar que el estado anterior
	  del pedido sea "Listo para ser despachado" y que sea para consumir en el lugar. 
	 
	 public void llevarPedido(Pedido pedido) { <--- Un poco inutil?
		
	}*/
	
	
	/* Metodo que permite al cliente conocer el total de su pedido, mediante el atributo "precioTotal". Recibe como parametro un pedido.*/
	public void llevarCuenta(Pedido pedido) {
		
	}
	
}

/*Esta clase me genera dudas sobre su utilidad a la hora de simular el proceso.*/