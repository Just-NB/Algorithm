# 가지고 있는 수 N을 연산을 거치면서, 홀수를 최대한 많이 보고자 한다.
# 1. 각 자리 숫자중 홀수의 갯수
# 2. 한 자리 이면 더이상 안하고 종료
# 3. 두 자리 이상이면 2개로 나눠서 합을 구하여 새로운 수로 생각
# 4. 세 자리 이상이면 임의의 위치에서 끊어서 3개의 수로 분할, 3개를 더한 값을 새로운 수로 생각
import math

min_val, max_val = math.inf, 0

def count_odd(num: int) -> int:
    ret = 0
    while num > 0:
        tmp = num % 10
        if tmp % 2 != 0:
            ret += 1
        num = num // 10
    return ret

def devide_num(num: int) -> list:
    if num < 100:
        return [num // 10 + num % 10]
    num = str(num)
    nums = []
    for i in range(1, len(num) - 1): # i, j, k는 나눌때 길이
        for j in range(1, len(num) - 1):
            for k in range(1, len(num) - 1):
                if i + j + k > len(num): continue
                if i + j + k < len(num): continue
                new_num = int(num[:i]) + int(num[i:i + j]) + int(num[i + j:i + j + k])
                nums.append(new_num)
    return nums

def calculate(num: int, cnt: int) -> None:
    global min_val, max_val
    cnt += count_odd(num)
    if num < 10: # 2. 한자리 수이면 종료한다.
        min_val, max_val = min(min_val, cnt), max(max_val, cnt)
        return

    new_nums = devide_num(num)
    for n in new_nums:
        calculate(n, cnt)

N = int(input())
calculate(N, 0)

print(min_val, max_val)