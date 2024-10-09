'''
Realizar una función que reciba como parámetros dos cadenas de caracteres conteniendo números reales, 
sume ambos valores y devuelva el resultado como un número real. 
Devolver None si alguna de las cadenas no contiene un número válido, utilizando manejo de excepciones para detectar el error.
'''

def sumarReales (real1,real2):
    try:
        suma = float(real1) + float(real2)
        return suma
    except:
        print('Por lo menos uno de los datos ingresados no puede convertirse a float')
        return None

print(sumarReales('1.1','2.3'))