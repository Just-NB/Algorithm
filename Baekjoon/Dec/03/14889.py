'''
Title   : 스타트와 링크
Level   : S3
Problem : 축구를 하기 위해 모인 사람이 N명(짝수)이다.
          N/2명으로 이루어진 스타트/링크 팀으로 나눈다.
          번호를 1~N으로 배정하고 능력치를 조사했다.
          S_ij는 i번 사람과 j번 사람이 같은 팀일때, 능력치이다.
          팀의 능력치는 팀원 모든 쌍의 S_ij의 합이다.
          두 팀의 능력치의 차이를 최소로 하는 프로그램을 만든다.
Type    : 조합
Idea    : 1. N//2 명씩 나누어 팀을 정한다. 이 때, 팀 구성원은 조합으로 구할 수 있다.
          2. combinations를 통해 얻은 팀원의 조합의 모든 경우의 수를 판단한다.
          3. set 자료구조를 이용하여 다른 한 팀의 구성원을 얻는다.
          4. 팀원의 시너지를 계산하기 위해, 각 팀원의 조합을 다시 2명씩 combinations한다.
'''
import math
from itertools import combinations
N = int(input())
stats = []
for _ in range(N):
    stats.append(list(map(int, input().split())))

comb = set(combinations(range(N), N//2))
answer = math.inf
for start in comb:
    link = set(range(N)) - set(start)
    pair = combinations(start, 2)
    s_stat, l_stat = 0, 0
    for a, b in pair:
        s_stat += (stats[a][b] + stats[b][a])
    pair = combinations(link, 2)
    for a, b in pair:
        l_stat += (stats[a][b]) + stats[b][a]

    answer = min(abs(l_stat - s_stat), answer)
print(answer)