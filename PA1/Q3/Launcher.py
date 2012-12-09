__author__ = 'Dmitry'

from Utils import *
from sys import maxint



list, nodesCount = read("edges.txt")               # Get all the arguments
edgesMatrix = [[maxint for y in xrange(nodesCount + 1)] for x in xrange(nodesCount + 1)] #we will not use 0 indexed elements

fillMatrix(edgesMatrix, list)

v = range(2, nodesCount + 1)
x = [1]

mstWeight = 0
while len(v):
    print "V length %s" % len(v)

    detectedEdge = None
    minimumWeight = maxint
    isBack = False
    for vertex in x:
        for secondVertexIndex in range(1, nodesCount + 1):
            if secondVertexIndex in v:
                edgeWeight = edgesMatrix[vertex][secondVertexIndex]
                if edgeWeight < minimumWeight:
                    minimumWeight = edgeWeight
                    detectedEdge = [vertex, secondVertexIndex]
                    isBack = False
                edgeWeight = edgesMatrix[secondVertexIndex][vertex]
                if edgeWeight < minimumWeight:
                    minimumWeight = edgeWeight
                    detectedEdge = [secondVertexIndex, vertex]
                    isBack = True

    if detectedEdge is None: break
    detectedVertex = detectedEdge[0] if isBack else detectedEdge[1]
    x.append(detectedVertex)
    v.remove(detectedVertex)
    mstWeight += edgesMatrix[detectedEdge[0]][detectedEdge[1]]

print "MST weight: %s" % mstWeight







