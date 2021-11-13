## 문제

https://www.acmicpc.net/problem/15886

- N크기의 배열중 임의의 위치에 있는 사람에게 선물을 주고자 한다.
- N크기의 배열에 E,W가 입력되어있다.
  - E는 오른쪽으로 이동, W는 왼쪽으로 이동을 의미한다.
  - 어떤 위치에서 시작하더라도 선물을 1개 이상 받을 수 있도록 하기 위해 최소 몇개의 칸 위에 선물을 놓으면 되는가

## 풀이 아이디어

### 핵심 아이디어

- union-find 개념을 응용한 순환 여부 체크
  - 순환의 갯수만큼 선물을 놓으면 된다.

### 풀이 아이디어

- 부모를 저장할 `node` 리스트 사용
- 반복문을 통해 입력된 지도`path`를 순회
  - `path[idx]`의 값이 `E`일 경우 `node[idx] = idx+1`
    - `E`의 경우 오른쪽으로 이동이다. 
    - 현재 위치의 부모는 `idx+1`을 의미한다.
  - `path[idx]`의 값이 `W`일 경우 `node[idx] = idx-1`
    - `W`의 경우 왼쪽으로 이동이다.
    - 현재 위치의 부모는 `idx-1`을 의미한다.
  - `node[idx-1] == idx` 혹은 `node[idx+1] == idx` 의 경우 `idx`를 기점으로 순환한다는것을 의미한다.
    - 이 경우는 부모를 변경하지 않는다.
- 노드의 부모가 본인이라면 `answer` 를 1 증가시킨다.
  - `node[idx] == idx` 인 경우 `idx`를 기점으로 순환이 된다.
