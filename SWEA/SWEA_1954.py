# 달팽이 숫자

for _ in range(10):
    t = int(input())
    N = 100
    lst = [list(map(int, input().split())) for _ in range(N)]
    maxx = 0
    sol = []
    dd, ud = 0, 0
    for i in range(N):
        r, c = 0, 0
        # down diagonal
        dd += lst[i][i]
        # up diagonal
        ud += lst[i][N - 1 - i]
        for j in range(N):
            # row
            r += lst[i][j]
            # column
            c += lst[j][i]
        sol.append(r)
        sol.append(c)
    sol.append(dd)
    sol.append(ud)

    for n in sol:
        if maxx < n:
            maxx = n
    print(f'#{t} {maxx}')