valor = 5
texto = "Hola"

#Evaluamos verdadero

print((valor > 1) and (texto == "Hola"))

#Evaluamos Falso

print((valor > 1) and (texto == "hola"))

#Evaluar el siguiente caso
#Es mayor de edad
#Es menor de edad y tiene permiso de los padrres, puede viajar
#Es menor y no tiene permiso, no puede viajar
#Si es mayor de edad, puede viajar

print("----------------------------------------------------------")
mayoriaEdad = False
permisoParental = False

if ((mayoriaEdad == False) and (permisoParental == True)):
    print("No puede viajar")
elif ((mayoriaEdad == False) and (permisoParental == True)):
    print("Puede viajar con persmio")
elif (mayoriaEdad == True):
    print("Puede viajar, es mayor de edad")

if (mayoriaEdad == False):
    if (permisoParental == False):
        print("No puede viajar")
    elif(permisoParental == True):
        print("Puede viajar con permiso")
    elif(mayoriaEdad == True):
        print("Puede viajar, es mayor de edad")
