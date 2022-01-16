## 문제

https://www.acmicpc.net/problem/2635

- 첫 번째 수는 양의 정수 N이 주어진다.
- 두 번째 수는 임의의 양의 정수 하나를 선택한다.
- 그 이 후의 수는 앞의 수 - 앞앞 수를 빼서 만든다.
- 음의 정수가 만들어지면 더 이상 수를 만들지 않는다.
  - N = 100 일 때, 두 번째 수로 60을 선택할 경우
  - 100 60 40 20 20 0 20 이 완성

## 풀이 알고리즘

### 핵심 알고리즘

- 완전탐색
  - 두 번째 수의 경우를 1~N까지의 모든 수를 확인한다.

### 풀이 알고리즘

- 완전 탐색
  - `N`이 주어지면 `1~N+1` 까지의 반복문을 진행한다.
  - 두 번째 수 마다 `while` 반복을 진행하며 `answer`후보를 만든다.
  - `idx`의 값은 `answer[idx] = answer[-1] - answer[-2]`
  - `answer`의 길이가 가장 긴 것을 선택한다.
