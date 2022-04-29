'''
6 4
4 1
8
'''
import sys

input = sys.stdin.readline

def get_pos(p: int, s: int, t: int) -> int:
    '''
    :param p: 현재 위치
    :param s: 범위 0 ~ s
    :param t: 이동 시간
    :return: 최종 좌표
    '''
    pos = 0
    if p + t > s:
        pos = s
        t -= (s - p)
    else:
        return (p + t) % (s + 1)

    if (t // s) % 2 == 0:
        return s - t % s
    else:
        return t % s

def get_pos_better(p: int, s: int, t: int) -> int:
    # s가 6일 경우
    # abs(s - (p + t) % (2 * s)) : 6 5 4 3 2 1 0 1 2 3 4 5 의 값중 하나가 나온다.
    # s - abs(s - (p + t) % (2 * s)) : 0 1 2 3 4 5 6 5 4 3 2 1 의 값 중 하나가 나온다.
    return s - abs(s - (p + t) % (2 * s))


def solution() -> None:
    w, h = map(int, input().split())
    x, y = map(int, input().split())
    t = int(input())

    # print(f'{get_pos(x, w, t)} {get_pos(y, h, t)}')
    print(f'{get_pos_better(x, w, t)} {get_pos_better(y, h, t)}')
solution()