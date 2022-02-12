# 구간합

T = int(input())
for t in range(1, T + 1):
    N, M = map(int, input().split())
    lst = list(map(int, input().split()))

    # test case 내 충분히 작은 수 와 충분히 큰 수
    minn = int(1e8)
    maxx = -int(1e8)

    for i in range(N - M + 1):
        total = 0
        for j in range(i, i + M):
            total += lst[j]
        if maxx < total:
            maxx = total
        if minn > total:
            minn = total

    print(f'#{t} {maxx - minn}')