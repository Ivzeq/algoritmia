'''
Se desea analizar cuántos autos circulan con patente con numeración par y
cuántos con numeración impar en un día. Escribir un programa que permita ingresar
la terminación de la patente (entre 0 y 9) hasta ingresar -1 e informe
cuántos vehículos pasaron con numeración par y cuántos con numeración impar.
'''

ultimoDigitoPatente = int(input('Ingrese el ultimo digito de la patente\n'))
nPatentesPares = 0
nPatentesImpares = 0

while (ultimoDigitoPatente != -1):
    if ultimoDigitoPatente %2 == 0:
        nPatentesPares += 1
    elif ultimoDigitoPatente %2 != 0:
        nPatentesImpares += 1
    ultimoDigitoPatente = int(input('Ingrese el ultimo digito de la patente\n'))
    
print('El numero de patentes pares es', nPatentesPares, 'y el nummero de impares es', nPatentesImpares)