__author__ = 'Dmitry'

from Utils import *
from Structures import *

CLUSTER_DISTANCE = 3

vertexList, vertexCount, bitLength = read("clustering2.txt")

vertices = []
for index in range(vertexCount) :
    vertices.append(Vertex(vertexList[index], index, CLUSTER_DISTANCE))

foundUnion = FoundUnion(vertices)

for currentMergerIndex in range(vertexCount) :
    merger = vertices[currentMergerIndex]

    for currentAnalyzedIndex in range(currentMergerIndex + 1, vertexCount):
        analyzed = vertices[currentAnalyzedIndex]
        if merger.cluster == analyzed.cluster: continue
        if isApplicableForMergeAnalyze(merger, analyzed):
            distance = calcDistance(merger, analyzed)
            if distance < CLUSTER_DISTANCE:
                foundUnion.union(merger, analyzed)

print foundUnion.clustersCount





