'''
2.	Escriba un programa que ingrese (por teclado) los datos de diez personas (nombre, edad, genero, dirección, teléfono), 
los almacene en un diccionario y los muestre.
Al realizar dicha muestra, destacar la persona más joven en edad.
'''

import json

def crearCancion (nombre, edad, genero, direccion, telefono):
    cancion = {
        'Nombre': nombre,
        'Edad': edad,
        'Genero': genero,
        'Direccion': direccion,
        'Telefono': telefono,
    }
    
    return cancion


listaCanciones = []

nombre = input('Ingrese el artista de la cancion: ')
edad = input('Ingrese el titulo de la cancion: ')
genero = input('Ingrese la duracion de la cancion: ')
direccion = input('Ingrese el tamaño de la cancion en kb: ')
telefono = input('Ingrese el tamaño de la cancion en kb: ')

for persona in range(0,9):
    persona = crearCancion(artista, titulo, duracion, size)

    listaCanciones.append(persona)
    artista = input('Ingrese el artista de la cancion: ')
    if (artista != ''):
        titulo = input('Ingrese el titulo de la cancion: ')
        duracion = input('Ingrese la duracion de la cancion: ')
        size = input('Ingrese el tamaño de la cancion en kb: ')
        
for element in listaCanciones:
    for key,value in element.items():
        print(key, ':', value,',')
    print('-------------------------------------------------------------')
