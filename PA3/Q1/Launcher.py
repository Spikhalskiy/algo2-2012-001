__author__ = 'Dmitry'

from Utils import *

list, fullCapacity = read("knapsack1.txt")

matrix = [[0 for x in xrange(fullCapacity + 1)] for x in xrange(len(list) + 1)]

for count in xrange(1, len(list) + 1) :
    for capacity in xrange(0, fullCapacity + 1) :
        item = list[count - 1]
        matrix[count][capacity] = max(
            matrix[count - 1][capacity],
            matrix[count - 1][capacity - item[1]] + item[0] if capacity - item[1] > 0 else 0)

print matrix[len(list)][fullCapacity]