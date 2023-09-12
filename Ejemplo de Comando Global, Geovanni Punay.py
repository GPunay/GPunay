#Uso de return para asignar un valor a una variable global

def devolverResultado(num1, num2):
    resultado = num1 + num2
    resultado2 = resultado * 2
    return resultado, resultado2

def devolverLista(num1, num2):
    resultado = num1 + num2
    resultado2 = resultado * 2
    lista = [resultado, resultado2]
    return lista

def mostrarRespuesta():
    print(respuesta)

#Principal
respuesta = devolverResultado(3, 5)
mostrarRespuesta()
print(type(mostrarRespuesta))