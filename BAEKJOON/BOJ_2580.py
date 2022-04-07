# 스도쿠

# 시간 초과 풀이

def sudoku(arr):
    # 가로줄 탐색
    for i in range(9):
        if arr[i].count(0) == 1:
            j = arr[i].index(0)
            x = list(num - set(arr[i]))
            arr[i].pop(j)
            arr[i].insert(j, x[0])

    # 세로줄 탐색
    for j in range(9):
        l = [arr[0][j], arr[1][j], arr[2][j], arr[3][j], arr[4][j], arr[5][j], arr[6][j], arr[7][j], arr[8][j]]
        if l.count(0) == 1:
            i = l.index(0)
            x = list(num - set(l))
            arr[i].pop(j)
            arr[i].insert(j, x[0])

    # 3x3 탐색
    for i in range(0, 9, 3):
        for j in range(0, 9, 3):
            l = [arr[i][j], arr[i][j+1], arr[i][j+2], arr[i+1][j], arr[i+1][j+1], arr[i+1][j+2], arr[i+2][j], arr[i+2][j+1], arr[i+2][j+2]]
            if l.count(0) == 1:
                ii = l.index(0)
                jj = ii % 3
                ii //= 3
                x = list(num - set(l))
                arr[i+ii].pop(j+jj)
                arr[i+ii].insert(j+jj, x[0])

num = set(range(1, 10))
arr = [list(map(int, input().split())) for _ in range(9)]
while 0 in set(arr[0]) and 0 in set(arr[1]) and 0 in set(arr[2]) and 0 in set(arr[3]) and 0 in set(arr[4]) and 0 in set(arr[5]) and 0 in set(arr[6]) and 0 in set(arr[7]) and 0 in set(arr[8]):
    sudoku(arr)
for l in arr:
    print(*l)