N,M = 0,0

def solution(M,pair) :
    if False not in student : 
        return 1
    ret,i = 0,0    
    while i < M:
        if student[pair[i]] == 0 and student[pair[i+1]] == 0:
            tmp = pair[:i] + pair[i+2:]
            student[pair[i]], student[pair[i+1]] = True,True
            ret += solution(M-2,tmp)
            student[pair[i]], student[pair[i+1]] = False,False
            del[pair[i]]
            del[pair[i]]
            M -= 2
            i -= 2
        i += 2
    return ret

if __name__ == '__main__' :
    C = int(input())
    for i in range(C) :
        N,M = [int(x) for x in input().split()]
        student = [False]*(N)
        pair = list(map(int, input().split()))
        print(solution(M*2,pair))