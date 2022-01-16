'''
온라인 저지에 가입한 사람들의 나이와 이름이 가입한 순서대로 주어진다. 이때, 회원들을 나이가 증가하는 순으로, 나이가 같으면 먼저 가입한 사람이 앞에 오는 순서로 정렬하는 프로그램을 작성하시오.
'''

N = int(input())
member = []
for n in range(N):
    tmp = input().split()
    member.append([int(tmp[0]), tmp[1],n])

member.sort(key = lambda x : (x[0], x[2]))
for m in member :
    print(f'{m[0]} {m[1]}')