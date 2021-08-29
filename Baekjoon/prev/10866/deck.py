import sys

input = sys.stdin.readline


class queue:
    def __init__(self):
        self.val = list()
        self.s = 0

    def push_front(self, x): # 정수 X를 덱의 앞에 넣는다.
        self.val.insert(0,x)
        self.s += 1
    def push_back(self,x): # 정수 X를 덱의 뒤에 넣는다.
        self.val.append(x)
        self.s += 1

    def pop_front(self): #덱의 가장 앞에 수를 빼고 출력한다. 없으면 -1
        if self.s > 0 :
            self.s -= 1
            return self.val.pop(0)
        else :
            return -1

    def pop_back(self): # 덱의 가장 뒤의 수를 빼고 출력, 없으면 -1
        if self.s > 0:
            self.s -= 1
            return self.val.pop(self.s)
        else :
            return -1

    def size(self): # 정수 개수 출력
        return self.s

    def empty(self): #비어 있으면 1 아니면 0
        return 1 if self.s == 0 else 0

    def front(self): # 덱의 가장 앞의 정수 출력, 없으면 -1
        return -1 if self.s == 0 else self.val[0]

    def back(self): # 덱의 가장 뒤 정수 출력, 없으면 -1
        return -1 if self.s == 0 else self.val[-1]

q = queue()
tc = int(input())
for t in range(tc):
    query = input().split()

    if query[0] == "push_back":
        q.push_back(int(query[1]))
    elif query[0] == "push_front":
        q.push_front(int(query[1]))
    elif query[0] == "front":
        print(q.front())
    elif query[0] == "back":
        print(q.back())
    elif query[0] == "size":
        print(q.size())
    elif query[0] == "empty":
        print(q.empty())
    elif query[0] == "pop_back":
        print(q.pop_back())
    elif query[0] == "pop_front" :
        print(q.pop_front())
