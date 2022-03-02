# 골드바흐의 추측

'''
# N 이하의 소수들 찾기
def prime_list(N):
    is_prime = [1 for _ in range(N)]
    is_prime[0] = is_prime[1] = 0
    for i in range(2, int(N ** 0.5) + 1):
        if is_prime[i]:
            for j in range(i + i, N, i):
                is_prime[j] = 0
    return [x for x in range(N) if is_prime[x]]
'''

is_prime = [1 for _ in range(1000001)]
for i in range(2, int(1000001 ** 0.5) + 1):
    if is_prime[i]:
        for j in range(i + i, 1000001, i):
            is_prime[j] = 0

while 1:
    N = int(input())
    if not N:
        break
    for i in range(3, len(is_prime)):
        # 인덱스가 곧 그 수이니까
        if is_prime[i] and is_prime[N - i]:
            print(f'{N} = {i} + {N - i}')
            break
    # break 하지 않았다면 else문 출력
    else:
        print('Goldbach\'s conjecture is wrong.')