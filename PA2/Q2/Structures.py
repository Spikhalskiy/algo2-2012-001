__author__ = 'Dmitry'
class Vertex:
    bitIntArray = None
    bitSum = None
    cluster = None
    applicableMin = None
    applicableMax = None

    def __init__(self, bitIntArray, cluster, clusterSize):
        self.bitIntArray = bitIntArray
        self.bitSum = reduce(lambda x,y : x + y, bitIntArray)
        self.applicableMin = self.bitSum - clusterSize + 1
        self.applicableMax = self.bitSum + clusterSize - 1
        self.cluster = cluster

def setVertexClusterInternal(vertex, cluster):
    vertex.cluster = cluster

class FoundUnion:
    vertices = None
    clustersCount = None

    #should be inited by list of vertices, all of them must have different clusters
    def __init__(self, vertices):
        self.vertices = vertices
        self.clustersCount = len(vertices)

    def union(self, vertex1, vertex2):
        cluster1 = vertex1.cluster
        cluster2 = vertex2.cluster

        if cluster1 != cluster2:
            self.clustersCount -= 1
            print "Clusters count: %d" % self.clustersCount
        map(lambda vertex : setVertexClusterInternal(vertex, cluster1), filter(lambda vertex : vertex.cluster == cluster2, self.vertices))

def isApplicableForMergeAnalyze(vertex1, vertex2):
    return vertex1.applicableMin <= vertex2.bitSum <= vertex1.applicableMax

def calcDistance(vertex1, vertex2):
    return sum(1 if bit1 != bit2 else 0 for bit1, bit2 in zip(vertex1.bitIntArray, vertex2.bitIntArray))