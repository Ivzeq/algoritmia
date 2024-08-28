'''
Mostrar la tabla de multiplicar (entre 1 y 12) del número 4. ¿Cómo cambiaría el
algoritmo para que el usuario pueda decidir la tabla de multiplicar a mostrar?
'''

factor = 1
tablaElegida = int(input('Ingrese el numero de la tabla que quiere ver\n'))

resultado = 0

while (factor <= 12):
    resultado = tablaElegida * factor
    print(tablaElegida, 'x', factor, '=', resultado)
    factor += 1