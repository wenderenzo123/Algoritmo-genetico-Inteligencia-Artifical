from math import sqrt
import random as rd
Population = 20
generations = 6
listaX = []
listaY = []
listaIndividuosBin = []


def convertIntToBinaryString(intValue, nBits):
    # Converte um inteiro para uma string binária sem o prefixo '0b' e com nBits
    binaryString = bin(intValue)[2:]
    if len(binaryString) < nBits:
        binaryString = '0' * (nBits - len(binaryString)) + binaryString
    return binaryString


def convertBinaryStringToInt(binaryString):
    # Converte uma string binária para um inteiro
    intValue = int(binaryString, 2)
    return intValue


def fitnessFunction(listIndividuos):
    # Calcula o fitness de cada individuo
    for i in range(len(listIndividuos)):
        # Calcula a função fitness
        fitness = sqrt(
            (listIndividuos[i][0] ** 3) + (2*listIndividuos[i][1]**4))
        listIndividuos[i].append(fitness)
    listIndividuos.sort(key=lambda x: x[-1])
    return listIndividuos


def inverterUltimoBit(binaryString):
    if binaryString[-1] == '0':
        binaryString = binaryString[:-1] + '1'
    else:
        binaryString = binaryString[:-1] + '0'
    return binaryString


def mutation(listIndividuos):
    # Mutação de 10%
    for i in range(int(len(listIndividuos))):
        number = rd.randint(0, 100)  # Gera um número aleatório de 0 a 100
        if number >= 90:
            listIndividuos[i][0] = inverterUltimoBit(listIndividuos[i][0])
            listIndividuos[i][1] = inverterUltimoBit(listIndividuos[i][1])
    return listIndividuos


def crossover(listIndividuos):
    # Crossover de 90%
    for i in range(int(len(listIndividuos))):
        number = rd.randint(0, 100)  # Gera um número aleatório de 0 a 100
        if number < 90:
            # Gera um ponto de corte aleatório de 1 a 7
            point = rd.randint(0, 2)
            # Gera um ponto de corte aleatório de 1 a 7
            point2 = rd.randint(0, 2)
            # Faz o crossover entre os dois pontos
            listIndividuos[i][0] = listIndividuos[i][0][:point] + \
                listIndividuos[i][0][point2:]
            listIndividuos[i][1] = listIndividuos[i][1][:point] + \
                listIndividuos[i][1][point2:]
    return listIndividuos

for i in range(0, Population):
    listaX.append(rd.randint(0, 7))
    listaY.append(rd.randint(0, 7))

listaIndividuosInt = [[x, y] for x, y in zip(listaX, listaY)]
listaIndividuosInt = fitnessFunction(listaIndividuosInt)
melhoresIndividuos = []
while True:
    print('Geração: ', 6-generations)
    print('Melhor individuo: ', listaIndividuosInt[0])
    melhoresIndividuos.append(listaIndividuosInt[0])
    print('Fitness: ', listaIndividuosInt[0][-1])
    for i in listaIndividuosInt:
        print("Individuo: ", i)
    if listaIndividuosInt[0][-1] == 0:
        break
    listaIndividuosBin = []
    for i in range(len(listaIndividuosInt)):
        listaIndividuosBin.append(
            [convertIntToBinaryString(listaIndividuosInt[i][0], 3),
             convertIntToBinaryString(listaIndividuosInt[i][1], 3)])
    listaIndividuosBin = mutation(listaIndividuosBin)
    listaIndividuosInt = []
    listaIndividuosInt = crossover(listaIndividuosInt)
    for i in range(len(listaIndividuosBin)):
        listaIndividuosInt.append(
            [convertBinaryStringToInt(listaIndividuosBin[i][0]),
             convertBinaryStringToInt(listaIndividuosBin[i][1])])
    listaIndividuosInt = fitnessFunction(listaIndividuosInt)
    generations -= 1
    if generations == 0:
        break