'''
1.	Desarrolle un programa que almacene datos de canciones en formato MP3: Artista, Título, Duración (en segundos), Tamaño del fichero (en KB). 
Un programa debe pedir los datos de una canción al usuario y después mostrarlos en pantalla. Debe interrumpirse la carga cuando el artista ingresado sea vacío.
'''

import json

def crearCancion (artist, title, duration, size):
    cancion = {
        'Artista': artist,
        'Titulo': title,
        'Duracion': duration,
        'Tamaño': size,
    }
    
    return cancion


listaCanciones = [
    {
      "artist": "The Beatles",
      "title": "Let It Be",
      "duration": "4:03",
      "size": "9 MB"
    },
    {
      "artist": "Taylor Swift",
      "title": "Shake It Off",
      "duration": "3:39",
      "size": "7.5 MB"
    },
    {
      "artist": "Ed Sheeran",
      "title": "Shape of You",
      "duration": "3:53",
      "size": "8.1 MB"
    },
    {
      "artist": "Drake",
      "title": "God's Plan",
      "duration": "3:19",
      "size": "6.9 MB"
    },
    {
      "artist": "Billie Eilish",
      "title": "Bad Guy",
      "duration": "3:14",
      "size": "6.5 MB"
    },
    {
      "artist": "Adele",
      "title": "Hello",
      "duration": "4:55",
      "size": "11.2 MB"
    },
    {
      "artist": "BTS",
      "title": "Dynamite",
      "duration": "3:19",
      "size": "7.0 MB"
    }
  ]
  

artista = input('Ingrese el artista de la cancion: ')
titulo = input('Ingrese el titulo de la cancion: ')
duracion = input('Ingrese la duracion de la cancion: ')
size = input('Ingrese el tamaño de la cancion en kb: ')

while(artista != ''):
    cancion = crearCancion(artista, titulo, duracion, size)

    listaCanciones.append(cancion)
    artista = input('Ingrese el artista de la cancion: ')
    if (artista != ''):
        titulo = input('Ingrese el titulo de la cancion: ')
        duracion = input('Ingrese la duracion de la cancion: ')
        size = input('Ingrese el tamaño de la cancion en kb: ')
        
for element in listaCanciones:
    for key,value in element.items():
        print(key, ':', value,',')
    print('-------------------------------------------------------------')
