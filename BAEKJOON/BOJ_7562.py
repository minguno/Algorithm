# 나이트의 이동

from collections import deque

def bfs(i, j):
    q = deque()
    q.append((i, j))
    arr[i][j] = 1
    while q:
        i, j = q.popleft()
        if i == ei and j == ej:
            print(arr[i][j] - 1)
            return
        for di, dj in zip([-2, -1, 1, 2, 2, 1, -1, -2], [1, 2, 2, 1, -1, -2, -2, -1]):
            ni, nj = i + di, j + dj
            if 0 <= ni < N and 0 <= nj < N and not arr[ni][nj]:
                arr[ni][nj] = arr[i][j] + 1
                q.append((ni, nj))


for _ in range(int(input())):
    N = int(input())
    arr = [[0] * N for _ in range(N)]
    si, sj = map(int, input().split())
    ei, ej = map(int, input().split())
    bfs(si, sj)