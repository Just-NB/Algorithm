'''
Title   : 수 찾기
Level   : S4
Problem : N개의 정수 A배열이 주어졌을때, 이 안에 X라는 정수가 존재하는지 알아낸다.
          자연수의 크기는 -2^31 ~ 2^31 이다.
Type    : 이분탐색
Idea    : 1. 자연수의 범위가 너무 크므로, i가 있다면 a[i] = 1 없다면 a[i] = 0 으로 하는식의 방법은 불가능하다.
          2. A배열의 크기가 100,000이하이므로, 단순한 서치로는 시간초과
          3. 이분탐색을 이용하여 풀이, A를 먼저 오름차순으로 정렬한다.
          4. left = 0, right = n, mid = (left + right)/2 로 한다.
          5. A[mid] == f 이면, 값을 찾았다.
          6. A[mid] < f 이면 left = mid+1, A[mid] > f 이면 right = mid
'''

import sys
input = sys.stdin.readline
n = int(input())
A = list(map(int, input().split()))
m = int(input())
find = list(map(int, input().split()))
A.sort()
for f in find:
     left, right = 0, n-1
     flag = False
     while left <= right:
         mid = (left + right) // 2
         if A[mid] == f :
             flag = True
             break
         elif A[mid] < f :
             left = mid+1
         else:
             right = mid-1
     if flag:
         print('1')
     else:
         print('0')