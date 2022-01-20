T = int(input())

# T만큼 반복되는 작업
for i in range(T):
    # OX 문자열 받기
    N = list(input())
    # 출력값
    total = 0
    # O가 나올 때 증가할 점수
    score = 1
    # 문자열 한개씩 호출
    for j in N:
        # O일 때
        if j == 'O':
            total += score
            # 연속 될 때 실행 
            score += 1
        else:
            # 연속되지 않을 때 다시 1점으로 회귀
            score = 1
    print(total)