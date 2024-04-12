'''
Escribir un programa que permita ingresar los números de legajo de los alumnos de un curso y su nota de examen final. El fin de la carga se determina 
ingresando un -1 en el legajo. Informar para cada alumno si aprobó o no el examen considerando que se aprueba con nota mayor o igual a 4. Se debe 
validar que la nota ingresada sea entre 1 y 10. Terminada la carga de datos, informar:
· Cantidad de alumnos que aprobaron con nota mayor o igual a 4.
· Cantidad de alumnos que desaprobaron el examen con nota menor a 4.
· Porcentaje de alumnos que están aplazados (tienen 1 en el examen).
'''

legajo = input('Ingrese el legajo del alumno')
notaFinal = int(input('Ingrese la nota del alumno'))
nAprobados = 0
nDesaprobados = 0
nAplazados = 0

while legajo != -1:
    notaFinal = int(input('Ingrese la nota del alumno'))
    while not (notaFinal <=10 and notaFinal >=1):
        notaFinal = int(input('Ingrese una nota valida del 1 al 10'))
    if notaFinal <=4:
        print('El alumno con legajo', legajo, 'aprobo el Final')  
    elif notaFinal <4 and notaFinal>1:
        print('El alumno con legajo', legajo, 'no aprobo el Final')
    else:
        print('El alumno con legajo', legajo, 'aplazo la materia')
    
    legajo = input('Ingrese el legajo del alumno')