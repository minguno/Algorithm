# 9단계 기본 수학2 베르트랑 공준
# 소수 응용 문제1

'''
X 시간 초과 X

while 1:
    n = int(input())
    if n == 0: break

    cnt = 0
    for i in range(n + 1, 2 * n + 1):
        if i < 2:
            break
        if all(i % x for x in range(2, i)):
            cnt += 1

    print(cnt)

    
'''


while 1:
    n = int(input())
    if n == 0: break

    is_prime = [True] * (2 * n + 1)
    is_prime[0], is_prime[1] = False, False

    for i in range(2, int((2 * n + 1) ** 0.5) + 1):
        if is_prime[i]:
            for j in range(i + i, 2 * n + 1, i):
                is_prime[j] = False

    print(sum(is_prime[n + 1: 2 * n + 1]))