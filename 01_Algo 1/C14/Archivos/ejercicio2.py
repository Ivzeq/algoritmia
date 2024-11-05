'''
En base al primer punto, luego de generar la carga de las frases, visualizar el archivo cargado.
'''

def printFile ():
    try:
        file = open('./01_Algo 1/C13/Archivos/frasesFinal1.txt', 'r', encoding='UTF-8')
        content = file.read()
        renglones = content.split('\n')

        for renglon in renglones:
            print(renglon)

    except Exception as e:
        print('El error es', e)
    finally:
        file.close()


printFile()