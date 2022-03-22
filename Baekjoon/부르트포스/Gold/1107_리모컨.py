import sys

N = int(input())
M = int(input())
btn = {i for i in range(10)}
if M > 0:
    btn -= set(map(int, input().split()))

min_press = sys.maxsize
def brute(cur_num: int, press: int):
    global min_press

    for i in btn:
        new_num = cur_num * 10 + i
        min_press = min(min_press, press + 1 + abs(new_num - N))
        if len(str(new_num)) < 6 and new_num != 0:
            brute(new_num, press + 1) # 무언갈 눌렀을 때.

brute(0, 0)
print(min(min_press, abs(100 - N)))
