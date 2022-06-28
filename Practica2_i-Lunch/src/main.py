from guiMain.ventanaInicio import VentanaInicio
from gestorAplicacion.inicializar import inicializar
from baseDatos.deserializador import deserializarTodo

# Deserializar
deserializarTodo()

# Inicializar datos si no los hay
inicializar()

# Crear ventana de Tkinter
ventana =  VentanaInicio()

# Loop de Tkinter
ventana.mainloop()