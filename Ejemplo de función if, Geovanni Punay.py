#Programa que solicita una nota y notifica si se aprueba

punteo_minimo = 60
nota_obtenida = int(input("Ingrese nota: "))

if nota_obtenida < punteo_minimo:
    print("No aprobado, intente de nuevo")
else:
    print("Aprobado, sigue adelante")
    
print("Fin del Programa")
