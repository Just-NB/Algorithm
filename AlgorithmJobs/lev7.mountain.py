## template
N = int(input())
size = pow(2,N)
tree = [0 for _ in range(size)]
cnt,val,valCnt = 0,N,1
for i in range(1,size) :
    tree[i] = val
    cnt+=1
    #1,2,4,8,16,
    if cnt == valCnt :
        cnt = 0
        valCnt *= 2
        val -= 1

def inoder(idx) :
    if (2*idx+1) >= size :
        return str(tree[idx])
    return inoder(2*idx) + str(tree[idx]) + inoder(2*idx+1)

print(inoder(1))