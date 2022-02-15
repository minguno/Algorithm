# 스도쿠 검증

def is_sudoku(arr):
    for i in range(9):
        solR = []; solC = []
        for j in range(9):
            # 가로
            if arr[i][j] in solR:
                return 0
            else:
                solR.append(arr[i][j])
            # 세로
            if arr[j][i] in solC:
                return 0
            else:
                solC.append(arr[j][i])
    # 3*3
    for i in range(0, 7, 3):
        for j in range(0, 7, 3):
            solSq = []
            for a in range(3):
                for b in range(3):
                    if arr[i + a][j + b] in solSq:
                        return 0
                    else:
                        solSq.append(arr[i + a][j + b])
    return 1

for t in range(int(input())):
    arr = [list(map(int, input().split())) for _ in range(9)]
    print(f'#{t + 1} {is_sudoku(arr)}')