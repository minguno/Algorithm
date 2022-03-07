# 토마토
# 공백 q에 시작 노드 값을 주고 while문을 돌리는게 아니라
# 일단 익은 토마토의 좌표를 q에 다 push 후 bfs 돌리기
# collections 안하면 시간 초과

from collections import deque

def bfs():
    while q:
        i, j = q.popleft()
        for di, dj in zip([-1, 1, 0, 0], [0, 0, -1, 1]):
            ni, nj = i + di, j + dj
            if 0 <= ni < N and 0 <= nj < M and not arr[ni][nj]:
                arr[ni][nj] = arr[i][j] + 1
                q.append((ni, nj))



M, N  = map(int, input().split())
arr = [list(map(int, input().split())) for _ in range(N)]
q = deque([])
for i in range(N):
    for j in range(M):
        if  arr[i][j] == 1:
            q.append((i, j))
bfs()
sol = 0
flag = False
for i in range(N):
    for j in range(M):
        if not arr[i][j]:
            sol = 0
            flag = True
            break
    if flag:
        break
    sol = max(sol, max(arr[i]))

print(sol - 1)