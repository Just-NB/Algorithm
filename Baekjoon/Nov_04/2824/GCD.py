def gcd(m,n):
    if m < n :
        m,n = n,m
    while n != 0:
       t = m%n
       (m,n) = (n,t)
    return abs(m)


N = int(input())
n_nums = list(map(int, input().split()))
M = int(input())
m_nums = list(map(int, input().split()))
n_mul = 1
m_mul = 1
for n in n_nums:
    n_mul *= n
for m in m_nums:
    m_mul *= m

ret = str(gcd(n_mul, m_mul))
if len(ret) >= 9:
    print(ret[len(ret)-9:])
else :
    print(ret)