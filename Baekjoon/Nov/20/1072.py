'''
Title   : 게임
Level   : S3
Problem : 게임횟수 = X, 이긴 게임 = Y, 승률 = Z일 때, 몇번을 더 이겨야 Z가 변하는지 구한다.
Type    : 수학
Idea    : 1. Z = (100 * Y) / X
          2. Z + 1 = 100 * (Y + K) / (X+K) : K횟수 더 했을때 Z가 변한다
          3. K = (X(Z+1) - 100Y) / (99-Z)
          4. 승률이 99%일 경우 100%는 될 수 없다.(100%는 승 == 횟수 이기떄문에)

          #Python은 안되는데 같은 코드로 C++은 가능.
'''
import math
X, Y = map(int, input().split())
Z = math.floor((100 * Y) / X)
if Z == 99 :
    print(-1)
else:
    K = math.ceil((X *(Z + 1) - 100 * Y) / (99 - Z))
    print(K)
