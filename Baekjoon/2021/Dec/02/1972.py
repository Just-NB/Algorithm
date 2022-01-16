'''
Title   : 놀라운 문자열
Level   : S3
Problem : D-쌍 = 거리가 D인 두 문자를 순서대로 나열한 것
          모든 D-쌍 들이 서로 다를때, D-유일하다.
          모든 D에 대해 D-유일하면 놀라운 문자열이다.
          주어진 문자열이 놀라운 문자열인지 아닌지를 구하는 프로그램을 작성한다.
Type    : 시뮬레이션, 구현, 문자열
Idea    : 1. 2중 반복문을 이용한다.
          2. 첫번째 반복은 문자열 사이의 거리 D를 조절한다.
          3. 두번째 반복은 D거리 떨어져있는 문자열 2개를 합친다.
          4. 합친 문자열을 dict자료형에 넣고, 이미 문자열이 keys로 존재한다면 D_유일하지 않다.
'''


def d_pair(string: str):
    """
    D-쌍이 D-유일 한지 확인하는 함수.
    string : D-쌍 확인하기 위한 원본 문자열
    return : True(D-유일) / False(D-유일하지않음)
    """
    for d in range(1, N-1):
        d_dict = dict()
        for i in range(N - d):
            tmp = string[i] + string[i + d]
            if tmp in d_dict.keys():
                return False
            else:
                d_dict[tmp] = 1
    return True


while True:
    s = input()
    if s == '*':
        break
    N = len(s)
    if d_pair(s) is True:
        print(f'{s} is surprising.')
    else:
        print(f'{s} is NOT surprising.')
