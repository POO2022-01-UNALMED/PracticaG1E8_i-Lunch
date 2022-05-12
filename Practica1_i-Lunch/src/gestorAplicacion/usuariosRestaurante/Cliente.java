package gestorAplicacion.usuariosRestaurante;

import java.time.LocalDateTime;
import java.util.ArrayList;
import java.util.Random;
import java.io.Serializable;

import gestorAplicacion.gestionRestaurante.*;

public class Cliente implements Serializable {
	
	// Serializacion
	private static final long serialVersionUID = 1L;
	private static ArrayList<Cliente> clientes;
	static {
		clientes = new ArrayList<Cliente>();
	}
	
	// Atributos
	private int telefono;
	private String primerNombre;
	private String segundoNombre;
	private String primerApellido;
	private String segundoApellido;
	private String direccion;
	private LocalDateTime fechaNacimiento;
	

	public Cliente(int telefono, String primerNombre, String segundoNombre, String primerApellido,
			String segundoApellido, String direccion, LocalDateTime fechaNacimiento, Pedido pedidoActivo,
			ArrayList<Pedido> historialPedidos) {
		super();
		this.telefono = telefono;
		this.primerNombre = primerNombre;
		this.segundoNombre = segundoNombre;
		this.primerApellido = primerApellido;
		this.segundoApellido = segundoApellido;
		this.direccion = direccion;
		this.fechaNacimiento = fechaNacimiento;
		this.pedidoActivo = pedidoActivo;
		this.historialPedidos = historialPedidos;
		clientes.add(this);
	}
	
	public Cliente() {
		this(0, "", "", "", "", "", null, null, null);
	}

	// Aca se almacenara el pedido que este la persona realizando en el momento,
	// al despachar o cancelar dicho pedido este atributo tiene que volver a null.
	// y en particular despues de ser despachado este pedido activo tiene que ser agregado al historial.
	private Pedido pedidoActivo = null;
	
	// ArrayList en el cual se agregaran todos los pedidos hechos por el cliente a lo largo del tiempo.
	private ArrayList<Pedido> historialPedidos = new ArrayList<Pedido>();
	
	////////////// METODOS ////////////////
	public Pedido iniciarPedido() {
		return new Pedido(this, new Random().nextInt(999999),"Ni idea, falta implementar", LocalDateTime.now(), null);		
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
	
	///////// GETTERS AND SETTERS /////////
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
	public LocalDateTime getfechaNacimiento() {
		return fechaNacimiento;
	}
	public void setfechaNacimiento(LocalDateTime fechaNacimiento) {
		this.fechaNacimiento = fechaNacimiento;
	}

	public static ArrayList<Cliente> getClientes() {
		return clientes;
	}

	public Pedido getPedidoActivo() {
		return pedidoActivo;
	}

	public void setPedidoActivo(Pedido pedidoActivo) {
		this.pedidoActivo = pedidoActivo;
	}

	public ArrayList<Pedido> getHistorialPedidos() {
		return historialPedidos;
	}

	public void setHistorialPedidos(ArrayList<Pedido> historialPedidos) {
		this.historialPedidos = historialPedidos;
	}	
}
