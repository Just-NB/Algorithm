'''
Title   : 음악프로그램
Level   : G2
Problem : 출연 순서를 정하기 위해서는 많은 조건을 따져야 한다.
          보조 PD들이 가져 온 출연 순서를 보고 전체 가수 출연 순서를 정하는 프로그램을 작성한다.
Type    : 위상 정렬
Idea    : 1. 각 PD들의 순서를 graph로 표현한다. (1,4,3) 의 경우 1->4/ 4->3 을 나타내는 그래프
          2. 보조 PD들이 정한 순서에 나타난 횟수(진입차수)를 list에 적는다.
          3. 값이 0인 가수들을 큐에 넣는다.
          4. 큐에서 pop()이 된 가수의 list값을 -1 한다.
          5. list값이 0이 되면 해당 가수에 연결되어 있는 다른 가수들을 queue에 넣고, 값을 출력한다.
'''
from collections import deque

def topol_sort(graph, in_degree):
    dq = deque()
    ret = []
    # 시작지점.
    for i, d in enumerate(in_degree):
        if d == 0:
            dq.append(i)

    while len(dq) != 0:
        cur = dq.popleft()
        in_degree[cur] -= 1
        # 진입 차수가 0이 되면, 해당 노드에서 갈 수 있는 노드를 모두 큐에 넣는다.
        if in_degree[cur] <= 0:
            ret.append(cur)
            for g in graph[cur]:
                dq.append(g)

    return ret


if __name__ == '__main__':
    N, M = map(int, input().split())
    in_degree = [0 for _ in range(N)]
    graph = [[] for _ in range(N)]
    for m in range(M):
        tmp = list(map(int, input().split()))[1:]
        for i in range(len(tmp)-1):
            graph[tmp[i]-1].append(tmp[i+1]-1)
            in_degree[tmp[i+1]-1] += 1
    answer = topol_sort(graph, in_degree)
    if len(answer) != N:
        print(0)
    else:
        for a in answer:
            print(a+1)