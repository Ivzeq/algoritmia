''' 
Ejercicio 7: Una persona invierte su capital en un banco y desea saber cuánto dinero ganará
en un mes, teniendo en cuenta que el banco paga 2% mensual. ¿Cuánto ganará
en seis meses si deja su dinero invertido?
'''

inversionInicial = float(input('Ingrese la inversion inicial\n'))

inversionPrimerMes = inversionInicial * 1.02

gananciaPrimerMes = inversionPrimerMes - inversionInicial

inversionSextoMes = inversionPrimerMes * 1.02 * 1.02 * 1.02 * 1.02 * 1.02

gananciaSextoMes = inversionSextoMes - inversionInicial

print('La ganancia en el primer mes es de $', gananciaPrimerMes)
print('La ganancia en el sexto mes es de $', gananciaSextoMes)