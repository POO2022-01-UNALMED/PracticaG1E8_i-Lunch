from excepciones.excepcionLista import ExcepcionLista
from excepciones.excepcionNumerica import ExcepcionNumerica

def tirarErrorLista(lista, valor):
    if len(lista) <= valor or valor < 0:
        raise ExcepcionLista([valor, len(lista)-1])

def tirarErrorNumerico(valor):
    if type(valor) == int or type(valor) == float:
        print(valor)
    else:    
        raise ExcepcionNumerica(valor)

print("\n")

try:
    tirarErrorLista([1,2,3], -10)
except ExcepcionLista as mensajeError:
    print(str(mensajeError))

print("\n")

try:
    tirarErrorNumerico("1")
except ExcepcionNumerica as mensajeError:
    print(str(mensajeError))

print("\n")