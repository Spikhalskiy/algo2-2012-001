__author__ = 'Dmitry'

def read(fileName):
    with open(fileName, "r") as f:
        lines = f.readlines()
        nodesCount = int(lines[0].split(" ", 1)[0])
        array = list(map(int, line.split(" ", 2)) for line in lines[1:])
        return array, nodesCount

def fillMatrix(matrix, list):
    for triplet in list:
        matrix[triplet[0]][triplet[1]] = triplet[2]