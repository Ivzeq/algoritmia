'''
Ejercicio 13: Escribir un programa para convertir un número binario de 4 cifras en un número decimal. El número binario se ingresa como un solo número entero de cuatro dígitos.

Procedimiento: Para convertir un número binario a decimal es necesario multiplicar el valor de cada dígito por el número 2 elevado a un exponente. Este
exponente se obtiene de la posición que ocupa el dígito dentro del número, comenzando desde la derecha con la posición 0. Todos estos resultados se
suman para obtener el valor final. 
'''

binarioInicial = int(input('Ingrese el numero binario\n'))
binarioProcesado = binarioInicial

cifra1000 = binarioProcesado//1000

if binarioProcesado >= 1000:
    binarioProcesado = binarioProcesado - cifra1000 *1000


cifra100 = binarioProcesado//100

if binarioProcesado >= 100:
    binarioProcesado = binarioProcesado - cifra100 *100

cifra10 = binarioProcesado//10

if binarioProcesado >= 10:
    binarioProcesado = binarioProcesado - cifra10 *10

cifra1 = binarioProcesado//1

if binarioProcesado >= 1:
    binarioProcesado = binarioProcesado - cifra1 *1

binarioEnDecimal = cifra1 * 1 + cifra10 * 2 + cifra100 * 4 + cifra1000 * 8

print('El numero binario', binarioInicial, 'representa en decimal el', binarioEnDecimal)