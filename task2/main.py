import json
INF = float('inf')

with open("task2/places.json", "r") as f:
    places = json.loads(f.read())

n = len(places)

roads = [[INF for _ in range(n)] for _ in range(n)]


def o(c):
    return ord(c) - ord('A')


with open("task2/roads.txt") as f:
    for road in f.readlines():
        src, dst, len = road.strip().split()
        s, d, l = o(src), o(dst), int(len)
        roads[s][s] = roads[d][d] = 0
        roads[s][d] = roads[d][s] = l

# for road in roads:
#     print(road)


def solve():
    pass
