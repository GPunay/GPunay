def validarValores(valor):
    #Si la condicion al ser verdadera causa la salida de la funcion
    #Se recomienda que se evalue primero
    print('Dentro de la funcion')
    if(valor > 20):
        return
    elif(valor % 2 == 0):
        print('Es numero par', valor)
    elif(valor % 2 != 0):
        print('Es numero impar', valor)
    
for i in range(1, 31):
    print(i)
    validarValores(i)