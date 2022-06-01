package uiMain;

public class DatosAleatorios {
	// Nombres aleatorios para empleados
	public static String[] nombresAleatorios = { "Yasemin Phillips", "Lavinia Banks", "Kodi Paine", "Phebe Beaumont",
			"Amba Bowman", "Mila-Rose Bartlett", "Alejandro Ventura", "Zavier Burns", "Rivka Cantu",
			"Anastasia Mckeown", "Vivaan Craft", "Leonie Hardin", "Naima Peck", "Sammy-Jo Hollis", "Gus Jefferson",
			"Tate Greene", "Jai Holmes", "Ella-Mai Moran", "Clayton Hanna", "Guy Holding", "Cherie Valentine",
			"Zakariah Copeland", "Jane Mccartney", "Iosif Morrison", "Moshe Fenton", "Kylie Mcguire", "Mikael Caldwell",
			"Eshaal Zavala", "Amanpreet Galloway", "Marek Rocha", "Maison Alvarado", "Conner Contreras",
			"Macie Needham", "Huseyin Bassett", "Nuala Arroyo", "Brendan Whitworth", "Armaan Espinosa",
			"Danielius Bravo", "Maja Atherton", "Bryson Nava", "Mateusz Mackie", "Daphne Lim", "Duane Sargent",
			"Una Graham", "Sioned Crane", "Rogan Milne", "Teri Porter", "Garrett Vazquez", "Dominika Harvey",
			"Giselle Croft" };

	// Nombres aleatorios para productos
	public static String[] productosAleatorios = { "Pizza", "Hamburguesa", "Bandeja Paisa", "Sushi", "Empanadas",
			"Pollo frito", "Spaghetti", "Paella", "Tacos" };

	// Tipos de cargos en la cocina
	public static String[] cargosEnCocina = { "Chef ejecutivo", "Chef general", "Chef repostero", "Lavaplatos" };

	// Tipos de especialidades de chefs
	public static String[] especialidadesChefs = { "Saucier", "Poissonnier", "Rotisseur", "Grillardin", "Friturier",
			"Entremetier", "Tournant", "Garde Manger", "Boucher", "Patissier" };

	// Tipos de vehiculos
	public static String[] tiposVehiculos = { "Automovil", "Motoicicleta", "Bicicleta", "Cuatrimoto", "Monopatin",
			"Helicoptero", "Dirigible", "Globo aerostatico", "Tanque de guerra", "Excavadora industrial", "Tractor" };

	// Metodo util para sacar ints randoms
	public static int randInt(int min, int max) {
		return min + (int) (Math.random() * ((max - min) + 1));
	}

	// Metodo util para sacar bools randoms
	public static boolean randBool() {
		int rand = randInt(0, 1);
		if (rand == 0) {
			return true;
		} else {
			return false;
		}
	}

	// Metodo util para sacar strings randoms de una lista
	public static String randString(String[] lista) {
		return lista[randInt(0, lista.length - 1)];
	}
}
