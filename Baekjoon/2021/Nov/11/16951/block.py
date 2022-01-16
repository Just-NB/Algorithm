'''
Level   : S4
Problem : 높이 1인 블록으로 탑 N개를 만든다. 일렬로 배열한다.
          왼쪽부터 i번째 탑의 높이는 Ai다.
          인접한 두 탑의 높이 차이를 K로 만드려고 한다.
          1분동안 탑 하나를 고르고, 높이를 변경한다.
          필요한 시간?
Idea    : 탑의 수가 1000개 이하 이므로, N^2의 알고리즘도 무리없이 돌아갈 수 있다.
          i번째 값을 기준으로 타워의 크기를 맞춘다고 가정하고 풀이한다.
          1. i 번째 값을 기준으로 한다.
          2. 처음부터 끝까지 반복을 하며(인덱스 j사용), pivot - k * (i - j) 의 값과 tower[j]의 값이 다르다면 변경해야 한다.
          3. 만약 pivot - k *(i - j) 값이 0보다 작으면 i 인덱스를 기준으로 하는 정렬은 불가능하다.
          4. pivot - k * (i - j)는 i번째를 기준으로 뒀을 때, j번째에 와야할 값이다.
'''

n, k = map(int, input().split())
tower = list(map(int, input().split()))
answer = 1001
for i in range(n) :
    pivot = tower[i]
    change = 0
    for j in range(n):
        if pivot - (k * (i - j)) <= 0:
            change = 1001
            break
        if tower[j] != pivot - (k * (i - j)):
            change += 1
    answer = min(answer, change)
print(answer)