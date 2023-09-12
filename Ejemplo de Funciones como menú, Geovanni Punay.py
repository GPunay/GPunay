#Trabajando un menú con funciones
#Trabajaremos sobre una lista

#Consultar datos (listar contenido)
#Agregar datos (append)
#Insertar datos (insert)
#Eliminar un dato (del)

def mostrarMenu():
    print('*'*25)
    print("Seleccione una opción")
    print("1.- Consultar datos")
    print("2.- Agregar datos (append)")
    print("3.- Insertar datos (insert)")
    print("4.- Eliminar datos (del)")
    print("5.- Salir")

#Esta función, devolverá la opción que indique el usuario
def solicitarOpcion():
    print('*'*25)
    opcion = input("Ingrese opción: ")
    #To do -> por hacer
    #TODO validaciones, pendiente
    return opcion

def ejecutarOpcion(opcion):
    if (opcion == '1'):
        #TODO Invocamos función para mostrar contenido de la lista
        print('*'*25)
        print("Mostramos contenido de la lista\n")
        mostrarContenidoLista()
    elif (opcion == '2'):
        #TODO Invocamos función para agregar contenido a la lista
        print('*'*25)
        print("Agregar datos a la lista (append)\n")
        elemento = input("Ingrese valor para agregar a la lista: ")
        agregarElemento(elemento)
    elif (opcion == '3'):
        #TODO Incovamos la función para insertar datos a la lista
        print('*'*25)
        print("Insertar datos a la lista (insert)\n")
        elemento = input("Ingrese el elemento a insertar a la lista: ")
        indice = int(input("Coloca el indice en donde deseas que se inserte el elemento: "))
        insertarElemento(indice, elemento)
    elif(opcion == '4'):
        #TODO Invocamos a la función eliminar datos de la lista
        print('*'*25)
        print("Eliminar datos de la lista (del)\n")
        indice = int(input("Ingrese el indice del elemento a eliminar: "))
        eliminarElemento(indice)
    else:
        print('*'*25)
        print("Saliendo del programa....")

def mostrarContenidoLista():
    print(lista)

def agregarElemento(elemento):
    lista.append(elemento)

def insertarElemento(indice, elemento):
    lista.insert(indice, elemento)

def eliminarElemento(indice):
    del(lista[indice])

#Inicio del programa
lista = ['A', 'B', 'C']

#while de acá en adelante
opcion = 1
while(opcion != '5'):
    mostrarMenu()
    opcion = solicitarOpcion()
    ejecutarOpcion(opcion)

#TODO
#Función para insertar elemento a la lista (pedir indice en donde se insertara)
#Pedir el elemento a insertar

#Función para eliminar elemento de la lista (pedir indice de elemento a eliminar)

#Colocar el programa para que se pueda repetir y seleccionar opción múltiples veces
#Cuidado, la definición de la lista dejarla fuera del ciclo

#Al ingresar opción salir, debe salir del programa (finalizar el ciclo)