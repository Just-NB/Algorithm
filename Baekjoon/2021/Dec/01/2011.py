'''
Title   : 암호코드
Level   : S1
Problem : 대화를 암호화 한다.
          상 : A = 1/ B = 2 ... Z = 26으로 하자.
          선 : "BEAN"을 암호화하면 25114가 나오는데, 다시 글자로 바꾸는 방법이 여러가지다.
          상 : "BEAAD", "YAAD", "YAN", "YKD", "BEKD", "BEAN" 6가지 나온다.
          선 : 500자리 글자를 암호화하면 해석이 너무많다.
          해석이 몇 가지 나올 수 있는지 구하는 프로그램을 만든다.
Type    : DP
Idea    : 1. 21510를 예시로 생각한다.
          2. 2 : b 한개 만들 수 있다.
          3. 21 : 2개의 숫자를 합쳤을 때, 26(z)보다 작으므로 2개의 숫자를 합쳤을때도 문자를 만들 수 있다.
                  2,1/21 2개의 문자를 만들 수 있다.
          4. 215 : (21)로 만든 문자 + 1개
                   15이 26보다 작으므로, 2+(15) 이 가능하다.
                   2,1,5/21,5/2,15 3개의 문자가 가능하다.
          5. 2151 : (215)로 만든 문자 + 1개
                    51는 26보다 크므로 21+(51)로 문자를 만들 수 없다.
                    2,1,5,1/ 21,5,1/2,15,1 3개의 문자가 가능하다.
          6. 21510 : (2151)로 만든 문자 + 1개?
                     10은 26보다 작아서 문자로 추가할 수 있지만, 0은 독립적으로 존재할 수 없다.
                     따라서 이전단계에서 얻은 문자열은 현재 문자와 함께있어야만 존재가능하므로 0개가 되어야 한다.
                     (2151)로 만든 문자 : 0개, 215로 만든 문자 + 1개 가 되어야 한다.
          7. 이를 통해 dp[i] = dp[i-1] or dp[i] = dp[i-2]+dp[i-1] 을 추론할 수 있다.
          8. 숫자가 10,20이 될 경우, 그 이전단계에서의 만든 갯수를 0개로 바꿔야 한다.
'''

crp = input()
dp = [1] * (len(crp)+1) # idx : idx갯수만큼 숫자를 사용할 때, 만들 수 있는 암호문자 갯수
prev = '3'
for i, c in enumerate(crp):
    tmp = prev + c
    if int(tmp) < 27: # 2자리 조합이 알파벳 범위안에 들어온다면.
        if tmp == '10' or tmp == '20':
            dp[i] = 0
        dp[i+1] = dp[i-1] + dp[i]
    else:
        dp[i+1] = dp[i]

    #  0이 입력됬을경우
    if c == '0':
        # 암호가 잘못되었을 경우
        if prev == '0':  # CASE 1. 00
            dp[-1] = 0
            break
        if int(prev) >= 3:  # CASE 2. 두 숫자의 조합이 30이상될 경우
            dp[-1] = 0
            break
    prev = c
print(dp[-1]%1000000)