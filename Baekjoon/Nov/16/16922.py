'''
Title   : 로마 숫자 만들기
Level   : S3
Problem : I, V, X, L을 사용하여 로마 숫자를 만든다.
          각 문자는 1,5,10,50을 의미한다.
          여러개의 문자를 이용하여 수를 나타낼 수 있고, 각 문자가 의미하는 수를 합한 값이다.
          순서를 신경쓰지 않고 N개를 사용하여 만들 수 있는 서로 다른 수의 개수를 구한다.
Type    : 구현
Idea    : 1. 만들 수 있는 최대 숫자는 L을 20개 연결한 1000
          2. 사용할 문자의 최대갯수는 20개, 사용할 문자는 4종류이므로 완전탐색을 하더라도 20^4번 반복이라 가능하다.
          3. 3중 for문을 이용하여 각각의 문자의 사용갯수를 정한다.
          4. make_num배열의 idx에 해당하는 숫자가 만들어지면 값을 1로 한다.
          5. 최종적으로 make_num의 값을 모두 더한값이 만들 수 있는 갯수.
'''
make_num = [0 for _ in range(1001)]
n = int(input())
for i in range(n+1) : #  I를 i개 사용한다.
    for v in range(n-i+1): # V를 v개 사용한다.
        for x in range(n-i-v+1): # X를 x개 사용한다.
            l = n-i-v-x
            make = i + 5*v + 10*x + 50*l
            make_num[make] = 1
print(sum(make_num))

