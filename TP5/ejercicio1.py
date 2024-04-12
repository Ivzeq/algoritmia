'''
Leer números que representan edades de un grupo de personas, finalizando la lectura cuando se ingrese el número -1. Imprimir cuántos son menores de 18
años, cuántos tienen 18 años o más y el promedio de edad de ambos grupos. Descartar valores que no representan una edad válida. (Se considera 
válida una edad entre 0 y 100).
'''

nMenores18 = 0
nMayores18 = 0
promedioEdad = 0
nPersonasIngresadas = 0
nTotalEdades = 0

edadIngresada = 0

edadIngresada = int(input('Ingresar una edad entre 0 y 100 años\n'))

while edadIngresada != -1:
    while not (edadIngresada <= 100 and edadIngresada >0) or edadIngresada == -1:
        edadIngresada = int(input('El numero ingresado excede el rango requerido. Ingresar una edad entre 0 y 100 años\n'))  
    if edadIngresada < 18:
        nMenores18 += 1
    else:
        nMayores18 += 1
    nPersonasIngresadas += 1
    nTotalEdades += edadIngresada  
    edadIngresada = int(input('Ingresar una edad entre 0 y 100 años\n'))  

if nTotalEdades >0:
    promedioEdad = nTotalEdades//nPersonasIngresadas

print('La cantidad de menores de 18 años es', nMenores18)
print('La cantidad de mayores de 18 años es', nMayores18)
print('El promedio de edad en el grupo de personas es', promedioEdad)