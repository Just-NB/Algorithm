'''
2차원 평면 위의 점 N개가 주어진다. 좌표를 x좌표가 증가하는 순으로, x좌표가 같으면 y좌표가 증가하는 순서로 정렬한 다음 출력하는 프로그램을 작성하시오.
5
3 4
1 1
1 -1
2 2
3 3
'''

N = int(input())
coord = []
for n in range(N):
    coord.append(list(map(int, input().split())))
coord.sort(key= lambda x: (x[0], x[1]))
for c in coord:
    print(f'{c[0]} {c[1]}')
