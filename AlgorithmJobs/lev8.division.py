N = int(input())
result = [N+1]
cnt = 0
def brute(num, curVal) :
  global cnt
  if curVal == N :
    print('+'.join(map(str,result[1:])))
    cnt+=1
  else :
    for i in range(num, 0, -1) :
      if i == N : continue
      if result[-1] < i : continue
      result.append(i)
      curVal += i
      brute(num-i, curVal)
      result.pop()
      curVal -= i

brute(N,0)
print(cnt)