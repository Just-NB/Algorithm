import sys

input = sys.stdin.readline

N = int(input())
ant_den = dict() # { 'food' : child_dict }


def insert_food(ant_den: dict, food: list, idx: int) -> None:
    if idx == len(food):
        return
    if food[idx] not in ant_den.keys():
        ant_den[food[idx]] = dict()
    insert_food(ant_den[food[idx]], food, idx + 1)


def print_structure(ant_den: dict, depth: int) -> None:
    floor = '--' * depth
    ant_den = sort(ant_den)
    for food, nxt_floor in ant_den.items():
        print(floor + food)
        print_structure(nxt_floor, depth + 1)


def sort(ant_den: dict) -> dict:
    sorted_den = sorted(ant_den.items())
    return dict(sorted_den)


for _ in range(N):
    query = input().split()[1:]
    insert_food(ant_den, query, 0)


print_structure(ant_den, 0)
