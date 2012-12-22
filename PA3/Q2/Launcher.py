__author__ = 'Dmitry'

from Utils import *

def optimize(list, capacity, cache):
    if capacity < 0: raise Exception("Error!")
    if not list: return 0
    if (len(list), capacity) in cache: return cache[(len(list), capacity)]
    testItem = list[-1]
    previosCapacityIfInclude = capacity - testItem[1]
    result = max(
        optimize(list[:-1], previosCapacityIfInclude, cache) + testItem[0] if previosCapacityIfInclude >= 0 else 0,
        optimize(list[:-1], capacity, cache))
    cache[(len(list), capacity)] = result
    return result

list, fullCapacity = read("knapsack2.txt")

print optimize(list, fullCapacity, dict())

