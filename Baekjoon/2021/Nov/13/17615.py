'''
Title   : 볼 모으기
Level   : S1
Problem : R/B 색의 공이 일직선상에 섞여서 놓여있다
          볼을 옮겨 같은 색 볼 끼리 인접하게 놓이도록 한다.
          1. 바로 옆에 다른 색의 공이 있으면 그 공을 모두 뛰어 넘길 수 있다.
          2. 한가지 색의 공만 옮길 수 있다.
Type    : 구현
Idea    : R/B 옮길 때의 최소 횟수를 모두 확인한다.
          1. R만 움직여 왼쪽으로 R을 모으기
          2. R만 움직여 오른쪽으로 R을 모으기
          3. B만 움직여 왼쪽으로 B를 모으기
          4. B만 움직여 오른쪽으로 B를 모으기
          가장 왼쪽/오른쪽에 있는 공을 먼저 옮긴다면 이동할 공은 1번씩 이동하는것으로 문제를 해결할 수 있다.
          따라서 전체 공의 갯수 - 왼쪽/오른쪽에 뭉쳐져 있는 공의 갯수로 이동횟수를 판단할 수 있다.
'''

N = int(input())
balls = list(input())
r_left, r_right, b_left, b_right = 0, 0, 0, 0
red_cnt, blue_cnt = 0, 0
for b in balls:
    if b == 'R':
        red_cnt += 1
    else:
        blue_cnt += 1
#  Idea 1.
for b in balls:
    if b == 'R' : # 왼쪽에 뭉쳐져 있는 R의 갯수 찾기
        r_left += 1
    else:
        break
#  Idea 2.
for b in balls:
    if b == 'B':
        b_left += 1
    else:
        break
#  Idea 3.
for b in balls[::-1]:
    if b == 'R':
        r_right += 1
    else:
        break
#  Idea 4.
for b in balls[::-1]:
    if b == 'B':
        b_right += 1
    else:
        break
answer = min(red_cnt-r_left, red_cnt-r_right, blue_cnt-b_left, blue_cnt-b_right)
print(answer)