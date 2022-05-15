package gestorAplicacion.gestionRestaurante;

import java.util.ArrayList;

import javax.swing.text.TabStop;

import java.io.Serializable;
import gestorAplicacion.usuariosRestaurante.*;

public class Restaurante implements Serializable {

	// Serializacion
	private static final long serialVersionUID = 1L;
	private static ArrayList<Restaurante> restaurantes;
	static {
		restaurantes = new ArrayList<Restaurante>();
	}

	// Atributos
	private String nombre;
	private int nit;
	private int telefono;
	private String direccion;
	private String correo;
	private boolean abierto;
	private int capacidad;
	private ArrayList<Empleado> empleados = new ArrayList<Empleado>();
	private ArrayList<Producto> menu = new ArrayList<Producto>();
	private ArrayList<Pedido> pedidos = new ArrayList<Pedido>();
	private int balanceCuenta;

	// Constructores
	public Restaurante(String nombre, int nit, int telefono, String direccion, String correo, boolean abierto,
			int capacidad, ArrayList<Empleado> empleados, ArrayList<Producto> menu, ArrayList<Pedido> pedidos,
			int balanceCuenta) {
		super();
		this.nombre = nombre;
		this.nit = nit;
		this.telefono = telefono;
		this.direccion = direccion;
		this.correo = correo;
		this.abierto = abierto;
		this.capacidad = capacidad;
		this.empleados = empleados;
		this.menu = menu;
		this.pedidos = pedidos;
		this.balanceCuenta = balanceCuenta;
		restaurantes.add(this);
	}

	public Restaurante() {
		this("", 0, 0, "", "", false, 0, null, null, null, 0);
	}

	// Getters y Setters
	public String getNombre() {
		return nombre;
	}

	public void setNombre(String nombre) {
		this.nombre = nombre;
	}

	public int getNit() {
		return nit;
	}

	public void setNit(int nit) {
		this.nit = nit;
	}

	public int getTelefono() {
		return telefono;
	}

	public void setTelefono(int telefono) {
		this.telefono = telefono;
	}

	public String getDireccion() {
		return direccion;
	}

	public void setDireccion(String direccion) {
		this.direccion = direccion;
	}

	public String getCorreo() {
		return correo;
	}

	public void setCorreo(String correo) {
		this.correo = correo;
	}

	public boolean isAbierto() {
		return abierto;
	}

	public void setAbierto(boolean abierto) {
		this.abierto = abierto;
	}

	public int getCapacidad() {
		return capacidad;
	}

	public void setCapacidad(int capacidad) {
		this.capacidad = capacidad;
	}

	public ArrayList<Empleado> getEmpleados() {
		return empleados;
	}

	public void setEmpleados(ArrayList<Empleado> empleados) {
		this.empleados = empleados;
	}

	public ArrayList<Producto> getMenu() {
		return menu;
	}

	public void setMenu(ArrayList<Producto> menu) {
		this.menu = menu;
	}

	public ArrayList<Pedido> getPedidos() {
		return pedidos;
	}

	public void setPedidos(ArrayList<Pedido> pedidos) {
		this.pedidos = pedidos;
	}

	public int getBalanceCuenta() {
		return balanceCuenta;
	}

	public void setBalanceCuenta(int balanceCuenta) {
		this.balanceCuenta = balanceCuenta;
	}

	public static ArrayList<Restaurante> getRestaurantes() {
		return restaurantes;
	}

	// Metodo que determina si existe el personal necesario en el restaurante para
	// realizar un pedido solicitado
	public boolean verificarPersonal(Pedido pedido) {

		// Comprobamos si existe un chef en el restaurante
		boolean chef = false;
		for (int i = 0; i < empleados.size(); i++) {
			Empleado empleado = empleados.get(i);
			if (empleado.getCargo() == "Chef") {
				chef = true;
			}
		}

		// Identificar el tipo de pedido
		switch (pedido.getTipo()) {
		case "Domicilio": {

			// Rectificar el personal del restaurante y comprobar que haya el necesario para
			// el tipo de pedido
			boolean repartidor = false;
			for (int i = 0; i < empleados.size(); i++) {
				Empleado empleado = empleados.get(i);
				if (empleado.getCargo() == "Repartidor") {
					repartidor = true;
				}
			}
			// Si si no hay alguno no se puede realizar
			if (!chef && !repartidor) {
				return false;
			}
			// Si todo es aceptable se realiza el pedido
		}
		case "Consumir en el local": {

			// Rectificar el personal del restaurante y comprobar que haya el necesario para
			// el tipo de pedido
			boolean mesero = false;
			for (int i = 0; i < empleados.size(); i++) {
				Empleado empleado = empleados.get(i);
				if (empleado.getCargo() == "mesero") {
					mesero = true;
				}
			}
			// Si si no hay alguno no se puede realizar
			if (!chef && !mesero) {
				return false;
			}
			// Si todo es aceptable se realiza el pedido
		}

		case "Para llevar": {

			// Rectificar el personal del restaurante y comprobar que haya el necesario para
			// el tipo de pedido
			boolean mesero = false;
			for (int i = 0; i < empleados.size(); i++) {
				Empleado empleado = empleados.get(i);
				if (empleado.getCargo() == "mesero") {
					mesero = true;
				}
			}
			// Si si no hay alguno no se puede realizar
			if (!chef && !mesero) {
				return false;
			}
		}
		
		}

		// Si todo es aceptable se realiza el pedido
		return true;
	}

	//	Metodo que determina si el restaurante posee los productos solicitados en un pedido
	public boolean verificarProductos(Pedido pedido) {

		// Identificar los productos solicitados y la cantidad de ellos
		ArrayList<Producto> productos = pedido.getProductos();
		for (int i = 0; i < productos.size(); i++) {
			Producto demanda = productos.get(i);

			// Rectificar que el restaurante tenga los productos solicitados en las cantidad pedidas.
			for (int j = 0; j < menu.size(); j++) {
				Producto oferta = menu.get(j);

				// Si no hay alguno de los productos disponibles o en la cantidad deseada no se puede realizar
				if (demanda.getNombre() != oferta.getNombre() || !oferta.getDisponiblidad()
						|| demanda.getCantidad() > oferta.getCantidad()) {
					return false;
				}
			}
		}

		// Si todo es aceptable se puede realizar el pedido
		return true;
	}
	
	
	//////// ESTADISTICAS \\\\\\\
	public Repartidor getRepartidorConMasPedidos(){
		Repartidor topRepartidor = new Repartidor();
		for (Repartidor repartidor: Repartidor.getRepartidores()) {
			int repartidos1 = repartidor.getCantidadPedidosEntregados();
			int repartidos2 = topRepartidor.getCantidadPedidosEntregados();
			if(repartidos1 > repartidos2) {
				topRepartidor = repartidor;
			}
		}
		return topRepartidor;
	}
	
	public Mesero getMeseroConMasPropinas() {
		Mesero topMeseroPropinas = new Mesero();
		for (Mesero mesero: Mesero.getMeseros()) {
			int Propinas1 = topMeseroPropinas.totalPropinas();
			int Propinas2 = mesero.totalPropinas();
			if(Propinas2 > Propinas1) {
				topMeseroPropinas = mesero;
			}
		}
		return topMeseroPropinas;
	}
	
	// Este metodo de estadisticas es fail mente modificable para obener mas estadisticas, toca agregar enlos otros lcases 
	public String estadisticasRestaurante() {
		Mesero topMesero = getMeseroConMasPropinas();
		Repartidor topRepartidor = getRepartidorConMasPedidos();
		return "El mesero con mas propinas es:" + topMesero.getNombre() + 
				"con" + topMesero.totalPropinas() + "Recibido en propinas." +
				"\n"+
				"El repartidor con mas pedidos repartidos es:" + topRepartidor.getNombre() + 
				"con" + topRepartidor.getCantidadPedidosEntregados() + "Pedidos entregados.";
	}
}
