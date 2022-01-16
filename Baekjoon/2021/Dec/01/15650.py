'''
Title   : N과 M(2)
Level   : S3
Problem : N개의 자연수와 M이 주어졌을 때, 아래 조건을 만족하는 길이가 M인 수열을 모두 구한다.
          1. 1부터 N까지의 자연수 중 중복없이 M개를 고른 수열
          2. 고른 수열은 오름차순
Type    : 완전탐색, 백트래킹
Idea    : 1. dfs완전탐색한다.
          1-1. 깊이가 M이 되면 출력한다.
          2. 중복을 방지하기 위해 다음깊이는 idx+1부터 시작한다.
          3. dfs를 이어나가며 숫자를 추가시킨다.
'''
N, M = map(int, input().split())

def dfs(idx, depth, num):
    if depth == M:
        print(num.lstrip())
    else:
        for i in range(idx, N+1):
            dfs(i+1, depth+1, num+' '+str(i))
dfs(1,0,'')