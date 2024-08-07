'''
Crear una función que retorne una lista que tenga los valores pares que se encuentran 
dentro de un rango dado (dicho rango se recibe como parámetro de la función: desde/hasta).
'''
def GetNumerosParesEnRango (desde, hasta):
    listaPares = []
    for i in range (desde, hasta + 1):
        if i % 2 == 0:
            listaPares.append(i)

    return listaPares

print(GetNumerosParesEnRango(-40, 10))