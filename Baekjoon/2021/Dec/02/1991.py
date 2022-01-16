'''
Title   : 트리순회
Level   : S1
Problem : 이진트리를 입력받아, 전위/중위/후위 순회한 결과를 출력하는 프로그램을 작성한다.
Type    : 트리, 재귀
Idea    : 1. 트리를 dict()자료구조를 통해 구현한다.
          2. 현재 노드의 값을 keys, 자식을 value로 하는 dict를 트리로 한다.
          3. dfs를 이용하여 트리를 순회한다.
'''

N = int(input())
tree = dict()
for n in range(N):
    val, left, right = input().split()
    tree[val] = [left, right]

def preorder(node):
    """
    전위 순회
    node : 현재 방문중인 노드의 알파벳, dict의 key로 사용된다.
    return : 없음
    """
    if tree[node] == ['.', '.']: # 단말노드면 출력한다.
        print(node,end='')
        return
    print(node,end='')
    if tree[node][0] != '.': # 왼쪽 자식이 있으면
        preorder(tree[node][0])
    if tree[node][1] != '.': # 오른쪽 자식이 있으면
        preorder(tree[node][1])

def postorder(node):
    """
    후위 순회
    node : 현재 방문중인 노드의 알파벳, dict의 key로 사용된다.
    return : 없음
    """
    if tree[node] == ['.', '.']: # 단말노드면 출력한다.
        print(node,end='')
        return
    if tree[node][0] != '.': # 왼쪽 자식이 있으면
        postorder(tree[node][0])
    if tree[node][1] != '.':  # 오른쪽 자식이 있으면
        postorder(tree[node][1])
    print(node,end='')

def inorder(node):
    """
    중위 순회
    node : 현재 방문중인 노드의 알파벳, dict의 key로 사용된다.
    return : 없음
    """
    if tree[node] == ['.', '.']: # 단말노드면 출력한다.
        print(node,end='')
        return
    if tree[node][0] != '.': # 왼쪽 자식이 있으면
        inorder(tree[node][0])
    print(node,end='')
    if tree[node][1] != '.':  # 오른쪽 자식이 있으면
        inorder(tree[node][1])

preorder('A')
print()
inorder('A')
print()
postorder('A')