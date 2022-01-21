M, N = map(int, input().split())

sqrt_n = int(N ** 0.5)

# True 값이 제곱근 범위 내 수 만큼 생성된 리스트
    # 에라토스테네스의 체 개념: 어떤 수의 약수는 그 수의 제곱근보다 크지 않다
    # 에 근거하여 최대범위를 반절인 제곱근으로 줄인다
# 이 리스트의 index를 수로 치환해서 쓸 것이다
is_prime = [True] * (N + 1)

# 0과 1은 소수가 아니기 때문에 제외해준다
is_prime[0] = False
is_prime[1] = False

# 0, 1을 제외한 만큼 2부터 시작값을 잡고, 범위 + 1을 해서 (미만이라) 설정해준다
for i in range(2, sqrt_n + 1):
    # == True를 생략해도 된다. 이미 is_prime 자체가 boolean 으로 이루어진 리스트이기 때문.
    if is_prime[i]:
        # True == prime이라면, 그 수를 제외한 그 수의 다음 배수부터 (i + i) 지정한 범위(N)내에 모든 배수들을 (i씩 증감)
        for j in range(i + i, N + 1, i):
            # 제외해준다
            is_prime[j] = False

# 입력된 범위 (M, N + 1)로 자르고, boolean 리스트로 소수를 구분한 is_prime의 인덱스를 원소로 가져온다
# if 문에 '== True' 또한 생략되었다
prime_list = list(idx for idx in range(M, N + 1) if is_prime[idx])

print(prime_list)