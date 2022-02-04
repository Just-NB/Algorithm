from itertools import permutations


def solution(k, dungeons):
    answer = 0
    d_length = len(dungeons)

    per = permutations(range(d_length))
    for p in per:
        p_ans = 0
        p_fat = k
        for i in p:
            if p_fat >= dungeons[i][0]:  # 최소 피로도.
                p_fat -= dungeons[i][1]  # 소모 피로도
                p_ans += 1
        answer = max(p_ans, answer)

    return answer



print(solution(80, [[80, 20], [50, 40], [30, 10]]))