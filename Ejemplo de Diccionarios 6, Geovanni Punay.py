#Solución usando constructores y solicitando valores desde el teclado

def mostrarSeparador():
    print('-'*50)

#Función que toma como valor el mensaje a mostrar
#Solicitando valores desde el teclado y devuelve el valor ingresado
def solicitarTexto(mensaje):
    texto = input(mensaje)
    return texto

#Función que muestra los datos de todos los usuarios
#Recibe un lista de diccionarios
def mostrarUsuarios(lista):
    mostrarSeparador()
    print('Listado de Usuarios')
    mostrarSeparador()
    
    for elemento in lista:
        #usuario será cada diccionario
        print(elemento['usuario'])
        print(elemento['password'])
        mostrarSeparador()

#Inicio programa
mostrarSeparador()
listaUsuarios = []

for i in range(1, 4):
    print("Datos para usuario ", i)
    nombre = solicitarTexto("Ingrese nombre usuario: ")
    clave = solicitarTexto("Ingrese password: ")
    diccionario = dict(usuario = nombre, password = clave)
    listaUsuarios.append(diccionario)
    mostrarSeparador()

mostrarUsuarios(listaUsuarios)

#Listas, tuplas, diccionarios, sets

'''
nombre = solicitarTexto("Ingrese nombre: ")
print(nombre)
apellido = solicitarTexto("Ingrese apellido: ")
print(apellido)
direccion = solicitarTexto("Ingrese dirección: ")
print(direccion)
'''