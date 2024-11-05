'''
Crear una función recursiva para conceptualizar el funcionamiento de un semáforo con tres luces (rojo, amarillo y verde).
La función debe recibir como parámetro el color inicial y seguir esta secuencia para la representación de los colores: 
rojo, verde, amarillo (y repetir nuevamente a partir del rojo). La cantidad de veces que se va a realizar el ciclo estará parametrizada. 
La función tendrá la siguiente definición: def semaforo(ciclos, color). 

Ejemplo: semaforo(4, “verde”)
verde
amarillo
rojo
verde
'''

def simularSemaforo (ciclo, colorInicial):

    if ciclo == 1 :
        print(colorInicial)
    else:
        print(colorInicial)
        if colorInicial == 'rojo':
            simularSemaforo(ciclo-1, 'amarillo')
        if colorInicial == 'amarillo':
            simularSemaforo(ciclo-1, 'verde')
        if colorInicial == 'verde':
            simularSemaforo(ciclo-1, 'rojo')
        

simularSemaforo(4, 'rojo')