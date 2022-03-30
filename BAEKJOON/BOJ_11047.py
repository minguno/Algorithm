# 동전 0

N, K = map(int, input().split())
coin = [int(input()) for _ in range(N)][::-1]
sol = 0
for i in range(N):
    if K == 0:
        break
    if coin[i] > K:
        continue
    sol += K // coin[i]
    K %= coin[i]
print(sol)