# 어디에 단어가 들어갈 수 있을까

for t in range(int(input())):
    N, K = map(int, input().split())
    arr = [list(map(int, input().split())) for _ in range(N)]
    sol = 0
    sols = []
    for i in range(N):
        cntR = cntC = 0
        for j in range(N):
            # 가로 탐색 - row 고정
            if arr[i][j]:
                cntR += 1
            else:
                if cntR:
                    sols.append(cntR)
                    cntR = 0
            # 세로 탐색 - column 고정
            if arr[j][i]:
                cntC += 1
            else:
                if cntC:
                    sols.append(cntC)
                    cntC = 0
        if cntR:
            sols.append(cntR)
        if cntC:
            sols.append(cntC)

    for n in sols:
        if n == K:
            sol += 1

    print(f'#{t + 1} {sol}')