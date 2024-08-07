def ContarNNumerosIngresados (lista, numero):
    contador = 0
    for i in range (0, len(lista)-1):
        if lista[i] == numero:
            contador += 1

    return contador

listaEvaluar = [0,2,3,64,3,4,2,3,4,22,34,2,1,3,3,3,3]
numeroEvaluar = int(input('Ingrese un numero entero\n'))

print(ContarNNumerosIngresados(listaEvaluar, numeroEvaluar))