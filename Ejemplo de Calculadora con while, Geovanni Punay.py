#Solicitar al usuario dos números
#Desplegar un menú de operaciones
#Mostrar el resutlado de la operación seleccionada
#Preguntar si desea repetir el proceso
#Ingresar n para salir

continuar = "s"

while(continuar.lower() != "n"):
    num1 = int(input("Ingrese el primer número: "))
    num2 = int(input("Ingrese el segundo número: "))
    
    #mostramos el menú
    print("\n---------------------------------")
    print("\tMenú Principal")
    print("---------------------------------")
    print(" 1.\tSuma")
    print(" 2.\tResta")
    print(" 3.\tMultiplicación")
    print(" 4.\tDivisión")
    print("---------------------------------\n")

    opcion = int(input("Ingrese opción: "))

    if (opcion == 1):
        print("\n", num1, " + ", num2, " = ", (num1+num2))
    elif(opcion == 2):
        print("\n", num1, " - ", num2, " = ", (num1-num2))
    elif(opcion == 3):
        print("\n", num1, " * ", num2, " = ", (num1*num2))
    elif(opcion == 4):
        print("\n", num1, " / ", num2, " = ", (num1/num2))
    else:
        print("\nOpción Incorrecta\n")

    continuar = input("\nDesea hacer más cálculos? (Ingrese n para salir): ")
    print("\n")
    
print("Fin del programa")
