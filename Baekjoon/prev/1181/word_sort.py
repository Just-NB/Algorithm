'''
알파벳 소문자로 이루어진 N개의 단어가 들어오면 아래와 같은 조건에 따라 정렬하는 프로그램을 작성하시오.

길이가 짧은 것부터
길이가 같으면 사전 순으로
'''
N = int(input())
word = set()
for n in range(N) :
    tmp = input()
    word.add((tmp,len(tmp)))

word = list(word)
word.sort(key = lambda x : [x[1],x[0]])

for w in word:
    print(w[0])