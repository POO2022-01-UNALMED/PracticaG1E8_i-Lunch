package gestorAplicacion.usuariosRestaurante;
////////////////////////////////////////
//////////////  IMPORTES //////////////
///////////////////////////////////////
import java.time.LocalDateTime;
import java.util.ArrayList;
import java.util.Random;

import gestorAplicacion.gestionRestaurante.Pedido;
import gestorAplicacion.gestionRestaurante.Producto;
import gestorAplicacion.gestionRestaurante.Restaurante;

public class Cliente {
////////////////////////////////////////
////////////// ATRIBUTOS //////////////
///////////////////////////////////////
	private int telefono;
	// Pienso que es mejor separar asi el nombre (pensando en bases de datos lol)
	private String primerNombre;
	private String segundoNombre;
	private String primerApellido;
	private String segundoApellido;
	
	private String direccion;
	private LocalDateTime fechaNacimientol;
	
	//Aca se almacenara el pedido que este la persona realizando en el momento,
	//al despachar o cancelar dicho pedido este atributo tiene que volver a null.
	//y en particular despues de ser despachado este pedido activo tiene que ser agregado al historial.
	private Pedido pedidoActivo = null;
	
	// ArrayList en el cual se agregaran todos los pedidos hechos por el cliente a lo largo del tiempo.
	private ArrayList<Pedido> historialPedidos = new ArrayList<Pedido>();
	
	
	
////////////////////////////////////////
////////////// METODOS ////////////////
///////////////////////////////////////	
	public Pedido iniciarPedido() {
		return new Pedido(this, new Random().nextInt(999999),"Ni idea, falta implementar", LocalDateTime.now(),
				Restaurante restaurante);		
	}
	
	public void agregarProducto(Producto producto) {
		pedidoActivo.getProductos().add(producto);
	}
	
	public void eliminarProducto(Producto producto) {
		pedidoActivo.getProductos().remove(producto);
	}
	
	public void pedir(Pedido pedido, String tipo, String mensaje) {
		//PENDIENTE
	}
	
	
	
	

////////////////////////////////////////
///////// GETTERS AND SETTERS /////////
///////////////////////////////////////
	public int getTelefono() {
		return telefono;
	}
	public void setTelefono(int telefono) {
		this.telefono = telefono;
	}
	public String getPrimerNombre() {
		return primerNombre;
	}
	public void setPrimerNombre(String primerNombre) {
		this.primerNombre = primerNombre;
	}
	public String getSegundoNombre() {
		return segundoNombre;
	}
	public void setSegundoNombre(String segundoNombre) {
		this.segundoNombre = segundoNombre;
	}
	public String getPrimerApellido() {
		return primerApellido;
	}
	public void setPrimerApellido(String primerApellido) {
		this.primerApellido = primerApellido;
	}
	public String getSegundoApellido() {
		return segundoApellido;
	}
	public void setSegundoApellido(String segundoApellido) {
		this.segundoApellido = segundoApellido;
	}
	public String getDireccion() {
		return direccion;
	}
	public void setDireccion(String direccion) {
		this.direccion = direccion;
	}
	public LocalDateTime getFechaNacimientol() {
		return fechaNacimientol;
	}
	public void setFechaNacimientol(LocalDateTime fechaNacimientol) {
		this.fechaNacimientol = fechaNacimientol;
	}
}
////////////////////////////////////////
////////////////////////////////////////
///////////////////////////////////////
