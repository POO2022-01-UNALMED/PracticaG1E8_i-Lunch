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

        # Lista de elementos
        self._elementos = []

        # Crear y colocar titulo de los criterios
        labelTituloCriterios = Label(self, text = tituloCriterios, font= ("Verdana", 14))
        labelTituloCriterios.grid(column=0, row=0, padx = (10,10), pady = (10,10))

        # Crear y colocar titulo de los valores
        labelTituloValores = Label(self, text = tituloValores, font= ("Verdana", 14))
        labelTituloValores.grid(column=1, row=0, padx = (10,10), pady = (10,10))

        # Crear cada uno de los criterios
        for  i in range(len(criterios)):
            # Crear y colocar nombre de cada criterio
            labelCriterio = Label(self, text = criterios[i], font = ("Verdana", 12))
            labelCriterio.grid(column=0, row=i+1, padx = (10,10), pady = (10,10))

            # Crear y colocar entrada de cada criterio
            entryValor = Entry(self, font = ("Verdana", 12))
            entryValor.grid(column=1, row=i+1, padx = (10,10), pady = (10,10))

            # Colocar el valor inicial si lo hay
            if valores is not None:
                entryValor.insert(0, valores[i])

            # Si el campo es no-editable, deshabilitarlo
            if habilitado is not None and not habilitado[i]:
                entryValor.configure(state = DISABLED)
            
            # Anadir a la lista de elementos
            self._elementos.append(entryValor)

    # GetValue
    # criterio: El criterio cuyo valor se quiere obtener

    def getValue(self, criterio):
        indice = self._criterios.index(criterio)
        return self._elementos[indice].get()

    def crearBotones(self, comando1):
        aceptar = Button(self, text="Aceptar", font = ("Verdana", 12), fg = "white", bg = "#245efd", command=comando1).grid(pady = 50, column = 0, row = len(self._criterios)+1)