import networkx as nx

__author__ = 'Dmitry'

from Utils import *

def process(filename):
    edges, vertexesNumber, edgesNumber = read(filename)
    G=nx.DiGraph()
    G.add_nodes_from(xrange(1, vertexesNumber + 1))
    G.add_weighted_edges_from(edges)

    print "Graph %s formed" % filename

    if nx.negative_edge_cycle(G):
        print "Graph %s has negative cycle" % filename
        return

    print "Begin FW for %s" %filename
    lengths = nx.floyd_warshall(G)

    shortestPathLengths = map(dict.values, lengths.values())

    shortestPathLength = min(min(raw) for raw in shortestPathLengths)

    print "Shortest path for %s: %d" % (filename, shortestPathLength)

process("g1.txt")
process("g2.txt")
process("g3.txt")
