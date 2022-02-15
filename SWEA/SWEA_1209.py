# sum

for _ in range(10):
    t = int(input())
    # N * N 배열
    N = 100
    # 2차원 리스트 생성
    arr = [list(map(int, input().split())) for _ in range(N)]
    maxx = 0
    # 각 row, column, diagonal의 합을 담을 리스트
    sol = []
    # 대각선은 한개씩 밖에 없으니 밖에다 빼주기
    dd, ud = 0, 0
    for i in range(N):
        # 반복문마다 초기화되어야 하기 때문에
        r, c = 0, 0
        # down diagonal
        dd += arr[i][i]
        # up diagonal
        ud += arr[i][N - 1 - i]
        for j in range(N):
            # row
            r += arr[i][j]
            # column
            c += arr[j][i]
        sol.append(r)
        sol.append(c)
    sol.append(dd)
    sol.append(ud)

    for n in sol:
        if maxx < n:
            maxx = n
    print(f'#{t} {maxx}')