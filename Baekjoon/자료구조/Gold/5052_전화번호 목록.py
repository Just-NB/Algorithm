import sys

input = sys.stdin.readline


class Node:
    def __init__(self):
        self.val = ''
        self.child = {}


class Trie:
    def __init__(self):
        self.head = Node()

    def insert(self, num):
        node = self.head
        for n in num:
            if n not in node.child:
                node.child[n] = Node()
            node = node.child[n]
        node.val = num

    def insert_and_find(self, num) -> bool:
        node = self.head
        for n in num:
            if n not in node.child:
                node.child[n] = Node()
            if node.val != '':
                return False
            node = node.child[n]
        if node.val != '':
            return False
        node.val = num
        return True

    def find_prefix(self, num) -> bool:
        node = self.head
        for n in num:
            node = node.child[n]

        if len(node.child):
            return True
        else:
            return False


def solve_one(N: int, trie: Trie, nums: list):
    flag = True
    for num in nums:
        trie.insert(num)
    for num in nums:
        if trie.find_prefix(num):
            flag = False
    if flag:
        print("YES")
    else:
        print("NO")


def solve_two(N: int, trie: Trie, nums: list):
    flag = True
    nums.sort()
    for n in nums:
        if not trie.insert_and_find(n):
            flag = False
    if flag:
        print("YES")
    else:
        print("NO")


T = int(input())
for t in range(T):
    N = int(input())
    trie = Trie()
    nums = [input().strip() for _ in range(N)]
    solve_two(N, trie, nums)
