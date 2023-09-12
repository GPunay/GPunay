#Programa que convierte segundos a horas y minutos
segundos = 9000
#Convertir a segundos
print(segundos % (24 * 3600))

#Convertir a horas
horas = segundos // 3600
print("Cantidad de horas en ", segundos, " segundos: ", horas)

#Encontramos los minutos sobrantes
segundos %= 3600
#print("Cantidad resultante: ", segundos)
minutos = segundos // 60
print("Cantidad de minutos: ", minutos)
