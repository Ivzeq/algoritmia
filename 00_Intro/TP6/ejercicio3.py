'''
Imprimir una columna de asteriscos, donde su altura se recibe como parámetro.
'''

nFilas = 0
contadorCiclo = 0

while (nFilas <= 0):
    nFilas = int(input('Ingrese el numero de filas deseado\n'))

while(contadorCiclo < nFilas):
    print('*')
    contadorCiclo += 1