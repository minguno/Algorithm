# N과 M (4)
# [0]을 M개만큼 만들어 순열을 채워나가는 방식은 가지치기를 할 수 없어
# 공백리스트에 차례대로 넣어주는 방식을 선택

def perm(n, p):
    if p != sorted(p):
        return
    if n == M:
        print(*p)
    for i in range(N):
        perm(n + 1, p + lst[i])


N, M = map(int, input().split())
lst = [i for i in range(1, N + 1)]
perm(0, [])