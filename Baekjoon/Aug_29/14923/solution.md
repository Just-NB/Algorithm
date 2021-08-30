## 문제

https://www.acmicpc.net/problem/14923

- N x M 크기의 미로, 현재위치, 탈출위치가 주어질 때 미로를 탈출하는 최단거리를 구한다.
- 미로를 탈출할 때, 1칸의 벽을 부술 수 있다.

## 풀이 아이디어

### 핵심 아이디어

- bfs를 이용한 완전탐색
- 재방문을 방지하기 위한 방문여부 체크
  - 해당 위치에 방문하기위해 벽을 뚫고 왔을때와 벽을 뚫지 않고 왔을때 2가지 경우를 체크 해야한다.

### 풀이 아이디어

- bfs를 이용한 완전탐색
  - `collections`의 `deque`를 이용하여 bfs탐색을 한다.
  - `deque`에는 `[현재위치(x,y), 비용(cost), 스킬사용여부(skill)]` 를 저장한다.
  - `visit` 리스트를 만들어 현재위치의 방문여부를 체크
  - `deque`에 값이 없을 때 까지 반복한다.
  - `visit[x][y][skill]` : `skill` 사용 여부에 따른, 현재 위치에 방문을 했는지 체크. `deque`의 값에 스킬 사용여부를 넣어두었다.
