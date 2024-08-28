'''
Diseñar un programa que calcule y muestre el sueldo neto de un empleado en base a su sueldo básico y su antigüedad en años. Si es soltero se le incrementa
el sueldo en 5% del salario bruto por cada año de antigüedad, mientras que si es casado se le incrementa el sueldo en 7% del bruto por cada año de antigüedad.
También se le realizan los siguientes descuentos: Jubilación: 11%, Obra Social: 3%, Sindicato: 3%
'''

sueldoBruto = int(input('Ingrese el sueldo bruto\n'))
antiguedad = int(input('Ingrese la antiguedad en años\n'))
isSoltero = input('Ingrese S en caso de ser soltero y C en caso de estar casado\n')

porcentajeJubilacion = 11
porcentajeObraSocial = 3
porcentajeSindicato = 3
porcentajeSoltero = 5
porcentajeCasado = 7

sueldoNeto = sueldoBruto 

if isSoltero == 'S':
    extraAntiguedad = antiguedad * porcentajeSoltero
elif isSoltero == 'C':
    extraAntiguedad = antiguedad * porcentajeCasado
    
sueldoNeto += (sueldoNeto * extraAntiguedad /100)
sueldoNeto -= (sueldoNeto * porcentajeJubilacion /100 + sueldoNeto * porcentajeObraSocial /100 + sueldoNeto * porcentajeSindicato /100)
print('El sueldo neto final es de $', sueldoNeto)