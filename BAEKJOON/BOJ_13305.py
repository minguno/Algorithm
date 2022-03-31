# 주유소

N = int(input())
d = list(map(int, input().split()))
p = list(map(int, input().split()))
sol = 0
minn = p[0]
for i in range(N - 1):
    if p[i] < minn:
        minn = p[i]
    sol += minn * d[i]
print(sol)