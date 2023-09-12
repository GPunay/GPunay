#Ciclos anidados
#Python permite colocar ciclos dentro de ciclos

limiteExterno = 3
contadorExterno = 1

while(contadorExterno <= limiteExterno):
    print("---------------------")
    #Mostrar los números de 1 a 5
    print("contadorExterno: ", contadorExterno)
    print("limiteExterno: ", limiteExterno)
    input()

    limiteInterno = 5
    contadorInterno = 1

    while(contadorInterno <= limiteInterno):
        print(contadorInterno)
        print("contadorInterno: ", contadorInterno)
        print("limiteInterno: ", limiteInterno)
        input()
        contadorInterno += 1

    contadorExterno += 1
    
print("Fin del programa")
