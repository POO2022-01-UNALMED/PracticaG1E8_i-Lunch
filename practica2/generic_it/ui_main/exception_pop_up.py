from tkinter import messagebox

class ExceptionPopUp():
    def __init__(self, mensaje):
        self._mensaje = mensaje
        messagebox.showinfo(title = "Error en la aplicación", message = mensaje)
        
    

    