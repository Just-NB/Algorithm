dp = [[]]
tree = dict()
INF = 100000


def find_min_sales(node):
    global dp, tree
    if len(tree[node]) == 0:
        return
    extra_cost = INF
    for child in tree[node]:
        find_min_sales(child)
        if dp[child][0] < dp[child][1]:  # 만약 자식노드를 사용안했을 때가 더 적게 사용된다면
            dp[node][0] += dp[child][0]
            dp[node][1] += dp[child][0]
            # 만약 자식노드를 단 하나도 사용하지 않았다면 자식노드를 강제로 사용시킨다.
            # 이 때, 자식노드를 사용했을때와 사용하지 않았을 때의 차가 가장 적을 때의 값을 선택한다.
            extra_cost = min(extra_cost, dp[child][1] - dp[child][0])
        else:
            dp[node][1] += dp[child][1]
            dp[node][0] += dp[child][1]
            # 자식 노드를 한번이라도 사용했다면 extra_cost가 없다.
            extra_cost = 0
    dp[node][0] += extra_cost


def solution(sales, links):
    global dp, tree
    tree = {u: [] for u in range(len(sales) + 1)}
    dp = [[0, sales[i - 1]] for i in range(len(sales) + 1)]
    for u, v in links:
        tree[u].append(v)
    find_min_sales(1)
    return min(dp[1][0], dp[1][1])


print(f'{solution([14, 17, 15, 18, 19, 14, 13, 16, 28, 17], [[10, 8], [1, 9], [9, 7], [5, 4], [1, 5], [5, 10], [10, 6], [1, 3], [10, 2]])} : 44')
