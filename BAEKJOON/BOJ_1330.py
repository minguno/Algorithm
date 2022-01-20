N = list(map(int, input().split()))
A, B = N[0], N[1]

if A > B:
    print('>')
elif A < B:
    print('<')
else:
    print('==')