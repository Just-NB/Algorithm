'''
Level   : S4
Problem : 계이름을 숫자로 표현한다.
          A음 을 시작으로 D음씩 올리면서 고음을 부르는 경우, 항의 갯수가 X일때 X단 고음이라 한다.
Idea    : 입력받은 tone을 순서대로 읽어나가며 시작음(a)이 나오면 고음체크를 시작한다.
'''

n, a, d = map(int, input().split())
tone = list(map(int, input().split()))
answer = 0
cur_tone = a
for t in tone:
    if t == cur_tone:
        cur_tone = t+d
        answer += 1

print(answer)
