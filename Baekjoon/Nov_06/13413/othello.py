'''
Level   : S4
Problem : 1. 임의의 말 2개를 골라 서로 위치를 바꾼다.
          2. 말 1개를 들어 뒤집어 놓아 색상을 변경한다.
          이 2작업을 통해 목표상태에 도달할 수 있는 최소 횟수 구하기
          1 <= 말의 개수 <= 100,000
Idea    : 1. 바꿔야 하는 말을 색깔별로 구분하여 위치를 저장한다.
          2. W,B 둘 다 바꿔야 할 게 남아있다면 둘의 위치를 swap한다.(1규칙 이용)
          3. 둘 중 하나라도 바꿀 게 없다면, 남은 변경해야 하는 말을 뒤집는다(2규칙 이용)
'''

T = int(input())
for tc in range(T):
    N = int(input())
    answer = 0
    init_state = input()
    dest_state = input()
    b_wrong = 0
    w_wrong = 0
    # Idea 1
    for i,d in zip(init_state, dest_state) :
        if i != d :
            if i == 'B' :
                b_wrong += 1
            else :
                w_wrong += 1
    # Idea 2
    # 변경 횟수만 알면 되므로 진짜 swap 하지 않고 갯수의 차이로 계산
    swap = min(b_wrong, w_wrong)
    # Idea 3
    flip = (b_wrong-swap + w_wrong-swap)
    answer = swap + flip
    print(answer)

    '''
3
5
WBBWW
WBWBW
7
BBBBBBB
BWBWBWB
4
WWBB
BBWB'''