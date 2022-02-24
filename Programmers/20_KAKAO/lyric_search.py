class Node:
    def __init__(self):
        self.word = None
        self.child = dict()
        self.cnt = 0


class Trie:
    def __init__(self):
        self.root = Node()

    def insert(self, word):
        cur_node = self.root

        for w in word:
            if w not in cur_node.child.keys():
                cur_node.child[w] = Node()
            cur_node.cnt += 1
            cur_node = cur_node.child[w]

        cur_node.word = word

    def match(self, query):
        # bfs 탐색이 필요할듯.
        cur_node = self.root
        ret = 1
        for q in query:
            if q == '?':
                return cur_node.cnt
            if q not in cur_node.child:
                return 0
            cur_node = cur_node.child[q]
        return ret


def solution(words, queries):
    answer = []
    trie = [Trie() for _ in range(10001)]
    reversed_trie = [Trie() for _ in range(10001)]
    for word in words:
        trie[len(word)].insert(word)
        reversed_trie[len(word)].insert(word[::-1])

    for query in queries:
        if query[0] == '?':
            answer.append(reversed_trie[len(query)].match(query[::-1]))
        else:
            answer.append(trie[len(query)].match(query))
    return answer


print(f'{solution(["frodo", "front", "frost", "frozen", "frame", "kakao"], ["fro??", "????o", "fr???", "fro???", "pro?"])} : [3, 2, 4, 1, 0]')
