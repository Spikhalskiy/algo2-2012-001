__author__ = 'Dmitry'

def read(fileName):
    with open(fileName, "r") as f:
        lines = f.readlines()
        eCount = int(lines[0])
        array = list(map(int, line.split(" ", 1)) for line in lines[1:])
        return array, eCount