'''
Desarrollar una función para ingresar a través del teclado un número. 
La función rechazará cualquier ingreso inválido de datos utilizando excepciones y mostrará la razón exacta del error. 
Devolver el valor ingresado cuando éste sea correcto.
Escribir también un programa que permita probar el correcto funcionamiento de la misma.
'''

def ingresarNumero ():
    numeroIngresado = input('Ingrese un numero: ')
    try:
        int(numeroIngresado)
        return numeroIngresado
    except:
        print('El dato ingresado no es un numero')
        return False

isNumeroCorrecto = False
numeroCorrecto = 0

while (isNumeroCorrecto == False):
    isNumeroCorrecto = ingresarNumero()
    if (isNumeroCorrecto != False):
        numeroCorrecto = isNumeroCorrecto

print ('El numero ingresado es:',numeroCorrecto)