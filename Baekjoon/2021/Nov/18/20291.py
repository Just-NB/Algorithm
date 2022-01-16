'''
Title   : 파일 정리
Level   : S3
Problem : 파일은 파일이름.확장자 로 이루어 져있다.
          1. 파일을 확장자 별로 정리해서 몇 개 씩 있는지 출력한다.
          2. 확장자들을 사전 수능로 정렬한다.
          파일의 이름은 알파벳과 소문자, 점으로만 구성되어 있고 점은 단 한번만 등장한다.
Type    : 구현, 문자열
Idea    : 1. 문자열 '.' 을 기준으로 split()한다
          2. dict 자료형을 이용하여, 확장자를 key, 갯수를 value로 하여 저장한다.
          3. dict를 정렬한다.
'''

n = int(input())
files = [[] for _ in range(n)]
for i in range(n):
    files[i] = input().split('.')
ext = {}

for file in files:
    if file[1] not in ext:
        ext[file[1]] = 1
    else:
        ext[file[1]] += 1

ans = sorted(ext.items())
for a in ans:
    print(a[0], a[1])