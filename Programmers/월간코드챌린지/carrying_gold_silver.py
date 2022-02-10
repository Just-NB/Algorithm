import sys
MAX = sys.maxsize

def check(a, b, golds, silvers, weights, times, T):
    total, gold, silver = 0, 0, 0
    for g, s, w, t in zip(golds, silvers, weights, times):
        move_cnt = T // (t * 2)
        if T % (t * 2) >= t:
            move_cnt += 1
        max_weight = w * move_cnt
        gold += min(max_weight, g)
        silver += min(max_weight, s)
        total += min(max_weight, g + s)

    if a <= gold and b <= silver and (a + b) <= total:
        return True
    return False

def solution(a, b, golds, silvers, weights, times):
    ''' 이분탐색으로 찾기 '''
    answer = MAX
    left, right = 0, MAX
    while left <= right:
        TIME = (left + right) // 2  # 주어진 시간 TIME
        if check(a, b, golds, silvers, weights, times, TIME):  # 가능하면 좀 더 짧은 시간안에 가능한지 확인한다.
            answer = min(answer, TIME)
            right = TIME - 1
        else:  # 불가능하면 시간을 더 준다.
            left = TIME + 1

    return answer




print(solution(10, 10, [100], [100], [7], [10]), " : 50")
print(solution(90, 500, [70, 70, 0], [0, 0, 500], [100, 100, 2], [4, 8, 1]), " : 499")