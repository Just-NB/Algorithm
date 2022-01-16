'''
Title   : 단축키 지정
Level   : S3
Problem : N개의 옵션이 있다. 각 옵션은 한 개 또는 여러 개의 단어로 설명하고 있다.
          각 옵션에 단축키를 의미하는 대표 알파벳을 지정하기로 한다.
          1. 왼쪽에서부터 오른쪽 순서로 단어의 첫 글자가 이미 단축키로 지정되었는지 살펴본다. 안되어있다면 그 알파벳이 단축키
          2. 모든 단어의 첫 글자가 이미 지정되어 있다면, 왼쪽에서부터 차례대로 알파벳을 보면서 단축키로 지정 안된 것이 있따면 지정한다.
          3. 어떠한 것도 불가능하다면 그냥 놔두고 대소문자를 구분치 않는다.
          4. 차례대로 적용한다.
Type    : 구현, 시뮬레이션
Idea    : 1. 3번 규칙을 적용하기 위해 먼저 입력받은 옵션들을 전부 소문자로 변경한다.
          2. dict자료구조를 이용한다.
'''

N = int(input())
options = [input() for _ in range(N)]
hotkeys = dict()
for option in options:
    name = option.lower() # 대소문자 구분이 없으므로, 소문자로 통일해둔다.
    hk_idx = 0
    flag = False # 단축키 지정 되었는지 확인/ True : 단축키 지정완료
    for n in name.split(): # 1조건, 첫 글자가 단축키에 지정되어있는지 확인한다.
        if n[0] not in hotkeys.keys():
            hotkeys[n[0]] = hk_idx
            flag = True
            break
        hk_idx += len(n)+1
    if flag is False:
        for i, n in enumerate(name): # 2조건
            if n != ' ':
                if n not in hotkeys.keys():
                    hotkeys[n] = i
                    hk_idx = i
                    flag = True
                    break

    if flag is True:
        for i, o in enumerate(option):
            if i == hk_idx:
                print(f'[{o}]',end='')
            else:
                print(f'{o}',end='')
        print()
    else:
        print(option)



