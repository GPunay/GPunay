#Programa que solicita un nombre y lo muestra en pantalla
#Posteriormente, pregunta si desea repetir la operación
#Se debe ingresar n o N para detenerse
#Cualquier otra letra continua

#!= diferente
#== igual

#Iniciamos nuestra variable con valor tal que cumpla con la condición
continuar = "S"

#La condición evalua si el valor cumple la condición
while(continuar.upper() != "N"):
    nombre = input("Ingrese nombre: ")
    print(nombre)
    continuar = input("Desea repetir? (n o N para salir): ")

print("Fin del programa")
