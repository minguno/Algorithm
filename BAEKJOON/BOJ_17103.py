# 골드바흐 파티션

is_prime = [1 for _ in range(1000001)]
for i in range(2, int(1000001 ** 0.5) + 1):
    if is_prime[i]:
        for j in range(i + i, 1000001, i):
            is_prime[j] = 0

primes = [i for i in range(2, 1000001) if is_prime[i]]
primes_set = set(primes)

for _ in range(int(input())):
    N = int(input())
    sol = 0
    for prime in primes:
        if prime > N // 2:
            break
        # set의 in 연산자 시간복잡도가 상수라
        # 리스트 연산보다 훨씬 빠르게 연산 가능
        if N - prime in primes_set:
            sol += 1

    print(sol)