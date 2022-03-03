# DFS와 BFS
# 탐색 시작하는 노드 s와 총 정점 개수 + 1 = N

def DFS(s, N):
    vst = [0] * N
    stck = [s]
    vst[s] = 1
    sol = [s]
    while stck:
        for d in range(1, N):
            if not vst[d] and adj[s][d]:
                stck.append(s)
                vst[d] = 1
                sol.append(d)
                s = d
                break
        else:
            s = stck.pop()
    return sol


def BFS(s, N):
    vst = [0] * N
    q = [s]
    vst[s] = 1
    sol = [s]
    while q:
        s = q.pop(0)
        for e in range(1, N):
            if not vst[e] and adj[s][e]:
                q.append(e)
                vst[e] = 1
                sol.append(e)
    return sol


# 정점의 개수, 간선의 개수, 탐색 시작할 정점 번호
n, m, v = map(int, input().split())
adj = [[0] * (n + 1) for _ in range(n + 1)]
for _ in range(m):
    n1, n2 = map(int, input().split())
    adj[n1][n2] = adj[n2][n1] = 1
sol1 = DFS(v, n + 1)
sol2 = BFS(v, n + 1)
print(*sol1)
print(*sol2)
