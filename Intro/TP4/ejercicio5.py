'''
- Ejercicio 5: Desarrollar un programa que imprima los números naturales comprendidos entre
1 y N. El valor de N se ingresa desde el teclado.
'''
numeroImprimir = 1
numeroNaturalN = 0
while numeroNaturalN <= 0:
    numeroNaturalN = int(input('Ingrese un numero natural\n'))


while numeroImprimir <= numeroNaturalN:
    print(numeroImprimir)
    numeroImprimir += 1