package gestorAplicacion.gestionRestaurante;

import java.util.ArrayList;

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
	private float balanceCuenta;

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

	public float getBalanceCuenta() {
		return balanceCuenta;
	}

	public void setBalanceCuenta(float balanceCuenta) {
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
		case "A domicilio": {

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
		case "Para consumir en la tienda": {

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

	// Metodo que determina si el restaurante posee los productos solicitados en un
	// pedido
	public boolean verificarProductos(Pedido pedido) {
		for (Producto demanda : pedido.getProductos()) {
			boolean existe = false;
			boolean cantidad = false;
			boolean disponible = false;
			for (Producto oferta : menu) {
				if (demanda.getNombre() == oferta.getNombre()) {
					existe = true;
					disponible = oferta.getDisponiblidad();
					if (oferta.getCantidad() >= demanda.getCantidad()) {
						cantidad = true;
					}
				}

			}
			if (!existe || !cantidad || !disponible) {
				return false;
			}
		}

		return true;
	}

	//////// ESTADISTICAS \\\\\\\
	public Repartidor getRepartidorConMasPedidos() {
		// Repartidor vacio para que el metodo funcione
		Repartidor topRepartidor = new Repartidor();
		// Loop para encontrar el repartidor con mas pedidos repartidos
		for (Repartidor repartidor : Repartidor.getRepartidores()) {
			// Comparamos cada repartidor en la lista de repartidores
			int repartidos1 = repartidor.getCantidadPedidosEntregados();
			int repartidos2 = topRepartidor.getCantidadPedidosEntregados();
			if (repartidos1 > repartidos2) {
				topRepartidor = repartidor;
			}
		}
		return topRepartidor;
	}

	public Mesero getMeseroConMasPropinas() {
		// Mesero vacio para que el metodo funcione
		Mesero topMeseroPropinas = new Mesero();
		// Loop para encontrar al mesero con mas propinas
		for (Mesero mesero : Mesero.getMeseros()) {
			// Comparamos todos los meseros en la lista de meseros
			int Propinas1 = topMeseroPropinas.totalPropinas();
			int Propinas2 = mesero.totalPropinas();
			if (Propinas2 > Propinas1) {
				topMeseroPropinas = mesero;
			}
		}
		return topMeseroPropinas;
	}

	public float PromedioPropinasMeseros() {
		int cantidad = 0;
		float propinas = 0;
		for (Mesero mesero : Mesero.getMeseros()) {
			cantidad += 1;
			propinas += mesero.totalPropinas();
		}
		return propinas / cantidad;
	}

	public float promedioPedidosRepartidores() {
		int cantidad = 0;
		float pedidos = 0;
		for (Repartidor repartidor : Repartidor.getRepartidores()) {
			cantidad += 1;
			pedidos += repartidor.getCantidadPedidosEntregados();
		}
		return pedidos / cantidad;
	}

	// Este es el metodo para mostrar todas las estadisticas que querramos
	// implementar juntas.
	public String estadisticasRestaurante() {
		Mesero topMesero = getMeseroConMasPropinas();
		Repartidor topRepartidor = getRepartidorConMasPedidos();
		return "El mesero con mas propinas es: " + topMesero.getNombre() +

				" con $" + topMesero.totalPropinas() + " Recibido en propinas." +

				"\n" +

				"El repartidor con mas pedidos repartidos es: " + topRepartidor.getNombre() +

				" con " + topRepartidor.getCantidadPedidosEntregados() + " Pedidos entregados." + "\n" +

				"En promedio un mesero recibe $" + PromedioPropinasMeseros() + " en propinas en el restaurante." + "\n"
				+

				"En promedio un mesero ha entregado " + promedioPedidosRepartidores()
				+ " pedidos a clientes del restaurante.";
	}

	// Metodo chequear pedido

	public Boolean chequearPedido(Pedido pedido) {
		if (verificarProductos(pedido) && verificarPersonal(pedido)) {
			return true;
		}
		return false;
	}

	// Agregar un pedido al historial
	public String agregarPedido(Pedido pedido) {

		if (!pedidos.contains(pedido)) {
			pedidos.add(pedido);
			return "Pedido anadido con exito";
		} else {
			return "ERROR: El pedido ya se encuentra anadido";
		}
	}
}
