import json
from collections import deque
INF = float('inf')


def printMatrix(matrix):
    for row in matrix:
        print(*row)


def o(c):
    return ord(c) - ord('A')


def c(o):
    return chr(o + ord('A'))


def dijkstra(W, n, src):
    length = [W[src][i] for i in range(n)]
    vselected = [False] * n

    parent = [[] for _ in range(n)]
    parent[src] = [-1]

    for _ in range(n):
        MIN = INF

        for i in range(n):
            if not vselected[i] and length[i] < MIN:
                MIN = length[i]
                vnear = i

        vselected[vnear] = True

        for i in range(n):
            if not vselected[i]:
                if length[vnear] + W[vnear][i] < length[i]:
                    length[i] = length[vnear] + W[vnear][i]
                    parent[i] = [vnear]
                elif length[vnear] + W[vnear][i] == length[i]:
                    parent[i].append(vnear)

    return length, parent


def print_path(places, path):
    print(' -> '.join([places[c(place)] for place in path]))


def find_paths(parents, src, dst):
    path = [src]
    q = deque([path])

    while q:
        path = q.popleft()
        last = path[-1]

        if last == dst:
            yield path[::-1]

        for parent in parents[last]:
            if parent not in path:
                newpath = path + [parent]
                q.append(newpath)


def find_place(places, place_name):
    for symbol, name in places.items():
        if name == place_name:
            return o(symbol)
    return -1


def TSP(graph, v, currPos, n, count, cost, order):
    if (count == n and graph[currPos][src]):
        answer.append(cost + graph[currPos][src])
        solutions.append(" ".join([str(element) for element in order]))
        return

    for i in temp:
        if (v[i] == False and graph[currPos][i]):
            v[i] = True
            order.append(i)
            TSP(graph, v, i, n, count + 1,
                cost + graph[currPos][i], order)
            order.remove(i)
            v[i] = False


if __name__ == "__main__":

    with open("task2/places.json", "r") as f:
        places = json.loads(f.read())

    n = len(places)

    roads = [[INF for _ in range(n)] for _ in range(n)]

    with open("task2/roads.txt") as f:
        for road in f.readlines():
            src, dst, dist = road.strip().split()
            s, d, l = o(src), o(dst), int(dist)
            roads[s][s] = roads[d][d] = 0
            roads[s][d] = roads[d][s] = l

    src = find_place(places, 'Parking')
    dst = find_place(places, 'University')

    if dst == -1:
        print('Invalid place name')

    else:
        length, parent = dijkstra(roads, n, src)
        paths = find_paths(parent, dst, src)
        print('Shortest path lenght: ', length[dst])
        for path in paths:
            print_path(places, path)

    # task2-2
    answer = []
    solutions = []
    src = find_place(places, 'Hospital')
    toTraverse = [find_place(places, 'Park'), find_place(
        places, 'Terminal'), find_place(places, 'Restaurant')]

    temp = toTraverse
    temp.append(src)

    v = [False for _ in range(n)]
    v[src] = True

    TSP(roads, v, src, len(temp), 1, 0, [])

    x = min(answer)
    print("Length of Path:", x)
    nodes = []

    for i in range(len(answer)):
        if x == answer[i]:
            temp_list = [src]
            temp_list.extend(list(map(int, solutions[i].split(" "))))
            temp_list.append(src)
            nodes.append(temp_list)

    for way in nodes:
        print_path(places, way)
