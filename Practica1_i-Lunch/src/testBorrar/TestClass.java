package testBorrar;

import java.util.ArrayList;

import baseDatos.*;
import gestorAplicacion.gestionRestaurante.*;
import gestorAplicacion.usuariosRestaurante.*;

public class TestClass {

	public static void main(String[] args) {
		//Deserializador.deserializarTodo();
		Restaurante restaurante = new Restaurante("RestauranteTest1", 0, 0, null, null, false, 0, null, new ArrayList<Producto>(),  new ArrayList<Pedido>(), 0);
		Administrador admin = new Administrador();
		admin.setRestaurante(restaurante);
		admin.crearProducto("Hamburguesa",  "Hamburguesa con queso", 15000, true, false, 10);
		admin.crearProducto("Perro",  "Perro caliente", 9000, true, false, 5);
		admin.crearProducto("Pizza",  "Pizza con pepperonni", 20000, true, false, 7);
		admin.crearProducto("Papitas",  "Papas cochinas", 13000, true, false, 15);
		admin.crearProducto("Sushi",  "Su chicharron", 25000, true, false, 3);	
		System.out.println(restaurante.getMenu().size());
		admin.simularPedido(new Cliente());
		System.out.println(restaurante.getPedidos().size());
		
		//Serializador.serializarTodo();
	}
}
