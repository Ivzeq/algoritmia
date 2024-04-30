'''
Un complejo de cines necesita un programa para contabilizar el dinero que recauda.
Por cada función se ingresa la cantidad de espectadores y si esa función
tiene descuento o no (1=Sí, 2=No). La carga finaliza cuando la cantidad de espectadores
sea igual a cero. En ese momento el programa deberá:
· Calcular la recaudación total del complejo, considerando que el valor de la
entrada es de $3500 en los días de descuento $5000 en los días sin
descuento.
· Determinar cuántos espectadores ingresaron con descuento y qué
porcentaje representan sobre el total de funciones.
'''

nEspectadores = 0
nEspectadoresTotal = 0
tieneDescuento = ''
recaudacionTotal = 0
nEspectadoresDescuento = 0
porcentajeEspectadoresDescuento = 0


nEspectadores = int(input('Ingrese la cantidad de espectadores en la funcion\n'))

while (nEspectadores != 0):
    while(nEspectadores < 0):
        nEspectadores = int(input('Cantidad negativa no permitida. Ingrese la cantidad de espectadores en la funcion\n'))
    
    tieneDescuento = input('Ingrese Si en caso de que la funcion tenga descuento y No en el que no lo tenga\n')

    if(tieneDescuento == 'Si'):
        recaudacionTotal += nEspectadores * 3500
        nEspectadoresDescuento += nEspectadores

    elif (tieneDescuento == 'No'):
        recaudacionTotal += nEspectadores * 5000

    nEspectadoresTotal += nEspectadores
    nEspectadores = int(input('Ingrese la cantidad de espectadores en la funcion\n'))

porcentajeEspectadoresDescuento = nEspectadoresDescuento * 100 / nEspectadoresTotal

print('La reacudacion total es de', recaudacionTotal)
print('La cantidad de espectadores con descuento son', recaudacionTotal, ' que representan un porcentaje del', porcentajeEspectadoresDescuento)