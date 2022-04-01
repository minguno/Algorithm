# N과 M (2)
# 1에서 sorted 조건만 걸어줬다

def perm(n, k, m):
    if n == k:
        if p == sorted(p):
            print(*p)
    else:
        for i in range(m):
            if not vst[i]:
                vst[i] = 1
                p[n] = lst[i]
                perm(n + 1, k, m)
                vst[i] = 0


N, M = map(int, input().split())
lst = [i for i in range(1, N + 1)]
p = [0] * M
vst = [0] * N
perm(0, M, N)