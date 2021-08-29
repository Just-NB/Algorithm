N, M = map(int, input().split())
db = [] #듣보
d = dict() #듣
for n in range(N):
    name = input().strip()
    d[name] = 1
for m in range(M):
    name = input().strip()
    if name in d:
        db.append(name)
print(len(db))
db.sort()
for answer in db:
    print(answer)