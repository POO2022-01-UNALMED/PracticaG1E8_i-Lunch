/*CLASE CREADA POR JERONIMO GOMEZ RESTREPO
  Clase que hereda de EMPLEADO y que tiene como finalidad la preparacion de los pedidos para que puedan ser despachados. 
  Se le asignan 2 nuevos atributos: cargoEnCocina y especialidad.*/


package gestorAplicacion.usuariosRestaurante;

import java.io.Serializable;
import java.util.ArrayList;

import gestorAplicacion.gestionRestaurante.*;

public class Chef extends Empleado implements Serializable {
	
	// Serializacion
	private static final long serialVersionUID = 1L;
	private static ArrayList<Chef> chefs;
	static {
		chefs = new ArrayList<Chef>();
	}
	
	/*Como CHEF hereda de EMPLEADO, utiliza sus atributos y ademas se crean 2 nuevos.*/
	private String cargoEnCocina;
	private String especialidad;
	
	/*Constructor de la clase Chef*/
	public Chef(int cedula, String nombre, String cargo, boolean disponibilidad, int salario, Restaurante restaurante/*, boolean pagado*/, 
			String cargoEnCocina, String especialidad) {
		this.setCedula(cedula);
		this.setNombre(nombre);
		this.setCargo(cargo);
		this.setDisponibilidad(disponibilidad);
		this.setSalario(salario);
		this.setRestaurante(restaurante);
		/*this.setPagado = pagado;*/
		
		this.cargoEnCocina = cargoEnCocina;
		this.especialidad = especialidad;
		chefs.add(this);
	}

	/*Sobrecarga del constructor para valores predeterminados*/
	public Chef() {
		this(0, "NN","NA", false, 0, null/*, false*/, "NA", "NA");
	}
	
	/*Metodos GET y SET para los 2 nuevos atributos*/
	public String getCargoEnCocina() {
		return this.cargoEnCocina;
	}
	
	public void setCargoEnCocina(String cargoEnCocina) {
		this.cargoEnCocina = cargoEnCocina;
	}
	
	public String getEspecialidad() {
		return this.especialidad;
	}
	
	public void setEspecialidad(String especialidad) {
		this.especialidad = especialidad;
	}
	
	public static ArrayList<Chef> getChefs() {
		return chefs;
	}

	/*Metodo que permite a un chef preparar un producto de la lista de productos de la clase Pedido(Suponemos que un chef crea un solo producto a 
	 * la vez?). Recibe como argumento un pedido, se toma un producto de la listo y se prepara. Asi, hasta preparar todos los productos de la lista.*/
	
	public void prepararProducto(Pedido pedido) {
		for (int i=0;i<pedido.getProductos().size();i++) {
				pedido.getProductos().get(i).setEstado(true);}
			}


	/*Metodo que permite saber si el pedido ha sido preparado de manera correcta y asi cambiar su estado a "Listo para ser despachado".
	  Esta revision la realiza el chef en jefe del restaurante, quien decide si esta listo o no. Recibe como parametros un pedido y 
	  (Lista de productos??) y tiene como finalidad ser el requisito para poder cambiar el estado de un pedido a su estado final 
	  "Listo para ser despachado"*/
	
	public void revisionPedido(Pedido pedido) {
		if(this.cargoEnCocina.equals("Chef en jefe")) {
			int contador = 0;
			for (int i=0;i<pedido.getProductos().size();i++) {
				if(pedido.getProductos().get(i).getEstado() == true) {
					contador++;
				}
			}
			if (contador == pedido.getProductos().size()) {
				pedido.setEstado("Listo para ser despachado"); /* <-------- Falta aplicar el ENUM*/
			}
		}
	}
}
