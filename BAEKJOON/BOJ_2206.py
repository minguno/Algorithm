# 벽 부수고 이동하기
# 벽을 부쉈나 안부쉈나 상태를 3차원 배열로 저장하기

from collections import deque

def bfs(i, j):
    q = deque()
    vst = [[[0] * 2 for _ in range(M)] for _ in range(N)]
    # 벽 안 부신 상태
    flag = 0
    q.append((i, j, flag))
    arr[i][j] = 1
    vst[i][j][flag] = 1
    while q:
        i, j, flag = q.popleft()
        if i == N - 1 and j == M - 1:
            return vst[i][j][flag]
        for di, dj in zip([-1, 1, 0, 0], [0, 0, -1, 1]):
            ni, nj = i + di, j + dj
            if 0 <= ni < N and 0 <= nj < M:
                # 벽 부수기 전 vst[ni][nj][0] 에 값 저장
                # 벽 부순 후 vst[ni][nj][1] 에 값 저장
                if not arr[ni][nj] and not vst[ni][nj][flag]:
                    vst[ni][nj][flag] = vst[i][j][flag] + 1
                    q.append((ni, nj, flag))
                # 벽 부수기 (한 번 부셔서 flag == 1되면 작동 X)
                elif arr[ni][nj] and not flag:
                    vst[ni][nj][flag + 1] = vst[i][j][flag] + 1
                    q.append((ni, nj, flag + 1))
    return -1


N, M = map(int, input().split())
arr = [list(int(x) for x in input()) for _ in range(N)]
print(bfs(0, 0))