#Funciones e identificadores

def mostrarMensaje():
    texto = input("Ingrese texto: ")
    print(texto)

mostrarMensaje()
#Usamos el identificador para ver su referencia en memoria
print(mostrarMensaje)

#Uso el identificador de la función y le asigno un nuevo valor
#La convierte en una variable
mostrarMensaje = "Nuevo Valor"
print(mostrarMensaje)
#Tratamos de invocar o mandar a llamar una variable, esto producirá un error
mostrarMensaje()