from random import randint

def generarMazo ():
    mazo = []
    palos = ['espada', 'copa', 'basto', 'oro']
    for palo in palos:
        for carta in range (1,13):
            mazo.append((palo,carta))
    return mazo

def getCartas(cantidad, mazo):
    cartasSeleccionadas = []
    while len(cartasSeleccionadas) < cantidad:
        index = randint(0,len(mazo)-1)
        if mazo[index] not in cartasSeleccionadas:
            cartasSeleccionadas.append(mazo[index])
        
    return cartasSeleccionadas

def getCantPalo(palo, cartas):
    cantPalo = 0
    for carta in cartas:
        if palo in carta:
            cantPalo += 1
    return cantPalo

cantidadASeleccionar = int(input('Ingrese la cantidad a seleccionar\n'))
cartasObtenidas = getCartas(cantidadASeleccionar, generarMazo())
paloAContar = input('Ingrese el palo a contar\n')

print(len(generarMazo()))

print(cartasObtenidas)

print(getCantPalo(paloAContar,cartasObtenidas))

