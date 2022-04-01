# N과 M (1)
# 수열 오름차순 정렬
# 주어진 숫자 개수 N, 고를 개수 M

def perm(n, k, m):
    if n == k:
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