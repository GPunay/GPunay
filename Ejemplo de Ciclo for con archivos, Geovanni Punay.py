

#w -> write -> escritura

with open("prueba.txt", "w") as archivo:
    for tercerOcteto in range(255):
        for cuartoOcteto in range (255):
            direccion = "192.168." +  str(tercerOcteto) + "." + str(cuartoOcteto) + "\n"
            archivo.write(direccion)
