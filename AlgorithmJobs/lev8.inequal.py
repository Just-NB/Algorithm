def findMin(idx) :
  global isFind
  if idx == N+1 :
    printResult(number)
    isFind = True
  else :
    for num in range(10) :
      if isFind : return 0
      #첫번째는 일단 다 넣어본다.
      if idx == 0:
        number[idx] = num
        isUse[num] = True
      #그다음부터는 부등호를 비교한다.
      else :
        if isUse[num] : continue
        if compare(num,idx) :
          number[idx] = num
          isUse[num] = True
        else :
          return 0
      findMin(idx+1)
      isUse[num] = False
  return 0

def findMax(idx) :
  global isFind
  if idx == N+1 :
    printResult(number)
    isFind = True
  else :
    for num in range(9,-1,-1) :
      if isFind : return 0
      #첫번째는 일단 다 넣어본다.
      if idx == 0:
        number[idx] = num
        isUse[num] = True
      #그다음부터는 부등호를 비교한다.
      else :
        if isUse[num] : continue
        if compare(num,idx) :
          number[idx] = num
          isUse[num] = True
        else :
          return 0
      findMax(idx+1)
      isUse[num] = False
  return 0

#부등호 비교
def compare(num,idx) :
  if sign[idx-1] == '<' :
    if number[idx-1] < num : return True
    else : return False
  else :
    if number[idx-1] > num : return True
    else : return False

def printResult(num) :
  for n in num[:N+1]:
    print(f'{n}',end = '')
  print()

N = int(input())
sign = input().split()
#숫자를 저장할 리스트
number = [0 for i in range(10)]
#숫자가 사용되었는지 여부를 체크할 리스트
isUse = [False for i in range(10)]
isFind = False
findMax(0)

#숫자를 저장할 리스트
number = [0 for i in range(10)]
#숫자가 사용되었는지 여부를 체크할 리스트
isUse = [False for i in range(10)]
isFind = False
findMin(0)