'''
Title   : 감소하는 수
Level   : G5
Problem : 음이 아닌 정수 X의 자릿수가 가장 큰 자릿수부터 작은 자릿수까지 감소한다면, 그 수를 감소하는 수라고 한다
          ex) 321, 951은 감소하는수/ 322, 958은 아니다.
          N번째 감소하는 수를 출력한다
          0은 0번쨰, 1은 1번째
Type    : 완전탐색, dfs
Idea    : 1. 감소하는 수의 최댓값은 9876543210이다. 즉 최대 자리수는 10자리수이다.
          2. 각 자릿수 별, 시작숫자가 정해졌을 때, 그 숫자로 만들 수 있는 감소하는 수를 모두 만든다.
          3. 입력받은 N번째 수가 나온다면 출력하고 종료한다.
'''



N = int(input())
cnt = 9


def dfs(l, idx, num):
    global cnt
    if len(num) == l:
        cnt += 1
        if cnt == N:
            print(num)
    else:
        for i in range(idx):
            if cnt == N:
                return
            dfs(l, i, num+str(i))


if N < 10:
    print(N)
else:
    for i in range(2, 11): # 1 ~ 9 자릿수
        for j in range(1, 10): # 0 ~ 9 시작
            dfs(i, j, str(j))

    if cnt != N:
        print(-1)
