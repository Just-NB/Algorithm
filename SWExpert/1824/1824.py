N = int(input())
road = input()
ans = 0
# def dfs(depth) :
# 	global ans
# 	if depth == N-1 :
# 		ans += 1
# 		return

# 	#1칸씩 점프, 0은 애초에 걍 통과해야뎌
# 	if depth+1 < N and road[depth+1] == '1':
# 		dfs(depth+1)

# 	#2칸씩 점프, 0은 안됨
# 	if depth+2 < N and road[depth+2] == '1' :
# 		dfs(depth+2)

# 	return
newRoad = N
if road[0] == '1' and road[1] == '0' and road[2] == '1':
    newRoad -= 2
if road[N - 3] == '1' and road[N - 2] == '0' and road[N - 1] == '1':
    newRoad -= 2
for i in range(1, len(road) - 2):
    if road[i - 1] == '1' and road[i] == '0' and road[i + 1] == '1':
        newRoad -= 3

dp = [1, 1]
for i in range(2, newRoad):
    dp.append(dp[i - 2] + dp[i - 1])
print(dp)
print(dp[-1])