import sys
input = sys.stdin.readline
N = int(input())
path = list(input().strip())
node = [i for i in range(N)]
for i,p in enumerate(path):
    if p == 'E':
        if node[i+1] != i :
            node[i] = i+1
    else :
        if node[i-1] != i:
            node[i] = i-1
answer = 0
for i,v in enumerate(node):
    if i == v : answer += 1
print(answer)