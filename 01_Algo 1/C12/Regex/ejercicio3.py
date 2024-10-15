'''
Escribe una función para verificar si una cadena comienza con una letra mayúscula. 
De ser así, retornará True; False en caso contrario. Utilice el método match para su resolución.
'''
import re

def verifyFirstUpperCase (cadena):
    patron = '^[A-Z]'
    regex = re.match(patron, cadena)
    return regex

stringToevaluate = 'Escriba'

if verifyFirstUpperCase(stringToevaluate):
    print(True)