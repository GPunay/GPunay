Algoritmo sin_titulo
	contador = 0
	promedio = 0
	suma = 0
	numero = 0
	Mientras numero <> -1 Hacer
		Escribir "Ingresar un numero: "
		Escribir "Ingrese -1 para Terminar: "
		Leer numero
		Si numero <> -1 y numero > 0 Entonces
			suma = suma + numero
			contador = contador + 1
		FinSi
	FinMientras
	promedio = suma / contador
	Escribir "Numeros ingresados: ", contador
	Escribir "La suma es: ", suma
	Escribir "El promedio es: ", promedio
	Escribir "Fuera del Ciclo"
FinAlgoritmo
