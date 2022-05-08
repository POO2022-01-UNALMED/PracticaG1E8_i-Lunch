/*CLASE CREADA POR JERONIMO GOMEZ RESTREPO
 * Clase que hereda de EMPLEADO y que tiene como finalidad llevar un pedido a su etapa final "Entregado". Se le asignan 3 nuevos atributos: 
   PoseeVehiculo, Placa, tipoVehiculo.*/

package gestorAplicacion.usuariosRestaurante;
import gestorAplicacion.gestionRestaurante.Restaurante;
import gestorAplicacion.gestionRestaurante.Pedido;

public class Repartidor extends Empleado {
	/*Como REPARTIDOR hereda de EMPLEADO, utiliza sus atributos y ademas se crean 3 nuevos.*/
	private boolean poseeVehiculo;
	private String placa;
	private String tipoVehiculo;
	
	/*Constructor*/
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
	}
	/*Constructor con valores por defecto*/
	public Repartidor() {
		this(0, "NN","NA", false, 0, null/*, false*/, false, "NA", "NA" );
	}
	
	/*Metodos GET y SET para los 3 nuevos atributos*/
	public boolean getPoseeVehiculo() {
		return this.poseeVehiculo;
	}
	
	public void setposeeVehiculo(boolean poseeVehiculo) {
		this.poseeVehiculo = poseeVehiculo;
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
	
	/*Metodo para cambiar el estado de pedido a su estado final "Entregado". Recibe como parametro estado 
	 * y se debe revisar que este "Listo para ser despachado"*/
	public void repartirPedido(Pedido pedido) {
		
	}
	

}
