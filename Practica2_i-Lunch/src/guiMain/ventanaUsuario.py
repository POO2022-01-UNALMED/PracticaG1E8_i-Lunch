from tkinter import *

class VentanaUsuario(Tk):
    def __init__(self):
        super().__init__()

        # Configuracion de la ventana

        self.title('i-Lunch - Ventana de Usuario')
        self.option_add("*tearOff",  False)
        self.geometry("1280x720")

        # ! Continuar