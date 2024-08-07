'''
Crear una función que reciba como parámetro un valor numérico. 
En caso de que ese valor recibido como parámetro sea múltiplo de 3, 
se debe retornar el resultado de su cubo (para calcular el cubo de dicho valor, utilizar otra función). 
De no se múltiplo de 3, retornar el valor -1.
'''
def VerifyMultiplo3 (numero):
    finalValue = -1
    if (numero % 3 == 0):
        finalValue = CuboDelNumero(numero)

    return finalValue

def CuboDelNumero (numero):
    return numero **3

print(VerifyMultiplo3(3))