# 최단경로
# Dijkstra approach

import heapq
import sys
input = sys.stdin.readline

def DIJK(s):
    q = []
    D[s] = 0
    # 시작 노드로 가기 위한 최단 경로를 0으로 설정 후 q에 삽입
    heapq.heappush(q, (0, s))
    while q:
        dist, cur = heapq.heappop(q)
        # 현재 노드가 이미 처리된 적이 있다면 넘어가기
        if D[cur] < dist:
            continue
        # 현재 노드의 인접 노드들 확인
        for i in adj[cur]:
            cost = dist + i[1]
            # 현재 노드에서 다른 노드로 이동하는 거리가 더 짧은 경우
            if cost < D[i[0]]:
                D[i[0]] = cost
                heapq.heappush(q, (cost, i[0]))


INF = 100000000

V, E = map(int, input().split())
S = int(input())
adj = [[] * (V + 1) for _ in range(V + 1)]
# 최단거리 테이블
D = [INF] * (V + 1)
# 경로 입력받기
for _ in range(E):
    u, v, w = map(int, input().split())
    # u -> v 이동 costs w
    adj[u].append([v, w])

DIJK(S)

for i in D[1:]:
    print(i if i != INF else 'INF')