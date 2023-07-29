from random import randint
from time import sleep
def titulo():
    print('Gerador de senha 1.0 | Python')
    print('O programa gera uma senha de 8, 10 e 12números e eles não se repetem!')
    print('Totalmente aleatorio.')
def gerador():
    print()
    agua = []
    while len(agua) < 8:
        cubo = randint(0, 10)
        if cubo not in agua:
            agua.append(cubo)
    print('Sua senha é:', agua)
    print()

    agua1 = []
    while len(agua1) < 10:
        cubo = randint(0, 10)
        if cubo not in agua1:
            agua1.append(cubo)
    print('Sua senha é:', agua1)
    print()
    agua2 = []
    while len(agua2) < 12:
        cubo = randint(0, 12)
        if cubo not in agua2:
            agua2.append(cubo)
    print('Sua senha é:', agua2)


titulo()
gerador()
