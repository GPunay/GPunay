#Ciclo For

#Mostrar la tabla de multiplicar del 5, desde 1 hasta 10

for contador in range (1, 21):
    if (contador >= 1 and contador <= 10):
        print(5, " x ", contador , " = ", (contador * 5))
    elif(contador >= 15):
        print(5, " x ", contador, " = ", (contador * 5 ))

for contador in range (1, 21):
    if ((contador >= 1 and contador <= 10) or (contador >= 15)):
        print(5, " x ", contador, " = ", (contador * 5))
