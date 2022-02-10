def solution(n, left, right):
    answer = [0 for _ in range(right - left + 1)]
    for i in range(left, right + 1):
        r = i // n
        c = i % n
        answer[i - left] = max(r, c) + 1
    return answer


print(solution(3, 2, 5), " : [3, 2, 2, 3]")
print(solution(4, 7, 14), " : [4, 3, 3, 3, 4, 4, 4, 4]")