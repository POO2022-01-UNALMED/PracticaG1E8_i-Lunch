'''
@File    :   hoja_vida.py
@Time    :   2022/01/29
@Author  :   Erik Gonzalez
@Version :   1.0
@Desc    :   La clase HojaVida representa p2, basado en la figura 1 del documento practica 2
'''

from tkinter import Label, Entry, Button, Text, PhotoImage, Frame, INSERT
import os
import pathlib

class HojaVida(Frame):
    _posicion_imagen = [(0, 0), (0, 1), (1, 0), (1, 1)]
    def __init__(self, window):
        super().__init__(window)
        self._p5 = Frame(self)
        self._p6 = Frame(self)
        self._text = None
        self._next_hv = 0
        self._photos = [None, None, None, None]
        self._labels = []
        self.cargar_hv(0)
        for i in range(0, 4):
            label = Label(self._p6, width=300, height=200)
            (r, c) = HojaVida._posicion_imagen[i]
            label.grid(row=r, column=c)
            self._labels.append(label)
            # Se cargan las primeras imagenes
            self.cargar_hv_imagen(0, i)
        self._p5.grid()
        self._p6.grid()


    # Se usa para mostrar la hoja de vida que sigue, aumentando el atributo next_hv
    def proximo(self, _):
        if self._next_hv < 3:
            self._next_hv = self._next_hv + 1
        else:
            self._next_hv = 0

        self._photos = [None, None, None, None]
        self.cargar_hv(self._next_hv)
        for i in range(0, 4):
            self.cargar_hv_imagen(self._next_hv, i)

    # Carga el component imagen que sirve para mostrar las fotos
    def cargar_hv_imagen(self, hv_num, numero):
        path = os.path.join(pathlib.Path(__file__).parent.parent.parent.absolute(),'assets/hv_{0}_{1}.png'.format(hv_num, numero))
        photo = PhotoImage(file=path)
        self._labels[numero].configure(image=photo)
        self._labels[numero].image = photo

    # Carga el texto para la hoja de vida respecto al numero asignado 
    def cargar_hv(self, numero):
        self._text = Text(self._p5, height=10)
        self._text.grid(row=1, column=0)
        self._text.bind('<Button-1>', self.proximo)

        path = os.path.join(pathlib.Path(__file__).parent.parent.parent.absolute(), 'assets/hv{0}.txt'.format(numero))

        with open(path, "r+") as hv_text:
            self._text.insert(INSERT, hv_text.read())
