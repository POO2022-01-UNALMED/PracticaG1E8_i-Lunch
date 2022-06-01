package baseDatos;

import java.io.File;
import java.io.FileInputStream;
import java.io.FileNotFoundException;
import java.io.IOException;
import java.io.ObjectInputStream;
import java.util.ArrayList;
import java.util.List;

import gestorAplicacion.gestionRestaurante.*;
import gestorAplicacion.usuariosRestaurante.*;

public class Deserializador {
	public static <E> void deserializador(List<E> list, String className) {
		FileInputStream fileIn;
		try {
			// Creamos una cadena con la ruta del archivo que vamos a cargar
			String path = System.getProperty("user.dir") + "/src/baseDatos/temp/" + className + ".txt";
			System.out.println(path);
			// Utilizamos un file para crear este archivo si no existe aun
			File archivo = new File(path);
			archivo.createNewFile(); // Crea un nuevo archivo si no existe

			// Usamos un FileInputStream para poder saber de donde cargar el archivo
			fileIn = new FileInputStream(path);

			// Si el archivo esta vacio se lanza un throw EOFException y se muestra como un
			// mensaje de vacio, pero si no se usa el objeto in para leer el archivo
			ObjectInputStream in = new ObjectInputStream(fileIn);

			// Lee el listado de elementos
			ArrayList<E> listado = (ArrayList<E>) in.readObject();

			// Recorro el ArrayList
			for (E el : listado) {
				list.add(el);
			}

			in.close();
			fileIn.close();

		} catch (FileNotFoundException e) {
			e.printStackTrace();

		} catch (IOException e) {
			System.out.println("Esta vacio");

		} catch (ClassNotFoundException e) {
			e.printStackTrace();
		}
	}

	/* Funcion para deserializar toda la aplicacion Generic IT */
	public static void deserializarTodo() {
		Deserializador.deserializador(Pedido.getPedidos(), "pedidos");
		Deserializador.deserializador(Producto.getProductos(), "productos");
		Deserializador.deserializador(Restaurante.getRestaurantes(), "restaurantes");
		Deserializador.deserializador(Cliente.getClientes(), "clientes");
		Deserializador.deserializador(Empleado.getEmpleados(), "empleados");
		Deserializador.deserializador(Administrador.getAdministradores(), "administradores");
		Deserializador.deserializador(Mesero.getMeseros(), "meseros");
		Deserializador.deserializador(Repartidor.getRepartidores(), "repartidores");
	}
}
