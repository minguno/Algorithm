# 바이러스
#

def BFS(s, N):
    vst = [0] * N
    q = [s]
    vst[s] = 1
    sol = 0
    while q:
        s = q.pop(0)
        for e in range(1, N):
            if not vst[e] and adj[s][e]:
                q.append(e)
                vst[e] = 1
                sol += 1
    return sol

V = int(input())
adj = [[0] * (V + 1) for _ in range(V + 1)]
for _ in range(int(input())):
    n1, n2 = map(int, input().split())
    adj[n1][n2] = adj[n2][n1] = 1
print(BFS(1, V + 1))