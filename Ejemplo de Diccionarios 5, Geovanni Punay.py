
#1.- Defina un script que permita capturar (por el teclado)
#el nombre de usuario y password de 3 diferentes usuarios
#Diccionario{'user': '', 'pass' : ''}

#2.- Mostrar los datos capturados

#Definimos el diccionario vacío
diccionarioUsuario = {}

#Agregamos varios diccionarios a la lista
listaUsuarios = []

for i in range(1, 4):
    print('Datos para el usuario ', i)
    usuario = input("Ingrese nombre de usuario: ")
    password = input("Ingrese password de usuario: ")

    #Agregamos valores al diccionario
    diccionarioUsuario['user'] = usuario
    diccionarioUsuario['pass'] = password

    #Agregamos el diccionario a la lista
    listaUsuarios.append(diccionarioUsuario)

#Mostramos el contenido de la lista
print(listaUsuarios)