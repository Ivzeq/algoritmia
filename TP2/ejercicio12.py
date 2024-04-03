'''
Ejercicio 12: Un banco necesita para sus cajeros automáticos un programa que lea una cantidad de dinero e imprima a cuántos billetes equivale, considerando que
existen billetes de $1000, $500, $100, $50, $10, $5 y $1. 
Desarrollar dicho programa de tal forma que se minimice la cantidad de billetes entregados por el cajero.
'''

cantidadDineroInicial = int(input('Ingrese la cantidad de dinero a procesar\n'))
cantidadDineroProcesado = cantidadDineroInicial

nBilletes1000 = cantidadDineroProcesado//1000

if cantidadDineroProcesado >= 1000:
    cantidadDineroProcesado = cantidadDineroProcesado - nBilletes1000 *1000

nBilletes500 = cantidadDineroProcesado//500

if cantidadDineroProcesado >= 500:
    cantidadDineroProcesado = cantidadDineroProcesado - nBilletes500 *500

nBilletes100 = cantidadDineroProcesado//100

if cantidadDineroProcesado >= 100:
    cantidadDineroProcesado = cantidadDineroProcesado - nBilletes100 *100

nBilletes50 = cantidadDineroProcesado//50

if cantidadDineroProcesado >= 50:
    cantidadDineroProcesado = cantidadDineroProcesado - nBilletes50 *50

nBilletes10 = cantidadDineroProcesado//10

if cantidadDineroProcesado >= 10:
    cantidadDineroProcesado = cantidadDineroProcesado - nBilletes10 *10

nBilletes5 = cantidadDineroProcesado//5

if cantidadDineroProcesado >= 5:
    cantidadDineroProcesado = cantidadDineroProcesado - nBilletes5 *5

nBilletes1 = cantidadDineroProcesado//1

if cantidadDineroProcesado >= 1:
    cantidadDineroProcesado = cantidadDineroProcesado - nBilletes1 *1


print('Se necesitan la siguiente cantidad de cada billete\n',
      nBilletes1000,'de $1000', '\n',
      nBilletes500, 'de $500', '\n',
      nBilletes100, 'de $100', '\n',
      nBilletes50, 'de $50', '\n',
      nBilletes10, 'de $10', '\n',
      nBilletes5, 'de $5', '\n',
      nBilletes1, 'de $1', '\n',
       )