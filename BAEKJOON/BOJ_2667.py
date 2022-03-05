# 단지 번호 붙이기
# 1012 배추 키우기 문제랑 비슷한 접근

# 상하좌우
d = [(-1, 0), (1, 0), (0, -1), (0, 1)]

def bfs(si, sj, N):
    global lst
    q = [(si, sj)]
    arr[si][sj] = 0
    cnt = 1
    while q:
        i, j = q.pop(0)
        for dir in range(4):
            ni, nj = i + d[dir][0], j + d[dir][1]
            if 0 <= ni < N and 0 <= nj < N and arr[ni][nj]:
                arr[ni][nj] = 0
                q.append((ni, nj))
                cnt += 1
    lst.append(cnt)
    return


n = int(input())
arr = [list(int(x) for x in input()) for _ in range(n)]
sol = [0]
lst = []
for i in range(n):
    for j in range(n):
        if arr[i][j]:
            bfs(i, j, n)
            sol[0] += 1
sol.extend(sorted(lst))
print(*sol, sep='\n')