# 킹

delta = [(0, 1), (0, -1), (1, 0), (-1, 0), (-1, 1), (-1, -1), (1, 1), (1, -1)]

arr = [[0 for _ in range(8)] for _ in range(8)]
K, S, N = input().split()
i, j = 8 - int(K[1]), ord(K[0]) - 65
ii, jj = 8 - int(S[1]), ord(S[0]) - 65

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
        if ni == ii and nj == jj:
            if 0 <= nii < 8 and 0 <= njj < 8:
                ii, jj = nii, njj
            else:
                continue
        i, j = ni, nj

solK = chr(j + 65) + str(8 - i)
solS = chr(jj + 65) + str(8 - ii)
print(solK, solS, sep='\n')