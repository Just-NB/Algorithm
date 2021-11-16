'''
Title   : 징검다리
Level   : S4
Problem : 1번 ~ N번 징검다리가 차례대로 놓여있다.
          1. 첫 징검다리는 점프해서 아무 것이나 밟을 수 있다.
          2. 두 번째 점프부터는 이전에 점프한 거리보다 1 이상 더 긴 거리를 뛰어야만 한다.
          3. N번 징검다리는 반드시 밟아야 한다.
          4. N번 징검다리를 밟은 후 강 건너로 이동할 땐 점프를 하지 않는다.
          이 규칙을 지키며 강을 건널때 밟을 수 있는 징검다리의 최대 갯수
Type    : 이분탐색.
Idea    : 1. 최대한 많이 밟으려면, 최대한 짧게 뛰어야 한다. 따라서 1칸씩 늘려가며 뛴다.
          2. i번 밟았을 때, 갈 수 있는 최소 거리(d)는 (i * (i+1))/2 이다.
          3. 이분탐색을 통해 (i * (i+1))/2 <= N 이 되는 최초 시점을 찾는다.
'''

T = int(input())
for tc in range(T):
    n = int(input())
    left, right = 1, n
    while left <= right:
        mid = (left + right) // 2 # mid번 뛴다.
        if (mid * (mid+1)) // 2 <= n: # mid번 뛰어서 목적지에 도착하지 못한다면
            left = mid+1
        else: # mid번 뛰어서 목적지를 넘겼다면 if (mid * (mid+1)) // 2 > n
            right = mid-1
    print(right)