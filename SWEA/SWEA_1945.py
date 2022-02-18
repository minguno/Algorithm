# 간단한 소인수분해

for t in range(int(input())):
    N = int(input())
    sol = []
    dct = {}
    for k, v in enumerate([2, 3, 5, 7, 11]):
        dct[v] = 0

    while N != 1:
        while N % 2 == 0:
            N /= 2
            dct[2] += 1
        while N % 3 == 0:
            N /= 3
            dct[3] += 1
        while N % 5 == 0:
            N /= 5
            dct[5] += 1
        while N % 7 == 0:
            N /= 7
            dct[7] += 1
        while N % 11 == 0:
            N /= 11
            dct[11] += 1

    for i in [2, 3, 5, 7, 11]:
        sol.append(dct.get(i))

    print(f'#{t + 1}', *sol)