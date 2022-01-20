N = list(map(int, input().split()))
A, B = N[0], N[1]

while A >= 0 and B >= 0:
    print(A + B)
    N = list(map(int, input().split()))
    A, B = N[0], N[1]
    if A == 0 and B == 0:
        break