package uiMain;

import java.io.IOException;
import java.util.Scanner;


public class Consola {

	static Scanner sc = new Scanner(System.in);
	
	//Se crean metodos para utilizar el Scanner de Java.
	static int readInt() {
		return sc.nextInt();
	}

	static String readString() {
		return sc.nextLine();
	}

	static double readDouble() {
		return sc.nextDouble();
	}

	public static void main(String[] args) {
		//Deserializa todos los objetos.
		
		System.out.println(""); //Mensaje de bienvenida
		
		String opcion = "0";
		
		do {
			System.out.println(""); //Mensaje de elección
			System.out.println(" 1. Ver información del Restaurante"); 
			System.out.println(" 2. Gestionar Menú");
			System.out.println(" 3. Gestionar Pesonal");
			System.out.println(" 4. Cola de pedidos");
			System.out.println(" 5. Pagar nómina");
			System.out.println(" Funciones extras del sistemas");
			System.out.println(" 6. Simular Pedido");
			System.out.println(" 7. Gestionar Clientela");
			System.out.println(" 8. Guardar y Salir");

			System.out.println("Elija una opcion: ");
			try {
				opcion =  readString();
			} catch (Exception e) {
				// TODO: handle exception
				opcion = "0";
			}
			

			switch (opcion) {

			case "1": // David
				// Muestra la info basica del restaurante
				/* 1. empleados
				 * 2. productos
				 * 3. historial pedidos
				 * 4. balance de cuenta
				 * 5. estadisticas (Funcionalidad)
				 * 6. Volver al menu principal*/
				break;
				
			case "2": // Emma
				/* 1. Ver menu.
				 * 2. Crear Producto
				 * 3. Eliminar Producto
				 * 4. Actualizar Producto
				 * 4.1 Nombre
				 * 4.2 Descripción
				 * 4.3 Precio
				 * 4.4 Restriccion
				 * 4.5 Disponibilidad
				 * 4.6 Cantidad
				 * 5. Volver al menu principal*/	
				
				break;
				
			case "3": //Jero
				/* 1. Ver personal
				 * 2. Contratar empleado
				 * 2.1 Manual
				 * 2.2 Automatico
				 * 3. Despedir empleado 
				 * 4. Volver al menu principal*/
				break;
				
			case "4": // Apa
				// Se muestran todos los pedidos en espera
				/* 1. Aceptar
				 * 2. Rechazar */
				break;
				
			case "5": // Emma
				/* 1. Pagar a un empleado
				 * 2. Pagar a todos los empleados*/
				break;
			
			case "6": // Apa
				// Mensaje de control
				// Cliente, código pedido
				break;	
				
			case "7": // Jero
				// 1. Ver clientes
				// 2. Crear cliente
				// 2.1 Manual
				// 2.2 Automatico
				break;	
			
			case "8": // David
				//Serializador
				break;
				
			default:
				System.out.println("La opción ingresada no es valida. Por favor intentelo nuevamente"); //Mensaje de control para inputs invalidos.
				break;
			
			}
			
		} while (!opcion.equals("8"));

}
	

}

