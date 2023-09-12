#Trabajando con diccionarios

#Diccionario eng-spa
diccionario = {'cat' : 'gato', 'dog' : 'perro', 'horse' : 'caballo'}

contactos = {'profesor' : 12345678, 'paco' : 87458963, 'tia luisa' : 23654789}

print(diccionario)
print(contactos)

print(diccionario['cat'])
print(contactos['tia luisa'])
diccionario[0] = 'cero' # type: ignore

#No es un indice, es una clave
print(diccionario[0]) # type: ignore
print(type(diccionario))

#Si repetimos claves, la más reciente sobrescribe a los demás valores
marcasPaises = {'toyota' : 'Japon', 'bmw' : 'Alemania', 'mercedes' : 'Alemania', 'vw' : 'Alemania', 'BMW' : 'Italia', 'audi' : 'Guatemala'}

print(marcasPaises)

#A partir de la versión 3.7 de python, los diccionarios son ordenados
#Podemos acceder a los elementos por medio de indices
