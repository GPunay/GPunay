from typing import OrderedDict


agenda = {}
agenda['Henry'] = ['2345-8754', '5487-9658']
agenda['Geo'] = ['2487-8754', '5478-9632']
agenda['Dennis'] = ['2345-6598', '5236-6487']

print(agenda)
print("-"*50)
print(agenda['Geo'])
print("-"*50)
print(agenda['Geo'][0])
print("-"*50)
print(agenda['Geo'][0][0])
print("-"*50)

#Método Keys()
print(agenda.keys())

for llave in agenda.keys():
    print(llave)
    print(agenda[llave])

#Función sorted()
print(agenda)
print('Ordenando agenda')
#sorted() devuelve una secuencia ordenada de forma descendente
print(sorted(agenda))
print(sorted(agenda, reverse = True))

#Método items()
print("-"*50)
print(agenda.items())
print()

for item in agenda.items():
    print(item)

print()
for clave, valor in agenda.items():
    print(clave, '->', valor)

print()
lista = [
        ['Luis', 'Garcia', 25],
        ['Luisa', 'Gómez', 23]
        ]

for nombre, apellido, edad in lista:
    print(nombre, apellido, edad)

#Método values()
print(agenda.values())


#Usando sets
'''
print("-"*50)
setNumeros = {'Apple', 'Bee', 'Cat', 'Dice'}
listaNumeros = ['Apple', 'Bee', 'Cat', 'Dice']
diccionarioNumeros = {'a':'Apple', 'b':'Bee'}

print(setNumeros)
print(listaNumeros)
print(diccionarioNumeros)
'''