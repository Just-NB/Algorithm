'''
Title   : 이중 우선순위 큐
Level   : G5
Problem : 데이터를 삭제할 때, 연산 명령에 따라 우선순위가 가장 높은 데이터 혹은 낮은 데이터 중 하나를 삭제한다.
          삭제 연산은 우선순위가 높은/낮은 데이터를 삭제하는 것이다.
          저장된 값 자체를 우선순위라 가정할 때, 주어진 연산을 마치고 최종적으로 남은 데이터 중 최대 최솟값을 출력한다.
Type    : 자료구조, 구현
Idea    : 1. 우선순위 큐를 사용하기 위해 heapq 메소드를 사용한다.
          2. 최대/최소 힙 2개를 만들어서 구현한다
          3. 최대(최소) 힙의 원소를 삭제할 떄, 최소(최대) 힙의 원소도 함께 삭제하긴 어려우므로 dict자료구조를 사용하여
             삭제할 원소가 반대쪽 힙에도 남아있는지 확인하며, 남아있지 않을 경우 원소 삭제를 반복한다.
          4. dict자료구조에 남아있는 원소들 중, 값이 1이상인 keys중 최대,최소를 찾는다.
'''

import heapq
import math

T = int(input())
for tc in range(T):
    n = int(input())
    min_Q, max_Q = [], []
    length = 0
    dict_Q = dict()

    for _ in range(n):
        query, num = input().split()
        if query == 'I':
            num = int(num)
            length+=1
            heapq.heappush(min_Q, num)
            heapq.heappush(max_Q, (-num, num))
            if num not in dict_Q.keys():
                dict_Q[num] = 1
            else:
                dict_Q[num] += 1
        else:
            if length > 0:
                if num == '-1':
                    while True:
                        if length == 0: break
                        n = heapq.heappop(min_Q)
                        if dict_Q[n] != 0:
                            length -= 1
                            dict_Q[n] -= 1
                            break
                else:
                    while True:
                        if length == 0 : break
                        n = heapq.heappop(max_Q)[1]
                        if dict_Q[n] != 0:
                            length -= 1
                            dict_Q[n] -= 1
                            break
    if length == 0:
        print("EMPTY")
    else:
        answer = [-math.inf, math.inf] # max , min
        for k, v in dict_Q.items():
            if v != 0:
                if k > answer[0] :
                    answer[0] = k
                if k < answer[1]:
                    answer[1] = k
        print(answer[0], answer[1])