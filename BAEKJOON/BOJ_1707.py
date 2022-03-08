# 이분 그래프

for _ in range(int(input())):
    V, E = map(int, input().split())
    arr = [[0] * (V + 1) for _ in range(V + 1)]
    for _ in range(E):
        n1, n2 = map(int, input().split())
        arr[n1][n2] =