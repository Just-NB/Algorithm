'''
Title   : 텀 프로젝트
Level   : G3
Problem : 프로젝트 팀원 수에는 제한이 없다. 프로젝트 팀을 구성하기 위해 함께 하고 싶은 학생을 선택해야 한다.
          선택의 결과를 보고 어느 프로젝트 팀에도 속하지 않는 학생들의 수를 계산하는 프로그램을 작성한다.
Type    : dfs
Idea    : 1. dfs순회하며 재방문이 일어나면 순환이 생긴것.
          2. 재방문이 생겼을 경우, 순환되는 노드의 수를 counting한다.
          3. 방문하지 않은 노드(학생)들을 모두 dfs순회하며 순환(팀)되는 노드(학생)의 수를 누적한다.
          4. 전체 학생의 수 - 팀이 된 학생의 수 = 정답.
'''
import sys

sys.setrecursionlimit(10**6)
def dfs(cur):
    ret = 0
    nxt = students[cur] # 내가 원하는 짝
    if visit[cur] is False:
        if cycle[cur] < 2: # 확인하지 않았으면, 내가 원하는 짝 확인.
            cycle[cur] += 1
            ret += dfs(nxt)
        else: # 확인한 친구에게 돌아오면 순환 확인.
            start = cur # 순환의 시작지점.
            while nxt != cur:
                ret += 1
                cycle[nxt] = 2
                nxt = students[nxt]
            students[nxt] = 2
            ret += 1
        visit[cur] = True
    return ret


if __name__ == '__main__':
    T = int(input())
    for tc in range(T):
        N = int(input())
        answer = 0
        students = [0] + list(map(int, input().split()))
        length = len(students)
        cycle = [0 for _ in range(length)] # 2 : 순환, 1 : 1번 방문.
        visit = [False for _ in range(length)] # 팀 완성 여부.
        for i in range(1, length):
            if visit[i] is False:
                answer += dfs(i)
        print(length - answer - 1)

