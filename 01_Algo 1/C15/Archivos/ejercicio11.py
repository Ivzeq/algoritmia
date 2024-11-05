'''
Escribe una función recursiva llamada imprimirPiramideDescendente(numero) 
que tome un número entero como parámetro e imprima una pirámide descendente 
utilizando ese número como el valor más grande de la pirámide. 
Cada línea de la pirámide debe contener el número repetido el mismo número de veces que su valor.

Por ejemplo, si se llama a la función imprimirPiramideDescendente(5), se debe mostrar la siguiente salida:

55555
4444
333
22
1

'''

def imprimirPiramideDescendente (numero):

    if (numero) == 0 :
        return ''
    else:
        numString = ''
        for num in len(numero):
            numString += str(numero)
        return int(numString)
        

print (imprimirPiramideDescendente(5))