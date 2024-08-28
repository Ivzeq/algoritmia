'''
Escriba una función, que dada una lista con notas entre 0 y 10, 
retorne otra lista indicando su resultado por cada posición; 
utilizando una función que al recibir una nota retorne:

0: Ausente
Entre 1 y 3: Desaprobado
Entre 4 y 6: Aprobado
Entre 7 y 10: Promocionado
'''

def EvaluarAprobados (lista1):
    finalList = []
    for i in range (0,len(lista1)):
        if(lista1[i] == 0):
            return 'Ausente'
    return finalList

listaEvaluar1 = [0,2,3,10,3,4,2,7,4,8,6,2,1,3,5,3,4]

print(EvaluarAprobados(listaEvaluar1))