__author__ = 'Dmitry'

def read(fileName):
    with open(fileName, "r") as f:
        lines = f.readlines()
        array = list(map(int, line.split(" ", 1)) for line in lines[1:])
        return array

def computeWeightEndTimeMetric(weightDurationList):
    metric = 0
    endTime = 0
    for pair in weightDurationList:
        endTime += pair[1]
        metric += pair[0] * endTime
    return metric