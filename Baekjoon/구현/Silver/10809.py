def solution(S):
    answer = ['-1' for _ in range(26)]
    for i, s in enumerate(S):
        if answer[ord(s) - 97] == '-1':
            answer[ord(s) - 97] = str(i)
    return ' '.join(answer)

N = input()
print(solution(N))