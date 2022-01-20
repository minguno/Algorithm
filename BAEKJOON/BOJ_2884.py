N = list(map(int, input().split()))
H, M = N[0], N[1]

if (M - 45) < 0:
    H -= 1
    if H < 0:
        H += 24
    M = 60 + (M - 45)
    print('{} {}'.format(H, M))
else:
    print('{} {}'.format(H, M - 45))