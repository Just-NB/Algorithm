def d(num):
    ret = num
    while num:
        ret += num % 10
        num = num // 10
    return ret

self_num = [i for i in range(10001)]
for i in range(1, 10001):
    tmp = d(i)
    if tmp > 10000:
        continue
    self_num[d(i)] = -1

for s in self_num[1:]:
    if s != -1:
        print(s)