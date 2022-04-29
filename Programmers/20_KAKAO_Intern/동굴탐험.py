from collections import defaultdict, deque

def solution(n, path, order):
    tree = defaultdict(list)
    order_dict = defaultdict(int)
    answer = True
    for p, c in path:
        tree[p].append(c)
        tree[c].append(p)
    for p, c in order:
        order_dict[c] = p

    return answer


print(f'{solution(9, [[0, 1], [0, 3], [0, 7], [8, 1], [3, 6], [1, 2], [4, 7], [7, 5]], [[8, 5], [6, 7], [4, 1]])} : True')
print(f'{solution(9, [[8, 1], [0, 1], [1, 2], [0, 7], [4, 7], [0, 3], [7, 5], [3, 6]], [[4, 1], [5, 2]])} : True')
print(f'{solution(9, [[0, 1], [0, 3], [0, 7], [8, 1], [3, 6], [1, 2], [4, 7], [7, 5]], [[4, 1], [8, 7], [6, 5]])} : False')