num = input()
stickers = [0 for _ in range(9)]
for n in num:
    if n == '9':
        n = 6
    stickers[int(n)] += 1
stickers[6] = (stickers[6] // 2) if stickers[6] % 2 == 0 else stickers[6] // 2 + 1
print(max(stickers))
