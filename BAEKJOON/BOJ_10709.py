# 기상캐스터

H, W = map(int, input().split())
arr = [[0 for _ in range(W)] for _ in range(H)]
for i in range(H):
    lst = input()
    for j in range(W):
        if lst[j] == 'c':
            arr[i][j] = 0
            k = 1
            while 0 <= j + k < W:
                arr[i][j + k] = k
                k += 1
        elif not arr[i][j]:
            arr[i][j] = -1
for i in range(H):
    print(*arr[i])
