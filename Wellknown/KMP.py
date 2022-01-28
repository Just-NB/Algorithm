
def kmp(S, N):
    s_size, n_size = len(S), len(N)
    ret = []
    table = make_table(N)

    # 시작위치 (i + )k, 일치하는 정도 match, 접두사 접미사가 같은 길이 l (table)
    # l = match - k 일 때 i + k는 시작위치가 될 수 있다.
    # k = match - l
    k, matched = 0, 0
    while k <= s_size - n_size:  # 시작위치는 (긴 글의 길이) - (찾고자 하는 글의 길이)를 넘어가면 안된다. 당연히 못찾는다.
        if matched < n_size and S[k + matched] == N[matched]:
            matched += 1
            if matched == n_size:
                ret.append(k)
        else:
            if matched == 0:
                k += 1
            else:
                k += matched - table[matched - 1]
                matched = table[matched - 1]

    return ret


def make_table(N):
    n_size = len(N)
    table = [0 for _ in range(n_size)]
    # 시작위치 begin, 일치하는 정도 matched
    begin, matched = 1, 0  # begin = 0 이면 자기 자신을 찾아버린다.
    while begin + matched < n_size:
        if N[begin + matched] == N[matched]:
            matched += 1
            table[begin + matched - 1] = matched
        else:
            if matched == 0:
                begin += 1
            else:
                begin += matched - table[matched - 1]
                matched = table[matched - 1]

    return table


def make_table(N):
    size = len(N)
    table = [0 for _ in range(size)]
    j = 0  # 접두사 idx
    for i in range(1, size):  # 접미사 idx
        while j > 0 and N[i] != N[j]:  # 접두사와 접미사가 다르다면
            j = table[j - 1]  # 일치했던 부분으로 되돌아간다.
        if N[i] == N[j]:  # 접두사와 접미사가 같다면
            j += 1  #
            table[i] = j
    return table

def kmp(S, N):
    table = make_table(N)
    s_size = len(S)
    n_size = len(N)
    j = 0
    for i in range(s_size):
        while j > 0 and S[i] != N[j]:
            # 다음 확인할 위치 = 일치한 문자열의 길이 - 접두사와 접미사가 일치한 길이
            j = table[j - 1]  # k(다음 j) = matched(j) - table[j - 1]
        if S[i] == N[j]:
            if j == n_size - 1:
                print(f'시작위치 {i - n_size + 2}에서 일치')
                j = table[j]
            else:
                j += 1

kmp('ababacabacaabacaaba', 'abacaaba')