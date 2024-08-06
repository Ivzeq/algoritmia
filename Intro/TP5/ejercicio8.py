'''
Una empresa cuenta con N empleados, divididos en tres categorías (1, 2 y 3).
Por cada empleado se lee su legajo, categoría y salario. Se solicita elaborar un
informe que contenga:
· Importe total de salarios pagados por la empresa.
· Cantidad de empleados que ganan más de $200000.
· Cantidad de empleados que ganan menos de $50000, cuya categoría sea 3.
· Legajo del empleado que más gana.
· Sueldo más bajo.
· Importe total de sueldos por cada categoría.
· Salario promedio
'''

legajo = ''
categoria = ''
salario = 0

importeTotalSalarios = 0
nEmpleados = 0
nEmpleadosMas200k = 0
nEmpleadosMenos50kCategoria3 = 0
sueldoMasAlto = 0
legajoMayorSalario = ''
sueldoMasBajo = 0
totalSueldosCategoria1 = 0
totalSueldosCategoria2 = 0
totalSueldosCategoria3 = 0
salarioPromedio = 0

legajo = input('Ingrese un legajo\n')

while (legajo!= '-1'):
    categoria = input('Ingrese una categoria\n')
    salario = int(input('Ingrese un salario\n'))

    while (salario<=0):
        salario = int(input('Ingrese un salario correcto\n'))
    
    if (sueldoMasBajo == 0 and sueldoMasAlto == 0):
        sueldoMasAlto = salario
        sueldoMasBajo = salario
        legajoMayorSalario = legajo
    
    if (salario > 200000):
        nEmpleadosMas200k += 1

    if (categoria == '3' and salario <= 50000):
        nEmpleadosMenos50kCategoria3 += 1

    if (salario > sueldoMasAlto):
        sueldoMasAlto = salario
        legajoMayorSalario = legajo
        
    if (salario < sueldoMasBajo):
        sueldoMasBajo = salario

    if (categoria == '1'):
        totalSueldosCategoria1 += salario
    elif (categoria == '2'):
        totalSueldosCategoria2 += salario
    elif (categoria == '3'):
        totalSueldosCategoria3 += salario

    importeTotalSalarios += salario
    nEmpleados += 1
    salarioPromedio = importeTotalSalarios / nEmpleados

    legajo = input('Ingrese un legajo\n')

print('El importe total es:', importeTotalSalarios)
print('La cantidad de empleados que gana mas de $200000 es:', nEmpleadosMas200k)
print('La cantidad de empleados que gana menos de $50000 y tiene categoria 3 es:', nEmpleadosMenos50kCategoria3)
print('El legajo del empleado que mas gana es:', legajoMayorSalario)
print('El sueldo mas bajo es:', sueldoMasBajo)
print('El importe total de la categoria 1 es:', totalSueldosCategoria1)
print('El importe total de la categoria 2 es:', totalSueldosCategoria2)
print('El importe total de la categoria 3 es:', totalSueldosCategoria3)
print('El salario promedio es:', salarioPromedio)