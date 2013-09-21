from __future__ import division #make division non truncated

__author__ = 'Dmitry Spikhalskiy'

def getKey(pair):
    return pair[0] - pair[1] + pair[0] / 10000
    # pair[0] / 1000 - we should put jobs with higher weight first in case of equal by assignment

def minusSort(tasksArray):
    return list(reversed(sorted(tasksArray, key = getKey)))

def divisionSort(taskArray):
    return list(reversed(sorted(taskArray, key = lambda task: task[0] / task[1])))