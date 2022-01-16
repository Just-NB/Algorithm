N,M = map(int, input().split())
lst = ['' for _ in range(N)]
dct = {}
for n in range(N):
    name = input().strip()
    dct[name] = n
    lst[n] = name
for m in range(M):
    quiz = input().strip()
    if quiz.isdigit():
        print(lst[int(quiz)-1])
    else:
        print(dct[quiz]+1)
