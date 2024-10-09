'''
El método index permite buscar un elemento dentro de una lista, devolviendo la posición que éste ocupa. Sin embargo, 
si el elemento no pertenece a la lista se produce una excepción de tipo ValueError. 
Desarrollar un programa que cargue una lista con números enteros ingresados a través del teclado (terminando con -1) 
y permita que el usuario ingrese el valor de algunos elementos para visualizar la posición que ocupan, utilizando el método index. 
Si el número no pertenece a la lista se imprimirá un mensaje de error y se solicitará otro para buscar. 
Abortar el proceso al tercer error detectado. No utilizar el operador in durante la búsqueda.
'''

def verifyNumberinList (number):
    contadorNoEncontrado = 0
    position = 0
    while contadorNoEncontrado < 3:
        try:
            position = lista.index(number)
            print('El numero ingresado se encuentra en la posicion: ', position)  
        except:
            print('El valor no existe dentro de la lista')
            contadorNoEncontrado += 1
            return None

def ingresarNumero ():
    isNumeroInt = False
    number = input('Ingrese un numero para agregar a la lista')

    while not isNumeroInt:
        try:
            int(number)
            isNumeroInt = True
            return number
        except:
            print('El valor no es un entero')
            input('Ingrese un numero para agregar a la lista')

lista = []
numero = ingresarNumero()

while numero != -1:
    lista.append(numero)
    numero =  ingresarNumero()

verifyNumberinList(numero)