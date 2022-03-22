import sys

input = sys.stdin.readline

class Node:
    def __init__(self):
        self.val = ''
        self.child = {}

class Trie:
    def __init__(self):
        self.head = Node()

    def insert(self, word):
        node = self.head
        for w in word:
            if w not in node.child:
                node.child[w] = Node()
            node = node.child[w]
        node.val = word

    def find(self, word):
        node = self.head
        for w in word:
            if w not in node.child:
                return False
            node = node.child[w]
        if node.val == '':
            return False
        return True


N, M = map(int, input().split())
trie = Trie()
for n in range(N):
    word = input().strip()
    trie.insert(word)
answer = 0
for m in range(M):
    word = input().strip()
    if trie.find(word):
        answer += 1
print(answer)
