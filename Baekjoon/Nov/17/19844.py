'''
Title   : 단어 개수 세기
Level   : S4
Problem : 프랑스어의 단어 구분
          먼저 띄어쓰기와 -(하이픈)을 기준으로 “단어”를 쪼갠다.
          각각의 “단어”에서, 위처럼 줄어들었을 가능성이 있는 경우
          (즉, c', j', n', m', t', s', l', d', qu'로 시작하고 어포스트로피 뒤 글자가 모음인 경우)
          이 단어들을 한 번 더 분리해 준다.
Type    : 구현, 문자열
Idea    : 1. 띄어쓰기와 - 을 기준으로 단어를 쪼갠 후 갯수를 저장한다.
          2. 단어마다 1개의 글자씩 읽으며 start를 누적한다.
          3. 만약 ' 를 만난다면 start가 약어 목록에 있는지 확인하고, 다음 단어가 모음인지 확인한다.
          4. 기준에 맞는다면 단어를 1개 추가한다.
'''
sentence = input()
words = sentence.replace('-',' ').split(' ')

abb = ('c', 'j', 'n', 'm', 't', 's', 'l', 'd', 'qu')
vowel = ('a','e','i','o','u','h')

answer = len(words)
for word in words:
    start = ''
    for i,w in enumerate(word):
        if w == '\'' and start in abb and word[i+1] in vowel:
            answer += 1
            break
        start += w
print(answer)
