from math import sqrt
from sys import maxint

__author__ = 'Dmitry'

from Utils import *
import numpy

def getFullSubsetDefinition(number):
    return (number << 1) + 1

def getShortSubsetDefinition(number):
    return number >> 1

def getDistance(vertex1, vertex2):
    return sqrt((vertex1[0] - vertex2[0]) ** 2 + (vertex1[1] - vertex2[1]) ** 2)

def fill(number, matrix, matrixInited, vertexes, vertexesCount):
    fullSubsetDefinition = getFullSubsetDefinition(number)
    for j in xrange(1, vertexesCount):
        matrix[number, j] = maxint
        jMask = getMaskForPosition(j)

        if isPosition(fullSubsetDefinition, jMask): #if j in set
            subsetWithoutJFullDefinition = addOrRemovePosition(fullSubsetDefinition, jMask)
            subsetWithoutJShortDefinition = getShortSubsetDefinition(subsetWithoutJFullDefinition)
            for k in xrange(vertexesCount):
                if k == j:
                    continue
                if not isPosition(subsetWithoutJFullDefinition, getMaskForPosition(k)):
                    continue
                if not matrixInited[subsetWithoutJShortDefinition]: fill(subsetWithoutJShortDefinition, matrix, matrixInited, vertexes, vertexesCount)
                value = matrix[subsetWithoutJShortDefinition, k] + getDistance(vertexes[k], vertexes[j])
                if value < matrix[number, j]: matrix[number, j] = value

    matrixInited[number] = True

def process(filename):
    vertexes, vertexesCount = read(filename)


    #we use only subsets with 1 on the end because we need only subsets with {0}. See getFullSubsetDefinition
    matrix = numpy.zeros(shape=(2 ** (vertexesCount - 1), vertexesCount), dtype=numpy.float32)
    matrixInited = [False for x in xrange(2 ** (vertexesCount - 1))]

    for sub in xrange(1, 2 ** (vertexesCount - 1)):
        matrix[sub, 0] = maxint

    #init subset=0 - {0}
    matrix[0, 0] = 0
    for x in xrange(1, vertexesCount):
        matrix[0, x] = maxint
    matrixInited[0] = True

    #start from index 1, because subset = 0 filled already
    for subset in xrange(1, 2 ** (vertexesCount - 1)):
        if not matrixInited[subset]:
            if subset % 200 == 0: print "Progress... %s %%" % (subset * 100 / 2 ** (vertexesCount - 1))
            fill(subset, matrix, matrixInited, vertexes, vertexesCount)

    minValue = maxint
    for j in xrange(1, vertexesCount):
        value = matrix[2 ** (vertexesCount - 1) - 1, j] + getDistance(vertexes[j], vertexes[0])
        if value < minValue: minValue = value

    print "Minimum path: %f" % minValue

process("tsp.txt")
