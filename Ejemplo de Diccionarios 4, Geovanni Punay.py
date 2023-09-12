
#1.- Defina un script que permita capturar (por el teclado)
#el nombre de usuario y password de 3 diferentes usuarios
#Diccionario{'user': '', 'pass' : ''}

#2.- Mostrar los datos capturados

#Permite agregar, eliminar elementos
lista = [
    {'user' : 'abc', 'pass' : 'pass1'},
    {'user' : 'abc2', 'pass' : 'pass2'}
]

#Solo de lectura
tupla = (
    {'user' : 'abc', 'pass' : 'pass1'},
    {'user' : 'abc2', 'pass' : 'pass2'}
)

print(lista)
print(tupla)

nombres = []
passwords = []
diccionario = {'user' : '', 'pass' : ''}

for i in range (0, 3):
    nombre = input("\nIngrese nombre de usuario: ")
    password = input("Ingrese la contraseña del usuario: ")

    nombres.append(nombre)
    passwords.append(password)
    

for i in range (0, 3):

    diccionario['user'] = nombres[i]
    diccionario['pass'] = passwords[i]
    print(diccionario)
