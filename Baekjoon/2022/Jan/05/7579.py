'''
Title   : 앱
Level   : G3
Problem : 화면에 보이는 '실행 중'앱은 하나뿐이지만 보이지 않은 상태로 많은 앱이 '활성화' 되어있다.
          '활성화' 되어있다는 것은 메인 메모리에 직전의 상태가 기록되어 있는 것을 말한다.
          메모리 부족 상태를 막기 위해, 활성화 앱중 몇개를 선택하여 메모리로부터 삭제해야 한다.
          이를 '비 활성화' 라고 한다.
          N개의 앱이 활성화 되어 있을때, i앱은 각 Mi 메모리를 사용하고, 비활성화->활성화 시 추가적으로 들어가는 비용읓 Ci라 한다.
          새로운 앱 B를 실행하고자 하여, 추가로 M 바이트 메모리가 필요할 때, 활성화 되어있는 앱중 몇개를 비활성화 시켜 M바이트 메모리를 추가로 확보해야 한다.
          비활성화 했을 경우의 비용 Ci의 합을 최소화 하여 M바이트를 확보한다.
Type    : 다이나믹 프로그래밍, 냅색(배낭 문제)
Idea    : 1. 2차원 배열을 이용한 DP memoization
          2. col : 사용된 cost, MAX : cost들의 합
          3. row : 비활성화 시킬 app
          4. dp[i][j] = max(memory + dp[i-1][j-cost], dp[i][j])

'''
import math

if __name__ == '__main__':
    N, M = map(int, input().split())
    memories = list(map(int, input().split()))
    costs = list(map(int, input().split()))
    apps = list(zip(memories, costs))
    MAX = sum(costs) + 1
    dp = [[0 for _ in range(MAX)] for _ in range(N + 1)]
    ret = math.inf
    # 0행 : 아무것도 안넣었을 때
    for r in range(1, N + 1):
        memory = memories[r - 1]
        cost = costs[r - 1]
        for c in range(MAX):
            if c < cost:
                dp[r][c] = dp[r-1][c]
            else:
                dp[r][c] = max(dp[r - 1][c - cost] + memory, dp[r-1][c])
            if dp[r][c] >= M and ret > c:
                ret = c
    print(ret)
