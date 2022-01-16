'''
Title   : N과 M(6)
Level   : S3
Problem : N개의 자연수와 M이 주어졌을 때, 아래 조건을 만족하는 길이가 M인 수열을 모두 구한다.
          1. N개의 자연수 중에서 M개를 고른 수열
          2. 고른 수열은 오름차순
Type    : 완전탐색, 백트래킹
Idea    : 1. dfs완전탐색한다.
          1-1. 깊이가 M이 되면 출력한다.
          2. N개의 수를 오름차순으로 미리 정렬한다.
'''

N, M = map(int, input().split())
nums = list(map(int, input().split()))
nums.sort()
ans = ['' for _ in range(M)]
def dfs(idx, depth):
    if depth == M:
        print(' '.join(ans))
        return
    for i in range(idx+1, N): # 중복된 숫자 제외하기 위해 idx + 1부터 시작
        ans[depth] = str(nums[i])
        dfs(i, depth+1)
        ans[depth] = ''
dfs(-1,0) #idx + 1부터 반복하기 때문에 시작은 -1