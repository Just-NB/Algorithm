'''
Title   : 에리 카드
Level   : S3
Problem : N개의 공유/팀 숫자 카드를 갖고 시작한다.
          상대 팀은 K장을 견제하며, 견제된 카드는 낼 수 없다.
          공유 카드 * 팀 카드의 곱이 우리 팀의 점수이다.
          같은 방식으로 상대팀도 진행하며, 상대 팀 보다 점수가 높으면 이긴다.
          우리팀이 얻을 수 있는 최대 점수를 출력한다.
Type    : 완전탐색
Idea    : 1. 숫자 카드들을 오름차순으로 정렬한다.
          2. 각 카드들이 곱했을때 최대가 되는 숫자들을 저장하고 정렬한다.
          3. 곱했을때 최대가 되는 수는, 현재 숫자가 음수일 경우, 공유카드의 가장 작은값과 곱한다.
          4. 현재 숫자가 양수일 경우, 공유카드의 가장 큰값과 곱한다.
          5. 최대가 되는 숫자배열중 k개를 뺀 후, 맨 뒤의 값을 출력한다.
'''

n, k = map(int, input().split())
s_cards = sorted(list(map(int, input().split()))) # 공유 카드
t_cards = sorted(list(map(int, input().split()))) # 팀 카드

max_point = []
for card in t_cards:
    if card < 0 :
        max_point.append(card * s_cards[0])
    else:
        max_point.append(card * s_cards[-1])
max_point.sort()
print(max_point[n-1-k])
