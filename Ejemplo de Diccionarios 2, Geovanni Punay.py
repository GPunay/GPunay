
paisesIdiomas = {'GT' : 'Español', 'EEUU' : 'Inglés'}

#print(paisesIdiomas[0])

paisesIdiomas[0] = "Zero" # type: ignore
print(paisesIdiomas[0]) # type: ignore

#Mostrando las llaves (keys) de un diccionario
for elemento in paisesIdiomas:
    print(elemento)

#Devuelve las claves del diccionario
print(paisesIdiomas.keys())

print(type(paisesIdiomas.keys()))

#Devuelve cada clave con el valor correspondinete
print(paisesIdiomas.items())

#Devuelve todos los valores
print(paisesIdiomas.values())

#Recorriendo keys()
for llave in paisesIdiomas.keys():
    print(llave)
    print(llave, '->', paisesIdiomas[llave])

print('-'*50)
for clave, valor in paisesIdiomas.items():
    print(clave, '->', valor)

lista = [['Luis', 'Ruiz', 25], ['Pedro', 'García', 30]]

for nombre, apellido, edad in lista:
    print(nombre, apellido, edad)