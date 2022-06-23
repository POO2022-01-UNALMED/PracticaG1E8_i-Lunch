from operator import length_hint
from tkinter import *
from unicodedata import numeric

from numpy import empty
from .empty_exception import EmptyException
from .numeric_exception import NumericException
from .length_exception import LengthException
from .empty_exception import EmptyException
'''
@File    :   field_frame.py
@Time    :   2022/01/29
@Author  :   Emilio Porras, Esteban Garcia
@Version :   1.0
@Desc    :   FieldFrames necesarios para todo el codigo con insercion de datos. 
'''
#Creación de la clase field frame, de la cual surgirán todos los formularios de la aplicación
class FieldFrame(Frame):
    def __init__(self, master, tituloCriterios, criterios, tituloValores, valores, habilitado, tipos):
        self._tituloCriterios = tituloCriterios
        self._criterios = criterios
        self._tituloValores = tituloValores
        self._valores = valores
        self._habilitado = habilitado
        self._entries = list()
        self._tipos = tipos
        super().__init__(master)
        self.actualizacion()

#Funcion que permite crear el grid del FieldFrame y actualizarlo con nuevos datos.
    def actualizacion(self):
        Label(self, text=self._tituloCriterios).grid(padx = 80, column = 0, row = 0)
        Label(self, text=self._tituloValores).grid(padx = 80, column = 1, row = 0)
        for i in range(1, len(self._valores)+1):
            Label(self, text=self._criterios[i-1]).grid(padx = 80, pady=2, column=0, row=i)
            if self._criterios[i-1] in self._habilitado:
                texto = StringVar(value=self._valores[i-1])
                entrada = Entry(self, width = 40, textvariable=texto, state=DISABLED, justify="center")
            else:
                texto = StringVar(value=self._valores[i-1])
                entrada = Entry(self, width = 40, textvariable=texto, justify="center")
        
            entrada.grid(pady =2, column=1, row=i)
            self._entries.append(entrada)

        
    #Funcion auxiliar del boton aceptar
    def aceptarCheck(self):
        criteriosFaltantes = []
        datosErroneos = []
        faltan = False
        erroneos = False
        for i in range(len(self._entries)): #_entries es la lista con las entradas.
            self._valores[i] = self._entries[i].get()
            if self._valores[i] == "":
                faltan = True
                criteriosFaltantes.append(self._criterios[i])

        if faltan:
            faltantes = ", ".join(criteriosFaltantes)
            raise EmptyException("Los siguientes campos faltan por rellenar: " + faltantes)
        
        for i in range(len(self._entries)):
            if self._tipos[i] == 0:
                if self._valores[i].isdigit():
                    erroneos = True
                    datosErroneos.append(self._criterios[i])
                elif len(self._valores[i]) < 3: 
                    raise LengthException(self._criterios[i] + " muy corto.")
            elif self._tipos[i] == 1:
                if not self._valores[i].isdigit():
                    erroneos = True
                    datosErroneos.append(self._criterios[i])
        if erroneos:
            errores = ", ".join(datosErroneos)
            raise NumericException("Tipo de dato erroneo en: " + errores)


    
    #Funcion auxiliar del boton borrar
    def borrarEntry(self):
        for entrada in self._entries:
            entrada.delete(0, "end")
        
    def getValue(self, criterio):
        criterios_dict = dict(zip(self._criterios, self._valores))
        return criterios_dict[criterio]
    
    def getCriterios(self): 
        return self._criterios
        
    def getValores(self):
        return self._valores

    def setValores(self, valores):
        self._valores = valores
    
    def setEntries(self, entries):
        self._entries = entries


    def crearBotones(self, comando1):
        aceptar = Button(self, text="Aceptar",command=comando1).grid(pady = 50, column = 0, row = len(self._criterios)+1)
        borrar = Button(self, text="Borrar",command=self.borrarEntry).grid(pady = 50, column = 1, row = len(self._criterios)+1)
