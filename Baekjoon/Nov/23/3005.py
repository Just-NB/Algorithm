'''
Title   : 크로스워드 퍼즐 쳐다보기
Level   : S1
Problem : RxC 크기의 직사각형 크로스워드 퍼즐이 있다.
          가로/세로로 연속된 빈 칸에 단어를 채우면서 푼다.
          풀려있는 퍼즐을 보고, 퍼즐에서 사전순으로 제일 앞서는 단어를 찾는다.
Type    : 완전탐색, dfs
Idea    : 1. dfs 완전탐색하며 단어들을 저장한다.
          2. 저장한 단어를 정렬한다.
'''

R, C = map(int, input().split())
puzzle = [input() for _ in range(R)]
words = []

def dfs_right(row, col, depth, word):
    if col == C or depth == C or puzzle[row][col] == '#':
        return word
    else:
        return dfs_right(row, col+1, depth+1, word+puzzle[row][col])


def dfs_down(row, col, depth, word):
    if row == R or depth == R or puzzle[row][col] == '#':
        return word
    else:
        return dfs_down(row+1, col, depth + 1, word + puzzle[row][col])

for r in range(R):
    r_flag = False
    for c in range(C):
        if puzzle[r][c] != '#' and r_flag is False:
            r_flag = True
            cand = dfs_right(r, c, 0, '')
            if len(cand) > 1:
                words.append(cand)
        if puzzle[r][c] == '#':
            r_flag = False

for c in range(C):
    d_flag = False
    for r in range(R):
        if puzzle[r][c] != '#' and d_flag is False:
            d_flag = True
            cand = dfs_down(r, c, 0, '')
            if len(cand) > 1:
                words.append(cand)
        if puzzle[r][c] == '#':
            d_flag = False

words.sort()
print(words[0])