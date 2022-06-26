import json

with open("task1/data.json", "r") as f:
    data = json.loads(f.read())

n, m = data['size']
target = data['target']
camera = data['camera']
cars = data['cars']


def dimension(pos):
    row = n - ((pos-1) // m) - 1
    column = (pos - 1) % m
    return row, column


def build_matrix():
    matrix = [[0 for _ in range(m)] for _ in range(n)]
    i, j = dimension(camera)
    matrix[i][j] = "C"

    count = 1
    for car in cars:
        for pos in car:
            i, j = dimension(pos)
            matrix[i][j] = count
        count += 1
    return matrix


dirs = [(0, -1), (-1, 0), (0, 1), (1, 0)]

history = []


def hist():
    stamp = ''
    for row in range(n):
        for column in range(m):
            stamp += str(matrix[row][column])
    return stamp


def vertical(car):
    return abs(car[1]-car[0]) != 1


answer = []
ways = []


def solve(i, j):
    if (i, j) == dimension(target):  # target cell is empty
        # append answer as a solution
        ways.append((len(answer), answer.copy()))
        return
    else:
        for dir in dirs:  # top down left right
            x, y = i+dir[0], j+dir[1]
            if promising(x, y):
                car = cars[matrix[x][y]-1]
                # (x, y) will be position of the end of the car
                x = i + len(car) * dir[0]
                y = j + len(car) * dir[1]
                if promising(x, y):
                    # cars with length 1 can move in all directions
                    # horizontal cars only moves horizontally
                    # verticall cars only move vertically
                    if len(car) == 1 or\
                            vertical(car) and dir in [(-1, 0), (1, 0)] or\
                            not vertical(car) and dir in [(0, -1), (0, 1)]:
                        history.append(hist())
                        # swap end of car with empty cell
                        matrix[i][j], matrix[x][y] = matrix[x][y], matrix[i][j]
                        # add this car to answer as moved car
                        answer.append(matrix[i][j])
                        # solve for next empty cell
                        solve(x, y)
                        answer.remove(matrix[i][j])
                        # bactrackt
                        matrix[x][y], matrix[i][j] = matrix[i][j], matrix[x][y]
                        history.remove(hist())


def promising(i, j):
    if i < 0 or j < 0 or i >= n or j >= m:
        return False

    if (i, j) == dimension(camera):
        return False

    return hist() not in history


if __name__ == "__main__":
    matrix = build_matrix()

    # (i, j) will be the position of initial empty cell
    i = 0
    while 0 not in matrix[i]:
        i += 1
    j = matrix[i].index(0)

    solve(i, j)
    moves, way = min(ways)
    print('Min moves: ', moves)
    print('Cars: ', way)
