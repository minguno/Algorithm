# 유기농 배추
'''
기존에 하나의 인덱스 값을 노드로 탐색해오던 방식과 달리 i, j 좌표가
하나의 노드가 됨. 탐색할 때 한 칸씩 이동하여 인접한 노드를 찾기 위해
delta를 사용해야 함.

2중 for문에서 arr[i][j]가 1인 노드를 만나면, bfs를 실행해 거기서부터
모든 연결된 노드를 0으로 바꿔주고 하나의 인접한 덩어리를
카운트했다는 의미로 sol을 1 더해준다.

bfs를 실행한 표시로 arr에서 연결점이 사라지니 vst로 방문 표시 할 필요 X

'''

# 상하좌우
d = [(-1, 0), (1, 0), (0, -1), (0, 1)]

def bfs(i, j, N, M):
    q = [(i, j)]
    arr[i][j] = 0
    while q:
        i, j = q.pop(0)
        for dir in range(4):
            ni, nj = i + d[dir][0], j + d[dir][1]
            if 0 <= ni < N and 0 <= nj < M and arr[ni][nj]:
                arr[ni][nj] = 0
                q.append((ni, nj))
    return


for _ in range(int(input())):
    m, n, k = map(int, input().split())
    arr = [[0] * m for _ in range(n)]
    for _ in range(k):
        jj, ii = map(int, input().split())
        arr[ii][jj] = 1
    sol = 0
    for si in range(n):
        for sj in range(m):
            if arr[si][sj]:
                bfs(si, sj, n, m)
                sol += 1
    print(sol)