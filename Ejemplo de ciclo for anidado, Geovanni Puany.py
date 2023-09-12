
#Generamos direcciones IP con la ayuda de for

for i in range (1, 4): #3 veces
    print(" * ")
    for j in range (1, 4): #9 veces
        print("**")
        for k in range (1, 4): #27 veces
            print("***")
            print(i, j, k)
