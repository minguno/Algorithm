# 킹

delta = [(0, 1), (0, -1), (1, 0), (-1, 0), (-1, 1), (-1, -1), (1, 1), (1, -1)]

arr = [[0 for _ in range(8)] for _ in range(8)]
K, S, N = input().split()
i, j = 8 - int(K[1]), ord(K[0]) - 65
ii, jj = 8 - int(S[1]), ord(S[0]) - 65
arr[i][j] = 1
arr[ii][jj] = 1

for _ in range(int(N)):
    move = input()
    if move == 'R':
        dir = 0
    elif move == 'L':
        dir = 1
    elif move == 'B':
        dir = 2
    elif move == 'T':
        dir  = 3
    elif move == 'RT':
        dir = 4
    elif move == 'LT':
        dir = 5
    elif move == 'RB':
        dir = 6
    elif move == 'LB':
        dir = 7

    ni, nj = i + delta[dir][0], j + delta[dir][1]
    nii, njj = ii + delta[dir][0], jj + delta[dir][1]
    if 0 <= ni < 8 and 0 <= nj < 8:
        if arr[ni][nj]:
            if 0 <= nii < 8 and 0 <= njj < 8:
                arr[ii][jj] = 0
                ii, jj = nii, njj
                arr[ii][jj] = 1
            else:
                continue
        arr[i][j] = 0
        i, j = ni, nj
        arr[i][j] = 1

solK = chr(j + 65) + str(abs(i - 8))
solS = chr(jj + 65) + str(abs(ii - 8))
print(solK, solS, sep='\n')