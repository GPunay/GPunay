#Funciones y parámetros

def mostrarNombre(nombreVariable):
    print("El nombre es: ", nombreVariable)

mostrarNombre('Enrique')
mostrarNombre('Luis')
mostrarNombre('Paco')
mostrarNombre('Pedro')

def mostrarSuma(num1, num2):
    print("La suma de ", num1, " y ", num2, " = ", (num1+num2))

num1 = int(input("ingrese primer número: "))
num2 = int(input("ingrese segundo número: "))
mostrarSuma(num1, num2)
mostrarSuma(10, 50)
mostrarSuma(50, 20)
mostrarSuma(5, 2)
mostrarSuma(2, 4)

#Defina una función que tome 3 parámetros en donde:
#Parámetro 1: número entero
#Parámetro 2: número entero
#Parámetro 3: cadena de texto que representa operación
# + (suma), - (resta), * (multi), / (división)
#Ingresar los valores por medio de input

def Calculadora(num1, num2, op):
    if (op == '+'):
        print(num1, " + ", num2, " = ", (num1+num2))
    elif (op == '-'):
        print(num1, " - ", num2, " = ", (num1-num2))
    elif (op == '*'):
        print(num1, " * ", num2, " = ", (num1*num2))
    elif (op == '/'):
        print(num1, " / ", num2, " = ", (num1/num2))
    else:
        print("Escogió una opción no válida, debe colocar '+', '-', '*' o '/'")

n1 = int(input("Ingrese un primer número para usar la calculadora: "))
n2 = int(input("ingrese un segundo número para usar la calculadora: "))
op2 = input("Coloque un signo para realizar la operación ('+', '-', '*' o '/'): ")

Calculadora(n1, n2, op2)