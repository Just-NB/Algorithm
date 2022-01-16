'''
Title   : N과 M(7)
Level   : S3
Problem : N개의 자연수와 M이 주어졌을 때, 아래 조건을 만족하는 길이가 M인 수열을 모두 구한다.
          1. N개의 자연수 중에서 M개를 고른 수열
          2. 같은 수를 여러 번 골라도 된다.

Type    : 완전탐색, 백트래킹
Idea    : 1. dfs완전탐색한다.
          1-1. 깊이가 M이 되면 출력한다.
          2. N개의 수를 오름차순으로 미리 정렬한다.
'''
N, M = map(int, input().split())
nums = list(map(int, input().split()))
nums.sort()
ans = ['' for _ in range(M)]
def dfs(depth):
    if depth == M:
        print(' '.join(ans))
        return
    for i in range(N):
        ans[depth] = str(nums[i])
        dfs(depth+1)
        ans[depth] = ''
dfs(0)