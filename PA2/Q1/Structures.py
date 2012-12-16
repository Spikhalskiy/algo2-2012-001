__author__ = 'Dmitry'

class Edge:
    node1 = None
    node2 = None
    cost = None

    def __init__(self, node1, node2, cost):
        self.node1 = node1
        self.node2 = node2
        self.cost = cost

def createEdge(array):
    return Edge(array[0], array[1], array[2])

class Vertex:
    number = None
    cluster = None

    def __init__(self, number):
        self.number = number
        self.cluster = number

def setVertexClusterInternal(vertex, cluster):
    vertex.cluster = cluster

class FoundUnion:
    vertices = None
    clustersCount = None

    #should be inited by sorted list of vertices, where number of vertex is (index in this list + 1) and all of them must have different clusters
    def __init__(self, sortedVertices):
        self.vertices = sortedVertices
        self.clustersCount = len(sortedVertices)

    def union(self, vertex1Number, vertex2Number):
        cluster1 = self.getVertexCluster(vertex1Number)
        cluster2 = self.getVertexCluster(vertex2Number)

        if cluster1 != cluster2:
            self.clustersCount -= 1
            map(lambda vertex : setVertexClusterInternal(vertex, cluster1), filter(lambda vertex : vertex.cluster == cluster2, self.vertices))

    def getVertexCluster(self, vertexNumber):
        return self.vertices[vertexNumber - 1].cluster