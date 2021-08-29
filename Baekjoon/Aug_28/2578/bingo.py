import sys
input = sys.stdin.readline
# 빙고는 선이 3개
bingo_book = []
for _ in range(5):
    line = input().split()
    bingo_book.append(line)

# 사회자가 부른 숫자가 어디에 위치했는지 찾기.
def find_num(num):
    for r in range(5):
        for c in range(5):
            if bingo_book[r][c] == num:
                return r,c

# row_check : ㅡ 빙고 체크, row가 일정하고 col이 변하는 빙고, row행에 값이 들어오면 col에 관계없이 +=1 한다. 5가 되면 빙고 
row_check = [0 for _ in range(5)]
# col_check : ㅣ 빙고 체크, row_check와 같은 원리
col_check = [0 for _ in range(5)]
# slash/bslash_check : /,\ 빙고 체크, row==col 은 slash, row==col-4 or row==4-col 은 bslash
slash_check = 0
bslash_check = 0
bingo_check = 0
answer = 0
for i in range(5):
    host = input().split()
    for j,h in enumerate(host):
        r,c = find_num(h)
        # 사회자가 부른 넘버의 r,c에 따라 체크한다.
        row_check[r] += 1
        if row_check[r] == 5:
            bingo_check += 1
        col_check[c] += 1
        if col_check[c] == 5:
            bingo_check += 1

        if r == c :
            slash_check += 1
            if slash_check == 5:
                bingo_check += 1
        if r == 4-c or r == c-4 :
            bslash_check += 1
            if bslash_check == 5:
                bingo_check += 1
        answer += 1
        # 3빙고면 끝
        if bingo_check >= 3:
            print(answer)
            break
    # 3빙고면 끝
    if bingo_check >= 3:
        break


