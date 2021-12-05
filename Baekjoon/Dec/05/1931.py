'''
Title   : 회의실 배정
Level   : S2
Problem : 한 개의 회의실이 있다. 이를 사용하고자 하는 N개의 회의에 대해 사용표를 만드려고 한다.
          각 회의에 대해 시작/종료 시간이 주어져있고, 회의가 겹치지 않으면서 최대한 많이 사용할 수 있는 회의 개수를 찾는다.
Type    : 정렬, 탐욕적
Idea    : 1. 종료 시간을 1번 기준으로 오름차순 정렬한다
          2. 현재 사용중인 회의의 종료시간이, 요구하는 회의의 시작시간보다 작으면 회의실이 비어있고 사용할 수 있다.
'''

import sys

input = sys.stdin.readline
N = int(input())
times = [[] for _ in range(N)]

for n in range(N):
    times[n] = list(map(int, input().split()))

times.sort(key = lambda x:(x[1], x[0]))
answer = 0

cur_end = 0
for s, e in times:
    if s >= cur_end: # 현재 시간이 사용중인 회의실 마감시간보다 크거나 같으면 사용가능
        cur_end = e
        answer += 1
print(answer)
