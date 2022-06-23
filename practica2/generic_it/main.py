# @author: Emilio Porras
# @author: Esteban Garcia
# @author: Felipe Miranda
# @author: Erik Gonzalez
# @summary programa principal de la aplicacion
from base_datos.deserializador import Deserializador
from ui_main.ventana_inicio.inicio import VentanaInicio

if __name__ == "__main__":
    Deserializador.deserializarTodo()
    ventana = VentanaInicio()
    ventana.mainloop()


