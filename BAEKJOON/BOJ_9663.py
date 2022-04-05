# N-Queen
# Pypy3 3초; 파이썬 시간초과

def check(n):
    for i in range(n):
        # 같은 column 혹은
        # up, down 대각선에 퀸이 이미 있는 경우
        # -> row, column 별로 빼준 값이 같을 때
        if v[n] == v[i] or abs(v[n] - v[i]) == abs(n - i):
            return 0
    return 1


def DFS(n):
    global sol
    if n == N:
        sol += 1
        return
    for i in range(N):
        v[n] = i
        if check(n):
            DFS(n + 1)


N = int(input())
# 2 차원 배열을 쓸 필요 X
# arr[i][j] -> v[i] = j 개념으로 사용
v = [0] * N
sol = 0
DFS(0)
print(sol)



'''
# 시간 초과 풀이

def check(si, sj):
    # 위쪽 방향
    for i in range(si - 1, -1, -1):
        if v[i][sj]:
            return 0
    # 좌상단
    i, j = si - 1, sj - 1
    while i >= 0 and j >= 0:
        if v[i][j]:
            return 0
        i, j = i - 1, j - 1
    # 우상단
    i, j = si - 1, sj + 1
    while i >= 0 and j < N:
        if v[i][j]:
            return 0
        i, j = i - 1, j + 1
    # 3방향 모두 퀸이 없다면 성공
    return 1

def DFS(n):
    global sol
    if n == N:
        sol += 1
        return
    for j in range(N):
        if check(n, j):
            v[n][j] = 1
            DFS(n + 1)
            v[n][j] = 0


N = int(input())
v = [[0] * N for _ in range(N)]
sol = 0
DFS(0)
print(sol)
'''