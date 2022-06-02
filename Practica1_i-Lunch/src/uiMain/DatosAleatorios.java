package uiMain;

public class DatosAleatorios {
	// Nombres aleatorios para empleados y clientes
	public static String[] nombresAleatorios = { "Phoebe Bright", "Nikolas Beltran", "Jimmy Harrell", "Onur Macias",
			"Russell Oconnor", "August Roberson", "Madeline Yang", "Dilan Lutz", "Sorcha Sharples", "Chase Parker",
			"Bob Quinn", "Veronika O'Neill", "Conall Holloway", "Hermione Durham", "Calista Morton", "Yolanda Thatcher",
			"Suhail O'Brien", "Kayden Reeve", "Carlo Wells", "Rosemarie Cortes", "Kelsie Strickland", "Jaheim Wickens",
			"Piper Whittaker", "Roy Barker", "Carter Sumner", "Jayda Chaney", "Heath Thomas", "Devan Lopez",
			"Leopold Simpson", "Domonic Neal", "Verity Shah", "Chaya Ruiz", "Niyah Mercado", "Gerrard Gonzalez",
			"Izabelle Field", "Ashton Solis", "Aimee Nelson", "Abbey Howells", "Giovanni Dawson", "Kason Kline",
			"omas Whittington", "Dominika Mccallum", "Roxy Kouma", "Faizaan Mcdougall", "Sahara Sweet", "Gage Humphrey",
			"Marcie Dodd", "Danyal Howe", "Asiyah Rivers", "Isla-Grace Macgregor", "Sammy Love", "Pippa Simons",
			"Sarina Best", "Finn Clements", "Adnaan Bradley", "Kenzo Allman", "Ayat Iles", "Caspar Rice",
			"Arif Aguilar", "Pearce Reyes", "Jorge Cantrell", "Joanna Lim", "Dwayne Mcmanus", "Addie Felix",
			"Charis Clegg", "Miah O'Moore", "Tayyab Thorpe", "Hannah Watts", "Milli Laing", "Huda Mcmahon",
			"Keziah Decker", "Theia Glover", "Isobel Henderson", "Marsha Andersen", "Soraya Roman", "Radhika Camacho",
			"Clara Hopper", "Halimah Derrick", "Evie-Grace Forbes", "Kieren Hickman", "Viola Wilkinson",
			"Adriana Navarro", "Saba Mckenzie", "Aaminah Poole", "Kalum Plant", "Ursula Mosley", "Nour Maynard",
			"Frances Everett", "Umayr Wheatley", "Leona Small", "Kylan Zhang", "Aneesah Burgess", "Saara Redmond",
			"Princess Fletcher", "Margie David", "Hari Langley", "Kayson Stark", "Shana Medrano", "Caoimhe Talley",
			"Zaid Hawkins" };

	// Nombres aleatorios para productos
	public static String[] productosAleatorios = { "Pizza sin pinha", "Hamburguesa", "Bandeja Paisa", "Sushi",
			"Empanadas", "Pollo frito", "Spaghetti", "Paella", "Tacos", "Fondue", "Burrito", "Chop Suey", "Ratatouille",
			"Ceviche", "Risotto", "Papas fritas", "Lasagna", "Arepas", "Kebab", "Langosta", "Donas", "Curry",
			"Chicken Teriyaki", "Ramen", "Tamales", "Tortilla", "Shawarma", "Hummus", "Ajiaco", "Fish and Chips",
			"Rollitos de Primavera", "Buhuelos", "Pozole", "Milanesa", "Croissant", "Helado", "Fideos", "Tofu",
			"Sashimi", "Costillas BBQ", "Cupcake", "Pastel", "Brownies (Legales)", "Nachos", "Pastas", "Mac and Cheese",
			"Ensalada", "Quesadilla", "Galletas", "Fajitas", "Macarrones", "Churrasco", "Tiramisu", "Tarta de Manazana",
			"Churros", "Hot Dog" };

	// Tipos de cargos en la cocina
	public static String[] cargosEnCocina = { "Chef ejecutivo", "Chef general", "Chef repostero", "Lavaplatos" };

	// Tipos de especialidades de chefs
	public static String[] especialidadesChefs = { "Saucier", "Poissonnier", "Rotisseur", "Grillardin", "Friturier",
			"Entremetier", "Tournant", "Garde Manger", "Boucher", "Patissier" };

	// Tipos de vehiculos
	public static String[] tiposVehiculos = { "Automovil", "Motoicicleta", "Bicicleta", "Cuatrimoto", "Monopatin",
			"Helicoptero de la Policia", "Zeppelin", "Globo Aerostatico", "Tanque de Guerra Sovietico",
			"Excavadora Industrial", "Tractor", "Helicoptero de Guerra Apache AH-64", "Xavineta",
			"Monoplaza de Formula 1", "OVNI", "Papamovil" };

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
