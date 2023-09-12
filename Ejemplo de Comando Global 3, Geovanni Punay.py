#Comando Global cuando no existe una variable global con ese identificador

def mostrarGlobal():
    #Global hace que python declare la variable como global
    global total
    total = 10 + 20

#Principal
mostrarGlobal()
print(total)