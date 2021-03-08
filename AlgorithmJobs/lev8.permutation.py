## template
N,R = map(int,input().split())
MAX = 105
result = ['' for _ in range(MAX)]
check = [False for _ in range(27)]
alpha = 'abcdefghijklmnopqrstuvwxyz'
def getResult(x) :
    if x >= R :
        print(''.join(result))
    else :
        for i in range(N) :
            if check[i] == False:
                result[x] = alpha[i]
                check[i] = True
                getResult(x+1)
                check[i] = False
getResult(0)
