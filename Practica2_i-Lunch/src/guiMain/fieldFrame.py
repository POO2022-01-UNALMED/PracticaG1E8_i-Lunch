from tkinter import *

class FieldFrame(Frame):

    # Constructor
    # tituloCriterios: Titulo para la columna "Criterio" 
    # criterios: Array con los nombres de los criterios 
    # tituloValores: Titulo para la columna "Valor" 
    # valores: Array con los valores iniciales. Si None, no hay valores iniciales 
    # habilitado: Array con los campos no-editables por el usuario. Si None, todos son editables 
    
    def __init__(self, ventana, tituloCriterios = "", criterios = None, tituloValores = "", valores = None, habilitado = None):
        super().__init__(ventana)
        self._tituloCriterios = tituloCriterios
        self._criterios = criterios
        self._tituloValores = tituloValores
        self._valores = valores
        self._habilitado = habilitado

        self._elementos = []

        labelTituloCriterios = Label(self, text = tituloCriterios, font= ("Verdana", 16))
        labelTituloValores = Label(self, text = tituloValores, font= ("Verdana", 16))

        labelTituloCriterios.grid(column=0, row=0, padx = (10,10), pady = (10,10))
        labelTituloValores.grid(column=1, row=0, padx = (10,10), pady = (10,10))

        for  i in range(len(criterios)):
            labelCriterio = Label(self, text = criterios[i], font = ("Verdana", 16))
            labelCriterio.grid(column=0, row=i+1, padx = (10,10), pady = (10,10))

            entryValor = Entry(self, font = ("Verdana", 16))
            entryValor.grid(column=1, row=i+1, padx = (10,10), pady = (10,10))

            if valores is not None:
                entryValor.insert(0, valores[i])

            if habilitado is not None and not habilitado[i]:
                entryValor.configure(state = DISABLED)
                
            self._elementos.append(entryValor)

    # GetValue
    # criterio: El criterio cuyo valor se quiere obtener

    def getValue(self, criterio):
        indice = self._criterios.index(criterio)
        return self._elementos[indice].get()
