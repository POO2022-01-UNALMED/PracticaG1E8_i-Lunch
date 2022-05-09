package gestorAplicacion.gestionRestaurante;

import java.util.ArrayList;
import gestorAplicacion.usuariosRestaurante.Empleado;

public class Restaurante {
//	Atributos de la clase Restaurante
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
	
//	Metodo constructor del la clase Restaurante
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
	}
	
// Metodos gets y sets de los atributos 
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
	
//	Metodo que rectifica si el restaurante cuenta con todos los implementos y personal necesario para
//	atender un pedido solicitado
	public boolean procesarPedido(Pedido pedido) {
		
//		Identificar los productos solicitados y la cantidad de ellos
//		Rectificar en el menú si se encuentran disponibles
//		Identificar el tipo de pedido
//		Rectificar el personal del restaurante y comprobar que haya el necesario
//		para el tipo de pedido
//		Si falla alguno de los anteriores no se puede realizar
//		Si todo es aceptable se realiza el pedido
		return true;
		
	}

//	Metodo que determina si existe el personal necesario 
//	en el restaurante para realizar un pedido solicitado
	public boolean verificarPersonal() {
//		Identificar el tipo de pedido
//		Rectificar el personal del restaurante y comprobar que haya el necesario
//		para el tipo de pedido
//		Si si no hay alguno no se puede realizar
//		Si todo es aceptable se realiza el pedido
		return true;
	}
	
//	Metodo que determina si el restaurante posee los productos 
//	solicitados en un pedido
	public boolean verificarProductos() {
//		Identificar los productos solicitados y la cantidad de ellos
//		Rectificar en el menú si se encuentran disponibles
//		Si si no hay alguno no se puede realizar
//		Si todo es aceptable se realiza el pedido
		return true;
	}
	
//	Analizando no le veo mucha lógica a esto ahora
	public boolean verificarBalance() {
		return true;
	}
	

	
	
	
	

}
