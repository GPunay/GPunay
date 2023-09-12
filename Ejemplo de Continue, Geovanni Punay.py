#Trabajando con Continue

contador = 0
while(contador <= 10):
    contador += 1
    if (contador > 5):
        continue
    print(contador)
    
print("Fuera del ciclo")

contador = 0
while (contador < 10):
    contador += 1
    if (contador == 5):
        break
    print("Hola")
