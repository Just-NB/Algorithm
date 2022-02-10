def compare(a, b):
    if a[0] > b[0] and a[1] > b[1]:
        return True
    return False

N = int(input())
bodies = []
bigger = [0 for _ in range(N)]
for n in range(N):
    bodies.append(list(map(int, input().split())))

for i in range(N):
    for j in range(N):
        if compare(bodies[i], bodies[j]):
            bigger[j] += 1  # i가 j보다 크다. 등수는 자신보다 큰 덩치인 사람의 수로 정해진다.

for b in bigger:
    print(b + 1, end=' ')
