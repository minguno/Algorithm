# 오목 판정

def check(grid, N):

    for i in range(N):
        for j in range(N - 4):
            cntR = cntC = 0
            for k in range(5):
                # 가로 탐색
                if grid[i][j + k] == 'o':
                    cntR += 1
                # 세로 탐색
                if grid[j + k][i] == 'o':
                    cntC += 1
            if cntR == 5 or cntC == 5:
                return 'YES'
    # 대각선 탐색
    for i in range(N - 4):
        for j in range(N - 4):
            cntU = cntD = 0
            for k in range(5):
                if grid[i + k][j + k] == 'o':
                    cntD += 1
                if grid[i + k][j + 4 - k] == 'o':
                    cntU += 1
            if cntD == 5 or cntU == 5:
                return 'YES'

    return 'NO'

for t in range(int(input())):
    N = int(input())
    lst = [list(input()) for _ in range(N)]
    print(f'#{t + 1} {check(lst, N)}')