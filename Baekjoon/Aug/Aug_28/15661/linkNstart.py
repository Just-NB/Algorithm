'''
축구하기 위해 모인사람 N명
팀 분배 하겠다. 인원수 안같아도 되고 한명이상.
능력치 조사.

'''
import sys
from itertools import combinations
input = sys.stdin.readline
N = int(input())
board = []
for _ in range(N):
    board.append(list(map(int, input().split())))

check = set()
member_list = [n for n in range(N)]
tmp = []
answer = 10**8
for i in range(1, (N//2)+1): # 1:N-1 ~ N//2 : N//2 때까지 분배
    team_comb = list(combinations(member_list, i)) # 팀원 분배
    for comb in team_comb:
        link_member = comb
        start_member = list(set(member_list) - set(link_member))
        link_comb = list(combinations(link_member,2)) # 팀원 2명씩의 조합
        start_comb = list(combinations(start_member,2)) # 팀원 2명씩의 조합
        link_score,start_score = 0,0
        for lc in link_comb:
            r,c = lc
            link_score += (board[r][c] + board[c][r]) # 팀원 시너지 점수를 합한다.
        for sc in start_comb:
            r,c = sc
            start_score += board[r][c] + board[c][r]
        diff = abs(link_score - start_score)
        answer = min(answer, diff)
print(answer)
#
# def calculate_score(link_member):
#         start_member = [i for i, val in enumerate(link_member) if val is False]
#         link_member = [i for i, val in enumerate(link_member) if val is True]
#         link_comb = list(combinations(link_member, 2))
#         start_comb = list(combinations(start_member, 2))
#         link_score = 0
#         start_score = 0
#         for comb in link_comb:
#             r, c = comb
#             link_score += board[r][c] + board[c][r]
#         for comb in start_comb:
#             r, c = comb
#             start_score += board[r][c] + board[c][r]
#
#         return abs(link_score - start_score)
#
#
# def dfs(link_member, num_member):
#     if num_member == N-1:
#         return calculate_score(link_member)
#     ret = 10**8
#     for i in range(N):
#         if link_member[i] is False:
#             link_member[i] = True
#             check_str = ''.join(map(str, link_member))
#             if check_str not in check :
#                 check.add(check_str)
#                 tmp.append([i+1 for i, val in enumerate(link_member) if val is True])
#                 cur_score = calculate_score(link_member)
#                 ret = min(dfs(link_member, num_member + 1), cur_score, ret)
#             link_member[i] = False
#     return ret
#
# print(dfs([False for _ in range(N)],0))
