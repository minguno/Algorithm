# 9단계 기본 수학2 골드바흐의 추측
# 소수 응용 문제2

# 1. 0 - 10001 사이의 수에 대한 소수 판별 리스트 구하기
# 가능한 범위 개수만큼 True 리스트 생성
prime = [True] * 10002

# 0과 1은 소수에서 제외
prime[0] = False
prime[1] = False

# 에라토스테네스의 체 원리로 소수 판별한 리스트 prime
for i in range(2, 101):
    if prime[i]:
        for j in range(i + i, 10002, i):
            prime[j] = False


# 2. 입력값 받기
# 반복할 test case 수 입력받기
T = int(input())

# 3. T 만큼 출력 작업 반복하기
for _ in range(T):

    n = int(input())

    # 중간몫부터 잡고
    a = n // 2
    b = a
    while 1:
        if prime[a] and prime[b]:
            print(a, b)
            break
        # 차이가 적은 수부터 출력하기 위해 차를 하나씩 벌려가기
        else:
            a -= 1
            b += 1