'''
Title   : 프린터 큐
Level   : S3
Problem : 다음 조건에 따라 인쇄를 하게 된다.
          1. 현재 Queue의 가장 앞에 있는 문서의 '중요도'를 확인한다.
          2. 나머지 문서들 중 현재 문서보다 중요도가 높은 문서가 하나라도 있다면, 문서를 인쇄하지 않고
             Queue의 가장 뒤에 재배치 한다.
          3. 그렇지 않다면 바로 인쇄를 한다.
Type    : 큐, 구현, 시뮬레이션
Idea    : 1. 입력받은 우선순위를 순서와 함께 deque에 넣는다.
          2. 우선순위를 내림차순으로 정렬한다.
          3. deque의 front가 우선순위의 값과 일치하면 pop한다.
          4. front가 우선순위의 값보다 작으면 맨 뒤로 옮긴다.
'''
from collections import deque

T = int(input())
for tc in range(T):
    N, O = map(int, input().split())
    priorities = list(map(int, input().split()))
    dq = deque()
    for i, p in enumerate(priorities):
        dq.append([p, i]) # 문서의 순서를 저장한다.
    priorities.sort(reverse=True) # 우선순위를 내림차순으로 저장한다.
    idx = 0 # 우선순위를 따라갈 인덱스

    while True:
        c_p, c_i = dq.popleft() # cur_priority, cur_index
        if c_p < priorities[idx] : # 우선순위가 작으면 맨 뒤로 옮긴다.
            dq.append([c_p, c_i])
        else: # 우선순위가 같으면 원하는 문서가 출력됬는지 확인한다.
            if c_i == O:
                print(idx+1)
                break
            else:
                idx += 1
