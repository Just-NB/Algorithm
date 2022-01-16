'''
Title   : 신입 사원
Level   : S1
Problem : 신규 사원 채용을 실시한다. 1차 서류/ 2차 면접시험을 본다.
          다른 모든 지원자와 비교했을 때,
          서류심사 성적과 면접시험 성적 중 적어도 하나가
          다른 지원자보다 떨어지지 않는 자만 선발한다.
          이번 신규 사원 채용에서 선발할 수 있는 신입사원의 최대 인원수를 구하는 프로그램을 작성한다.
Type    : 정렬, 그리디
Idea    : 1. 성적을 서류심사 값을 기준으로 오름차순 정렬한다.
          2. 반복문을 통해 i 번째 사람은, 0~i번 사람과 면접성적만을 비교하면 된다.
          3. 면접성적 비교는 모두 비교하지 않고, 지금까지 비교한 사람들의 최고 등수와 비교한다.
'''

T = int(input())
for tc in range(T):
    N = int(input())
    scores = [[] for _ in range(N)]
    for n in range(N):
        scores[n] = list(map(int, input().split()))
    scores.sort()

    answer = N
    min_score = scores[0][1] # 최고 등수와 비교하면 된다.

    for i in range(N):
        if scores[i][1] > min_score: # 현재 면접 점수가 그 이전사람들의 최고 등수보다 낮으면 불가능
            answer -= 1
            continue
        elif scores[i][1] < min_score: # 현재 면접 등수가 가장 높으면 변경한다.
            min_score = scores[i][1]

    print(answer)
