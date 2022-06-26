import json
from collections import deque
INF = float('inf')


def o(c):
    return ord(c) - ord('A')


def city(o):
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
    print(' -> '.join([places[city(place)] for place in path]))


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


def print_road(places, src, dst):
    print(places[city(src)], ' -> ', places[city(dst)])


def TSP(W, n, curr, visited, path, cost, rem, answer):
    if rem == 0 and 0 < W[curr][src] < INF:
        answer.append((cost + W[curr][src], path + [src]))
        return

    for next in range(n):
        if not visited[next] and 0 < W[curr][next] < INF:
            visited[next] = True
            path.append(next)
            TSP(W, n, next, visited, path, cost + W[curr][next], rem-1, answer)
            visited[next] = False
            path.remove(next)


# def TSP2(W, n, curr, visited, path, cost):
#     MIN = INF

#     for i in range(n):
#         if not visited[i] and W[curr][i] + W[i][curr] < MIN:
#             MIN = W[i][curr] + W[curr][i]
#             next = i

#     if MIN != INF:
#         visited[next] = True
#         path.append(next)
#         cost += W[curr][next]
#         return TSP2(W, n, next, visited, path, cost)
#     else:
#         path.append(src)
#         cost += W[curr][src]
#         return cost


def min_spanning_tree(W, n):
    length = [W[0][i] for i in range(n)]
    vselected = [False] * n
    nearest = [0] * n

    for _ in range(n):
        MIN = INF

        for i in range(n):
            if not vselected[i] and length[i] < MIN:
                MIN = length[i]
                vnear = i

        vselected[vnear] = True

        for i in range(n):
            if not vselected[i] and W[i][vnear] < length[i]:
                length[i] = W[i][vnear]
                nearest[i] = vnear

    return length, nearest


if __name__ == '__main__':

    with open('task2/places.json', 'r') as f:
        places = json.loads(f.read())

    n = len(places)

    roads = [[INF for _ in range(n)] for _ in range(n)]

    with open('task2/roads.txt') as f:
        for road in f.readlines():
            src, dst, dist = road.strip().split()
            s, d, l = o(src), o(dst), int(dist)
            roads[s][s] = roads[d][d] = 0
            roads[s][d] = roads[d][s] = l
    while True:
        print('Main Menu\n1. Task 2-1\n2. Task 2-2\n3. Task 3\n4. Exit')
        inp = int(input())
        if inp == 1:
            src = find_place(places, 'Parking')
            dst = find_place(places, input('Enter destination: '))
            # src = find_place(places, 'Parking')
            # dst = find_place(places, 'University')

            if dst == -1:
                print('Invalid place name')

            else:
                # task 2-1
                length, parent = dijkstra(roads, n, src)
                paths = find_paths(parent, dst, src)
                print('Shortest path lenght: ', length[dst])
                for path in paths:
                    print_path(places, path)
        elif inp == 2:
            # task 2-2
            #src = find_place(places, 'Hospital')
            #pathway = ['Park', 'Terminal', 'Restaurant']
            src = find_place(places, input('Source:'))
            print('Enter visit places in one line:')
            pathway = [find_place(places, place) for place in input().split()]
            path = [src]

            if -1 in path + pathway:
                print('Invalid place name')
                continue

            visited = [True] * n
            for place in pathway:
                visited[place] = False

            answer = []
            TSP(roads, n, src, visited, path, 0, len(pathway), answer)

            if len(answer) == 0:
                print('No path exist')
                continue

            cost, path = min(answer)

            print('Min Length: ', cost)
            for c, p in answer:
                if c == cost:
                    print_path(places, p)

            # cost = TSP2(roads, n, src, visited, path, 0)
            # print('Min Length: ', cost)
            # print_path(places, path)
        elif inp == 3:
            # task 3
            length, nearest = min_spanning_tree(roads, n)
            print('Min length: ', sum(length))
            for i in range(1, n):
                print_road(places, nearest[i], i)
        else:
            break
