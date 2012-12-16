import sys

__author__ = 'Dmitry'

from Utils import *
from Structures import *

CLUSTERS_COUNT = 4

list, vertexCount = read("clustering1.txt")
edges = map(createEdge, list)
sortedEdges = sorted(edges, key = lambda edge : edge.cost)
vertices = map(Vertex, range(1, 501, 1))
foundUnion = FoundUnion(vertices)

for edge in sortedEdges:
    if foundUnion.clustersCount == CLUSTERS_COUNT:
        break
    foundUnion.union(edge.node1, edge.node2)

distance = sys.maxint

for edge in sortedEdges:
    if foundUnion.getVertexCluster(edge.node1) != foundUnion.getVertexCluster(edge.node2) and edge.cost < distance:
        distance = edge.cost

print "Distance: %s" % distance

