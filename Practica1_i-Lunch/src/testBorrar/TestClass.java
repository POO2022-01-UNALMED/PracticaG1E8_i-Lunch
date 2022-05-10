package testBorrar;

import baseDatos.*;
import gestorAplicacion.gestionRestaurante.*;
import gestorAplicacion.usuariosRestaurante.*;

public class TestClass {

	public static void main(String[] args) {
		Deserializador.deserializarTodo();
		
		Pedido test1 = new Pedido(null, 0, null, null, null);
		Producto test2 = new Producto(null, null, 0, false, false, 0);
		Restaurante test3 = new Restaurante(null, 0, 0, null, null, false, 0, null, null, null, 0);
		Administrador test4 = new Administrador();
		Chef test5 = new Chef();
		Cliente test6 = new Cliente();
		Empleado test7 = new Empleado();
		Mesero test8 = new Mesero();
		Repartidor test9 = new Repartidor();
		
		Serializador.serializarTodo();
	}
}
