global cache


def solution(board, N, x, y):
  global cache
  if x == N and y == N:
    return "YES"
  if x > N or y > N:
    return "NO"

  if cache[y][x] == '1':
    down = solution(board, N, x, y+board[y][x])
    right = solution(board, N, x+board[y][x], y)
    if down == "YES" or right == "YES":
      cache[y][x] = "YES"
    else:
      cache[y][x] = "NO"
  elif cache[y][x] == 'NO':
    return "NO"
  elif cache[y][x] == 'YES':
    return "YES"

  if down == "YES" or right == "YES":
    return "YES"
  else:
    return "NO"


C = int(input())
for _ in range(C):
  global cache
  N = int(input())
  BOARD = []
  cache = [['1' for _ in range(N)] for _ in range(N)]
  for _n in range(N):
    BOARD.append(list(map(int, input().split())))
  print(solution(BOARD, N-1, 0, 0))
