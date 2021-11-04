class Node :
    def __init__(self):
        self.word = None
        self.children = {}

class Trie :
    def __init__(self):
        self.head = Node()

    def insert(self, string):
        curNode = self.head

        for s in string:
            if s not in curNode.children :
                curNode.children[s] = Node()
            curNode = curNode.children[s]

        curNode.word = string

    def find(self, string):
        curNode = self.head

        for s in string:
            if s in curNode.children:
                curNode = curNode.children[s]
            else :
                return False

        if curNode.word == string :
            return True
        else :
            return False


trie = Trie()

words = ["fire", "firefox", "frodo","frog"]

for word in words:
    trie.insert(word)

print(trie.find("fire"))
print(trie.find("firefo"))
print(trie.find("firefox"))
