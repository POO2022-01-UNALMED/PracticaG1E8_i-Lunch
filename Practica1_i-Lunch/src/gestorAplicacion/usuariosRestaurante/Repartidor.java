/*CLASE CREADA POR JERONIMO GOMEZ RESTREPO
 * Clase que hereda de EMPLEADO y que tiene como finalidad llevar un pedido a su etapa final "Entregado". Se le asignan 3 nuevos atributos: 
   poseeVehiculo, placa, tipoVehiculo.*/

package gestorAplicacion.usuariosRestaurante;
import java.io.Serializable;
import java.util.ArrayList;

import gestorAplicacion.gestionRestaurante.*;


public class Repartidor extends Empleado implements Serializable {
	
	private static final long serialVersionUID = 1L;
	private static ArrayList<Repartidor> repartidores;
	static {
		repartidores = new ArrayList<Repartidor>();
	}
	
	/*Como REPARTIDOR hereda de EMPLEADO, utiliza sus atributos y ademas se crean 3 nuevos.*/
	private boolean poseeVehiculo;
	private String placa;
	private String tipoVehiculo;
	
	/*Constructor de la clase Repartidor*/
	public Repartidor(int cedula, String nombre, String cargo, boolean disponibilidad, int salario, Restaurante restaurante/*, boolean pagado*/, 
			boolean poseeVehiculo, String placa, String tipoVehiculo) {
		this.setCedula(cedula);
		this.setNombre(nombre);
		this.setCargo(cargo);
		this.setDisponibilidad(disponibilidad);
		this.setSalario(salario);
		this.setRestaurante(restaurante);
		/*this.setPagado = pagado;*/
		
		this.poseeVehiculo = poseeVehiculo;
		this.placa = placa;
		this.tipoVehiculo = tipoVehiculo;
		repartidores.add(this);
	}

	/*Sobrecarga del constructor para valores predeterminados*/
	public Repartidor() {
		this(0, "NN","NA", false, 0, null/*, false*/, false, "NA", "NA" );
	}
	
	/*Metodos GET y SET para los 3 nuevos atributos*/
	public boolean getPoseeVehiculo() {
		return this.poseeVehiculo;
	}
	
	public String getPlaca() {
		return this.placa;
	}
	
	public void setPlaca(String placa) {
		this.placa = placa;
	}
	
	public String getTipoVehiculo() {
		return this.tipoVehiculo;
	}
	
	public void setTipoVehiculo(String tipoVehiculo) {
		this.tipoVehiculo = tipoVehiculo;
	}
	
	public static ArrayList<Repartidor> getRepartidores() {
		return repartidores;
	}

	public void setPoseeVehiculo(boolean poseeVehiculo) {
		this.poseeVehiculo = poseeVehiculo;
	}

	/*Metodo para cambiar el estado de un pedido(atributo "estado") a su estado final "Entregado". Recibe como parametro un pedido 
	  y tiene como finalidad modificar el atributo "estado", por ultima vez y de manera unica. Se debe revisar que el estado anterior
	  del pedido sea "Listo para ser despachado" y que sea para llevar*/
	public void repartirPedido(Pedido pedido) {
		if(pedido.getEstado().equals("Listo") && pedido.getTipo().equals("Para llevar")) { /*<<<<<--------- Falta aplicar el ENUM*/
			pedido.setEstado("Enviado"); 		/*<<<<<--------- Falta aplicar el ENUM*/
		}
		
		
	}
	

}
