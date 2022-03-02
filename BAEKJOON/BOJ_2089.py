# -2진수

N = int(input())

sol = ''
if N == 0:
    print(0)
else:
    while N != 1:
        N, x = divmod(N, 2)
        sol = str(x) + sol
        N *= (-1)

    print('1' + sol)