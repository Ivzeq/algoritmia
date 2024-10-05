'''
Leer los números de legajo de los alumnos de un curso y su nota de examen
final. El fin de la carga se determina ingresando un -1 como legajo. Se debe validar
que la nota ingresada esté entre 1 y 10. Terminada la lectura de datos, informar:
· Cantidad de alumnos que aprobaron con nota mayor o igual a 4
· Cantidad de alumnos que desaprobaron el examen. Nota menor a 4
· Promedio de nota y los legajos que superan el promedio
Luego se solicita mostrar un listado de legajos y calificaciones ordenado de manera
ascendente según el número de legajo. Resolver de dos formas: Utilizando
dos listas paralelas y utilizando una matriz de dos filas.
'''

# Inicialización de listas
legajos = []
notas = []

# Lectura de datos
legajo = int(input("Ingrese número de legajo (o -1 para terminar): "))

while legajo != -1:
    nota = int(input("Ingrese la nota del examen final (1-10): "))

    # Validación de la nota
    while nota < 1 or nota > 10:
        print("Nota inválida. Debe estar entre 1 y 10.")
        nota = int(input("Ingrese la nota del examen final (1-10): "))

    # Agregar a las listas
    legajos.append(legajo)
    notas.append(nota)

    # Solicitar el siguiente legajo
    legajo = int(input("Ingrese número de legajo (o -1 para terminar): "))

# Inicialización de contadores
aprobados = 0
desaprobados = 0
suma_notas = 0

# Recorrer las listas para contar aprobados y desaprobados
for i in range(len(notas)):
    if notas[i] >= 4:
        aprobados += 1
    else:
        desaprobados += 1
    suma_notas += notas[i]

# Calcular el promedio de notas
promedio = suma_notas / len(notas)

# Listar legajos que superan el promedio
legajos_superan_promedio = []
for i in range(len(notas)):
    if notas[i] > promedio:
        legajos_superan_promedio.append(legajos[i])

# Ordenar legajos y notas de manera ascendente según el número de legajo
legajos_ordenados = sorted(legajos)
notas_ordenadas = [nota for _, nota in sorted(zip(legajos, notas))]

# Mostrar resultados
print("Cantidad de alumnos que aprobaron con nota mayor o igual a 4:", aprobados)
print("Cantidad de alumnos que desaprobaron el examen (nota menor a 4):", desaprobados)
print("Promedio de nota:", promedio)
print("Legajos que superan el promedio:", legajos_superan_promedio)
print("Listado de legajos y calificaciones ordenado:")
for i in range(len(legajos_ordenados)):
    print("Legajo:", legajos_ordenados[i], "- Nota:", notas_ordenadas[i])
