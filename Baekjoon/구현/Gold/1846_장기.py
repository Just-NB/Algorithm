N = int(input())
if N == 3:
    print(-1)
if N % 2 == 0: # 짝수
    print(N // 2)
    for i in range(1, N // 2):
        print(i)
    for i in range(N // 2, N - 1):
        print(i + 2)
    print(N // 2 + 1)
else:
    print(N // 2 + 1)
    for i in range(1, N // 2 + 1):
        print(i)
    print(N)
    for i in range(N // 2 + 2, N):
        print(i)
# used_col = [-1 for _ in range(N)]
# answer = [0 for _ in range(N)]
#
#
# def backtracking(row: int) -> bool:
#     if row == N:
#         for i, c in enumerate(used_col):
#             answer[c] = i + 1
#         return True
#     ret = False
#     for i in range(N):
#         if ret: return ret
#         if used_col[i] != -1: continue
#         if i == row or i == N - row - 1: continue
#         used_col[i] = row
#         ret = backtracking(row + 1)
#         used_col[i] = -1
#
#     return ret
#
#
# if backtracking(0):
#     for a in answer:
#         print(a)
# else:
#     print(-1)
