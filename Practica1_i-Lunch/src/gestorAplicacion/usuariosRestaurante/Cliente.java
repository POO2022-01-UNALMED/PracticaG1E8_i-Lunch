package gestorAplicacion.usuariosRestaurante;

import java.util.ArrayList;
import java.util.Random;
import java.io.Serializable;
import java.time.LocalDateTime;

import gestorAplicacion.gestionRestaurante.*;

public class Cliente implements Serializable, Usuario {
	
	// Serializacion
	private static final long serialVersionUID = 1L;
	private static ArrayList<Cliente> clientes;
	static {
		clientes = new ArrayList<Cliente>();
	}
	
	// Atributos
	private int telefono;
	private String nombre;
	private String direccion;
	private int edad;
	private String correoElectronico;
	// ArrayList en el cual se agregaran todos los pedidos hechos por el cliente a lo largo del tiempo.
	private ArrayList<Pedido> historialPedidos = new ArrayList<Pedido>();

	public Cliente(int telefono, String nombre, String direccion, int edad, Pedido pedidoActivo, ArrayList<Pedido> historialPedidos, String correo) {
		super();
		this.telefono = telefono;
		this.nombre = nombre;
		this.direccion = direccion;
		this.edad = edad;
		this.pedidoActivo = pedidoActivo;
		this.historialPedidos = historialPedidos;
		this.correoElectronico = correo;
		clientes.add(this);
	}
	
	public Cliente() {
		this(0, "", "", 0, null, null,null);
	}

	// Aca se almacenara el pedido que este la persona realizando en el momento,
	// al despachar o cancelar dicho pedido este atributo tiene que volver a null.
	// y en particular despues de ser despachado este pedido activo tiene que ser agregado al historial.
	private Pedido pedidoActivo = null;

	
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
		///
		//// NO SE QUE HACER ACA JSJSJSJSJ
		////
		
		historialPedidos.add(pedido);
	}
	
	///////// GETTERS AND SETTERS /////////
	public int getTelefono() {
		return telefono;
	}
	public void setTelefono(int telefono) {
		this.telefono = telefono;
	}
	public String getNombre() {
		return nombre;
	}
	public void setPrimerNombre(String nombre) {
		this.nombre = nombre;
	}
	public String getDireccion() {
		return direccion;
	}
	public void setDireccion(String direccion) {
		this.direccion = direccion;
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
	
	public int getEdad() {
		return edad;
	}

	public void setEdad(int edad) {
		this.edad = edad;
	}

	public void setNombre(String nombre) {
		this.nombre = nombre;
	}

	public String getCorreoElectronico() {
		return correoElectronico;
	}

	public void setCorreoElectronico(String correoElectronico) {
		this.correoElectronico = correoElectronico;
	}

	public static void setClientes(ArrayList<Cliente> clientes) {
		Cliente.clientes = clientes;
	}	
	
	// Implementación de la interfaz Usuario
	public String informacion() {
		return "El cliente " + this.nombre + " con email " + this.correoElectronico + " y teléfono " + this.telefono + " vive en la dirección " + this.direccion + " y tiene " + this.edad + " años.\n"
				+ "Ha hecho " + this.historialPedidos.size() + " pedidos en la aplicacion.";
	}
}
