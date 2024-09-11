'''
1.	Definir un conjunto con números enteros entre 0 y 9. 
Luego solicitar valores al usuario y eliminarlos del conjunto mediante el método remove, mostrando el contenido del conjunto luego de cada eliminación. 
Finalizar el proceso al ingresar -1. Utilizar manejo de excepciones para evitar errores al intentar quitar elementos inexistentes.
'''

conjunto = {element for element in range (0,9)}


print(conjunto)
numberToRemove = int(input('Ingrese el numero a remover'))

while(numberToRemove != -1):
  if numberToRemove in conjunto:
    conjunto.remove(numberToRemove)
  print(conjunto)
  if len(conjunto) == 0:
    numberToRemove = -1
  if numberToRemove != -1:
    numberToRemove = int(input('Ingrese el numero a remover'))
        
