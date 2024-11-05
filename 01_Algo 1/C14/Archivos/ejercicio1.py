'''
Crea un programa que vaya leyendo las frases que el usuario teclea y las guarde en un fichero de texto llamado “frases.txt”. 
Terminará cuando la frase introducida sea "fin" (esa frase no deberá guardarse en el fichero).
'''

def saveFrases ():
    frase = input('Ingrese una frase o fin para terminar:')

    while frase.lower() != 'fin':
        try:
            frasesFile = open('frases.txt', 'a', encoding="UTF-8")
            frasesFile.write(frase + '\n')
        except Exception as e:
            print('El error es', e)
        finally:
            frasesFile.close()
            frase = input('Ingrese una frase o fin para terminar:')

saveFrases()