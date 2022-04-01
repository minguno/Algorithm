# N과 M (3)
# 1에서 vst배열을 빼줬다

def perm(n, k, m):
    if n == k:
        print(*p)
    else:
        for i in range(m):
            p[n] = lst[i]
            perm(n + 1, k, m)


N, M = map(int, input().split())
lst = [i for i in range(1, N + 1)]
p = [0] * M
vst = [0] * N
perm(0, M, N)