'''
Crear un archivo que se llame “montos.txt”, en el mismo se almacenarán valores numéricos.
Realizar un proceso que visualice su contenido y, al finalizar, muestre el total (sumatoria de los valores) y promedio.
'''

def generateMontosFile ():
    numero = input('Ingrese un numero o -1 para terminar:')

    while int(numero) != -1:
        try:
            file = open('montos.txt', 'a', encoding="UTF-8")
            file.write(numero + '\n')
        except Exception as e:
            print('El error es', e)
        finally:
            file.close()
            numero = input('Ingrese un numero o -1 para terminar:')


def printFile ():
    try:
        file = open('montos.txt', 'r', encoding='UTF-8')
        content = file.read()
        renglones = content.split('\n')
        suma = 0
        cantidad = 0

        for renglon in renglones:
            if renglon != '':
                suma += int(renglon)
                cantidad += 1

        print('El total es:', suma, 'y el promedio es', suma/cantidad)

    except Exception as e:
        print('El error es', e)
    finally:
        file.close()

generateMontosFile()    
printFile()