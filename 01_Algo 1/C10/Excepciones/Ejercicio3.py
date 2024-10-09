'''
Desarrollar una función que devuelva una cadena de caracteres con el nombre del mes cuyo número se recibe como parámetro. 
Los nombres de los meses deberán obtenerse de una tupla de cadenas de caracteres inicializada dentro de la función. 
Devolver una cadena vacía si el número de mes es inválido. La detección de meses inválidos deberá realizarse a través de excepciones.
'''

def getMonthName (monthNumber):
    meses = ['Enero', 'Febrero', 'Marzo']
    try:
        if (monthNumber > 12 | monthNumber < 1):
            raise (ValueError('El numero ingresado no corresponde a un mes'))
        return meses[monthNumber - 1]
        
    except:
        print('Por lo menos uno de los datos ingresados no puede convertirse a float')
        return None

isMesCorrecto = False
mesIngresado = int(input('Ingrese un mes: '))
mesCorrecto = ''

while (isMesCorrecto == False):
    isMesCorrecto = getMonthName(mesIngresado)
    if (isMesCorrecto != False):
        mesCorrecto = isMesCorrecto

print ('El mes es:',mesCorrecto)