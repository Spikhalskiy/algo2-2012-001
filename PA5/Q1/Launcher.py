from math import sqrt
from sys import maxint

__author__ = 'Dmitry'

from Utils import *
import numpy

def getDistance(vertex1, vertex2):
    return sqrt((vertex1[0] - vertex2[0]) ** 2 + (vertex1[1] - vertex2[1]) ** 2)

def fill(number, matrix, matrixInited, vertexes, vertexesCount):
    for j in xrange(1, vertexesCount):
        matrix[number, j] = maxint
        jMask = getMaskForPosition(j)

        if isPosition(number, jMask): #if j in set
            subsetWithoutJ = addOrRemovePosition(number, jMask)

            for k in xrange(vertexesCount):
                if not isPosition(number, getMaskForPosition(k)): continue
                if k == j: continue
                if not matrixInited[subsetWithoutJ]: fill(subsetWithoutJ, matrix, matrixInited, vertexes, vertexesCount)
                value = matrix[subsetWithoutJ, k] + getDistance(vertexes[k], vertexes[j])
                if value < matrix[number, j]: matrix[number, j] = value

    matrixInited[number] = True

def process(filename):
    vertexes, vertexesCount = read(filename)

    matrix = numpy.zeros(shape=(2 ** vertexesCount, vertexesCount))
    matrixInited = [False for x in xrange(2 ** vertexesCount)]

    for sub in xrange(2, 2 ** vertexesCount):
        matrix[sub, 0] = maxint

    #init subset=1 - {0}
    matrix[1, 0] = 0
    for x in xrange(2, vertexesCount):
        matrix[1, x] = maxint
    matrixInited[1] = True

    #start from index 2, because subset = 0 is not actual, subset = 1 filled already
    for subset in xrange(2, 2 ** vertexesCount):
        if not matrixInited[subset] and isPosition(subset, 1):
            fill(subset, matrix, matrixInited, vertexes, vertexesCount)

    minValue = maxint
    for j in xrange(1, vertexesCount):
        value = matrix[2 ** vertexesCount - 1][j] + getDistance(vertexes[j], vertexes[0])
        if value < minValue: minValue = value

    print matrix
    print "Minimum path: %s" % minValue

process("tsp.txt")
