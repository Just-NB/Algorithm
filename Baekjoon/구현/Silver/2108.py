import sys

input = sys.stdin.readline

N = int(input())
nums = []
freq = dict()
max_freq = 0
for n in range(N):
    num = int(input())
    nums.append(num)
    if num not in freq:
        freq[num] = 1
    else:
        freq[num] += 1
    max_freq = max(freq[num], max_freq)
freq = sorted(freq.items(), key=lambda x: (-x[1], x[0]))
mode = freq[0][0]
if len(freq) > 1 and freq[1][1] == max_freq:
    mode = freq[1][0]
nums.sort()
mean = round(sum(nums)/N)
median = nums[N // 2]
r = nums[-1] - nums[0]

print(mean)
print(median)
print(mode)
print(r)
