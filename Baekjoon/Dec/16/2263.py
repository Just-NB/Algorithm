'''
Title   : 트리의 순회
Level   : G2
Problem : N개의 정점을 갖는 이진 트리의 정점에 1 ~ N까지의 번호가 중복없이 매겨져 있다.
          이 이진트리의 inorder/postorder가 주어졌을때 preorder를 구하는 프로그램을 작성한다.
Type    : 트리, 재귀
Idea    : 1. postorder의 특성상, post order의 마지막 출력 값은 해당 트리의 루트 이다.
          2. inorder의 특성상, 루트 idx를 기준으로 0~idx 까지는 왼쪽 자식, idx+1~N까지는 오른쪽 자식이다.
          3. preorder는 root , left, right 순서로 출력한다.
          4. postorder와 inorder의 특징으로 root의 idx와, left, right 자식들을 찾는다.
          5. root는 그대로 출력, left, right 자식은 분할하여 재귀적인 방식으로 탐색한다.
          6. 분할된 inorder 혹은 postorder의 크기가 1개라면 단말노드를 의미하고, 그대로 출력하고 함수를 종료한다.
'''
import sys
sys.setrecursionlimit(10**5)
N = int(input())
inorder = list(map(int, input().split()))
postorder = list(map(int, input().split()))
i_idx = dict()
for i in range(N):
    i_idx[inorder[i]] = i
def preorder(i_left, i_right, p_left, p_right):
    '''
    :param i_left: 해당 부분 트리의 inorder 시작 인덱스
    :param i_right: 해당 부분 트리의 inorder 종료 인덱스
    :param p_left: 해당 부분 트리의 postorder 시작 인덱스
    :param p_right: 해당 부분 트리의 postorder 종료 인덱스
    :return:
    '''
    if i_left > i_right or p_left > p_right:
        return
    root = postorder[p_right] # 루트는 postorder의 맨 뒤.
    root_idx = i_idx[root] # inorder에서 루트의 idx
    left_cnt = root_idx - i_left
    right_cnt = i_right - root_idx
    print(root, end=' ')
    preorder(i_left, root_idx - 1, p_left, p_left + left_cnt - 1) # root의 위치를 기준으로 왼쪽 자식
    preorder(root_idx + 1, i_right, p_right-right_cnt, p_right-1) # root의 위치를 기준으로 오른쪽 자식

preorder(0, N-1, 0, N-1)
