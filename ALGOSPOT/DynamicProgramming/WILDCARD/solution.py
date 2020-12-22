cache = [ [-1 for i in range(101)] for i in range(101)]

def match(W, file) -> bool:
    pos = 0
    # pos이 file, W 길이 안에서
    # W가 ? 이거나 둘이 같을때 반복
    while ((pos < len(file)) and (pos < len(W))) and \
            (W[pos] == '?' or W[pos] == file[pos]) :
        pos += 1
    # 대응 할 수 없으면 왜 while이 끝났는지 확인
    # 패턴 끝에 도달해서 끝난 경우 : 문자열도 끝났어야 대응
    if pos == len(W) :
        return pos == len(file)

    if (W[pos] == '*') :
        for skip in range(pos, len(file)+1) :
            if match(W[pos+1:], file[skip:]) == True:
                return True
    return False

def match_memo(W,w,F,f) :

    if cache[w][f] != -1 :
        return cache[w][f]

    while (f < len(F) and w < len(W)) and \
            (W[w] == '?' or W[w] == F[f])  :
         w += 1
         f += 1

    if w == len(W) :
        cache[w][f] = 1 if (f == len(F)) else 0
        return cache[w][f]

    if W[w] == '*' :
        for skip in range(f, len(F)+1) :
            if match_memo(W,w+1,F,skip) :
                cache[w][f] = 1
                return cache[w][f]

    cache[w][f] = 0
    return cache[w][f]

def match_memo_enhance(W,w,F,f) :

    if cache[w][f] != -1 :
        return cache[w][f]
    if (w < len(W) and f < len(F)) and \
            (W[w] == '?' or W[w] == F[f]) :
        cache[w][f] = match_memo_enhance(W,w+1,F,f+1)
        return cache[w][f]
    if w == len(W) :
        cache[w][f] = 1 if (f == len(F)) else 0
        return cache[w][f]
    if W[w] == '*' :
        if (match_memo_enhance(W,w+1,F,f)) or \
                (f < len(F) and match_memo_enhance(W,w,F,f+1)) :
            cache[w][f] = 1
            return cache[w][f]
    cache[w][f] = 0
    return cache[w][f]

C = int(input())
for _ in range(C) :
    W = input()
    N = int(input())
    files,answer= [],[]
    for __ in range(N) :
        files.append(input())
    for file in files :
        cache = [ [-1 for i in range(101)] for i in range(101)]

        # if match(W, file) == True:
        #     print(file)
        if match_memo_enhance(W,0,file,0) == True:
            answer.append(file)
    for a in sorted(answer) :
        print(a)
