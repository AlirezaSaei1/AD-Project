import json

with open("task1/data.json", "r") as f:
    data = json.loads(f.read())

size = data['size']
target = data['target']
camera = data['camera']
cars = data['cars']


def solve():
    pass
