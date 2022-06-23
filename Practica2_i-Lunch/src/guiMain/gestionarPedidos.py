from tkinter import *
from tkinter import messagebox
from fieldFrame import FieldFrame

# # class GestionarPedidos(Frame):

#     def __init__(self):
#         super().__init__()
#         # Se establece el nombre de la funcionalidad y su descripción para ser ambos mostrados en la GUI.
#         nombre = Label(master=self, text="Gestionar Petidos", font="Helvetica 11 bold")
#         info = """Para curar un animal primero seleccione el animal enfermo, luego seleccionar el ID del cuidador que 
#                   trasladara el animal y luego podra elegir el id del veterinario que va a revisar el animal. 
#                   La eleccion del cuidador y veterinario depende de la especie """
        
#         descripcion = Label(master=self, text=info, font="Helvetica 10")
#         nombre.pack(fill=BOTH, padx=5, pady=5)
#         descripcion.pack(fill=BOTH, padx=5, pady=5)
        
#         # Se especifican los nombres de los criterios que tendrá el FieldFrame de esta funcionalidad.
#         self.criterios = ["Especie", "Identificación", "Hábitat", "Género", "Edad", "Peso", "Cuidador revisor", "Veterinario encargado"]
#         # Se especifican los valores que tendrá el FieldFrame de esta funcionalidad para los criterios anteriormente especificados.
#         self.valores = [False, False, "", "", "", "", False, False]
#         # Igualmente, se especifican los valores que estarán habilitados para ser editados por el usuario.
#         self.habilitados = [True, True, False, False, False, False, True, True]
#         # Ahora, se especifican las listas de selección que usa la GUI para que el usuario elija entre los valores de la lista.
#         self.combobox = [Curar.especies(), Curar.animales(), False, False, False, False, Curar.cuidadores(), Curar.veterinarios()]
#         # Se crea el FieldFrame para esta funcionalidad con los parámetros anteriormente especificados.
#         self.dialogos = FieldFrame(self, "Criterios", self.criterios, "Valores", self.valores, self.habilitados, self.combobox)
#         self.dialogos.pack(padx=5, pady=5)
#         # Se crean además, y debajo del FieldFrame, los botones de Aceptar y Borrar.
#         botones = Frame(master=self)
#         aceptar = Button(master=botones, text="Revisar", font="Helvetica 11 bold", 
#                          bg="grey", fg="white", borderwidth=3, relief="raised",
#                          command=self.saludAnimal)
#         aceptar.pack(side=LEFT, padx=5, pady=5)
#         borrar = Button(master=botones, text="Borrar", font="Helvetica 11 bold", 
#                          bg="grey", fg="white", borderwidth=3, relief="raised",
#                          command=self.borrar)
#         borrar.pack(side=RIGHT, padx=5, pady=5)
#         botones.pack(padx=5, pady=5)
#         # Por último, se asigna el comando para el combobox de Especie y para el combobox de Identificación del animal.
#         comboboxEspecie = self.dialogos.getComponente("Especie")
#         comboboxEspecie.bind("<<ComboboxSelected>>", lambda e: self.especieSeleccionada())
#         comboboxAnimal = self.dialogos.getComponente("Identificación")
#         comboboxAnimal.bind("<<ComboboxSelected>>", lambda e: self.animalSeleccionado())

#     # A través del método cuidadores(...) se obtiene el cuidador que revisará al animal.
#     @staticmethod
#     def cuidadores(animal=None):
#         cuidadores = []

#         if animal==None:
#             # Con el siguiente for se obtienen cada uno de los cuidadores almacenandos en la lista de animales de la clase Administración.
#             for cuidador in Administracion.getCuidadores():
#                 cuidadores.append(str(cuidador.getIdentificacion()) + " - " + cuidador.getNombre() + " (Revisa: " + cuidador.getEspecieAsignada().getNombre() + ")")
#         else:
#             # Con el siguiente for se obtienen cada uno de los cuidadores almacenandos en la lista de animales de la clase Administración.
#             for cuidador in Administracion.getCuidadores():
#                 # Esto se hace para buscar los cuidadores correspondientes a la especie del animal que va a ser revisado, para luego listar 
#                 # las identificaciones de cada uno de estos cuidadores para que el usuario seleccione uno para que revise al animal.
#                 if(cuidador.getEspecieAsignada() == animal.getEspecie()):
#                     cuidadores.append(str(cuidador.getIdentificacion()) + " - " + cuidador.getNombre() + " (Revisa: " + cuidador.getEspecieAsignada().getNombre() + ")")
		
#     		# En caso que no haya ni un solo cuidador para la especie del animal, se le informa al usuario.
#             if(cuidadores == []):
#                 messagebox.showwarning(title="Advertencia",
#                                        message="No se ha encontrado ningún cuidador que esté disponible para revisar a la especie del animal.")
#         return cuidadores

#     # A través del método veterinarios(...) se obtiene el veterinario que curara al animal.
#     @staticmethod
#     def veterinarios(animal=None):
#         veterinarios = []

#         if animal==None:
#             # Con el siguiente for se obtienen cada uno de los veterinarios almacenandos en la lista de animales de la clase Administración.
#             for veterinario in Administracion.getVeterinarios():
#                 veterinarios.append(str(veterinario.getIdentificacion()) + " - " + veterinario.getNombre() + " (Revisa: " + veterinario.getEspecieAsignada().getNombre() + ")")
#         else:
#             # Con el siguiente for se obtienen cada uno de los veterinarios almacenandos en la lista de animales de la clase Administración.
#             for veterinario in Administracion.getVeterinarios():
#                 # Esto se hace para buscar los veterinarios correspondientes a la especie del animal que va a ser revisado, para luego listar 
#                 # las identificaciones de cada uno de estos veterinarios para que el usuario seleccione uno para que revise al animal.
#                 if(veterinario.getEspecieAsignada() == animal.getEspecie()):
#                     veterinarios.append(str(veterinario.getIdentificacion()) + " - " + veterinario.getNombre() + " (Revisa: " + veterinario.getEspecieAsignada().getNombre() + ")")
		
#     		# En caso que no haya ni un solo cuidador para la especie del animal, se le informa al usuario.
#             if(veterinarios == []):
#                 messagebox.showwarning(title="Advertencia", message="No se ha encontrado ningún veterinario que esté disponible para curar a la especie del animal.")
#         return veterinarios

#     # A través del método animales(...) se obtiene el animal que será trasladado y posteriormente curado
#     @staticmethod
#     def animales(especie=None):
#         animales = []

#         if especie==None:
#             # Con el siguiente for se obtienen cada uno de los animales almacenandos en la lista de animales de la clase Administración.
#             for animal in Administracion.getAnimales():
#                 animales.append(str(animal.getIdentificacion()) + " (" + animal.getEspecie().getNombre() + ")")
#         else:
#             # Con el siguiente for se obtienen cada uno de los animales almacenandos en la lista de animales de la clase Administración.
#             for animal in Administracion.getAnimales():
#                 # Esto se hace para buscar los animales correspondientes a la especie del animal que se va a trasladar, para luego listar 
#                 # las identificaciones de cada uno de estos animales para que el usuario seleccione uno para trasladar.
#                 if(animal.getEspecie() == especie):
#                     animales.append(str(animal.getIdentificacion()) + " (" + animal.getEspecie().getNombre() + ")")
#     		# En caso que no haya ni un solo animal de la especie seleccionada, se le informa al usuario.
#             if(animales == []):
#                 messagebox.showwarning(title="Advertencia",
#                                        message="No se ha encontrado ningún animal de esta especie que esté disponible ser revisado.")
#         return animales

#     # A través del método especies() se obtienen los nombres de las especies disponibles.
#     @staticmethod
#     def especies():
#         especies = []
# 		# El siguiente for obtiene el nombre de cada objeto de Especie almacenado en la lista de especies de Administración
#         for especie in Administracion.getEspecies():
#             especies.append(especie.getNombre())
#         return especies

#     # Por medio del método borrar() se limpian todos los campos del FieldFrame, tanto combobox como entry.
#     def borrar(self):
#        self.dialogos.getComponente("Especie").set("")
#        self.dialogos.getComponente("Identificación").set("")
#        habitat = self.dialogos.getComponente("Hábitat")
#        habitat.configure(state=NORMAL)
#        habitat.delete(0,"end")
#        habitat.configure(state=DISABLED)
#        genero = self.dialogos.getComponente("Género")
#        genero.configure(state=NORMAL)
#        genero.delete(0,"end")
#        genero.configure(state=DISABLED)
#        edad = self.dialogos.getComponente("Edad")
#        edad.configure(state=NORMAL)
#        edad.delete(0,"end")
#        edad.configure(state=DISABLED)
#        peso = self.dialogos.getComponente("Peso")
#        peso.configure(state=NORMAL)
#        peso.delete(0,"end")
#        peso.configure(state=DISABLED)
#        self.dialogos.getComponente("Cuidador revisor").set("")
#        self.dialogos.getComponente("Veterinario encargado").set("")
    
#     # Por medio del método especieSeleccionada(), cuando se elije una especie de las disponibles por medio de su combobox,
#     # el combobox de Identificación listará las identificaciones de los animales que sean solo de dicha especie, 
#     # esto a través del método estático animales(especie).
#     def especieSeleccionada(self):
#         nombreEspecie = self.dialogos.getValue("Especie")
#         # Cada vez que se cambia la especie se borrarán todos los campos.
#         self.borrar()
#         for especie in Administracion.getEspecies():
#             if especie.getNombre() == nombreEspecie:
#                 self.dialogos.getComponente("Identificación").configure(values=Curar.animales(especie))
#                 break
#         # Además, por cada vez que se cambie la especie seleccionada, como ya se limpiaron todos los demás campos, se vuelve a
#         # establecer el combobox de especie con la especie que fue selecionada.
#         self.dialogos.getComponente("Especie").set(nombreEspecie)
    
#     # Por medio del método animalSeleccionado(), cuando se elije una identificación de las disponibles por medio de su combobox,
#     # los campos de Hábitat, Género, Edad y Peso serán llenados con los valores de los atributos del animal seleccionado.  
#     def animalSeleccionado(self):
#         identificacion = self.dialogos.getValue("Identificación").split("(")[0].strip()
#         identificacion = int(identificacion)
#         habitat = self.dialogos.getComponente("Hábitat")
#         genero = self.dialogos.getComponente("Género")
#         edad = self.dialogos.getComponente("Edad")
#         peso = self.dialogos.getComponente("Peso")
#         cuidador = self.dialogos.getComponente("Cuidador revisor")
#         cuidador.set("")
#         veterinario = self.dialogos.getComponente("Veterinario encargado")
#         veterinario.set("")
#         for animal in Administracion.getAnimales():
#             if animal.getIdentificacion() == identificacion:
#                 habitat.configure(state=NORMAL)
#                 habitat.delete(0,"end")
#                 habitat.insert(0, animal.getHabitat().getNombre())
#                 habitat.configure(state=DISABLED)
#                 genero.configure(state=NORMAL)
#                 genero.delete(0,"end")
#                 genero.insert(0, animal.getGenero())
#                 genero.configure(state=DISABLED)
#                 edad.configure(state=NORMAL)
#                 edad.delete(0,"end")
#                 edad.insert(0, str(animal.getEdad()))
#                 edad.configure(state=DISABLED)
#                 peso.configure(state=NORMAL)
#                 peso.delete(0,"end")
#                 peso.insert(0, str(animal.getPeso()))
#                 peso.configure(state=DISABLED)
#                 # También se establece el combobox de "Cuidador revisor" con la lista de cuidadores que pueden revisar a
#                 # la especie del animal seleccionado por el usuario.
#                 cuidador.configure(values=Curar.cuidadores(animal))
#                 # También se establece el combobox de "Veterinario encargado" con la lista de veterinarios que pueden revisar a
#                 # la especie del animal seleccionado por el usuario.
#                 veterinario.configure(values=Curar.veterinarios(animal))
#                 break
    
#     # A traves del metodo saludAnimal() se hace el proceso de revisar el estado de salud del animal seleccionado desde el cuidador seleccionado y veterinario seleccionado.
#     def saludAnimal(self):
#         idAnimal = self.dialogos.getValue("Identificación").split("(")[0].strip()
#         idVeterinario = self.dialogos.getValue("Veterinario encargado").split("-")[0].strip()
        
#         # Se hace uso de la excepción sugerida para verificar si el campo de la identificación para el animal y el campo del veterinario encargado
#         # esten llenos (Si ID del animal corresponde a un valor y si ID del veterinario encargado corresponde a un valor).
#         try:
#             ExcepcionPresenciaDatos.presenciaDatos(["Identificación", "Veterinario encargado"], [idAnimal, idVeterinario])
#         except ExcepcionPresenciaArchivos:
#             return
        
#         # Y por medio de las otra excepcion sugerida para verificar el tipo de dato se comprueba si la identificación
#         # para el animal o la identificación para el veterinario no corresponden al tipo de dato que deberían.
#         try:
#             ExcepcionTipoInt.tipoInt(["Identificación", "Veterinario encargado"], [idAnimal, idVeterinario])
#         except ExcepcionTipoInt:
#             return
        
#         # Una vez hechas todas las comprobaciones, se puede proceder a obtener el objeto tipo Animal a revisar y el objeto tipo veterinario que revisará.
#         for elem in Administracion.getAnimales():
#             if elem.getIdentificacion() == int(idAnimal):
#                 animalSeleccionado = elem
#                 break   
#         for elem in Administracion.getVeterinarios():
#             if elem.getIdentificacion() == int(idVeterinario):
#                 veterinarioSeleccionado = elem
#                 break   

#         # En caso que el animal esté con buen estado de ánimo se le informará al usuario. 
#         if(veterinarioSeleccionado.revisar(animalSeleccionado)):
#             messagebox.showinfo(title="Resultado",
#                                 message="El animal se encuentra con buen estado de salud.")
#         # En caso que el animal esté con mal estado de salud, se le informará al usuario y el veterinario seleccionado procederá a curar al animal
#         # a través del método animentarAnimal(...).
#         else:
#             mensaje = "El animal se encuentra con mal estado de salud.\nEl veterinario decide entonces curar al animal para mejorar su estado de ánimo."
#             messagebox.showinfo(title="Resultado",
#                                 message=mensaje)
#             Veterinario.curarAnimal(animalSeleccionado)
#             #veterinarioSeleccionado.curarAnimal(animalSeleccionado)
			
#             # El estado de ánimo depende de su alimentación, su estado de salud y de la limpieza de su hábitat. El siguiente if cambia el estado
#             # de ánimo del animal a bueno (true) en caso que estos tres factores también sean buenos (true).
#             if(animalSeleccionado.isAlimentado() and animalSeleccionado.isEstadoSalud() and animalSeleccionado.getHabitat().isLimpio()):
#                 animalSeleccionado.setEstadoAnimo(True)
                
#             # Si luego de haber sido curado, el estado de ánimo del animal mejoró, se le informa al usuario y se termina la funcionalidad.
#             if(veterinarioSeleccionado.revisar(animalSeleccionado)):
#                 messagebox.showinfo(title="Resultado",
#                                     message="Curar al animal ha dado buen resultado y este ahora se encuentra con buen estado de ánimo.")
#             # En caso que el animal continúe con mal estado de ánimo, se le informará al usuario que alimentarlo no ha sido de ayuda. Además, se le    
#             # indicará al usuario que puede probar con la funcionalidad de mantenimiento y alimentar para así mejorar el estado de ánimo del animal.
#             else:
#                 mensaje = "Curar al animal no ha mejorado su estado de ánimo.\nPuede hacer mantenimiento a su hábitat o alimentarlo para mejorar su estado."
#                 messagebox.showinfo(title="Resultado",
#                                     message=mensaje)
#         self.borrar()