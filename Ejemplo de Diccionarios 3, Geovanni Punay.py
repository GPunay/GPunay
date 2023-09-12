
def mostrarSeparador():
    print("-"*100)

#Trabajando con secuencias:

dicEstudiante = {
    "nombre" : "Alfonso",
    "apellido" : "García",
    "edad" : 28
}

print(dicEstudiante)
print(dicEstudiante["nombre"])
#Error de llave (no existe en el diccionario)
#print(dicEstudiante["direccion"])

dicEstudiante['direccion'] = 'Guatemala'

print(dicEstudiante)
del dicEstudiante['direccion']
print(dicEstudiante)

mostrarSeparador()

#Función que permite imprimir los datos de un usuario
def mostrarInfoUsuario(usuario):
    print(usuario['user'])
    print(usuario['pass'])


usuario1 = {
    'user' : 'abc-1', 
    "pass" : "qwerty8794"
    }

usuario2 = {
    'user' : 'abc-2', 
    "pass" : "asdfg987"
    }

print(usuario1.keys())
print(type(usuario1.keys()))

#método keys y diccionario
for key in usuario1:
    print(key, "->", usuario1[key])

mostrarSeparador()
mostrarInfoUsuario(usuario1)
mostrarInfoUsuario(usuario2)