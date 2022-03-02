# 골드바흐의 추측

# N 이하의 소수들 찾기
def prime_list(N):
    is_prime = [1 for _ in range(N)]
    is_prime[0] = is_prime[1] = 0
    for i in range(int(N ** 0.5)):
        if is_prime[i]:
            for j in range(i + i, N, i):
                is_prime[j] = 0
    return [x for x in range(N) if is_prime[x]]

