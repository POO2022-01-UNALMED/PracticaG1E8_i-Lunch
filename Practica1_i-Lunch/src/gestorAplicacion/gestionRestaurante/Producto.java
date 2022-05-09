package gestorAplicacion.gestionRestaurante;

public class Producto {
	private String nombre;
	private String descripcion;
	private int precio;
	private boolean disponiblidad;
	private boolean restriccion;
	
	public Producto(String nombre, String descripcion, int precio, boolean disponiblidad, boolean restriccion) {
		super();
		this.nombre = nombre;
		this.descripcion = descripcion;
		this.precio = precio;
		this.disponiblidad = disponiblidad;
		this.restriccion = restriccion;
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

	public boolean isDisponiblidad() {
		return disponiblidad;
	}

	public void setDisponiblidad(boolean disponiblidad) {
		this.disponiblidad = disponiblidad;
	}

	public boolean isRestriccion() {
		return restriccion;
	}

	public void setRestriccion(boolean restriccion) {
		this.restriccion = restriccion;
	}
}
