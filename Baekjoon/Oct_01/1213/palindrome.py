'''
주어진 입력을 팰린드롬으로 만든다.
정답이 여러 개일 경우 사전순으로 앞서는 것을출력한다.
만들지 못한다면 "I'm Sorry Hansoo"를 출력한다.

AAAAA BBB CCC:
'''
from collections import Counter
name = Counter(input())
name = sorted(name.items())
flag = True
answer = ''
center = ''
for char, cnt in name:
    if cnt == 1 :
        center += char
    elif cnt % 2 == 0:
        answer += (char * (cnt//2))
    elif cnt % 2 == 1:
        answer += (char * (cnt // 2))
        center += char
    if len(center) > 1 :
        flag = False
        break
if flag :

    answer += (center+answer[::-1])
    print(answer)
else:
    print("I\'m Sorry Hansoo")