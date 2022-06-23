'''
@File    :   bienvenida.py
@Time    :   2022/01/29
@Author  :   Erik Gonzalez
@Version :   1.0
@Desc    :   La clase Bienvenida representa p1, basado en la figura 1 del documento practica 2
'''

from ui_main.ventana_usuario import iniciar_ventana_usuario
from tkinter import Label, Entry, Button, Text, PhotoImage, Frame, INSERT, scrolledtext
import os
import pathlib

class Bienvenida(Frame):
    def __init__(self, window):
        super().__init__(window)
        self._window = window
        self._p3 = Frame(self)
        self._p4 = Frame(self)
        self._next_el = 0
        saludo = Entry(self._p3, width=100)
        self.saludo2 = scrolledtext.ScrolledText(self._p3, height=5)
        self.saludo2.tag_configure("center", justify="center")
        saludo.insert(INSERT, "Bienvenido al software de Generic IT")
        self.saludo2.insert(INSERT, "Generic IT es una compañía tecnológica que se encarga de la reparación de equipos electrónicos. Se busca crear un programa que emule las interacciones de Generic IT, para mejorar la organización de la empresa y proveer un mejor servicio. Se tendrá en cuenta toda la cadena de servicio, desde que llega el cliente con un producto a reparar, su paso por las manos del ténico, las partes que tendrán que ser cambiadas, hasta finalizar con la devolución del producto y el pago del servicio.")
        self._pantallazos = []
        for i in range(0, 5):
            path = os.path.join(pathlib.Path(__file__).parent.parent.parent.absolute(),'assets/pantallazo_{0}.png'.format(i))
            pantallazo = PhotoImage(file=path)
            self._pantallazos.append(pantallazo)

        self._label = Label(self._p4, image=self._pantallazos[0], height=500, width=750)
        self._label.bind('<Enter>', self.proximo)
        self._label.pack()

        button = Button(self._p4, text="Ventana Principal del Admin", command=self.abrir_ventana_principal)
        button.pack()
        saludo.grid()
        self._p3.pack()
        self._p4.pack()

    # Actualiza el proximo pantallazo de la aplicacion
    def proximo(self, _):
        if self._next_el < 4:
            self._next_el = self._next_el + 1
        else:
            self._next_el = 0

        self._label.configure(image=self._pantallazos[self._next_el])
        self._label.image = self._pantallazos[self._next_el]

    # Carga la ventana principal del admin y cierra la ventana actual
    def abrir_ventana_principal(self):
        self._window.destroy()
        iniciar_ventana_usuario()
