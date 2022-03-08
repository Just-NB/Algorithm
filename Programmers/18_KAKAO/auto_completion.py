class Node:
    def __init__(self):
        self.word = None
        self.word_cnt = 0
        self.child = dict()


class Trie:
    def __init__(self):
        self.node = Node()

    def insert(self, word):
        node = self.node
        for w in word:
            if w not in node.child.keys():
                node.child[w] = Node()
            node.word_cnt += 1
            node = node.child[w]

        node.word = word
        node.word_cnt += 1

    def find_min_len(self, word):
        node = self.node
        for i, w in enumerate(word):
            node = node.child[w]
            if node.word_cnt < 2:
                return i + 1
        return len(word)


def solution(words):
    answer = 0
    trie = Trie()
    for word in words:
        trie.insert(word)
    for word in words:
        answer += trie.find_min_len(word)
    return answer


print(f'{solution(["go", "gone", "guild"])}: 7')
print(f'{solution(["abc", "def", "ghi", "jklm"])} : 4')
print(f'{solution(["word", "war", "warrior", "world"])} : 15')