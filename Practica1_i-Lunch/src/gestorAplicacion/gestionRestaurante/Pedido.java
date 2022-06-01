package gestorAplicacion.gestionRestaurante;

import java.io.Serializable;
import java.time.LocalDateTime;
import java.time.format.DateTimeFormatter;
import java.util.ArrayList;

import gestorAplicacion.usuariosRestaurante.*;

public class Pedido implements Serializable {
	
	// Serializacion
	private static final long serialVersionUID = 1L;
	private static ArrayList<Pedido> pedidos;
	static {
		pedidos = new ArrayList<Pedido>();
	}
	
	
	////////////// ATRIBUTOS //////////////
	private static int totalPedidos = 0;
	private Cliente cliente;
	private int codigo;
	private String estado;
	
	//ArrayList donde se encuentran todos los productos que componen el pedido.
	private ArrayList<Producto> productos = new ArrayList<Producto>();
	
	private String tipo;
	// Pienso que es mejor separar fecha.
	private LocalDateTime fechaHora;
	
	//Mensaje agregado por el usuario de forma opcional al realizar un pedido.
	private String mensaje;
	private int precioTotal;
	private Restaurante restaurante;

	////////////// METODOS ////////////////

	public int calcularPrecioTotal() {
		int sum = 0;
		for(int i = 0; i < productos.size(); i++){
			sum += productos.get(i).getPrecio();
		}
		return sum;
	}
	
	/////////// CONSTRUCTORES /////////////
	
	public Pedido(
			Cliente cliente, 
			int codigo, 
			String tipo, 
			LocalDateTime fechaHora, 
			Restaurante restaurante) {
		//Considero que estos son los datos necesarios para empezar un pedido
		this.cliente = cliente;
		this.codigo = codigo;
		this.tipo = tipo;
		this.fechaHora = fechaHora;
		this.restaurante = restaurante;
		pedidos.add(this);
		Pedido.totalPedidos += 1;
		
		// Sumar a los pedidos del cliente
		this.cliente.agregarPedidoHistorial(this);
		
	}
	
	public Pedido() {
		this(null, 0, "", null, null);
	}
	
	public Pedido(Cliente cliente) {
		this(cliente, 0, "", null, null);
	}
	
	///////// GETTERS AND SETTERS /////////

	public Cliente getCliente() {
		return cliente;
	}

	public void setCliente(Cliente cliente) {
		this.cliente = cliente;
	}

	public int getCodigo() {
		return codigo;
	}

	public void setCodigo(int codigo) {
		this.codigo = codigo;
	}

	public String getEstado() {
		return estado;
	}

	public void setEstado(String estado) {
		this.estado = estado;
	}

	public ArrayList<Producto> getProductos() {
		return productos;
	}

	public void setProductos(ArrayList<Producto> productos) {
		this.productos = productos;
	}

	public String getTipo() {
		return tipo;
	}

	public void setTipo(String tipo) {
		this.tipo = tipo;
	}

	public LocalDateTime getFechaHora() {
		return fechaHora;
	}

	public void setFechaHora(LocalDateTime fechaHora) {
		this.fechaHora = fechaHora;
	}

	public String getMensaje() {
		return mensaje;
	}

	public void setMensaje(String mensaje) {
		this.mensaje = mensaje;
	}

	public int getPrecioTotal() {
		return precioTotal;
	}

	public void setPrecioTotal(int precioTotal) {
		this.precioTotal = precioTotal;
	}

	public Restaurante getRestaurante() {
		return restaurante;
	}

	public void setRestaurante(Restaurante restaurante) {
		this.restaurante = restaurante;
	}

	public static ArrayList<Pedido> getPedidos() {
		return pedidos;
	}
	
	public static int getTotalPedidos() {
		return pedidos.size();
	}

	public static void setPedidos(ArrayList<Pedido> pedidos) {
		Pedido.pedidos = pedidos;
	}

	public static void setTotalPedidos(int totalPedidos) {
		Pedido.totalPedidos = totalPedidos;
	}

	@Override
	public String toString() {
		String productosString = "";
		
		// Fecha hora
		DateTimeFormatter formatter = DateTimeFormatter.ofPattern("yyyy-MM-dd - HH:mm:ss"); 
		String fechaHoraString = fechaHora.format(formatter);

		
		for(Producto producto: this.productos) {
			productosString += " - " + producto.getNombre() + " (" + producto.getCantidad() + ")\n";
		}
		
		return "\nPedido "+ codigo + " hecho por el cliente: \"" + cliente.getNombre() + "\"\n" +
			   "Fecha y hora: " + fechaHoraString + "\n" +
			   "Estado: " + estado + "\n" +
			   "Mensaje: " + mensaje + "\n" +
			   "Tipo: " + tipo + "\n" +
			   "Productos: \n" + productosString +
			   "Precio total: $" + precioTotal;
	}
}
