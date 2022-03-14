# 이분 그래프
'''
이분 그래프 Bipartite graph 란 정점을 두 그룹으로 나누되
같은 그룹의 정점끼리는 간선으로 이어지지 않은 경우를 의미한다.

빨강 정점과 연결된 모든 정점들은 파란색으로,
파란색 정점들과 이어진 모든 정점들은 빨간색으로 칠할 수 있는 그래프.
그리고 빨간색은 빨간색끼리, 파란색은 파란색끼리 인접하지 않는 그래프.

BFS, DFS 둘 다 구현 가능
BFS 접근법:
1. 최초 탐색 노드를 1로 저장
2. 탐색 시작 노트의 인접 노드를 -1로 저장
3. 해당 인접 노드를 탐색하며 1로 저장
4. 탐색 도중 이웃 정점이 같은 번호로 저장되어있다면 이분 그래프가 될 수 없다

시작 정점과 연결되지 못한 정점이 있는 비연결 그래프는
한 번의 bfs로 모든 정점을 탐색할 수 없기 때문에
모든 정점을 방문하며 bfs를 돌려주어야 한다
'''

from collections import deque
from sys import stdin
input = stdin.readline

def bfs(s):
    q = deque([s])
    vst[s] = 1
    while q:
        s = q.popleft()
        for e in adj[s]:
            if not vst[e]:
                q.append(e)
                vst[e] = -vst[s]
            elif vst[s] == vst[e]:
                return False
    return True


for _ in range(int(input())):
    V, E = map(int, input().split())
    adj = [[] for _ in range(V + 1)]
    vst = [0] * (V + 1)
    for _ in range(E):
        n1, n2 = map(int, input().split())
        adj[n1].append(n2)
        adj[n2].append(n1)
    flag = 1
    # 시작 정점과 연결되지 못한 정점이 있는 비연결 그래프는
    # 한 번의 bfs로 완전 탐색이 되지 않기 때문에
    # 모든 정점을 한 번씩 호출하여
    for k in range(1, V + 1):
        # 방문하지 않은 정점에 대해 bfs를 수행시켜준다
        if not vst[k] and not bfs(k):
            flag = 0
            break
    print("YES" if flag else "NO")