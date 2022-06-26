import json

with open("task1/data.json", "r") as f:
    data = json.loads(f.read())

size = data['size']
target = data['target']
camera = data['camera']
cars = data['cars']


def printMatrix(matrix):
    for row in matrix:
        print(*row)


def matrixToString():
    st = ""
    for x in matrix:
        st += "".join(str(c) for c in x)
    return st


def getDimension(n):
    row = size[0] - ((n-1) // size[1]) - 1
    column = (n - 1) % size[1]

    return row, column


def buildMatrix():
    matrix = [[0 for _ in range(size[1])] for _ in range(size[0])]
    i, j = getDimension(camera)
    matrix[i][j] = "C"

    count = 1
    for car in cars:
        for pos in car:
            i, j = getDimension(pos)
            matrix[i][j] = count
        count += 1
    return matrix


def solve(i, j):
    if promising(i, j):
        if (i, j) == getDimension(target):
            print('Solved')
            return
        else:
            for dir in moves:
                pass


def promising(i, j):
    if i < 0 or j < 0 or i >= size[0] or j >= size[1]:
        return False

    if (i, j) == getDimension(camera):
        return False

    return matrixToString() not in history


history = []
moves = [(0, -1), (-1, 0), (0, 1), (1, 0)]

matrix = buildMatrix()
printMatrix(matrix)
it, jt = getDimension(target)
solve(it, jt)
