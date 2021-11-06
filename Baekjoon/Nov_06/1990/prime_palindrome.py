'''
Level   : G5
Problem : 소수 이면서 팰린드롬인 숫자를 찾는다.
          5 <= a < b <= 100000000
Idea    : 1. 범위내의 가능한 팰린드롬 숫자를 모두 찾는다.
          2. 팰린드롬 수가 소수인지 판별한다.
          3. 팰린드롬의 길이가 짝수일 경우 모두 11의 배수이므로 범위가 10000000 으로 한정된다.
'''

a, b = map(int, input().split())
length = 0
palindrome = []
#Idea 1
for i in range(a, b+1):
    #Idea 3
    if i > 100000000 : break
    pal = str(i)
    if pal == pal[::-1]:
        palindrome.append(i)
#Idea 2
for p in palindrome:
    is_prime = True
    for i in range(2, int(p**(1/2))+1):
        if p % i == 0 :
            is_prime = False
            break
    if is_prime is True:
        print(p)
print(-1)