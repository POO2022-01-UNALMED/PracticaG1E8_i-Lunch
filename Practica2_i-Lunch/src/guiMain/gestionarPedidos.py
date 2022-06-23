from tkinter import *
from gestorAplicacion.gestionRestaurante.pedido import Pedido

class GestionarPedidos(Tk):
    def __init__(self):
        super().__init__()

        # Configuracion de la ventana

        self.title('i-Lunch - Cola de pedidos')
        self.option_add("*tearOff",  False)
        self.geometry("1280x720")
        self.resizable(False,False)

        