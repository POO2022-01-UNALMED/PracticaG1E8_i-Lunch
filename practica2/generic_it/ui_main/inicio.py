from tkinter import Text, Frame, INSERT, scrolledtext
import os
import pathlib
'''
@File    :   inicio.py
@Time    :   2022/01/29
@Author  :   Erik Gonzalez
@Version :   1.0
@Desc    :   Ventana de inicio, es la primera en mostrarse cuando se ejecuta el programa
'''

class Inicio(Frame):
    def __init__(self, window):
        super().__init__(window)
        text = scrolledtext.ScrolledText(self)
        path = os.path.join(pathlib.Path(__file__).parent.parent.absolute(),"instrucciones.txt")
        with open(path, "r+") as instrucciones:
            text.insert(INSERT, instrucciones.read())
        text.tag_configure('center', justify='center')
        text.pack()

