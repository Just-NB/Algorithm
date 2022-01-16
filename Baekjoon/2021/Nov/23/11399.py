'''
Title   : ATM
Level   : S3
Problem : N명에 사람이 줄을 서있고, i번째 사람이 일을 처리하는데 Pi분 걸린다.
          줄을 서 있는 사람의 수 N과 각 사람이 돈을 인출하는데 걸리는 시간 Pi가 주어졌을때,
          각 사람이 돈을 인출하는데 필요한 시간의 합의 최솟값을 구한다.
Type    : 정렬, 그리디 알고리즘
Idea    : 1. 가장 빨리 끝나는 사람을 먼저 처리시킨다면, 필요한 시간의 합이 최소가 된다.
          2. 오름차순으로 P를 정렬한다.
          3. i번째 사람에게 필요한 시간은 i-1번째 사람이 필요한 시간 + i번쨰 사람이 인출하는 시간
          4. ans[i] = ans[i-1]+P[i]
'''

N = int(input())
P = list(map(int, input().split()))
P.sort()
answer = 0
for i in range(N):
    answer += (P[i] * (N-i))
print(answer)