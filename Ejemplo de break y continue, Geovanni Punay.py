#Instrucción Break

#break -> romper
#break permite romper un ciclo
contador = 1

while(contador <= 10):
    print(contador)
    contador+= 1
    if (contador == 5):    
        break
    print("Dentro del ciclo")

print("Fuera del ciclo")

for i in range (1, 11):
    print(i)
    if (i == 5):
        break

print("Fuera del ciclo for")
