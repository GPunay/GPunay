#Mostrar los números de 1 en 1 hasta que el usuario ingrese la letra x

continuar = "o"
numero = 1

while(continuar.lower() != "x"):
    print(numero)
    numero += 1
    continuar = input("Desea continuar? x para salir: ")

print("Fin del programa")
