# 숨바꼭질
# 에라토스테네스의 체 처럼 주어진 범위 통으로 가능한 정점 리스트 만들기

from collections import deque

def bfs():
    q = deque()
    q.append(N)
    lst[N] = 1
    while q:
        i = q.popleft()
        for ni in [i + 1, i - 1, i * 2]:
            if 0 <= ni < maxx and not lst[ni]:
                lst[ni] = lst[i] + 1
                q.append(ni)


N, K = map(int, input().split())
maxx = 100001
lst = [0] * maxx
bfs()
print(lst[K] - 1)
