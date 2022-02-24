# 미로
# DFS를 이용한 미로 탐색

def dfs(i, j):
    stk = []
    stk.append([i, j])
    vst[i][j] = 1
    while stk:
        for dir in range(4):
            ni = i + di[dir]
            nj = j + dj[dir]
            if 0 <= ni < N and 0 <= nj < N and arr[ni][nj] != 1:
                if not vst[ni][nj]:
                    vst[ni][nj] = 1
                    if ni == ei and nj == ej:
                        return 1
                    stk.append([i, j])
                    i, j = ni, nj
                    break
        else:
            i, j = stk.pop()
    return 0


# 상하좌우
di = [-1, 1, 0, 0]
dj = [0, 0, -1, 1]

for t in range(int(input())):
    N = int(input())
    arr = [list(int(x) for x in input()) for _ in range(N)]
    for i in range(N):
        for j in range(N):
            if arr[i][j] == 2:
                si, sj = i, j
            elif arr[i][j] == 3:
                ei, ej = i, j
    vst = [[0] * N for _ in range(N)]
    sol = dfs(si, sj)
    print(f'#{t + 1} {sol}')