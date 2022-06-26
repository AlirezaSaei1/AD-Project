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


def getDimension(n):
    row = size[0] - ((n-1) // size[1]) - 1
    column = (n - 1) % size[1]

    return row, column


def buildMatrix():
    matrix = [[0 for _ in range(size[1])] for _ in range(size[0])]
    ic, jc = getDimension(camera)
    matrix[ic][jc] = "C"

    count = 1
    for car in cars:
        i1, j1 = getDimension(car[0])
        i2, j2 = getDimension(car[1])
        matrix[i1][j1] = count
        matrix[i2][j2] = count
        count += 1
    return matrix


def solve():
    if matrix[it][jt] == 0:
        return True

    for c in cars:
        pass


matrix = buildMatrix()
printMatrix(matrix)
it, jt = getDimension(target)
