'''
Title   : 전깃줄
Level   : S1
Problem : A, B 사이에 연결된 줄이 교차하지 않도록 몇 개의 줄을 없애고자 한다.
          없애야 하는 최소갯수를 출력한다.
Type    : DP
Idea    : 1. A,B를 2차원 배열로 묶는다.
          2. A,B 둘 중 하나를 기준으로 오름차순 정렬한다.
          3. A를 기준으로 정렬했을때, 줄이 교차한다는 것은 B가 그 이전의 B보다 값이 작다.
          3-1. A_i ~ B_i가 A_i-1 ~ B_i-1과 교차한다는 뜻은, B_i가 B_i-1보다 작다는 뜻이다.
          4. 따라서 A를 기준으로 정렬했을때, N - B의 증가하는 부분수열의 가장 큰 길이 이다.
'''
N = int(input())
lines = []
for _ in range(N):
    lines.append(list(map(int, input().split())))
lines.sort()
lis = [[] for _ in range(N)] # 증가하는 부분수열
lis[0] = [lines[0][1]]
for i in range(1, N):
    for j in range(0, i):
        if lis[j][-1] < lines[i][1]: # 증가한다면,
            if len(lis[i]) < len(lis[j]) + 1: # 기존의 LIS보다 새로 추가한 LIS가 더 크다면
                lis[i] = lis[j] + [lines[i][1]]
    if len(lis[i]) == 0: #
        lis[i].append(lines[i][1])

max_len = 0
for l in lis:
    max_len = max(len(l), max_len)
ans = N - max_len
print(ans)