# -2진수

N = int(input())

sol = ''
if N == 0:
    print(0)
else:
    while N != 1:
        # 나누는 건 2로만 나누되
        N, x = divmod(N, 2)
        sol = str(x) + sol
        # 몫에다가 -1을 곱해주기
        N *= (-1)

    print('1' + sol)

'''
-13 → -7 , 1

7 → 3, 1

-3 → -2. 1

2 → 1, 0

-1 → -1, 1

1

110111

'''