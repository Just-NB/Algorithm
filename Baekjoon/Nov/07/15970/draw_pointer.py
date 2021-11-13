'''
Level   : S4
Problem : 임의의 색이 있는 점 p,q에 대해 같은 색이면서 가장 거리가 짧은 점을 연결한다.
          거리(b-a)의 총 합을 출력한다.
          색은 편의상 1 <= 색 <= N 으로 표현된다.
Idea    : 1. 같은 색의 점 끼리 모은 후, 오름차순으로 정렬한다.
          2. 가장 가까운 양 옆의 점들의 거리를 비교하여 짧은 거리를 선택한다.
'''

N = int(input())
# 색을 배열의 인덱스로 접근
colors = [[] for _ in range(N+1)]
for _ in range(N):
    p, c = map(int, input().split())
    colors[c].append(p)

# 정렬
for _ in range(N+1):
    colors[_].sort()
answer = 0
for color in colors:
    for i in range(len(color)):
        # 처음이면 다음 점이랑 연결
        if i == 0:
            answer += (color[i+1] - color[i])
        # 마지막이면 이전 점이랑 연결
        elif i == (len(color)-1):
            answer += (color[i] - color[i-1])
        # 그 이외는 양 옆 중 가장 짧은 점이랑 연결
        else :
            answer += min((color[i] - color[i-1]), (color[i+1] - color[i]))
print(answer)