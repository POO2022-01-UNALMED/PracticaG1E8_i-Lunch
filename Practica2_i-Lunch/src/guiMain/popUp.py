from tkinter import messagebox

class PopUp():
    def __init__(self, mensaje):
        self._mensaje = mensaje
        messagebox.showinfo(title = "Manejo de errores de la aplicacion", message = mensaje)