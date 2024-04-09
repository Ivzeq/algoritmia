'''
Realizar un programa que lea un número natural H e imprima un mensaje indicando
si H es primo o no. Se dice que un número es primo cuando sólo es divisible
por sí mismo y por la unidad.
'''

numero = int(input('Ingresar numero a evaluar\n'))
contadorNumero = 2
divisibilidadCorrecta = True

while contadorNumero < numero:
    if numero % contadorNumero !=0:
        contadorNumero += 1
    elif numero % contadorNumero == 0:
        divisibilidadCorrecta = False
        contadorNumero = numero + 1
        

if divisibilidadCorrecta == True:
    print('El numero', numero, 'es primo')
else:
    print('El numero', numero, 'no es primo')