N = int(input())

for i in range(1, N + 1):
    print('{1:>{0}s}'.format(N, '*' * i))