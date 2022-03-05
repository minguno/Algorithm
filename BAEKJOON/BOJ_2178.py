# 미로 탐색

def bfs(si, sj, N, M):
    q = [(si, sj)]
    vst = [[0] * M for _ in range(N)]
    vst[si][sj] = 1
    while q:
        i, j = q.pop(0)
        if i == N - 1 and j == M - 1:
            return vst[i][j]
        for di, dj in zip([-1, 1, 0, 0], [0, 0, -1, 1]):
            ni, nj = i + di, j + dj
            if 0 <= ni < N and 0 <= nj < M and arr[ni][nj] and not vst[ni][nj]:
                vst[ni][nj] = vst[i][j] + 1
                q.append((ni, nj))


n, m = map(int, input().split())
arr = [list(int(x) for x in input()) for _ in range(n)]
print(bfs(0, 0, n, m))
