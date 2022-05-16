package testBorrar;

import baseDatos.*;
import gestorAplicacion.gestionRestaurante.*;
import gestorAplicacion.usuariosRestaurante.*;

public class TestClass {

	public static void main(String[] args) {
		Deserializador.deserializarTodo();
		
		Pedido test1 = new Pedido();
		Producto test2 = new Producto();
		Restaurante test3 = new Restaurante("RestauranteTest1", 0, 0, null, null, false, 0, null, null, null, 0);
		Administrador test4 = new Administrador();
		Chef test5 = new Chef();
		Cliente test6 = new Cliente();
		Empleado test7 = new Empleado();
		Mesero test8 = new Mesero();
		Repartidor test9 = new Repartidor(123456789, "Pepito Pérez", "Repartidor" , true, 100, test3, true, "ABC-123", "Moto");
		
		System.out.println(test9.informacion());
		
		Serializador.serializarTodo();
	}
}
