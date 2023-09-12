valor = [1, 2, 3]
diccionario = {
        'clave1':valor,
        'calve2':['a', 'b']
    }

print(diccionario)
del diccionario['clave1']
print(diccionario)
print(valor)

#del diccionario
#print(diccionario) No se puede porque ya se eliminó el diccionario, ya no existe