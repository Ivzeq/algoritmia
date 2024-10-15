'''
Escriba un programa que busque todas las letras mayúsculas en una cadena ingresada por el usuario e imprima cada una de ellas. 
Utilice el método findall para resolverlo.
'''
import re

def buscarUpperCase (cadena):
    patron = '[A-Z]'
    regex = re.findall(patron, cadena)
    return regex

stringToevaluate = 'Escriba un programa que busque la palabra "python" en una cadena ingresada por el usuario, sin importar que sea mayúsculas o minúsculas. Utilice el método findall para resolverlo. '

print(buscarUpperCase(stringToevaluate))