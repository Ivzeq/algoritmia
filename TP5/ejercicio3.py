'''
Una empresa aplica el siguiente procedimiento en la comercialización de sus productos:
· Aplica el precio base a la primera docena de unidades.
· Aplica un 10% de descuento a todas las unidades entre 13 y 100.
· Aplica un 25% de descuento a todas las unidades por encima de las 100.
Por ejemplo, supongamos que vende 230 unidades de un producto cuyo precio base es 100. El cálculo resultante sería:

100 * 12 + 90 * 88 + 75 * 130 = 18870 y el precio promedio es de 18870/230 = 82.04

Escribir un programa que lea la cantidad solicitada de un producto y su precio base, y muestre el valor total de la venta y el precio promedio por unidad. 
El finde carga se determina ingresando -1 como cantidad solicitada. Al finalizar informar:
· Cantidad de ventas realizadas total.
· Cantidad de ventas en las que se aplicó un 10% de descuento.
· Cantidad de ventas en las que SOLO se aplicó el precio base, es decir que no se le realizaron descuentos.
'''

precioBase = 0
nProducto = 0

nVentas = 0
valorTotalVentas = 0
precioPrmedio = 0
nVentas10percent = 0
nVentasPrecioBase = 0

nProducto = int(input('Ingrese la cantidad de producto\n'))

while (nProducto != -1):
    while (nProducto <= 0):
        nProducto = int(input('Ingrese la cantidad de producto\n'))
    if(nProducto> 0):
        precioBase = int(input('Ingrese el precio base del producto\n'))

    if (nProducto <= 12):
        nVentasPrecioBase += nProducto
        valorTotalVentas = nProducto * precioBase
    elif(nProducto > 12):
        nVentasPrecioBase += 12
        valorTotalVentas +=  12 * precioBase
        if (nProducto > 12 and nProducto <= 100):
            nVentas10percent += nProducto - 12
            valorTotalVentas += (nProducto - 12) * (precioBase * 0.9)
        elif (nProducto > 100):
            nVentas10percent += 88
            valorTotalVentas += 88 * (precioBase * 0.9) + (nProducto - 100) * (precioBase * 0.75)
            

    nVentas += nProducto
    precioPrmedio = valorTotalVentas / nVentas
    nProducto = int(input('Ingrese la cantidad de producto\n'))

print('El valor total de la venta es:', valorTotalVentas)
print('El precio promedio por unidad es:', precioPrmedio)
print('La cantidad total de ventas es:', nVentas)
print('La cantidad de ventas con un 10% de descuento es:', nVentas10percent)
print('La cantidad de ventas a precio base es:', nVentasPrecioBase)