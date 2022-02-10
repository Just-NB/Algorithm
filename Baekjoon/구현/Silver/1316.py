import sys

input = sys.stdin.readline


def check(s):
    alpha = set()
    prev = s[0]
    alpha.add(prev)
    for c in s[1:]:
        if c != prev:
            if c in alpha:
                return 0  # 그룹 단어가 아니다.
            alpha.add(c)  # 처음 만난 단어.
        prev = c
    return 1

N = int(input())
answer = 0
for n in range(N):
    answer += check(input())
print(answer)
