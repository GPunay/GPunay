#Uso de diccionarios en una agenda telefónica
#Cuál será la clave?
#Se permite varios números de teléfono en un mismo contacto?
#Nombre como clave y valores un listado de números

#Función que agrega contactos por defecto a la agenda
def inicializarAgenda():
    agenda['Henry'] = ['2345-8754', '5487-9658']
    agenda['Geo'] = ['2487-8754', '5478-9632']
    agenda['Dennis'] = ['2345-6598', '5236-6487']

def mostrarTodosContactos():
    #Recorremos cada contacto
    for contacto in agenda:
        print()
        #Mostramos el nombre del contacto
        print(contacto)
        #Recorremos la lista de numeros del contacto
        for numero in agenda[contacto]:
            print(numero, end=' ')
        print()

def agregarContacto(nombreContacto):
    #verificar que el nombre no esté en la lista de contactos
    if nombreContacto not in agenda:
        #Solicitar los números de teléfono
        telefonos = []
        telefonos.append(input("Ingrese número de teléfono: "))
        telefonos.append(input("Ingrese número de teléfono 2: "))
        #Agregamos la clave en la agenda
        agenda[nombreContacto] = telefonos
    else:
        print("El contacto ya existe")

def verificarExistencia():
    nombre = input("Ingrese el nombre de contacto: ")
    print()

    if nombre in agenda:
        print(nombre, ":", agenda[nombre][0])

    else:
        confirma = input("Desea agregar el contacto? Escriba si o no: ")
        
        if confirma.lower() == "si":
            agregarContacto(nombre)
    
    mostrarTodosContactos()

#Programa Principal
agenda = {}
inicializarAgenda()
mostrarTodosContactos()
verificarExistencia()

#Agregamos una función que solicite el nombre del contacto,
#Verificar si exsite:
    #Si existe mostrar el nombre del contacto y el primer número de teléfono
    #Si no existe preguntar al usuario si desea agregarlo
        #Si dice que si, invocar a la función para agregarlo
        #Caso contrario, continuar con el flujo del programa
#Mostrar todos los contactos en la agenda