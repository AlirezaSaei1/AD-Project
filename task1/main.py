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


def vertical(car):
    return abs(car[1]-car[0]) != 1


def solve(i, j):
    if promising(i, j):
        printMatrix(matrix)
        if (i, j) == getDimension(target):
            # print_matrix(matrix)
            print(answer)
            print('solved')
            return
        else:
            for dir in moves:
                x, y = i+dir[0], j+dir[1]
                if promising(x, y):
                    car = cars[matrix[x][y]-1]
                    x = i + len(car) * dir[0]
                    y = j + len(car) * dir[1]
                    if promising(x, y):
                        if len(car) == 1 or\
                                vertical(car) and dir in [(-1, 0), (1, 0)] or\
                                not vertical(car) and dir in [(0, -1), (0, 1)]:
                            history.append(matrixToString())
                            print(x, y)
                            matrix[i][j] = matrix[x][y]
                            matrix[x][y] = 0
                            solve(x, y)
                            matrix[x][y] = matrix[i][j]
                            matrix[i][j] = 0
                            history.remove(matrixToString())


def promising(i, j):
    if i < 0 or j < 0 or i >= size[0] or j >= size[1]:
        return False

    if (i, j) == getDimension(camera):
        return False

    return matrixToString() not in history


history = []
answer = []
moves = [(0, -1), (-1, 0), (0, 1), (1, 0)]
visited = [[False for _ in range(size[0])] for _ in range(size[1])]

matrix = buildMatrix()
printMatrix(matrix)
it, jt = getDimension(target)

# Indices of empty tile (15)
solve(0, 2)
