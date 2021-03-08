## template
N,M = map(int,input().split())

n,m = [],[]
for i in range(1, N+1) :
  if N%i == 0:
    n.append(i)
for j in range(1, M+1) :
  if M%j == 0:
    m.append(j)
GCD = -1
n.reverse()
m.reverse()
for i in n:
  for j in m:
    if i == j:
      GCD = i
      break
  if GCD != -1:
    break
LCM = N*M//GCD

print(GCD)
print(LCM)