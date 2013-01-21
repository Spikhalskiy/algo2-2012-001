__author__ = 'Dmitry'

def read(fileName):
    with open(fileName, "r") as f:
        lines = f.readlines()
        vCount = int(lines[0])
        array = list(map(float, line.split(" ", 1)) for line in lines[1:])
        return array, vCount

#number from 0
def getMaskForPosition(number):
    return 0b1 << number

def isPosition(code, mask):
    return code & mask != 0

def addOrRemovePosition(code, mask):
    return code ^ mask