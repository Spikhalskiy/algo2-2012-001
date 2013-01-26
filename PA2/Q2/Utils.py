__author__ = 'Dmitry Spikhalskiy'

def read(fileName):
    with open(fileName, "r") as f:
        lines = f.readlines()
        array = list(map(int, filter(lambda char : char != '\n', line.split(" "))) for line in lines[1:])
        return array, int(lines[0].split(" ")[0]), int(lines[0].split(" ")[1])