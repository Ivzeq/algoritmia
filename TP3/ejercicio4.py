'''
En el congreso se vota una ley muy importante. Desarrollar un programa que permita ingresar la cantidad de votos a favor y en contra, e informe el porcentaje
obtenido en cada caso y si la misma fue aprobada o no.
'''

votesFor = int(input('Ingrese los votos a favor\n'))
votesAgainst = int(input('Ingrese los votos en contra\n'))

votesTotal = votesFor + votesAgainst

votesForPercent = round(votesFor * 100 / votesTotal)
votesAgainstPercent = round(votesAgainst * 100 / votesTotal)

if votesFor> votesAgainst:
    print('La ley esta aprobada con un', votesForPercent, '% de votos a favor y un', votesAgainstPercent, '% de votos en contra.')
elif votesAgainst> votesFor:
    print('La ley esta desaprobada con un', votesForPercent, '% de votos a favor y un', votesAgainstPercent, '% de votos en contra.')
else:
    print('La cantidad de votos postivos y negativos es igual')