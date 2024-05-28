'''
Escribir una función para contar cuántas veces aparece un valor dentro de la
lista. La función recibe como parámetros la lista y el valor a buscar, y devuelve
un número entero.
'''
def rangoLista(a,b):
    listaValores = []
    inputValue = int(input('Ingrese un numero \n'))

    while(inputValue!= -1):
        if (a<b):
            if(inputValue >= a and inputValue <= b):
                    listaValores.append(inputValue)
        elif(b<a):
            if(inputValue >= b and inputValue <= a):
                    listaValores.append(inputValue)
        else:
            if(a==inputValue):
                listaValores.append(inputValue)

        inputValue = int(input('Ingrese un numero \n'))
        
    return listaValores

def ordenar_lista(lista):
    for i in range(0,len(lista)-1):
        for j in range(i+1, len(lista)):
            if lista[i] > lista[j]:
                aux = lista[i]
                lista[i] = lista[j]
                lista[j] = aux

def get_posiciones (lista, valor):
    posiciones = []
    print(lista)
    izq = 0
    der = len(lista) - 1 
    pos = -1

    while izq <= der and pos == -1:             #Falta funcionalidad cuando hay mas de un valor correcto dentro de la lista
        centro = (izq + der) // 2
        if lista[centro] == valor: 
            posiciones.append(centro)
            pos = centro
        elif lista[centro] < valor: 
            izq = centro + 1
        else:
            der = centro - 1

    return posiciones


a = int(input('Ingrese un numero \n'))
b = int(input('Ingrese un numero \n'))

listaParaEvaluacion = rangoLista(a,b)
ordenar_lista(listaParaEvaluacion)
nValoresEnLista = get_posiciones(listaParaEvaluacion,int(input('Ingrese valor a evaluar \n')))
print(nValoresEnLista)
