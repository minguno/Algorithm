
# 방법 1
# all()로 소수 거르기
# 시간 4896ms로 오래걸림

import sys

M, N = map(int, sys.stdin.readline().split())

for i in range(M, N + 1):
    if i > 1 and all(i % x for x in range (2, int(i ** 0.5) + 1)):
        print(i)



# 방법 2
# 에라토스테네스의 체 원리로 2배수를 False로 제외시켜 필요한 범위만큼 잘라서 출력
# 시간 소요가 상당히 적음


import sys

M, N = map(int, sys.stdin.readline().split())

# 소수인지 구분할 리스트
# 인덱스로 출력할 것이기 때문에 N + 1 해준다
is_prime = [True] * (N + 1)

# 고로 0과 1은 제외시켜준다
is_prime[0] = False
is_prime[1] = False

# 에라토스테네스의 체 원리를 사용해서 최대 범위를 제곱근 + 1 시켜 반복 횟수를 줄여준다
for i in range(2, int(N ** 0.5) + 1):
    # 생략해도 결과는 똑같이 출력되지만 시간 소요가 절반 감소한다 (720 -> 344ms)
    if is_prime[i]:
        # 2부터 그 배수를 False로 제외시켜준다
        for j in range(i + i, N + 1, i):
            is_prime[j] = False

for i in list(idx for idx in range(M, N + 1) if is_prime[idx]):
    print(i)