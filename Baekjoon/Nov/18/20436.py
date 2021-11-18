'''
Title   : ZOAC 3
Level   : S4
Problem : 쿼티 배열의 키보드가 있다.
          한글 자판 기준 왼손은 자음/ 오른손은 모음만 입력한다.
          손가락의 이동은 맨해탄 거리만큼의 시간이 걸린다.
Type    : 구현
Idea    : 1. 한글 자판 자음/ 모음에 해당하는 알파벳들을 분리하여 알파벳을 키/좌표를 밸류인 dict로 저장한다.
          2. 입력받은 알파벳이 자음/모음인지 확인하고, 움직일 손을 선택한다.
          3. 현재 손의 위치와 입력받은 알파벳의 위치를 맨해탄 거리를 이용해 시간을 구한다.
          4. 2~3을 반복한다.
'''

left_hand = {'q': (0, 0), 'w': (0, 1), 'e': (0, 2), 'r': (0, 3), 't': (0, 4),
             'a': (1, 0), 's': (1, 1), 'd': (1, 2), 'f': (1, 3), 'g': (1, 4),
             'z': (2, 0), 'x': (2, 1), 'c': (2, 2), 'v': (2, 3)
             }
right_hand = {'y': (0, 5), 'u': (0, 6), 'i': (0, 7), 'o': (0, 8), 'p': (0, 9),
              'h': (1, 5), 'j': (1, 6), 'k': (1, 7), 'l': (1, 8),
              'b': (2, 4), 'n': (2, 5), 'm': (2, 6)
              }

left, right = input().split()
left_pos, right_pos = left_hand[left], right_hand[right]
sentence = input()
answer = 0
for s in sentence:
    if s in left_hand:
        answer += abs(left_pos[0] - left_hand[s][0]) + abs(left_pos[1] - left_hand[s][1]) + 1
        left_pos = left_hand[s] #  왼쪽 손 이동.
    else:
        answer += abs(right_pos[0] - right_hand[s][0]) + abs(right_pos[1] - right_hand[s][1]) + 1
        right_pos = right_hand[s]  # 왼쪽 손 이동.
print(answer)
