#Comando Global

def mostrarNombre():
    #Colocamos global antes de identificar para poder hacer referencia a la variable global
    global nombreProducto
    nombreProducto ='Caja lapiceros'
    print(nombreProducto)

#Programa Principal
nombreProducto = 'Estuche para lentes'
mostrarNombre()
print(nombreProducto)