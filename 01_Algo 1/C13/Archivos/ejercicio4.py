'''
Crear un programa que maneje un archivo donde se almacena la siguiente información de una determinada cantidad personas: 
Nombre, Apellido, Edad y Estatura. El programa deberá almacenar la información a medida que se vayan cargando. 
El formato a ser almacenado será cada dato separado por el carácter punto y coma (;) en el mismo orden que se carga. 
Tenga en cuenta que cada vez que se ejecuta el programa, se debe incrementar el contenido del archivo (agregar al final).
'''

def generatePersonasFile (route):
    nombre = input('Ingrese un nombre o fin para terminar:')

    while nombre.lower() != 'fin':
        try:
            apellido = input('Ingrese un apellido:')
            edad = input('Ingrese una edad:')
            estatura = input('Ingrese una estatura:')

            file = open(route, 'a', encoding="UTF-8")

            print(nombre + ';' + apellido + ';' + edad + ';' + estatura + ';', file=file)
        except Exception as e:
            print('El error es', e)
        finally:
            file.close()
            nombre = input('Ingrese un nombre o fin para terminar:')


def printFile (route):
    try:
        file = open(route, 'r', encoding='UTF-8')
        content = file.read()
        renglones = content.split('\n')

        for renglon in renglones:
            print(renglon)

    except Exception as e:
        print('El error es', e)
    finally:
        file.close()

generatePersonasFile('personas.txt')    
printFile('personas.txt')