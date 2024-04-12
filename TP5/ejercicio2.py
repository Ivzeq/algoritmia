'''
Escribir un programa que permita ingresar los números de legajo de los alumnos de un curso y su nota de examen final. El fin de la carga se determina 
ingresando un -1 en el legajo. Informar para cada alumno si aprobó o no el examen considerando que se aprueba con nota mayor o igual a 4. Se debe 
validar que la nota ingresada sea entre 1 y 10. Terminada la carga de datos, informar:
· Cantidad de alumnos que aprobaron con nota mayor o igual a 4.
· Cantidad de alumnos que desaprobaron el examen con nota menor a 4.
· Porcentaje de alumnos que están aplazados (tienen 1 en el examen).
'''

legajo = int(input('Ingrese el legajo del alumno\n'))
nAprobados = 0
nDesaprobados = 0
nAplazados = 0
nAlumnos = 0

while legajo != -1:
    notaFinal = int(input('Ingrese la nota del alumno\n'))
    while not (notaFinal <=10 and notaFinal >=1):
        notaFinal = int(input('Ingrese una nota valida del 1 al 10\n'))
    
    if notaFinal >=4:
        print('El alumno con legajo', legajo, 'aprobo el Final')  
        nAprobados +=1
    elif notaFinal <4 and notaFinal>1:
        print('El alumno con legajo', legajo, 'no aprobo el Final')
        nDesaprobados +=1
    else:
        print('El alumno con legajo', legajo, 'aplazo la materia')
        nAplazados +=1
    nAlumnos += 1
    legajo = int(input('Ingrese el legajo del alumno\n'))

porcentajeAplazados = int(nAplazados * 100 /nAlumnos)

print('La cantidad de alumnos aprobados es', nAprobados)
print('La cantidad de alumnos desaprobados es', nDesaprobados)
print('El porcentaje de alumnos aplazados es', porcentajeAplazados, '%')