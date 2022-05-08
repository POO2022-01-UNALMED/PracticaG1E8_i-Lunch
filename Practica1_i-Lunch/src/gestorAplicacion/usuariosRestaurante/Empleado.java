/*CLASE CREADA POR JERONIMO GOMEZ RESTREPO 
 
 *Clase padre de las clases ADMINISTRADOR, REPARTIDOR, CHEF y MESERO. Aqui se definen los atributos cedula,
 *nombre, cargo, disponinilidad, salario, restaurante y ****pagado****. Ademas de sus respectivos metodos get y set.*/

package gestorAplicacion.usuariosRestaurante;
import gestorAplicacion.gestionRestaurante.Restaurante;
import gestorAplicacion.gestionRestaurante.Pedido;


public class Empleado { /*Por ahora puse todos protected, si no recuerdo mal por sugerencia del profe. Sujeto a revision*/
	protected int cedula;
	protected String nombre;
	protected String cargo;
	protected boolean disponibilidad;	
	protected int salario;
	protected Restaurante restaurante;
	/*protected boolean pagado=false; <--- Que tal este atributo pagado? Refiriendose a su salario.  */
	
	/*Constructor de la clase empleado*/								/*Tengo duda con este atributo restaurante, explicarme porfa que es. Falta set y get de esto*/
	public Empleado(int cedula, String nombre, String cargo, boolean disponibilidad, int salario, Restaurante restaurante/*, boolean pagado*/) {
		this.cedula = cedula;
		this.nombre = nombre;
		this.cargo = cargo;
		this.disponibilidad = disponibilidad;
		this.salario = salario;
		this.restaurante = restaurante;
		/*this.pagado = pagado;*/
	}
	/*Sobrecarga del constructor para valores predeterminados*/
	public Empleado() {
		this(0, "NN","NA", false, 0, null/*, false*/);
	}
	
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
	
	
	/*SET Y GET del atributo pagado
	 
	public boolean isPagado() {
		return pagado;
	}
	
	public void setPagado(boolean estado) {
		pagado=estado;}*/
	
	
	/*Metodo para cambiar el estado de un pedido a su fase inicial "En preparacion". Recibe como parametro pedido*/
	public void aceptarPedido(Pedido pedido) {
		
		
	}
	
	
}
