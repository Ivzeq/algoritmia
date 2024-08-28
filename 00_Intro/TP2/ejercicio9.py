'''
Ejercicio 9: Una inmobiliaria paga a sus vendedores un salario de $250000, más una comisión de $50000 por cada venta realizada, más el 5% del valor de las ventas.
Realizar un programa que imprima el número del vendedor y el salario que le corresponde en un determinado mes. Se leen el número del vendedor, 
la cantidad de ventas que realizó y el valor total de las mismas.
'''

salarioBase = 250000
bonoVentas = 50000
porcentajeVentas = 0.05

numeroVendedor = input('Ingrese el numero de vendedor\n')
nVentasRealizadas = int(input('Ingrese la cantidad de ventas realizadas\n'))
valorTotalVentasRealizadas = int(input('Ingrese el valor total de las ventas realizadas\n'))

salarioFinal = salarioBase + (bonoVentas * nVentasRealizadas) + (valorTotalVentasRealizadas * porcentajeVentas)

print('El vendedor Nro', numeroVendedor, 'tendra un salario de', salarioFinal)