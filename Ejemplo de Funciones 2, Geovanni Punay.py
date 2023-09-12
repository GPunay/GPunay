#Uso de Funciones

#El nombre de la función, debe de darnos una pista de lo que realiza 
#Usamos def para definir una función

def mostrarSeparador():
    print("-"*50)

#Inicio del programa
#Invocamos la función (la mandamos a llamar)
mostrarSeparador()

#Escriba una función que muestre los números del 1 al 10 e indique si es par o impar
#Para cada número
#Invocar la función

def parImpar(num):
    if (num % 2 == 0):
        print("El número ", num, " es un número par")
    else:
        print("El número ", num, " es número impar")

for i in range (1, 11):
    parImpar(i)
    