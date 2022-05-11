package gestorAplicacion.gestionRestaurante;

import java.io.Serializable;
import java.util.ArrayList;

public class Producto implements Serializable {
	
	private static final long serialVersionUID = 1L;
	private static ArrayList<Producto> productos;
	static {
		productos = new ArrayList<Producto>();
	}
	
	private String nombre;
	private String descripcion;
	private int precio;
	private boolean disponiblidad;
	private boolean restriccion;
	private int cantidad;
	private boolean estado;
	
	public Producto(String nombre, String descripcion, int precio, boolean disponiblidad, boolean restriccion, int cantidad) {
		super();
		this.nombre = nombre;
		this.descripcion = descripcion;
		this.precio = precio;
		this.disponiblidad = disponiblidad;
		this.restriccion = restriccion;
		this.cantidad = cantidad;
		this.estado = false;/*<<-- false significa sin preparar y true, preparado*/
		
	}

	public String getNombre() {
		return nombre;
	}

	public void setNombre(String nombre) {
		this.nombre = nombre;
	}

	public String getDescripcion() {
		return descripcion;
	}

	public void setDescripcion(String descripcion) {
		this.descripcion = descripcion;
	}

	public int getPrecio() {
		return precio;
	}

	public void setPrecio(int precio) {
		this.precio = precio;
	}

	public boolean getDisponiblidad() {
		return disponiblidad;
	}

	public void setDisponiblidad(boolean disponiblidad) {
		this.disponiblidad = disponiblidad;
	}

	public boolean getRestriccion() {
		return restriccion;
	}

	public void setRestriccion(boolean restriccion) {
		this.restriccion = restriccion;
	}

	public int getCantidad() {
		return cantidad;
	}

	public void setCantidad(int cantidad) {
		this.cantidad = cantidad;
	}

	public boolean getEstado() {
		return estado;
	}

	public void setEstado(boolean estado) {
		this.estado = estado;
	}
	
	public static ArrayList<Producto> getProductos() {
		return productos;
	}
}
