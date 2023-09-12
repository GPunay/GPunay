#Declarando variables fuera de una función

def mostrarNombre():
    print('El nombre almacenado es: ', nombre)

#Inicio del programa
nombre = 'Alex'
mostrarNombre()
print(nombre, 'desde el programa')

#Variable Local -> Una variable declarada dentro de un bloque de código (if, while, for)
#Solamente existirá dentro dicho bloque de código
#Variable Global -> Una variable declarada fuera de un bloque de código
#Existirá a lo largo de todo el programa,