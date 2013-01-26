__author__ = 'Dmitry Spikhalskiy'

def read(fileName):
    with open(fileName, "r") as f:
        lines = f.readlines()
        array = list(map(int, line.split(" ", 2)) for line in lines[1:])
        return array, int(lines[0].split(" ", 1)[0])