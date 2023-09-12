#Return puede ser usada para retornar un valor desde una funcion

def retornarNombre():
    return 'Alfonso'
    #Codigo inalcanzable
    print('Codigo inalcanzable (unreachable)')

print(retornarNombre())


def retornarNumero():
    print('linea 1')
    return 999
    print('linea 2')

retornarNumero()
print('linea 3')

#Salir de una funcion de manera selectiva

def ejecutarOpcion(opcion):
    if(opcion == 1):
        print('ejecutando opcion 1')
    elif(opcion == 2):
        print('ejecutando opcion 2')
    elif(opcion > 2):
        print('Opcion incorrecta')
        return #Hara que se salga de la funcion
    
    print('Continuamos con el proceso')

numero = int(input('Ingrese opcion: '))
ejecutarOpcion(numero)