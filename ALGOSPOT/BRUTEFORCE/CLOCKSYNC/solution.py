# import math
# switch = [[0,1,2],
#         [3,7,9,11],
#         [4,10,14,15],
#         [0,4,5,6,7],
#         [6,7,8,10,12],
#         [0,2,14,15],
#         [3,14,15],
#         [4,5,7,14,15],
#         [1,2,3,4,5],
#         [3,4,5,9,13]
#         ]

# def isAligned(block) : 
#     for b in block :
#         if b != 12 :
#             return False
#     return True

# def click(block,switchnum) :
#     for i in switch[switchnum] :
#         #0 3 6 9 
#         block[i] = block[i] + 3
#         if block[i] == 15 :
#             block[i] = 3


# def solution(block, switchnum) :
#     ret = math.inf
#     if switchnum == 10 :
#         if isAligned(block):
#             return 0
#         else:
#             return math.inf

#     #click count    
#     for i in range(4) :
#         ret = min(ret, i+solution(block, switchnum+1))
#         click(block, switchnum)

#     return ret



# '''
# TASE CASE
# 2
# 12 6 6 6 6 6 12 12 12 12 12 12 12 12 12 12 
# 12 9 3 12 6 6 9 3 12 9 12 9 12 12 6 6
# '''
# if __name__ == '__main__' :
#     #C = 2
#     #print(solution([12,6,6,6,6,6,12,12,12,12,12,12,12,12,12,12],0))
#     #print(solution([12,9,3,12,6,6,9,3,12,9,12,9,12,12,6,6],0))
#     C = int(input())
#     for _ in range(C) :
#         block = list(map(int, input().split()))
#         print(solution(block, 0))
linked = [
    [8, [6, 7, 8, 10, 12]],
    [10, [4, 10, 14, 15]],
    [11, [3, 7, 9, 11]],
    [9, [3, 4, 5, 9, 13]],
    [6, [0, 4, 5, 6, 7]],
    [7, [4, 5, 7, 14, 15]],
    [4, [1, 2, 3, 4, 5]],
    [1, [0, 1, 2]],
    [0, [0, 2, 14, 15]],
    [3, [3, 14, 15]]
]#2 5 12 13 14 15

for _ in range(int(input())):
    clocks = list(map(int, input().split()))

    ret = 0
    for clock, idx in linked:
        print(clock, end = ' ')
        # print(f'clock {clock} idx {idx}')
        cnt = ((12 - clocks[clock]) % 12) / 3
        print(clocks[clock], cnt)
        ret += cnt
        for i in idx:
            clocks[i] = (clocks[i] + 3 * cnt) % 12

    print(-1 if any(clocks) else int(ret))