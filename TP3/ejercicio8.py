'''
Leer un número correspondiente a un año e imprimir un mensaje indicando si es bisiesto o no. 
Un año es bisiesto cuando es divisible por 4. 
Sin embargo, aquellos años que sean divisibles por 4 y también por 100 no son bisiestos, a menos que también sean divisibles por 400. 
Por ejemplo, 1900 no fue bisiesto pero sí el 2000.
'''

year = int(input('Ingresar año a evaluar\n'))

mensajeBisiesto = 'El año ' + str(year) + ' es bisiesto'
mensajeNoBisiesto = 'El año ' + str(year) + ' no es bisiesto'

if year%4 == 0 and year % 100 != 0 or year % 400 ==0:
    print(mensajeBisiesto)
else:
    print(mensajeNoBisiesto)