'''
Title   : 후위 표기식
Level   : G3
Problem : 연산자가 피연산자 뒤에 위치하는 표기법을 후위 표기법이라 한다.
          중위 표기법으로 표현된 a+b는 후위 표기법으로는 ab+가 된다.
          중위 표기법을 후위 표기법으로 바꾸는 방법은 다음과 같다.
          1. 중위 표기식을 연산자의 우선순위에 따라 괄호로 묶어준다.
          2. 괄호 안의 연산자를 괄호의 오른쪽으로 옮겨준다.
            예를 들어 a+b*c = (a+(b*c))의 식이 된다.
          3. 안에 있는 괄호의 연산자 *를 괄호 밖으로 꺼내게 되면 (a+bc*)가 된다.
          4. 또 +를 괄호의 오른쪽으로 고치면 abc*+가 된다.
          중위 표기식이 주어졌을 때, 후위 표기식으로 고치는 프로그램을 작성한다.
Type    : 스택, 자료구조
Idea    : 1. 표기식을 한글자씩 읽어가며 피연산자일 경우 바로 출력한다.
          2. 연산자일 경우 스택에 넣는다.
          3. 스택의 top에 있는 연산자보다 현재 연산자의 우선순위가 낮거나 같으면,
             스택의 top에 있는 연산자가 현재 연산자의 우선순위보다 작아지거나 없을떄까지 밖으로 꺼내고 현재 연산자를 스택에 넣는다.
          4. 1~3을 반복한다.
'''

operation = input()
priority = {'*': 1, '/': 1, '+': 2, '-': 2, '(': 3, ')':3}
stack = []
for o in operation:
    if o in '()':
        if o == '(': # 여는 괄호일경우, 스택에 넣는다.
            stack.append('(')
        else: # 닫는 괄호일 경우, 여는 괄호가 나올때까지 스택의 값을 모두 뺀다.
            while len(stack) != 0:
                if stack[-1] == '(':
                    stack.pop()
                    break
                print(stack.pop(), end='')
    elif o in '+-*/': # 연산자의 경우
        if len(stack) == 0: # 스택에 값이 없으면 넣는다.
            stack.append(o)
        else:
            # 현재 연산자의 우선순위가 스택의 top보다 같거나 작으면
            # 같은 우선순위 연산자가 나올 때까지 모두 뺀다.
            if priority[o] >= priority[stack[-1]]:
                while len(stack) != 0:
                    if priority[o] < priority[stack[-1]]:
                        break
                    print(stack.pop(), end='')
            stack.append(o)
    else:
        print(o, end='')

while len(stack):
    print(stack.pop(), end='')
