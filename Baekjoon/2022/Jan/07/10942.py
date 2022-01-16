'''
Title   : 팰린드롬?
Level   : G3
Problem : N개의 자연수를 칠판에 적고 질문을 M번 한다.
          질문은 두 정수 S와 E(1<=S<=E<=N)로 나타내며, S~E까지의 수가 팰린드롬을 이루는지 물어본다.
          자연수와 질문이 주어졌을 때, 팰린드롬인지 아닌지를 구하는 프로그램을 작성한다.
Type    : 다이나믹 프로그래밍
Idea    : 1. 양 끝 값이 같을 때, 내부가 팰린드롬이라면 해당 값은 팰린드롬이다.
          2. DP[s][e] : (n[s] == n[e] and DP[s+1][e-1])
          3. 확인할 문자열의 길이를 기준으로 bottom-up
          4. 길이가 l, s = 1 일때, e = s + l
'''
import sys

input = sys.stdin.readline
N = int(input())
nums = list(map(int, input().split()))
palindrome = [[0 for _ in range(N)] for _ in range(N)]
# preprocess , 길이가 0, 1일때의 팰린드롬 경우 찾기
for length in range(2):
    for i in range(N - length):
        if nums[i] == nums[i + length]:
            palindrome[i][i + length] = 1

for length in range(2, N):
    for s in range(N - length):
        e = s + length
        if nums[s] == nums[e] and palindrome[s + 1][e - 1] == 1:
            palindrome[s][e] = 1

M = int(input())
for m in range(M):
    s, e = map(int, input().split())
    print(palindrome[s-1][e-1])

