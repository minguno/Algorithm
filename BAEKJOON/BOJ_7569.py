# 토마토 3D
# 3차원 배열

from collections import deque

def bfs():
    while q:
        i, j, k = q.popleft()
        for di, dj, dk in zip([-1, 1, 0, 0, 0, 0], [0, 0, -1, 1, 0, 0], [0, 0, 0, 0, -1, 1]):
            ni, nj, nk = i + di, j + dj, k + dk
            if 0 <= ni < H and 0 <= nj < N and 0 <= nk < M:
                if not arr[ni][nj][nk]:
                    arr[ni][nj][nk] = arr[i][j][k] + 1
                    q.append((ni, nj, nk))


M, N, H = map(int, input().split())
arr = [[list(map(int, input().split())) for _ in range(N)] for _ in range(H)]
q = deque()
for i in range(H):
    for j in range(N):
        for k in range(M):
            if arr[i][j][k] == 1:
                q.append((i, j, k))
bfs()
sol = 0
flag = False
for i in range(H):
    for j in range(N):
        for k in range(M):
            if not arr[i][j][k]:
                sol = 0
                flag = True
                break
        if flag:
            break
        sol = max(sol, max(arr[i][j]))
    if flag:
        break

print(sol - 1)