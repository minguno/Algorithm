import statistics

C = int(input())

for i in range(C):
    numbers = list(map(int, input().split()))
    # 학생 수
    N = numbers[0]
    # 점수 리스트
    scores = numbers[1:]
    # 평균 구하기
    avrg = statistics.mean(scores)
    cnt = 0
    for i in scores:
        if i > avrg:
            cnt += 1
    print('{:.3f}%'.format(round(cnt / N * 100, 3)))