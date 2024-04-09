'''
La sucesión de Fibonacci es una sucesión de números enteros donde cada término
se obtiene como suma de los dos anteriores, siendo los dos primeros 0 y 1.
Por lo tanto, Fib=0, 1, 1, 2, 3, 5, 8, 13, 21.... Realizar un programa que lea N e
imprima los N primeros términos de esta sucesión, como así también la suma de
los mismos.
'''

nTerminoFibonacci = int(input('Ingrese la cantidad de terminos de Fibonacci que desea visualizar\n'))
primerTermino = 0
segundoTermino = 1
terminoActual = 2
sumaFibonacci = 0
terminosFinales = str(primerTermino)

if nTerminoFibonacci >= 2:
    while terminoActual <= nTerminoFibonacci:
        terminosFinales += ' + ' + str(segundoTermino)
        sumaFibonacci += segundoTermino
        nuevoTermino = primerTermino + segundoTermino
        primerTermino = segundoTermino
        segundoTermino = nuevoTermino
        terminoActual += 1
        

print(terminosFinales, '=', sumaFibonacci)