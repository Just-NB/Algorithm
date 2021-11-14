'''
Title   : 용액
Level   : G5
Problem : -1,000,000,000 ~ 1,000,000,000 사이의 수가 N개 입력된다.
          2개의 수를 합쳐 최대한 0에 가깝게 만드는 쌍을 찾는다.
Type    : 투포인터
Idea    : 1. 2개의 포인터를 이용해 작은값 + 큰값을 한다.
          2. 두 수의 합이 0보다 크면 오른쪽 포인터를 왼쪽으로 옮긴다
          3. 두 수의 합이 0보다 작으면 왼쪽 포인터를 오른쪽으로 옮긴다
          4. 두 포인터가 같은 지점에 오거나 합이 0이되면 종료한다.
'''

N = int(input())
solution = list(map(int, input().split()))
left, right = 0, len(solution)-1
answer = [left, right]
while True:
    if left == right:
        break
    mix = solution[left] + solution[right]
    if abs(mix) < abs(solution[answer[0]] + solution[answer[1]]): # 0과 가장 가까운 값을 저장한다.
        answer = [left, right]
    if mix == 0:
        break
    elif mix > 0:
        right -= 1
    else:
        left += 1
print(solution[answer[0]], solution[answer[1]])