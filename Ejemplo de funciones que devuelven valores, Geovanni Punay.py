#Funciones que devuelven valores

def calcularSuma(numero1, numero2):
    return (numero1 + numero2)

resultado = calcularSuma(1, 9)
print(resultado)

print(calcularSuma(99, 100))

#Funciones y listas
def calcularSubtotal(listaPrecios):
    subtotal = 0
    for precio in listaPrecios:
        subtotal += precio
    
    return subtotal

def calcularTotal(subtotal):
    return (subtotal * 1.12)

preciosArticulos = [10, 50, 100, 20]
subtotal = calcularSubtotal(preciosArticulos)
total = calcularTotal(subtotal)
print("El subtotal es: ", round(subtotal, 2))
print("El total es: ", round(total, 2))
print("Gracias por su compra")

print(round(calcularTotal(calcularSubtotal(preciosArticulos)), 2))

total = calcularTotal(calcularSubtotal(preciosArticulos))
print(round(total, 2))

#Calcular Subtotal, la suma de todos los elementos de la lista

#Calcular total, aplicar impuesto (12%)