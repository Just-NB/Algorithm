
def solution_brute(sequence) :
    if len(sequence) == 0 :
        return 0
    ret = 0
    for i in range(len(sequence)) :
        tmp = sequence[i]
        subseq = []
        for j in range(i, len(sequence)) :
            if tmp < sequence[j] :
                subseq.append(sequence[j])
        ret = max(ret, 1 + solution_brute(subseq))

    return ret

def solution_DP1(seq,cache,start) :
    if cache[start] != -1 :
        return cache[start]
    cache[start] = 1
    for i in range(start+1, len(seq)) :
        if seq[start] < seq[i] :
            cache[start] = max(cache[start], solution_DP1(seq,cache, i) + 1)

    return cache[start]


C = int(input())

for _ in range(C) :
    length = int(input())
    sequence = list(map(int, input().split()))
    cache = [ -1 for i in range(100)]
    #print(solution_brute(sequence))
    answer = 0
    for i in range(length) :
        answer = max(answer, solution_DP1(sequence, cache, i))
    print(answer)
'''
input
3
4
1 2 3 4 
8
5 4 3 2 1 6 7 8 
12
5 6 7 1 1 1 4 5 1 2 4 5
7
9 1 3 7 5 6 20
output
4
4
5
'''