import sys

input = sys.stdin.readline
'''
비어있는 공집합 S가 주어졌을 때, 아래 연산을 수행하는 프로그램을 작성하시오.

add x: S에 x를 추가한다. (1 ≤ x ≤ 20) S에 x가 이미 있는 경우에는 연산을 무시한다.
remove x: S에서 x를 제거한다. (1 ≤ x ≤ 20) S에 x가 없는 경우에는 연산을 무시한다.
check x: S에 x가 있으면 1을, 없으면 0을 출력한다. (1 ≤ x ≤ 20)
toggle x: S에 x가 있으면 x를 제거하고, 없으면 x를 추가한다. (1 ≤ x ≤ 20)
all: S를 {1, 2, ..., 20} 으로 바꾼다.
empty: S를 공집합으로 바꾼다. 

'''

T = int(input())
s = [0]*21
for tc in range(T):
    query = input().split()
    if query[0] == 'all' :
        s = [1] * 21
        continue
    if query[0] == 'empty' :
        s = [0] * 21
        continue

    idx = int(query[1])
    if query[0] == 'add':
        s[idx] = 1
    elif query[0] == 'remove':
        s[idx] = 0
    elif query[0] == 'check':
        print(s[idx])
    elif query[0] == 'toggle':
        s[idx] = 1 - s[idx]


