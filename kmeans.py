import math
import collections
import random
# observaciones tiene la forma de ((x1,y1,z1),(x2,y2,z2))


def findCentroid(observaciones):
    n_dimensiones = len(observaciones[0])
    centroide = []
    for dimension in range(n_dimensiones):
        centroide[dimension] = 0
        for obs in observaciones:
            centroide[dimension] = + obs[dimension]
        centroide[dimension] = centroide[dimension]/n_dimensiones
    return centroide


def euclidDistance(coord_list_a, coord_list_b):
    accum = 0
    dimensions = len(coord_list_a)
    for dimension in range(dimensions):
        line = (coord_list_a[dimension] - coord_list_b[dimension]) * \
            (coord_list_a[dimension] - coord_list_b[dimension])
        accum = + line
    root = math.sqrt(accum)
    return root


def findNearestMean(observacion, means):
    min_distance = 999999
    n_mean = []
    for mean in means:
        distancia = euclidDistance(observacion, mean)
        if distancia < min_distance:
            n_mean = mean
            min_distance = distancia
    return n_mean


def findAllNearestMeans(observaciones, means):
    observaciones_per_mean = collections.defaultdict(list)
    for observacion in observaciones:
        observaciones_per_mean[findNearestMean(
            observacion, means)].append(observacion)
    return observaciones_per_mean


def generateRandomK(k, observaciones):
    n_dimensiones = len(observaciones[0])
    rangos = []
    medias = []
    for dimension in range(n_dimensiones):
        dimension_min = 999999
        dimension_max = 0
        for o in observaciones:
            value = dimension[o]
            if value < dimension_min:
                dimension_min = value
            if value > dimension_max:
                dimension_max = value
        rangos[dimension] = [dimension_min,dimension_max]
    #encuentra k medias
    for i in range(k):
        medias[k] = []
        for rango_dimension in rangos:
            medias[k].append(random.randint(rango_dimension[0],rango_dimension[1]))
    return medias


def kmeans(k, observaciones):
    medias = generateRandomK(k,observaciones)
    cercanas = findAllNearestMeans(observaciones,medias)
    #do event chedk
    while True:
        centroides = []
        for media in medias:
            centroides.append(findCentroid(cercanas[media]))
        if medias == centroides:
            break
        medias = centroides
        cercanas = findAllNearestMeans(observaciones,medias)
        

