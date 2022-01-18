'''
Title   : 외판원 순회
Level   : G1
Problem : 1 ~ N번 번호가 매겨져 있는 도시들이 있고, 도시들 사이에는 길이 있다.
          외판원은 한 도시에 출발하여 N개의 도시를 모두 거쳐 다시 원래의 도시로 돌아오는 순회 여행 경로를 계획한다.
          N과 비용행렬이 주어졌을 떄, 가장 적은 비용을 들이는 외판원의 순회 여행 경로를 구하는 프로그램을 작성한다.
Type    : 다이나믹 프로그래밍
'''

MAX = 1000000*16 + 1
N = int(input())
graph = [[] for _ in range(N)]
DP = [[MAX for _ in range(1 << N)] for _ in range(N)]  # col : 부분배열, row : 마을
all_visit = (1 << N) - 1
for n in range(N):
    graph[n] = list(map(int, input().split()))

# DP[i][v] : i를 시작으로 부분배열 v를 지나 1번으로 가는 값.
def find_tsp(start, visit):
    if visit == all_visit:  # 모든 마을을 방문했다면 종료.
        if graph[start][0] != 0:  # 해당 마을에서 0번 마을로 돌아갈 수 있다면 값 반환.
            return graph[start][0]
        else:
            return MAX
    if DP[start][visit] != MAX:
        return DP[start][visit]

    for i in range(N):  # i 마을을 거쳐 갈겁니다.
        if (visit & (1 << i)) != 0:  # 만약 방문한 적이 있으면 방문 안할 겁니다.
            continue
        if graph[start][i] == 0:  # 만약 길이 없다면 방문 안할겁니다.
            continue
        DP[start][visit] = min(DP[start][visit], graph[start][i] + find_tsp(i, visit | (1 << i)))

    return DP[start][visit]

print(find_tsp(0, 1))
