def solution_brute(sequence, length) :
    ret,tmp = 0,[]

    for i in range(length) :
        tmp = [sequence[i]]
        for j in range(i, length) :
            if sequence[i] < sequence[j] :
                tmp.append(sequence[j])
        print(tmp)
        ret = max(ret, len(tmp))
    return ret

C = int(input())

for _ in range(C) :
    length = int(input())
    sequence = list(map(int, input().split()))
    print(solution_brute(sequence, length))
'''
input
3
4
1 1 1 1 
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