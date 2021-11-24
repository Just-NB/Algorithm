'''
Title   : 물건팔기
Level   : S3
Problem : 상품을 최대 이익에 팔려고 한다.
          사려고 하는 사람이 N명이 있다. 각각 자기가 지불할 최대 한도가 있다.
          각 사람이 사용할 수 있는 최대 금액과 배송비가 주어졌을때, 이익을 최대로 하여 출력한다.
Type    : 완전탐색, 정렬
Idea    : 1. 최대 금액을 기준으로 오름차순으로 정렬한다.
          2. i는 판매할 가격, j는 이익 비교를 하는 2중 반복문을 한다
          2-1) 오름차순 정렬을 했으므로, j를 i인덱스부터 시작한다면 판매할 수 있으며, 이익만 고려하면 된다.
          3. 현재 가격 - 배송비 > 0 이면 판매 했을때 이익으로 추가한다.
'''

N = int(input())
prices = []
for _ in range(N):
    prices.append(list(map(int, input().split())))
prices.sort()

max_profit = 0
ans = 0
for i in range(N):
    profit = 0

    for j in range(i, N):
        if prices[i][0] - prices[j][1] > 0:
            profit += prices[i][0] - prices[j][1]
    if max_profit < profit:
        max_profit = profit
        ans = prices[i][0]
print(ans)
