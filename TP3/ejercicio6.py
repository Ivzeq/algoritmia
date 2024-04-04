'''
Una editorial determina el precio de un libro según la cantidad de páginas que contiene. El costo básico del libro es de $5000, más $32 por página con encuadernación
rústica. Si el número de páginas supera las 300 la encuadernación debe ser en tela, lo que incrementa el costo en $1200. Además, si el número de
páginas sobrepasa las 600 se hace necesario un procedimiento especial de encuadernación que incrementa el costo en otros $3360. Desarrollar un programa
que calcule el costo de un libro dado el número de páginas.
'''

cantPaginas = int(input('Ingrese la cantidad de paginas\n'))
precioBase = 5000
costoEncuadernacionTela = 1200
costoMayorA600 = 3360
precioPorPagina = 32
precioFinal = precioBase

precioFinal = precioBase + cantPaginas * precioPorPagina

if cantPaginas > 300 :
    precioFinal = precioFinal + costoEncuadernacionTela
    if cantPaginas > 600:
        precioFinal = precioFinal + costoMayorA600

print('El precio final para un libro de', cantPaginas, 'paginas es $', precioFinal)