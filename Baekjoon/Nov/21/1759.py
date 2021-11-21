'''
Title   : 암호 만들기
Level   : G5
Problem : 서로 다른 L개의 알파벳 소문자들로 구성되며 최소 한 개의 모음과 두 개의 자음으로 구성되어있다.
          암호는 오름차순으로 정렬되어있다.
          문자의 종류 C개가 주어졌을때, 가능성 있는 암호를 모두 구한다.
Type    : 완전탐색, 백트래킹
Idea    : 1. L,C의 크기가 작으므로 완전탐색한다.
          2. dfs를 통해 탐색하며, 조건에 안맞을경우 돌아간다.

'''
L, C = map(int, input().split())
char = input().split()
char.sort()
def condition(pw):
    c, v = 0, 0
    prev = pw[0]
    for p in pw:
        if p in 'aeiou':
            v += 1
        if p in 'bcdfghjklmnpqrstvwxyz':
            c += 1
        if prev > p:
            return False
        prev = p
    if v >= 1 and c >= 2:
        return True
    else:
        return False

def dfs(pw, idx) :
    if len(pw) == L:
        if condition(pw) is True:
            print(pw)
    else:
        for i in range(idx+1, C):
            dfs(pw+char[i], i)

dfs('', -1)