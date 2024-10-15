'''
Escriba un programa que busque la palabra "python" en una cadena ingresada por el usuario, 
sin importar que sea mayúsculas o minúsculas. 
Utilice el método findall para resolverlo. 
'''
import re

def buscarPython (cadena):
    patron = 'python'
    regex = re.findall(patron, cadena, re.IGNORECASE)
    return regex

stringToevaluate = 'Escriba un programa que busque la palabra "python" en una cadena ingresada por el usuario, sin importar que sea mayúsculas o minúsculas. Utilice el método findall para resolverlo. '

print(buscarPython(stringToevaluate))