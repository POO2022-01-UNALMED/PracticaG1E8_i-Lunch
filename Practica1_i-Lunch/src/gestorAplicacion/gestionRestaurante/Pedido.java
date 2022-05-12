package gestorAplicacion.gestionRestaurante;

import java.io.Serializable;
import java.time.LocalDateTime;
import java.time.zone.ZoneOffsetTransitionRule;
import java.util.ArrayList;
import java.util.concurrent.atomic.DoubleAdder;
import java.util.function.BiConsumer;

import gestorAplicacion.usuariosRestaurante.Administrador;
import gestorAplicacion.usuariosRestaurante.Cliente;

public class Pedido implements Serializable {

////////////////////////////////////////
//////////////ATRIBUTOS //////////////
///////////////////////////////////////
	
	private static final long serialVersionUID = 1L;
	private static ArrayList<Pedido> pedidos;
	static {
		int totalPedidos = 0;
		pedidos = new ArrayList<Pedido>();
	}
	
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

	
	
////////////////////////////////////////
////////////// METODOS ////////////////
///////////////////////////////////////

	private int calcularPrecioTotal() {
		int sum = 0;
		for(int i = 0; i < productos.size(); i++){
			sum += productos.get(i).getPrecio();
		}
		return sum;
	}
	
////////////////////////////////////////
/////////// CONSTRUCTORES /////////////
///////////////////////////////////////
	
	
	public Pedido(Cliente cliente, int codigo, String tipo, LocalDateTime fechaHora, Restaurante restaurante) {
		//Considero que estos son los datos necesarios para empezar un pedido
		this.cliente = cliente;
		this.codigo = codigo;
		this.tipo = tipo;
		this.fechaHora = fechaHora;
		this.restaurante = restaurante;
		pedidos.add(this);
	}
	
////////////////////////////////////////
///////// GETTERS AND SETTERS /////////
///////////////////////////////////////

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
	
////////////////////////////////////////
////////////////////////////////////////
///////////////////////////////////////
}
