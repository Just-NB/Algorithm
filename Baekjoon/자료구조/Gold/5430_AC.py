import sys
from  collections import deque
input = sys.stdin.readline

# R : 뒤집기/ D : 버리기
T = int(input())
for t in range(T):
    query = input().strip()
    N = int(input())
    nums = deque(input().strip()[1:-1].split(','))
    if nums[0] == '':
        nums.popleft()

    r_flag, e_flag = False, False

    for q in query:
        if q == 'R':
            r_flag = ~r_flag
        else:
            if len(nums) == 0:
                e_flag = True
                break
            if r_flag:
                nums.pop()
            else:
                nums.popleft()
    if e_flag:
        print('error')
    else:
        if len(nums) == 0:
            print('[]')
        else:
            print('[', end='')
            for i in range(len(nums) - 1):
                if r_flag:
                    i = len(nums) - i - 1
                print(nums[i], end=',')

            if r_flag:
                print(nums[0]+']')
            else:
                print(nums[-1]+']')