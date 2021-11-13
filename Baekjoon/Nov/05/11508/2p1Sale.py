'''
Level   : S4
Problem : 3개를 묶어서 음료를 살 때 가장 싼 음료의 가격은 내지 않는다. 이때, 최소비용으로 모든 음료를 구매하는 방법찾기.
Idea    : 최대한 돈을 내지 않는 음료의 가격이 높아야 한다. -> 3묶음의 음료중의 가장 싼 음료의 가격이 높게 한다. -> 가격을 내림차순 정렬한 후, 3개씩 묶어 계산한다.
'''

N = int(input())
costs = [0] * N
for i in range(N) :
    costs[i] = int(input())

costs.sort(reverse=True)
answer = 0
for idx, cost in enumerate(costs):
    if idx%3 != 2:
        answer+=cost
print(answer)