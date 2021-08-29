x = int(input())
answer = 0

def dfs(n,d) :
    if n == 1 :
        return d
    a,b,c = x,x,x

    if n % 3 == 0:
        a = dfs(n//3, d+1)
    if n % 2 == 0:
        b = dfs(n//2, d+1)
    c = dfs(n-1, d+1)
    return min(a,b,c)

print(dfs(x,0))