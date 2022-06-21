from tkinter import *
from tkinter import ttk
import pathlib
import os
class VentanaUsuario(Tk):
    def __init__(self):
        super().__init__()

        # Configuracion de la ventana

        self._p1 = Frame()
        self._p2 = Frame()
        self._p3 = Frame()

        self.title('i-Lunch - Ventana de Usuario')
        self.option_add("*tearOff",  False)
        self.geometry("1280x720")

        self._barraMenu = Menu(self)
        archivo = Menu(self._barraMenu)
        archivo.add_command(label = "Aplicacion", command = lambda: print("IDK"))
        archivo.add_command(label = "Salir", command = lambda: self.cerrar())
        self._barraMenu.add_cascade(label = "Archivo", menu = archivo)

        procesosYConsultas = Menu(self._barraMenu)
        procesosYConsultas.add_command(label="Informacion del restaurante", command=lambda:print("IDK"))
        procesosYConsultas.add_command(label="Gestionar Menu", command=lambda: print("IDK"))
        procesosYConsultas.add_command(label="Gestionar Personal", command=lambda: print("IDK"))
        procesosYConsultas.add_command(label="Cola de pedidos", command=lambda: print("IDK"))
        procesosYConsultas.add_separator()
        procesosYConsultas.add_command(label="Simular pedido", command=lambda: print("IDK"))
        procesosYConsultas.add_command(label="Gestionar clientela", command=lambda: print("IDK"))
        self._barraMenu.add_cascade(label="Procesos Y Consultas", menu= procesosYConsultas)


        ayuda = Menu(self._barraMenu)
        ayuda.add_command(label="Acerca de", command = lambda: print("IDK"))
        self._barraMenu.add_cascade(label="Ayuda", menu = ayuda)


        self.config(menu = self._barraMenu)

    def cerrar(self):
        from guiMain.ventanaInicio import VentanaInicio
        VentanaInicio()






ventana = VentanaUsuario()

# Loop de Tkinter

ventana.mainloop()

