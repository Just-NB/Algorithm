'''
Title   : N과 M(4)
Level   : S3
Problem : N개의 자연수와 M이 주어졌을 때, 아래 조건을 만족하는 길이가 M인 수열을 모두 구한다.
          1. N개의 자연수 중에서 M개를 고른 수열
          2. 같은 수를 여러 번 골라도 된다.
          3. 고른 수열은 비내림차순이여야한다.
Type    : 완전탐색, 백트래킹
Idea    : 1. dfs완전탐색한다.
          1-1. 깊이가 M이 되면 출력한다.
          2. idx를 매개변수로 받으며, idx부터 N까지 반복하며 dfs를 진행한다.
          2-1. 중복된 수가 가능하며, 현재 수보다 작은 숫자는 나오지 않는다.
'''


N, M = map(int, input().split())

def dfs(idx, depth, num):
    if depth == M:
        print(num.lstrip())
    else:
        for i in range(idx, N+1):
            dfs(i, depth+1, num+' '+str(i))
dfs(1,0,'')