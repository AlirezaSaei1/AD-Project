import json

with open("task1.json", "r") as f:
    data = json.loads(f.read())

dize = data['size']
target = data['target']
camera = data['camera']
cars = data['cars']


def solve():
    pass
