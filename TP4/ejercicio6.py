'''
Mostrar la tabla de multiplicar (entre 1 y 12) del número 4. ¿Cómo cambiaría el
algoritmo para que el usuario pueda decidir la tabla de multiplicar a mostrar?
'''

factor = 1

resultado = 0

while (factor <= 12):
    resultado = 4 * factor
    print('4 x', factor, '=', resultado)
    factor += 1