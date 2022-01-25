# 9단계 기본 수학2 소수
# 2부터 X - 1까지 모두 나눠서 X가 소수인지 판별하는 문제 2
# 소수인 수들의 합과 그 중 최솟값 출력하기

# 최솟 범위 값
M = int(input())
# 최대 범위 값
N = int(input())

prime = []

# 주어진 범위 내에 정수들을 하나씩 호출
for i in range(M, N + 1):
    # 1보다 크고
    # 2부터 해당 수 -1 까지의 수로 나눈 나머지가 전부 0(False)이 아닐 때 
    # true를 반환하는 all()을 써서 약수가 없는 경우만 if 문이 실행되게 한다
    if i > 1 and all(i % j for j in range(2, i)):
        prime.append(i)

# prime이 공백리스트라 False 면 if not 문 실행
if not prime:
    print(-1)
# 아닐 시엔 소수 리스트의 합과 최솟값 출력
else:
    print(sum(prime))
    print(min(prime))