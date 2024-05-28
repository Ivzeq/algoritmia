'''
Escribir una función para ingresar desde el teclado una serie de números entre A
y B y guardarlos en una lista. En caso de ingresar un valor fuera de rango la función
mostrará un mensaje de error y solicitará un nuevo número. Para finalizar la
carga se deberá ingresar -1. La función recibe como parámetros los valores de A
y B, y devuelve la lista cargada (o vacía, si el usuario no ingresó nada) como
valor de retorno. Tener en cuenta que A puede ser mayor, menor o igual a B.
'''
def rangoLista(a,b):
    listaValores = []
    inputValue = int(input('Ingrese un numero  \n'))

    while(inputValue!= -1):
        if (a<b):
            if(inputValue < b and inputValue > a):
                    listaValores.append(inputValue)
        elif(b<a):
            if(inputValue < a and inputValue > b):
                    listaValores.append(inputValue)
        else:
            if(a==inputValue):
                listaValores.append(inputValue)

        inputValue = int(input('Ingrese un numero \n'))
        
    return listaValores

a = int(input('Ingrese un numero \n'))
b = int(input('Ingrese un numero \n'))