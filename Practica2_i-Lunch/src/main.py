from baseDatos.deserializador import deserializarTodo

from gestorAplicacion.inicializar import inicializar

from guiMain.ventanaInicio import VentanaInicio

# Deserializar

deserializarTodo()

# Inicializar datos si no los hay

inicializar()

# Crear ventana de Tkinter

ventana = VentanaInicio()

# Loop de Tkinter

ventana.mainloop()